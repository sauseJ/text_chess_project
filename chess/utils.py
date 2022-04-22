import random

def register_user(user):
    user.name = input('Stage your name: ')
    user.age = input('Stage your age too: ')
    user.sexual_orientation = input('Are you gay or something? ')
    print('Enjoy terminal chess!')

def random_side(user1, user2):
    i = random.randint(0, 1)
    if i == 1:
        user1.color = 'w'
        user1.my_turn = True
        user2.color = 'b'
        user2.my_turn = False
        print(f'Looks like it\'s {user1.name}\'s turn to move now!')
    else:
        user1.color = 'b'
        user1.my_turn = False
        user2.color = 'w'
        user2.my_turn = True
        print(f'Looks like it\'s {user2.name}\'s turn to move now!')

def figure_check(move, user):
    letter = move[0]
    if letter == 'B':
        pass


def action(user):
    move = input(f'{user.name}, what\'s your move then: ')
    figure = figure_check(move, user)



        
