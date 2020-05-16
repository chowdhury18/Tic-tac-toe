# tic-tac-toe

class Game():
    def __init__(self):
        self.state = {}
        self.player = {1:'X',2:'O'}
        self.current_player = 1
        self.steps = 0
        self.attempt = 0
        self.play = True
        self.block = 3
        self.win_cases = []
        self.points = {1:0, 2:0}

    def reset_state(self):
        end = (self.block * self.block) + 1
        for i in range(1,end):
            self.state.update({str(i):str(i)})
            
    def print_state(self):
        print(f"Statistics: Player 1: {self.points[1]} - Player 2: {self.points[2]}")
        print("\n")
        idx = 1
        for i in range(self.block):
            for j in range(self.block):
                print(' | ' + self.state[str(idx)] + ' | ', end=" ")
                idx += 1
            print('\n')

    def game_over(self,pos,player,curr):
        count_player1 = 0
        count_player2 = 0
        for item in pos:
            if self.state[str(item)] == 'X':
                count_player1 += 1
            elif self.state[str(item)] == 'O':
                count_player2 += 1
        if count_player1 == self.block or count_player2 == self.block:
            self.print_state()
            self.points[curr] += 1
            print(f"******INFO: Game Over. Player {curr} wins")
            return True
        else:
            return False

    def possible_result(self):
        #row-wise
        temp = []
        start = 1
        for i in range(self.block):
            temp = [x for x in range(start,start+self.block)]
            start = start+self.block
            self.win_cases.append(temp)
        
        #col-wise
        temp = []
        for i in range(1,self.block+1):
            temp.append(i)
            start = i
            for j in range(self.block-1):
                temp.append(start+self.block)
                start = start+self.block
            self.win_cases.append(temp)
            temp = []

        #diagonal (left-right)
        temp = []
        start = 1
        temp.append(start)
        for i in range(self.block-1):
            temp.append(start+self.block+1)
            start = start+self.block+1
        self.win_cases.append(temp)

        #diagonal (right-left)
        temp = []
        start = self.block
        temp.append(start)
        for i in range(self.block-1):
            temp.append(start+self.block-1)
            start = start+self.block-1
        self.win_cases.append(temp)

    def mainGame(self):
        print("\n****** Welcome to Dynamic Tic-Tac-Toe Game ******\n")
        print("\n****** To start the game, please select block size. (e.g. for 3x3 block, press 3) ******\n")
        b = input("\nSelect block (e.g. 3x3,5x5): ")
        if b.isdigit() and int(b)%2 != 0 and int(b) != 1:
            self.block = int(b)
            self.reset_state()
            self.possible_result()
            self.current_player = 1
            self.steps = 0
            self.attempt = 0
            self.play = True
        else:
            print(f"\n******WARNING: Block must be odd number (execpt 1).")
            self.play = False 

        while self.play:
            self.print_state()
            print(f"\n==> Player {self.current_player}")
            select = input("Position: ")

            if not select.isdigit():
                print(f"\n******WARNING: Select a  number.")
                continue
            
            if int(select) < 1 or int(select) > (self.block*self.block):
                print("\n******WARNING: Please select correct position.")
                continue
            
            if select in self.state:
                if self.state[select] == 'X' or self.state[select] == 'O':
                    self.attempt += 1
                    if self.attempt == 3:
                        print(f"\n******INFO: Game Over. Player {self.current_player} loss.")
                        self.play = False
                        continue
                    else:
                        print("\n******WARNING: Already filled. Try different one. Remaining attempt: " + str(3-self.attempt))
                        continue
                else:
                    self.attempt = 0
                    self.state[select] = self.player[self.current_player]
                    self.steps += 1
  
                       
            if self.steps >= (2*self.block)-1:
                for item in self.win_cases:
                    if self.game_over(item,self.player,self.current_player):
                        self.play = False
                        break                
            
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1
            
            if self.play == True and self.steps == (self.block*self.block):
                print(f"\n******INFO: Tie. Want to play again? press 1 to play again. press any key to start over.")
                choice = input()
                if choice == '1':
                    self.reset_state()
                    self.current_player = 1
                    self.steps = 0
                    self.attempt = 0
                    self.play = True
                else:
                    self.play = False


def main():
    game = Game()
    while True:
        game.mainGame()

if __name__ == '__main__':
    main()