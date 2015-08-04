#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FizzBuzz(object):
  def __init__(self, number):
    self.number = number

  def parse(self):
    result = ''
    for i in range(1, self.number+1):
      result += self.parse_number(i)
    return result


  def parse_number(self, number):
    result = ''
    if number % 2 == 0:
      result = 'Fizz'
    if number % 3 == 0:
      result += 'Buzz'
    if result == '':
      result = '%s' % str(number)

    return result + '\n'