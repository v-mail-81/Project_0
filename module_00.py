#!/usr/bin/env python
# coding: utf-8

# In[79]:


'''Загружаем модуль numpy для работы со случайными числами и массивом из них'''
import numpy as np


'''Определяем функцию game_core_v2 с аргументом number (загаданное число), которая будет угадывать число'''
def game_core_v2(number):
  '''Первой попыткой предполагаем число 50, объявляя для этого переменную predict, 
  затем в зависимости от того, больше оно или меньше загаданного, изменяем предполагаемое число на шаг step,
  который с увеличением числа попыток на 1 уменьшается в 2 раза. Функция принимает загаданное число и
  возвращает число попыток'''
  predict = 50
  count = 1
  step = 51
  while number != predict:
      count += 1
      step = round(step / 2)
      if predict < number:
          predict += step
      elif predict > number:
          predict -= step
  return(count)
      

  '''Определяем функцию score_game, которая будет 1000 раз генерировать случайное число. 
  Функция принимает результат работы функции game_core_v2 и возвращает среднее количество попыток за заданное число повторов (1000)'''
def score_game(game_core_v2):
  count_ls = []
  np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
  random_array = np.random.randint(1,101, size=(1000))
  for number in random_array:
      count_ls.append(game_core_v2(number))
      #print(game_core_v2(number)) #эта часть кода выводит на экран число попыток для каждого повтора работы программы
      #print(len(count_ls)) #эта часть кода печатает номер текущей попытки (через длину списка)
  score = int(np.mean(count_ls)) #эта часть кода находит среднее количество попыток за 1000 повторов
  print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
  return(score)
score_game(game_core_v2)

