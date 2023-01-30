# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

total_candies = 150

def toss():
 toss_number = random.randint(1,2)
 if toss_number == 1:
   player1_move()
 else:
   player2_move()


def player1_move():
 global total_candies

 print(f'Сейчас ходит ИГРОК2. Осталось {total_candies} конфет')
 take_candies = int(input('Сколько конфет вы хотите взять?'))
 while take_candies > 28:
      take_candies = int(input('Вы взяли больше 28 конфет.\nСколько конфет вы хотите взять?'))     
 total_candies -= take_candies
 if total_candies > 0:
  player2_move()
 else:        
  print('Победил ИГРОК1')


def player2_move():
 global total_candies

 print(f'Сейчас ходит ИГРОК1. Осталось {total_candies} конфет')
 take_candies = int(input('Сколько конфет вы хотите взять?'))
 while take_candies > 28:
      take_candies = int(input('Вы взяли больше 28 конфет.\nСколько конфет вы хотите взять?'))
 total_candies -= take_candies
 if total_candies > 0:
  player1_move()
 else:        
  print('Победил ИГРОК2')

toss()