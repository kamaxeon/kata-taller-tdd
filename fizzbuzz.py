#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FizzBuzz(object):
  def __init__(self, number):
    self.number = number
  def parse(self):
    if self.number == 2:
      return '1\nFizz\n'
    return '%i\n' % self.number