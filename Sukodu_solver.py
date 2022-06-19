import numpy as np

sud=[0, 3, 0, 0, 5, 0, 0, 4, 0,
     0, 0, 8, 0, 1, 0, 5, 0, 0,
     4, 6, 0, 0, 0, 0, 0, 1, 2,
     0, 7, 0, 5, 0, 2, 0, 8, 0,
     0, 0, 0, 6, 0, 3, 0, 0, 0,
     0, 4, 0, 1, 0, 9, 0, 3, 0,
     2, 5, 0, 0, 0, 0, 0, 9, 8,
     0, 0, 1, 0, 2, 0, 6, 0, 0,
     0, 8, 0, 0, 6, 0, 0, 2, 0]

sud= [1, 0, 3, 0, 6, 5, 0, 0, 0,
      7, 0, 0, 0, 2, 0, 0, 0, 0,
      5, 0, 0, 3, 0, 0, 0, 0, 0,
      0, 0, 2, 6, 5, 0, 0, 3, 0,
      0, 0, 1, 4, 3, 0, 6, 0, 0,
      0, 0, 0, 0, 1, 7, 2, 0, 5,
      0, 0, 0, 0, 0, 6, 0, 5, 0,
      0, 0, 4, 0, 8, 0, 0, 6, 0,
      0, 6, 0, 0, 4, 0, 0, 1, 0]

temp_answer=0
repeat=True

def verify(plansza):
    for row in range(0,9):
        if np.unique(plansza[row,:]).sum()==45:
            pass
        else:
            return False
        if np.unique(plansza[row,:]).sum()==45:
            pass
        else:
            return False
    return True


class Sudoku():
    def __init__(self,sud):
        if type(sud)==list:
            self.board=np.array(sud).reshape(9,9)
        elif type(sud)==type(np.array([1,2,3,4]).reshape(2,2)):
            self.board=sud

        self.reset_board=self.board*1
        squares=[]
        squares.extend([self.board[0:3,0:3],
                        self.board[0:3,3:6],
                        self.board[0:3,6:9],
                        self.board[3:6,0:3],
                        self.board[3:6,3:6],
                        self.board[3:6,6:9],
                        self.board[6:9,0:3],
                        self.board[6:9,3:6],
                        self.board[6:9,6:9]])
        h_lines=[]
        v_lines=[]
        for i in range(0,9):
            h_lines.append(self.board[i,:].flatten().tolist())
            v_lines.append(self.board[:,i].flatten().tolist())

        self.h_lines=h_lines
        self.v_lines=v_lines
        self.squares=squares

    def signal(self):
        l1=np.hstack([self.squares[0],self.squares[1],self.squares[2]])
        l2=np.hstack([self.squares[3],self.squares[4],self.squares[5]])
        l3=np.hstack([self.squares[6],self.squares[7],self.squares[8]])
        self.board=np.vstack([l1,l2,l3])
        self.refresh()

    def refresh(self): #uaktualnia wszystkie skłądowes
        squares=[]
        squares.extend([self.board[0:3,0:3],
                        self.board[0:3,3:6],
                        self.board[0:3,6:9],
                        self.board[3:6,0:3],
                        self.board[3:6,3:6],
                        self.board[3:6,6:9],
                        self.board[6:9,0:3],
                        self.board[6:9,3:6],
                        self.board[6:9,6:9]])
        h_lines=[]
        v_lines=[]
        for i in range(0,9):
            h_lines.append(self.board[i,:].flatten().tolist())
            v_lines.append(self.board[:,i].flatten().tolist())
        self.h_lines=h_lines
        self.v_lines=v_lines
        self.squares=squares
        global repeat
        repeat=True

        #self.show()

    def show(self):
        #print((self.board<1).sum())
        print(self.board)

    def dump(self):
        ref=[1,2,3,4,5,6,7,8,9]
        for i in range(0,9): #weź kwadrat
            for el in [z for z in ref if z not in [x for x in self.squares[i].flatten().tolist() if x != 0]]:

                if i in [0,1,2]:
                    s_row=0
                elif i in [3,4,5]:
                    s_row=3
                else:
                    s_row=6

                if i in [0,3,6]:
                    s_col=0
                elif i in [1,4,7]:
                    s_col=3
                else:
                    s_col=6

                #analiza horyzontami

                if el in [x for x in self.h_lines[s_row] if x != 0]:
                    h_test= np.array([False,False,False])
                else:
                    h_test= np.array([True,True,True])

                if el in [x for x in self.h_lines[s_row+1] if x != 0]:
                    h_test= np.vstack([h_test,np.array([False,False,False])])
                else:
                    h_test= np.vstack([h_test,np.array([True,True,True])])

                if el in [x for x in self.h_lines[s_row+2] if x != 0]:
                    h_test= np.vstack([h_test,np.array([False,False,False])])
                else:
                    h_test= np.vstack([h_test,np.array([True,True,True])])

                #a. wertykalna
                if el in [x for x in self.v_lines[s_col] if x != 0]:
                    v_test= np.array([False,False,False]).reshape(-1,1)
                else:
                    v_test= np.array([True,True,True]).reshape(-1,1)

                if el in [x for x in self.v_lines[s_col+1] if x != 0]:
                    v_test= np.hstack([v_test,np.array([False,False,False]).reshape(-1,1)])
                else:
                    v_test= np.hstack([v_test,np.array([True,True,True]).reshape(-1,1)])

                if el in [x for x in self.v_lines[s_col+2] if x != 0]:
                    v_test= np.hstack([v_test,np.array([False,False,False]).reshape(-1,1)])
                else:
                    v_test= np.hstack([v_test,np.array([True,True,True]).reshape(-1,1)])

                ans_m=h_test*v_test*(self.squares[i]==0)

                if ans_m.sum()==1:
                    #print('Updating with',el)
                    #print(h_test,v_test,(kwadrat==0))
                    self.squares[i]=self.squares[i]+(el*ans_m)
                    self.signal()
    def lin(self):
        m=False
        ref=[1,2,3,4,5,6,7,8,9]
        for row in range(0,9): #wybór rzędów
            t_list=[x for x in ref if x not in self.h_lines[row]] #szukane
            for col in range(0,9): #kolumna
                if self.board[row,col]==0:
                    if len([y for y in t_list if y not in self.v_lines[col]])==1:
                        a=[y for y in t_list if y not in self.v_lines[col]][0]
                        self.board[row,col]=a
                        self.refresh()

    def ult(self):
        #print('F3')
        ref=[1,2,3,4,5,6,7,8,9]
        for row in range(0,9): #wybierz rząd
            for val in [x for x in ref if x not in self.h_lines[row]]: #szukana
                #print('rząd',row,'liczba',val)

                s=np.array(self.board[row,:])
                s=(s<1) #bool vector 1
                v_te=np.array([]).astype(bool)
                sq_t=np.array([]).astype(bool)
                for i in range(0,9):
                    if val not in self.v_lines[i]:
                        v_te=np.hstack([v_te,True])
                    else:
                        v_te=np.hstack([v_te,False])

                    if i < 3:
                        if row <3:

                            if val not in self.squares[0].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        elif row<6:
                            if val not in self.squares[3].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        else:
                            if val not in self.squares[6].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])

                    elif i < 6:
                        if row <3:
                            if val not in self.squares[1].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        elif row<6:
                            if val not in self.squares[4].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        else:
                            if val not in self.squares[7].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])


                    else:
                        if row <3:
                            if val not in self.squares[2].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        elif row<6:
                            if val not in self.squares[5].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])
                        else:
                            if val not in self.squares[8].flatten().tolist():
                                sq_t=np.hstack([sq_t,True])
                            else:
                                sq_t=np.hstack([sq_t,False])

                if (s*v_te*sq_t).sum() == 1:
                    #print('F3')
                    for k in range(0,9):
                        if (s*v_te*sq_t)[k] == True:
                            #self.h_lines[row].append(val)
                            #self.v_lines[k].append(val)
                            self.board[row,k]=val
                            self.refresh()



    def solve(self):
        global repeat
        repeat=True
        while repeat==True:
            repeat=False
            #faza dumpowania
            self.dump()
            #print('F1')
            if repeat==False:
                self.lin()
                #print('F2')
                if repeat==False:
                    self.ult()
                    #print('F3')

        if (self.board<1).sum()==0:
            print('Sudoku przeliczone')
            self.show()
            if verify(self.board)==True:
                global temp_answer
                temp_answer= self.board,True
                return self.board,True
            return self.board,True
        else:
            #print('Sudoku NIEUKOŃCZONE')
            #print("KOD SUD",sud)
            return self.board,False

