"""
lab3.py
Patrick Azzo
9/25/2019
"""

def my_find(word, letter):
    """
    Tests if letter is in word
    word: string
    letter: one-character string
    """
word = 'friendly'
letter = 'i'
word2 = 'insane'
letter2 = 'o'
word3 = 'tree'
letter3 = 'k'

#    str = "friendly"
#    str.find('i')
if letter in word:
    print('yes')
else:
    print('no')

if letter2 in word2:
    print('yes')
else:
    print('no')
if letter3 in word3:
    print('yes')
else:
    print('no')
      #returns {my_find('friendly','f')})


def sum_to(n):
    """
    Calculates the sum of all positive integers from 1 to number, including
    number.
    Uses the accumulator pattern.
    Do not use the formula that computes this sum.

    n: non-negative integer
    Returns: The sum of all numbers from 1 to n
"""
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for i in n:
   accum = accum + i
print(accum)
print(accum - 1)
print(accum * 2)

def sum_odd_to(n):
    """
    Calculates the sum of all odd positive integers from 1 to number.
    including number.
    Uses the accumulator pattern.

    n: non-negative integer
    Returns: the sum of all odd positive numbers from 1 to n
    """
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if n[i] % 2 != 0:
        print(i)
else:
        print('sike. thats the wrong number.')
