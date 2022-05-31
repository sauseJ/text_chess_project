from chess import utils as u
from chess import based as b
from chess.figures import Pawn, Bishop, Knight, Rook, Queen, King


class Game:
    moves = {}
    board = b.Board()

    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    a2Pawn = Pawn.Pawn(board, 'pa2', 'w', 'a2', is_protected=True)
    b2Pawn = Pawn.Pawn(board, 'pb2', 'w', 'b2', is_protected=True)
    c2Pawn = Pawn.Pawn(board, 'pc2', 'w', 'c2', is_protected=True)
    d2Pawn = Pawn.Pawn(board, 'pd2', 'w', 'd2', is_protected=True)
    e2Pawn = Pawn.Pawn(board, 'pe2', 'w', 'e2', is_protected=True)
    f2Pawn = Pawn.Pawn(board, 'pf2', 'w', 'f2', is_protected=True)
    g2Pawn = Pawn.Pawn(board, 'pg2', 'w', 'g2', is_protected=True)
    h2Pawn = Pawn.Pawn(board, 'ph2', 'w', 'h2', is_protected=True)
    a1Rook = Rook.Rook(board, 'Ra1', 'w', 'a1', is_protected=False)
    h1Rook = Rook.Rook(board, 'Rh1', 'w', 'h1', is_protected=False)
    b1Knight = Knight.Knight(board, 'Nb1', 'w', 'b1', is_protected=True)
    g1Knight = Knight.Knight(board, 'Ng1', 'w', 'g1', is_protected=True)
    c1Bishop = Bishop.Bishop(board, 'Bc1', 'w', 'c1', is_protected=True, bcolor='b')
    f1Bishop = Bishop.Bishop(board, 'Bf1', 'w', 'f1', is_protected=True, bcolor='w')
    d1Queen = Queen.Queen(board, 'Qd1', 'w', 'd1', is_protected=True)
    e1King = King.King(board, 'Ke1', 'w', 'e1', is_protected=True)

    a7Pawn = Pawn.Pawn(board, 'pa7', 'b', 'a7', is_protected=True)
    b7Pawn = Pawn.Pawn(board, 'pb7', 'b', 'b7', is_protected=True)
    c7Pawn = Pawn.Pawn(board, 'pc7', 'b', 'c7', is_protected=True)
    d7Pawn = Pawn.Pawn(board, 'pd7', 'b', 'd7', is_protected=True)
    e7Pawn = Pawn.Pawn(board, 'pe7', 'b', 'e7', is_protected=True)
    f7Pawn = Pawn.Pawn(board, 'pf7', 'b', 'f7', is_protected=True)
    g7Pawn = Pawn.Pawn(board, 'pg7', 'b', 'g7', is_protected=True)
    h7Pawn = Pawn.Pawn(board, 'ph7', 'b', 'h7', is_protected=True)
    a8Rook = Rook.Rook(board, 'Ra8', 'b', 'a8', is_protected=False)
    h8Rook = Rook.Rook(board, 'Rh8', 'b', 'h8', is_protected=False)
    b8Knight = Knight.Knight(board, 'Nb8', 'b', 'b8', is_protected=True)
    g8Knight = Knight.Knight(board, 'Ng8', 'b', 'g8', is_protected=True)
    c8Bishop = Bishop.Bishop(board, 'Bc8', 'b', 'c8', is_protected=True, bcolor='w')
    f8Bishop = Bishop.Bishop(board, 'Bf8', 'b', 'f8', is_protected=True, bcolor='b')
    d8Queen = Queen.Queen(board, 'Qd8', 'b', 'd8', is_protected=True)
    e8King = King.King(board, 'Ke8', 'b', 'e8', is_protected=True)

    def play(self):
        turn = 0
        order = 1
        positions_list = []
        
        while True:
            self.board.refresh()
            self.e8King.am_i_in_check(self.board)
            self.e1King.am_i_in_check(self.board)

            if u.check_for_mate(self.e8King) or u.check_for_mate(self.e1King):
                print('Lmao git gud\n')
                new_game_mb = input('Would you like to start a new game?\n')
                return new_game_mb


            turner = u.check_the_turn(self.user1, self.user2)
            if u.check_for_stalemate(turner, self.board): break
            move, position = u.action(turner, self.board)
            positions_list.append(position)

            if u.checking_for_draws(turner, self.board, positions_list, self.moves) == True:
                print('1/2 bitch\n')
                new_game_mb = input('Would you like to start a new game?\n')
                return new_game_mb
    
            else:
                u.change_turn(self.user1, self.user2)
                turn += 1

                if turn % 2 != 0:
                    self.moves[str(order)] = [move]
                else:
                    self.moves[str(order)].append(move)
                    order +=1
                print(self.moves)
            
            

        for move in self.moves:
            print(move + '\n')        
        
        print('GG\n')
        new_game_mb = input('Would you like to start a new game?\n')
        return new_game_mb



user1 = b.Users()
u.register_user(user1)
user2 = b.Users()
u.register_user(user2)

is_playing = True

while is_playing == True:
    how_many_games = 0
    if how_many_games > 0:
        user1, user2 = u.change_colors(user1, user2)
        game = Game(user1, user2)
        new_game = game.play()
        if new_game == 'Yes':
            is_playing = True
            how_many_games += 1
        else:
            is_playing = False
    else:
        user1, user2 = u.random_side(user1, user2)
        game = Game(user1, user2)
        new_game = game.play()
        if new_game == 'Yes':
            is_playing = True
            how_many_games += 1
        else:
            is_playing = False