def loor(obiekt):
    x=obiekt
    #x.show()
    ref=[1,2,3,4,5,6,7,8,9]
    for i in range(2,7): #dla liczby watpliwych
        for kolejny in range(0,9):
            if len([z for z in ref if z not in x.h_lines[kolejny]])==i:
                for k in range(0,9):
                    if x.board[kolejny,k]==0: #pierwsze 0 w row
                        return kolejny,k #row,col

def simul(plansza):
    if (plansza<1).sum() != 0:
        ref=[1,2,3,4,5,6,7,8,9]
        e=Sudoku(plansza*1)
        rr,cc=loor(e)
        #jak nie zadziała to return plansza
        for val in [z for z in ref if z not in e.h_lines[rr]]:

            if (plansza<1).sum() != 0:
                e.board[rr,cc]=val
                e.refresh()
                #print('SYMULACJA DLA', val)
                #e.show()
                #print(e.board)
                b,succ=e.solve()
                if succ==True:
                    plansza=b*1
                    return b,True
                else:
                    if (e.board<1).sum()>27:
                        e.board = simul(e.board)
                if (plansza<1).sum() != 0:
                    e.board=e.reset_board
                else:
                    #print('ZWRACAM#1',e.board)
                    return e.board,True
            else:
                #print('ZWRACAM#2',e.board)
                return e.board,True
        if (e.board<1).sum() !=0:
            #print('ZWRACAM#3',plansza)
            return plansza,False
        else:
            return b
#rozruch
def sudoku(board): #input: sudoku list
    sudoku=Sudoku(board)
    I_faza,test=sudoku.solve()
    if test==True:
        return sudoku.board,True
    else:
        #print('Druga faza dla board:',sudoku.board)
        y=Sudoku(I_faza*1)
        y.refresh()
        simul(y.board)
        return temp_answer

#sudoku(sud)
if __name__ == "__main__":
    sudoku(sud)
