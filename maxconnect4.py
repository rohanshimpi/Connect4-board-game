import Gameboard as g
import sys
import time

depth_limit = 0
computer_tournament = 0
human_tournament = 0

class MaxPlayer:

    initial_gameboard = None
    def __init__(self):
        initial_gameboard = g.Gameboard()

    def setInitailState(self,inputfile,mode,player_next):
        self.initial_gameboard = g.Gameboard()
        self.initial_gameboard.setboardfromfile(inputfile,mode,player_next)
        self.initial_gameboard.printGameBoard()
        return self.initial_gameboard

    def minmax_decision(self, initial_gameboard):
        c = 42 - initial_gameboard.getpieceCount()
        move = -1
        score = 0
        #final_move = 0
        start = time.time()
        #rohan = initial_gameboard.numberofpossibleColumns()
        map = self.successor_function(initial_gameboard)
        v = float(-100000)
        depth = 1
        alpha = -100000
        beta = 100000
        for key in map.iterkeys():
            temp = self.min_value(map[key], alpha, beta, depth)
            if temp >= v:
                v = temp
                move = key
        end = time.time()
        print 'Time required:', (end-start)
        #print 'move: ', move+1
        #print 'Score:', v
        isvalid, temp = initial_gameboard.placePiece(move)
        return temp, move

    def max_value(self,current_gameboard, alpha, beta, depth):
        v = float(-100000)
        #move = -1
        piece_count = current_gameboard.getpieceCount()
        if piece_count == 42:
            r = current_gameboard.utilityfunction()
            return r
        elif depth == globals()['depth_limit']:
            limit_score = current_gameboard.getmaxplayerscore()
            return limit_score
        else:
            depth = depth + 1
            map = self.successor_function(current_gameboard)
            for key in map.iterkeys():
                board = map[key]
                temp = self.min_value(board, alpha, beta, depth)
                if temp >= v:
                    v = temp
                    move = key
                if v >= beta:
                    #print 'in max prune'
                    return v
                alpha = max(alpha, v)
            return v

    def min_value(self, current_gameboard, alpha, beta, depth):
        v = float('inf')
        piece_count = current_gameboard.getpieceCount()
        if piece_count == 42:
            r = current_gameboard.utilityfunction()
            return r
        if depth == globals()['depth_limit']:
            limit_score = current_gameboard.getmaxplayerscore()
            return limit_score
        else:
            depth = depth + 1
            map = self.successor_function(current_gameboard)
            for key in map.iterkeys():
                board = map[key]
                temp = self.max_value(board, alpha, beta, depth)
                if temp <= v:
                    v = temp
                    move = key
                if v <= alpha:
                    return  v
                beta = min(beta, v)
            return v

    def successor_function(self, gameboard):
        map = {}
        count = 42 - gameboard.getpieceCount()
        rohan = gameboard.numberofpossibleColumns()
        for i in range(len(rohan)):
            move = rohan.pop()
            is_valid, new_gameboard = gameboard.placePiece(move)
            map[move] = new_gameboard
        return map


def main(argv):
    mode = argv[1]
    input_file = ''
    output_file = ''
    #depth = 0
    player_next = ''

    if mode == 'one-move':
        input_file = argv[2]
        output_file = argv[3]
        globals()['depth_limit'] = int(argv[4])
        player = MaxPlayer()
        t = player.setInitailState(input_file,mode,player_next)
        #start = time.time()
        temp, move = player.minmax_decision(t)
        print 'Move played: ', move+1
        print 'Game board after move:'
        temp.printGameBoard()
        temp.outputboardtofile(output_file)
        #print end - start

    elif mode == 'interactive':
        input_file = argv[2]
        player_next = argv[3]
        globals()['depth_limit'] = int(argv[4])
        player = MaxPlayer()
        t = player.setInitailState(input_file,mode,player_next)
        while True:
            count = t.getpieceCount()
            if count == 42:
                t.countScore()
                print 'Computer Score:', t.maxplayerscore
                print 'Your score: ', t.minplayerscore

                break
            if player_next == 'human-next':
                t.countScore()
                t.printGameBoard()
                print 'Computer Score:', t.maxplayerscore
                print 'Your score: ', t.minplayerscore
                print "Enter column between 1 and 7:"
                human_move = int(raw_input())
                while human_move<1 or human_move>7:
                    print "Enter column between 1 and 7:"
                    human_move = int(raw_input())
                is_valid, t = t.placePiece(human_move-1)
                while not is_valid:
                    print "Enter column between 1 and 7:"
                    human_move = int(raw_input())
                    is_valid, t = t.placePiece(human_move-1)
                #t.printGameBoard()
                t.outputboardtofile('human.txt')
                player_next = 'computer-next'
            #if player_next == 'computer-next':
            else:
                t, move = player.minmax_decision(t)
                t.printGameBoard()
                t.countScore()
                print 'Computer Score:', t.maxplayerscore
                print 'Your score: ', t.minplayerscore
                t.outputboardtofile('computer.txt')
                player_next = 'human-next'

if __name__ == '__main__':
    main(sys.argv)