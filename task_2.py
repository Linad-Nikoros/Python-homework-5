# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid=False
   while not valid:
     player_answer = int(input((f'Ходит игрок {player_token}. Куда вы ходите?')))
     if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print('Эта клетка уже занята')
     else:
      print('Некорректный ввод. Введите число от 1 до 9.')


def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for pos in win_coord:
       if board[pos[0]] == board[pos[1]] == board[pos[2]]:
          return board [pos[0]]
   return False

def main(board):
    num_moves = 0
    win = False
    while not win:
        draw_board(board)
        if num_moves % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        num_moves += 1
        if num_moves >= 3:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if num_moves == 9:
            print("Ничья!")
            break      
main(board)

