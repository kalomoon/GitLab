#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ln_path = 'D://Project/GitLab/Test/last_name.txt'
fn_path = 'D://Project/GitLab/Test/first_name.txt'
fnt = []
ln1t = []
ln2t = []

with open(fn_path, 'r') as f:
	for line in f.readlines():
		fnt.append(line.split('\n')[0])
fn = tuple(fnt.copy())

with open(ln_path, 'r') as f:
	for line in f.readlines():
		if len(line.split('\n')[0]) == 1:
			ln1t.append(line.split('\n')[0])
		else:
			ln2t.append(line.split('\n')[0])

ln1 = tuple(ln1t.copy())
ln2 = tuple(ln2t.copy())

class FakeUser():
	def fake_name(self,amount=1,one_word=False,two_words=False):
		n = 0
		while n <= amount:
			if one_word:
				full_name = random.choice(fn) + random.choice(ln1)
			elif two_words:
				full_name = random.choice(fn) + random.choice(ln2)
			else:
				full_name = random.choice(fn) + random.choice(ln1 + ln2)
			yield full_name
			n += 1

	def fake_gender(self, amount=1):
		n = 0
		while n <= amount:
			gender = random.choice(['男','女','未知'])
			yield gender
			n += 1

class SnsUser(FakeUser):
	def get_followers(self,amount=1,few=True,a_lot=False):
		n = 0
		while n <= amount :
			if few:
				followers = random.randrange(1,50)
			elif a_lot:
				followers = random.randrange(200,10000)
			yield followers
			n += 1

user_a = FakeUser()
user_b = SnsUser()
for name in user_a.fake_name(30):
	print(name)
for gender in user_a.fake_gender(30):
	print(gender)
