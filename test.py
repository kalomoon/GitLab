#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#4.2练习题1
def g2kg(g):
	return (str(g/1000) + 'kg')
#print(g2kg(1000))

#4.2练习题2
import math
def triangle(a,b):
	return ('The right triangle third side\'s length is {}'.format(math.sqrt(a**2+b**2)))
#print(triangle(3,4))

#梯形面积
def trapezoid_area(base_up,base_down,height):
	return (1/2 * (base_up + base_down ) * height)
base_up = 1
base_down = 2
height = 3
#print (trapezoid_area(height,base_down,base_up))

#圣诞树
#print ('  *',' * *','* * *','  |	',sep='\n')

#创建文件
def text_create(name,msg):
	desktop_path = 'D://Project/GitLab/Test/'
	full_path = desktop_path + name + '.txt'
	file = open(full_path,'w')
	file.write('msg')
	file.close()
	print('Done')
#text_create('hello','hello world')

#敏感字替换
def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
	return word.replace(censored_word, changed_word)
#print (text_filter('Python is lame!'))

# 九九乘法表
#for i in range(1,10):
#	for j in range(1,10):
#		print ('{} x {} = {}'.format(i,j,i*j))

#5.3练习题1
def cr_txt():
	name = 1
	while True:
		file = open('D://Project/GitLab/Test/' + str(name) + '.txt', 'w')
		file.write(str(name))
		file.close()
		name = name + 1
		if name > 10:
			break
#cr_txt()

#5.3练习题2
def invest(amount,rate,time):
	return ('The Final amount is {}'.format(amount*(1+rate/100)**time))
#print(invest(100,5,3))

#5.3练习题3
#for n in range(0,101):
#	if n % 2 ==0:
#		print (n)

#5.4练习题---roll.dice.py && number_test.py

#path = 'D://Project/GitLab/Test/Walden.txt'
#with open(path,'r',encoding='UTF-8') as text:
#	words = text.read().split()
#	print(words)
#	for word in words:
#		print('{}-{} times'.format(word, words.count(word)))

ln_path = 'D://Project/GitLab/Test/last_name.txt'
fn_path = 'D://Project/GitLab/Test/first_name.txt'
fnt = []
ln1t = []
ln2t = []
with open(fn_path, 'r') as f:
	for line in f.readlines():
		fnt.append(line.split('\n')[0])
fn = tuple(fnt.copy())
#print(fn)
with open(ln_path, 'r') as f:
	for line in f.readlines():
		if len(line.split('\n')[0]) == 1:
			ln1t.append(line.split('\n')[0])
		else:
			ln2t.append(line.split('\n')[0])
ln1 = tuple(ln1t.copy())
ln2 = tuple(ln2t.copy())
#print(ln1)
#print('=' * 70)
#print(ln2)

import random
class FakeUser:
	def fake_name(self,one_word=False,two_words=False):
		if one_word:
			full_name = random.choice(fn) + random.choice(ln1)
		elif two_words:
			full_name = random.choice(fn) + random.choice(ln2)
		else:
			full_name = random.choice(fn) + random.choice(ln1 + ln2)
		print(full_name)
	def fake_gender(self):
		gender = random.choice(['男','女','未知'])
		print(gender)

class SnsUser(FakeUser):
	def get_followers(self,few=False,a_lot=False):
		if few:
			followers = random.randrange(1,50)
		elif a_lot:
			followers = random.randrange(200,10000)
		print(followers)

#user_a = FakeUser()
#user_b = SnsUser()
#user_a.fake_name(two_words=True)
#user_b.get_followers(few=True)

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

def run_twice(animal):
	animal.run()
	animal.run()

a = Animal()
d = Dog()
c = Cat()

#print('a is Animal?', isinstance(a, Animal))
#print('a is Dog?', isinstance(a, Dog))
#print('a is Cat?', isinstance(a, Cat))

#print('d is Animal?', isinstance(d, Animal))
#print('d is Dog?', isinstance(d, Dog))
#print('d is Cat?', isinstance(d, Cat))

#run_twice(c)

