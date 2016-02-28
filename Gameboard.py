import sys
from copy import deepcopy

class Gameboard:

    def __init__(self):
        self.gameBoard = [[0 for i in range(7)] for j in range(6)]
        self.playerturn = 1
        #self.player1Score = 0
        #self.player2Score = 0
        self.maxplayer = 0
        self.minplayer = 0
        self.maxplayerscore = 0
        self.minplayerscore = 0
        self.pieceCount = 0

    def printGameBoard(self):
        print ' -----------------'
        for i in range(0,6):
            print ' |',
            for j in range(0,7):
                print('%d' % self.gameBoard[i][j]),
            print '| '
        print ' -----------------'

    def getpieceCount(self):
        self.pieceCount = 0
        for row in self.gameBoard:
            for piece in row:
                if piece != 0:
                    self.pieceCount+=1
        return self.pieceCount

    def setboardfromfile(self,filename,mode,next_player):
        #print filename
        count = 0
        for line in (open(filename).readlines()):
            if count == 6:
                self.playerturn = int(line)
                if mode =='one-move':
                    self.maxplayer = self.playerturn
                    if self.maxplayer == 1:
                        self.minplayer = 2
                    else:
                        self.minplayer = 1
                elif mode == 'interactive':
                    if next_player=='computer-next':
                        self.maxplayer = self.playerturn
                        self.minplayer = 3 - self.maxplayer
                    elif next_player == 'human-next':
                        self.minplayer = self.playerturn
                        self.maxplayer = 3 - self.minplayer


            else:
                self.gameBoard[count] = map(int, list(line.rstrip()))
                #print list(line.rstrip())
            count+=1

    def outputboardtofile(self,outputfile):
        fp = open(outputfile, 'wb')
        for row in self.gameBoard:
            for piece in row:
                fp.write(str(piece))
            fp.write('\n')
        fp.write(str(self.playerturn))
        fp.close()

    def isvalidMove(self,position):
        row = self.gameBoard[0]
        if row[position] == 0:
            return True
        else:
            return False

    def numberofpossibleColumns(self):
        return [i for i, x in enumerate(self.gameBoard[0]) if x == 0]

    def countScore(self):
        self.maxplayerscore = 0;
        self.minplayerscore = 0;

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[1:5] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[2:6] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[3:7] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            # Check player 2
            if row[0:4] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[1:5] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[2:6] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[3:7] == [self.minplayer]*4:
                self.minplayerscore += 1

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == self.maxplayer and self.gameBoard[1][j] == self.maxplayer and
                   self.gameBoard[2][j] == self.maxplayer and self.gameBoard[3][j] == self.maxplayer):
                self.maxplayerscore += 1
            if (self.gameBoard[1][j] == self.maxplayer and self.gameBoard[2][j] == self.maxplayer and
                   self.gameBoard[3][j] == self.maxplayer and self.gameBoard[4][j] == self.maxplayer):
                self.maxplayerscore += 1
            if (self.gameBoard[2][j] == self.maxplayer and self.gameBoard[3][j] == self.maxplayer and
                   self.gameBoard[4][j] == self.maxplayer and self.gameBoard[5][j] == self.maxplayer):
                self.maxplayerscore += 1
            # Check player 2
            if (self.gameBoard[0][j] == self.minplayer and self.gameBoard[1][j] == self.minplayer and
                   self.gameBoard[2][j] == self.minplayer and self.gameBoard[3][j] == self.minplayer):
                self.minplayerscore += 1
            if (self.gameBoard[1][j] == self.minplayer and self.gameBoard[2][j] == self.minplayer and
                   self.gameBoard[3][j] == self.minplayer and self.gameBoard[4][j] == self.minplayer):
                self.minplayerscore += 1
            if (self.gameBoard[2][j] == self.minplayer and self.gameBoard[3][j] == self.minplayer and
                   self.gameBoard[4][j] == self.minplayer and self.gameBoard[5][j] == self.minplayer):
                self.minplayerscore += 1

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer and self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][0] == self.maxplayer and self.gameBoard[2][1] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][1] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer and self.gameBoard[5][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][0] == self.maxplayer and self.gameBoard[1][1] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][1] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer and self.gameBoard[5][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][1] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][2] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][5] == self.maxplayer and self.gameBoard[5][6] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][2] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][5] == self.maxplayer and self.gameBoard[4][6] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][5] == self.maxplayer and self.gameBoard[3][6] == self.maxplayer):
            self.maxplayerscore += 1

        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][1] == self.maxplayer and self.gameBoard[3][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][4] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][1] == self.maxplayer and self.gameBoard[4][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][5] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][4] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][1] == self.maxplayer and self.gameBoard[5][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][6] == self.maxplayer and self.gameBoard[1][5] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][5] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer and self.gameBoard[5][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][6] == self.maxplayer and self.gameBoard[2][5] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][5] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer and self.gameBoard[5][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][6] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer and self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 1

        # Check player 2
        if (self.gameBoard[2][0] == self.minplayer and self.gameBoard[3][1] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer and self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][0] == self.minplayer and self.gameBoard[2][1] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][1] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer and self.gameBoard[5][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][0] == self.minplayer and self.gameBoard[1][1] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][1] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer and self.gameBoard[5][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][1] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][2] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer and self.gameBoard[4][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][5] == self.minplayer and self.gameBoard[5][6] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][2] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][5] == self.minplayer and self.gameBoard[4][6] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][6] == self.minplayer):
            self.minplayerscore += 1

        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][1] == self.minplayer and self.gameBoard[3][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][4] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][1] == self.minplayer and self.gameBoard[4][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][5] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][4] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][1] == self.minplayer and self.gameBoard[5][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][6] == self.minplayer and self.gameBoard[1][5] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][5] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer and self.gameBoard[5][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][6] == self.minplayer and self.gameBoard[2][5] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer and self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer and self.gameBoard[5][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][6] == self.minplayer and self.gameBoard[3][5] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer and self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 1

        #print 'Score 1: ', self.player1Score
        #print 'Score 2: ', self.player2Score

    def placePiece(self,column):
        temp = deepcopy(self)
        if temp.isvalidMove(column):
            for row in range(5,-1, -1):
                if temp.gameBoard[row][column] == 0:
                    temp.gameBoard[row][column] = temp.playerturn
                    if temp.playerturn == temp.maxplayer:
                        temp.playerturn = temp.minplayer
                    else:
                        temp.playerturn = temp.maxplayer
                    break
        else:
            print "Invalid move"
            return False, self
        return True, temp

    def utilityfunction(self):
        #self.printGameBoard()
        self.countScore()
        return self.maxplayerscore - self.minplayerscore

    def getmaxplayerscore(self):
        #self.countScore()
        self.countScore_depthLimit()
        return self.maxplayerscore - self.minplayerscore

    def countScore_depthLimit(self):
        self.maxplayerscore = 0;
        self.minplayerscore = 0;

        # Check horizontally
        for row in self.gameBoard:
            # Check player 1
            if row[0:4] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[1:5] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[2:6] == [self.maxplayer]*4:
                self.maxplayerscore += 1
            if row[3:7] == [self.maxplayer]*4:
                self.maxplayerscore += 1

            if row[0:3] == [self.maxplayer]*3:
                self.maxplayerscore += 0.75
            if row[1:4] == [self.maxplayer]*3:
                self.maxplayerscore += 0.75
            if row[2:5] == [self.maxplayer]*3:
                self.maxplayerscore += 0.75
            if row[3:6] == [self.maxplayer]*3:
                self.maxplayerscore += 0.75

            '''if row[0:2] == [self.maxplayer]*2:
                self.maxplayerscore += 0.5
            if row[1:3] == [self.maxplayer]*2:
                self.maxplayerscore += 0.5
            if row[2:4] == [self.maxplayer]*2:
                self.maxplayerscore += 0.5
            if row[3:5] == [self.maxplayer]*2:
                self.maxplayerscore += 0.5'''

            # Check player 2
            if row[0:4] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[1:5] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[2:6] == [self.minplayer]*4:
                self.minplayerscore += 1
            if row[3:7] == [self.minplayer]*4:
                self.minplayerscore += 1

            if row[0:3] == [self.minplayer]*3:
                self.minplayerscore += 0.75
            if row[1:4] == [self.minplayer]*3:
                self.minplayerscore += 0.75
            if row[2:4] == [self.minplayer]*3:
                self.minplayerscore += 0.75
            if row[3:5] == [self.minplayer]*3:
                self.minplayerscore += 0.75

            '''if row[0:2] == [self.minplayer]*2:
                self.minplayerscore += 0.5
            if row[1:3] == [self.minplayer]*2:
                self.minplayerscore += 0.5
            if row[2:4] == [self.minplayer]*2:
                self.minplayerscore += 0.5
            if row[3:5] == [self.minplayer]*2:
                self.minplayerscore += 0.5'''

        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.gameBoard[0][j] == self.maxplayer and self.gameBoard[1][j] == self.maxplayer and
                   self.gameBoard[2][j] == self.maxplayer and self.gameBoard[3][j] == self.maxplayer):
                self.maxplayerscore += 1
            if (self.gameBoard[1][j] == self.maxplayer and self.gameBoard[2][j] == self.maxplayer and
                   self.gameBoard[3][j] == self.maxplayer and self.gameBoard[4][j] == self.maxplayer):
                self.maxplayerscore += 1
            if (self.gameBoard[2][j] == self.maxplayer and self.gameBoard[3][j] == self.maxplayer and
                   self.gameBoard[4][j] == self.maxplayer and self.gameBoard[5][j] == self.maxplayer):
                self.maxplayerscore += 1

            if (self.gameBoard[0][j] == self.maxplayer and self.gameBoard[1][j] == self.maxplayer and
                   self.gameBoard[2][j] == self.maxplayer):
                self.maxplayerscore += 0.75
            if (self.gameBoard[1][j] == self.maxplayer and self.gameBoard[2][j] == self.maxplayer and
                   self.gameBoard[3][j] == self.maxplayer):
                self.maxplayerscore += 0.75
            if (self.gameBoard[2][j] == self.maxplayer and self.gameBoard[3][j] == self.maxplayer and
                   self.gameBoard[4][j] == self.maxplayer):
                self.maxplayerscore += 0.75
            if (self.gameBoard[3][j] == self.maxplayer and self.gameBoard[4][j] == self.maxplayer and
                   self.gameBoard[5][j] == self.maxplayer):
                self.maxplayerscore += 0.75
            # Check player 2
            if (self.gameBoard[0][j] == self.minplayer and self.gameBoard[1][j] == self.minplayer and
                   self.gameBoard[2][j] == self.minplayer and self.gameBoard[3][j] == self.minplayer):
                self.minplayerscore += 1
            if (self.gameBoard[1][j] == self.minplayer and self.gameBoard[2][j] == self.minplayer and
                   self.gameBoard[3][j] == self.minplayer and self.gameBoard[4][j] == self.minplayer):
                self.minplayerscore += 1
            if (self.gameBoard[2][j] == self.minplayer and self.gameBoard[3][j] == self.minplayer and
                   self.gameBoard[4][j] == self.minplayer and self.gameBoard[5][j] == self.minplayer):
                self.minplayerscore += 1

            if (self.gameBoard[0][j] == self.minplayer and self.gameBoard[1][j] == self.minplayer and
                   self.gameBoard[2][j] == self.minplayer):
                self.minplayerscore += 0.75
            if (self.gameBoard[1][j] == self.minplayer and self.gameBoard[2][j] == self.minplayer and
                   self.gameBoard[3][j] == self.minplayer):
                self.minplayerscore += 0.75
            if (self.gameBoard[2][j] == self.minplayer and self.gameBoard[3][j] == self.minplayer and
                   self.gameBoard[4][j] == self.minplayer):
                self.minplayerscore += 0.75
            if (self.gameBoard[3][j] == self.minplayer and self.gameBoard[4][j] == self.minplayer and
                   self.gameBoard[5][j] == self.minplayer):
                self.minplayerscore += 0.75

        # Check diagonally

        # Check player 1
        if (self.gameBoard[2][0] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer and self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][0] == self.maxplayer and self.gameBoard[2][1] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][1] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer and self.gameBoard[5][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][0] == self.maxplayer and self.gameBoard[1][1] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][1] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer and self.gameBoard[5][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][1] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][2] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][5] == self.maxplayer and self.gameBoard[5][6] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][2] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][5] == self.maxplayer and self.gameBoard[4][6] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][5] == self.maxplayer and self.gameBoard[3][6] == self.maxplayer):
            self.maxplayerscore += 1

        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][1] == self.maxplayer and self.gameBoard[3][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][4] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][1] == self.maxplayer and self.gameBoard[4][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][5] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][4] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][1] == self.maxplayer and self.gameBoard[5][0] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[0][6] == self.maxplayer and self.gameBoard[1][5] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][5] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer and self.gameBoard[5][1] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[1][6] == self.maxplayer and self.gameBoard[2][5] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][5] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer and self.gameBoard[5][2] == self.maxplayer):
            self.maxplayerscore += 1
        if (self.gameBoard[2][6] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer and self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 1

        ###############################################################
        if (self.gameBoard[3][0] == self.maxplayer and self.gameBoard[4][1] == self.maxplayer and
               self.gameBoard[5][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][0] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][1] == self.maxplayer and self.gameBoard[4][2] == self.maxplayer and
                     self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][0] == self.maxplayer and self.gameBoard[2][1] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][1] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer and
            self.gameBoard[5][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][0] == self.maxplayer and self.gameBoard[1][1] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][1] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][4] == self.maxplayer and
            self.gameBoard[5][5] == self.maxplayer ):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][1] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][2] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][5] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][5] == self.maxplayer and
            self.gameBoard[5][6] == self.maxplayer ):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][2] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][5] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer and
            self.gameBoard[4][6] == self.maxplayer ):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][5] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][4] == self.maxplayer and self.gameBoard[2][5] == self.maxplayer and
            self.gameBoard[3][6] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][4] == self.maxplayer and self.gameBoard[1][5] == self.maxplayer and
            self.gameBoard[2][6] == self.maxplayer):
            self.maxplayerscore += 0.75

        if (self.gameBoard[0][2] == self.maxplayer and self.gameBoard[1][1] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][3] == self.maxplayer and self.gameBoard[1][2] == self.maxplayer and
               self.gameBoard[2][1] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][2] == self.maxplayer and self.gameBoard[2][1] == self.maxplayer and
            self.gameBoard[3][0] == self.maxplayer ):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][4] == self.maxplayer and self.gameBoard[1][3] == self.maxplayer and
               self.gameBoard[2][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][3] == self.maxplayer and self.gameBoard[2][2] == self.maxplayer and
               self.gameBoard[3][1] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][2] == self.maxplayer and self.gameBoard[3][1] == self.maxplayer and
            self.gameBoard[4][0] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][5] == self.maxplayer and self.gameBoard[1][4] == self.maxplayer and
               self.gameBoard[2][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][4] == self.maxplayer and self.gameBoard[2][3] == self.maxplayer and
               self.gameBoard[3][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][3] == self.maxplayer and self.gameBoard[3][2] == self.maxplayer and
               self.gameBoard[4][1] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][2] == self.maxplayer and self.gameBoard[4][1] == self.maxplayer and
            self.gameBoard[5][0] == self.maxplayer ):
            self.maxplayerscore += 0.75
        if (self.gameBoard[0][6] == self.maxplayer and self.gameBoard[1][5] == self.maxplayer and
               self.gameBoard[2][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][5] == self.maxplayer and self.gameBoard[2][4] == self.maxplayer and
               self.gameBoard[3][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][4] == self.maxplayer and self.gameBoard[3][3] == self.maxplayer and
               self.gameBoard[4][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][3] == self.maxplayer and self.gameBoard[4][2] == self.maxplayer and
            self.gameBoard[5][1] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[1][6] == self.maxplayer and self.gameBoard[2][5] == self.maxplayer and
               self.gameBoard[3][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][5] == self.maxplayer and self.gameBoard[3][4] == self.maxplayer and
               self.gameBoard[4][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][4] == self.maxplayer and self.gameBoard[4][3] == self.maxplayer and
               self.gameBoard[5][2] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[2][6] == self.maxplayer and self.gameBoard[3][5] == self.maxplayer and
               self.gameBoard[4][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][5] == self.maxplayer and self.gameBoard[4][4] == self.maxplayer and
            self.gameBoard[5][3] == self.maxplayer):
            self.maxplayerscore += 0.75
        if (self.gameBoard[3][6] == self.maxplayer and self.gameBoard[4][5] == self.maxplayer and
               self.gameBoard[5][4] == self.maxplayer):
            self.maxplayerscore += 0.75
        ##############################################################

        # Check player 2
        if (self.gameBoard[2][0] == self.minplayer and self.gameBoard[3][1] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer and self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][0] == self.minplayer and self.gameBoard[2][1] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][1] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer and self.gameBoard[5][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][0] == self.minplayer and self.gameBoard[1][1] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][1] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer and self.gameBoard[5][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][1] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][4] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][2] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer and self.gameBoard[4][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][5] == self.minplayer and self.gameBoard[5][6] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][2] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][5] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][5] == self.minplayer and self.gameBoard[4][6] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][6] == self.minplayer):
            self.minplayerscore += 1

        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][1] == self.minplayer and self.gameBoard[3][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][4] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][1] == self.minplayer and self.gameBoard[4][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][5] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][4] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][1] == self.minplayer and self.gameBoard[5][0] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[0][6] == self.minplayer and self.gameBoard[1][5] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][5] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer and self.gameBoard[5][1] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[1][6] == self.minplayer and self.gameBoard[2][5] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer and self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer and self.gameBoard[5][2] == self.minplayer):
            self.minplayerscore += 1
        if (self.gameBoard[2][6] == self.minplayer and self.gameBoard[3][5] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer and self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 1

         ###############################################################
        if (self.gameBoard[3][0] == self.minplayer and self.gameBoard[4][1] == self.minplayer and
               self.gameBoard[5][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][0] == self.minplayer and self.gameBoard[3][1] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][1] == self.minplayer and self.gameBoard[4][2] == self.minplayer and
                     self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][0] == self.minplayer and self.gameBoard[2][1] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][1] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][3] == self.minplayer and
            self.gameBoard[5][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][0] == self.minplayer and self.gameBoard[1][1] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][1] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][4] == self.minplayer and
            self.gameBoard[5][5] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][1] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][2] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][5] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][4] == self.minplayer and self.gameBoard[4][5] == self.minplayer and
            self.gameBoard[5][6] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][2] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][5] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][5] == self.minplayer and
            self.gameBoard[4][6] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][5] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][4] == self.minplayer and self.gameBoard[2][5] == self.minplayer and
            self.gameBoard[3][6] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][4] == self.minplayer and self.gameBoard[1][5] == self.minplayer and
            self.gameBoard[2][6] == self.minplayer):
            self.minplayerscore += 0.75

        if (self.gameBoard[0][2] == self.minplayer and self.gameBoard[1][1] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][3] == self.minplayer and self.gameBoard[1][2] == self.minplayer and
               self.gameBoard[2][1] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][2] == self.minplayer and self.gameBoard[2][1] == self.minplayer and
            self.gameBoard[3][0] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][4] == self.minplayer and self.gameBoard[1][3] == self.minplayer and
               self.gameBoard[2][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][3] == self.minplayer and self.gameBoard[2][2] == self.minplayer and
               self.gameBoard[3][1] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][2] == self.minplayer and self.gameBoard[3][1] == self.minplayer and
            self.gameBoard[4][0] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][5] == self.minplayer and self.gameBoard[1][4] == self.minplayer and
               self.gameBoard[2][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][4] == self.minplayer and self.gameBoard[2][3] == self.minplayer and
               self.gameBoard[3][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][3] == self.minplayer and self.gameBoard[3][2] == self.minplayer and
               self.gameBoard[4][1] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][2] == self.minplayer and self.gameBoard[4][1] == self.minplayer and
            self.gameBoard[5][0] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[0][6] == self.minplayer and self.gameBoard[1][5] == self.minplayer and
               self.gameBoard[2][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][5] == self.minplayer and self.gameBoard[2][4] == self.minplayer and
               self.gameBoard[3][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][4] == self.minplayer and self.gameBoard[3][3] == self.minplayer and
               self.gameBoard[4][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][3] == self.minplayer and self.gameBoard[4][2] == self.minplayer and
            self.gameBoard[5][1] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[1][6] == self.minplayer and self.gameBoard[2][5] == self.minplayer and
               self.gameBoard[3][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[4][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][5] == self.minplayer and self.gameBoard[3][4] == self.minplayer and
               self.gameBoard[5][2] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[2][6] == self.minplayer and self.gameBoard[3][5] == self.minplayer and
               self.gameBoard[4][4] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][5] == self.minplayer and self.gameBoard[4][4] == self.minplayer and
            self.gameBoard[5][3] == self.minplayer):
            self.minplayerscore += 0.75
        if (self.gameBoard[3][6] == self.minplayer and self.gameBoard[4][5] == self.minplayer and
               self.gameBoard[5][4] == self.minplayer):
            self.minplayerscore += 0.75
        ##############################################################


def test():
    board = Gameboard()
    #board.printGameBoard()
    board.getpieceCount()
    print board.pieceCount
    board.setboardfromfile('input.txt')
    board.printGameBoard()
    board.countScore()
    #print board.player1Score
    #print board.player2Score
    board.placePiece(0)
    board.printGameBoard()
    board.countScore()
    board.outputboardtofile()
    #print board.player1Score

#test()
