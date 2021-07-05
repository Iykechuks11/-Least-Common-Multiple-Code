# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 22:44:48 2021

@author: user

print("Hello, World")  

def square(n):
    return n**2

print(square(10))

def gcd(x,y):
    return gcd(y, x%y) if y else x

def lcm(x, y):
    return x*y // gcd(x,y)
"""


def lcm(a, b):
  assert a > 0 and b > 0
  return a*b // gcd(a,b)
  # Write your code here
def gcd(a, b):
  return gcd(b, a%b) if b else a

print(lcm(24, 16))