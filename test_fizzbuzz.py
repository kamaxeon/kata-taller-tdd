#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from fizzbuzz import FizzBuzz

class FizzBuzzSould(unittest.TestCase):

 '''
 +     * TODO: para un número devuelve una secuencia desde el número 1 hasta el input
 +     * TODO: la secuencia debe estar parseada por las siguientes reglas
 +     *  cuando un número no es divisible por 2 ni 3 devolvemos el número
 +     *  cuando un número es divisible por 2 remplazamos por Fizz
 +     *  cuando un número es divisible por 3 remplazamos por Buzz
 +     *  cuando un número es divisible por 2 y 3 remplazamos por FizzBuzz
 +     *
 +     *  Examples:
 +     *   1 => 1 (porque no es divisible ni por 2 ni por 3)
 +     *   2 => 1\Fizz (porque 2 es divisible por 2)
 +     *   3 => 1\Fizz\Buzz (porque 2 es divisible por 2)
 +     *   6 => 1\Fizz\Buzz\Fizz\5\FizzBuzz
 '''
 def test_not_parse_numbers_when_they_are_not_divisible_by_two_or_three(self):
    self.assertEqual(FizzBuzz(1).parse(), '1\n')

 def test_parse_numbers_divisible_by_two_to_fizz(self):
    self.assertEqual(FizzBuzz(2).parse(), '1\nFizz\n')

 def test_parse_numbers_divisible_by_three_to_fizz(self):
    self.assertEqual(FizzBuzz(3).parse(), '1\nFizz\nBuzz\n')

 def test_parse_numbers_divisible_by_two_and_three_to_fizzbuzz(self):
    self.assertEqual(FizzBuzz(6).parse(), '1\nFizz\nBuzz\nFizz\n5\nFizzBuzz\n')

if __name__ == '__main__':
  unittest.main()
