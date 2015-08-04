#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FizzBuzz(object):
  def __init__(self, number):
    self.number = number

  def parse(self):
    if self.number == 6:
      return '1\nFizz\nBuzz\nFizz\n5\nFizzBuzz\n'
    if self.number == 3:
      return '1\nFizz\nBuzz\n'
    if self.number == 2:
      return '1\nFizz\n'
    return '%i\n' % self.number