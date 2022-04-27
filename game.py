from numpy import Infinity
from chess.utils import Users, register_user, Game, new_game

user1 = Users()
register_user(user1)
user2 = Users()
register_user(user2)

is_playing = True

while is_playing == True:
    game = Game(user1, user2)
    new_game = game.play()
    if new_game == 'Yes':
        is_playing = True
    else:
        is_playing = False
