import numpy as np

class Game:
    def __init__(self,state=np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])):
        self.state = state
        self.numofcolums = self.state.shape[0]
        self.numofrows = self.state.shape[1]

    
    def is_terminal(self):
        if (self.state[0][0] == 'X' and self.state[0][1] == 'X' and self.state[0][2] == 'X') or (self.state[0][0] == 'X' and self.state[1][0] == 'X' and self.state[2][0] == 'X') or (self.state[0][0] and self.state[1][1] == 'X' and self.state[2][2] == 'X') or( self.state[0][2] and self.state[1][2] == 'X' and self.state[2][2] == 'X') or (self.state[0][2] and self.state[1][1] == 'X' and self.state[2][0] == 'X') or (self.state[2][0] and self.state[2][1] == 'X' and self.state[2][2] == 'X' ):
            return True , 'X'
        
        if (self.state[0][0] == 'O' and self.state[0][1] == 'O' and self.state[0][2] == 'O') or (self.state[0][0] == 'O' and self.state[1][0] == 'O' and self.state[2][0] == 'O') or (self.state[0][0] and self.state[1][1] == 'O' and self.state[2][2] == 'O') or (self.state[0][2] and self.state[1][2] == 'O' and self.state[2][2] == 'O') or (self.state[0][2] and self.state[1][1] == 'O' and self.state[2][0] == 'O') or (self.state[2][0] and self.state[2][1] == 'O' and self.state[2][2] == 'O'):
            return True , 'O' 
        

    
        return False ,None
    



    