class Board:
    def __init__(self, state, player):
        self.state = state
        if player == 'X':
            self.player = 'X' 
            self.opponent = 'O'
        else:
            self.player = 'O' 
            self.opponent = 'X'
        
    
    def evaluate(self):
    	# Checking for Rows for X or O victory.
        for row in range(3):
            if (self.state[row][0] == self.state[row][1] and self.state[row][1] == self.state[row][2]) :       
                if (self.state[row][0] == self.player) :
                    return 10
                elif (self.state[row][0] == self.opponent) :
                    return -10
        for col in range(3):
            if (self.state[0][col] == self.state[1][col] and self.state[1][col] == self.state[2][col]) :       
                if (self.state[0][col] == self.player) :
                    return 10
                elif (self.state[0][col] == self.opponent) :
                    return -10
        if (self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]):           
            if (self.state[0][0] == self.player) :
                return 10
            elif (self.state[0][0] == self.opponent) :
                return -10
        
        if (self.state[0][2] == self.state[1][1] and self.state[2][0] == self.state[0][0]):
            if (self.state[1][1] == self.player):
                return 10   
            elif (self.state[1][1] == self.opponent):
                return -10
        return 0
        
       
                
                
                
                
    def isMovesLeft(self):
        for i in range(3):
            for j in range(3):
                 if (self.state[i][j] == '_') :         
                     return True
        return False
        
    def minimax(self, depth, isMax):
        score = self.evaluate()
        print(str(self.state) + '\n')
        if (score == 10) :
            return score
                          
        if (score == -10) :
            return score  
                    
        if (self.isMovesLeft() == False) :
            return 0
            
        if (isMax) :
            best = -1000
            
            for i in range(3) :
                for j in range(3):
                    
                    if (self.state[i][j]=='_') :
                        self.state[i][j] = self.player
                        
                        best = max( best, self.minimax(depth+1, not isMax))
                    
                        self.state[i][j] = '_'
            
            return best
        else :
            best = 1000
            
            for i in range(3) :
                for j in range(3):
                    
                    if (self.state[i][j] == '_'):
                    
                        self.state[i][j] = self.opponent
                        
                        best = min(best, self.minimax( depth+1, not isMax))
                        
                        self.state[i][j] = '_'
                        
            return best


    def findBestMove(self) :
        
        bestVal = -1000
        bestMove = (-1, -1)
        
        for i in range(3):
            for j in range(3):
                if (self.state[i][j] == '_'):
                    self.state[i][j] = self.player
                    print((i,j))
                    #tb = 
                    moveVal = self.minimax(0, False)
                    print(moveVal)
                    
                    self.state[i][j] = '_'
                    
                    if (moveVal > bestVal) :
                        bestMove = (i,j)
                        bestVal = moveVal
        print("The value of the best Move is :", bestVal)
        print()
        return bestMove               
         
                                                 
                        
                    
                    
                    
board = [
    [ 'x', 'x', 'o' ],
    [ 'o', 'x', 'o' ],
    [ '_', '_', '_' ]
]


b = Board(board, 'x')
#print(b.evaluate())
#print(b.isMovesLeft())
#print(b.minimax(0, True))
print(b.findBestMove())
