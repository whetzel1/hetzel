#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:57:39 2021

@author: williamhetzel
"""

#Q 1
x = []
res = []

while True:
    print("Press enter when you are done entering as many stocks as you'd like; simply press enter when done: ")
    watchlist = input("Enter a stock for your watch list: ")
    if watchlist == '':
        break
    x.append(watchlist)
    x.sort()
for element in x:
    if element not in res:
        res.append(element)
print(res)


#Q 2
dictionary = "Hi. I. am. Wills?!;"

x = "!,.?;"

for element in dictionary:
    if element in x:
        dictionary = dictionary.replace(element,"")
        print(dictionary)

#Q 4   
print("This program tests if two entered words are anagrams of eachother")

a = input("Please enter a word: ")
b = input("Please enter another word: ")

if sorted(a) == sorted(b):
   print("True")
if sorted(a) != sorted(b):
    print("False")

#Q 3        
empty_list = ["hi, my name is wills"]

values = [{'a':'4'}, {'e':3}, {'i':1}, {'o':'0'}, {'u':'8'}]

for keys in values:
    empty_list = empty_list.replace(values[0], values[1])
    print(empty_list)
    
    


