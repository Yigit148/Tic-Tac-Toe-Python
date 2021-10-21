#Tic-Tac-Toe
import sys
import string

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to be x or o" % user1)

print(
"""
1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
""")



game_board = ('''
1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9
''')

user_1_sign = user1_answer
if user_1_sign == "x":
    user_2_sign = "o"
else:
    user_2_sign = "x"

def game():
        x = int(input(user1 + " Choose a place "))
        new_board = game_board.replace(str(x), user_1_sign)
        print(new_board)

        y = int(input(user2 + " Choose a place "))
        new_board1 = new_board.replace(str(y), user_2_sign)
        print(new_board1)

        x = int(input(user1 + " Choose a place "))
        new_board2 = new_board1.replace(str(x), user_1_sign)
        print(new_board2)

        y = int(input(user2 + " Choose a place "))
        new_board3 = new_board2.replace(str(y), user_2_sign)
        print(new_board3)

        x = int(input(user1 + " Choose a place "))
        new_board4 = new_board3.replace(str(x), user_1_sign)
        print(new_board4)

        y = int(input(user2 + " Choose a place "))
        new_board5 = new_board4.replace(str(y), user_2_sign)
        print(new_board5)

        x = int(input(user1 + " Choose a place "))
        new_board6 = new_board5.replace(str(x), user_1_sign)
        print(new_board6)

        y = int(input(user2 + " Choose a place "))
        new_board7 = new_board6.replace(str(y), user_2_sign)
        print(new_board7)

        x = int(input(user1 + " Choose a place "))
        new_board8 = new_board7.replace(str(x), user_1_sign)
        print(new_board8)

        final()


#1 2 3  4  5  6  7  8  9
#1 5 9 23 27 31 45 49 53

def final():
        if str(game_board[1]) == str(game_board[5]) == str(game_board[9]): # 1 2 3
                print("Game Over")
        elif str(game_board[1]) == str(game_board[27]) == str(game_board[53]): # 1 5 9
                print("Game Over")
        elif str(game_board[23]) == str(game_board[27]) == str(game_board[31]): # 4 5 6
                print("Game Over")
        elif str(game_board[45]) == str(game_board[49]) == str(game_board[53]): # 7  8  9
                print("Game Over")
        elif str(game_board[1]) == str(game_board[23]) == str(game_board[45]): # 1 4 7
                print("Game Over")
        elif str(game_board[5]) == str(game_board[27]) == str(game_board[53]): # 2 5 8
                print("Game Over")
        elif str(game_board[9]) == str(game_board[31]) == str(game_board[53]): # 3 6 9
                print("Game Over")
        elif str(game_board[9]) == str(game_board[27]) == str(game_board[49]): # 3 5 7
                print("Game Over")
        else:
                print("Its a tie")
game()

input()