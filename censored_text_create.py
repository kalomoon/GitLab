#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def text_create(name,msg):
	desktop_path = 'D://Project/GitLab/Test/'
	full_path = desktop_path + name + '.txt'
	file = open(full_path,'w')
	file.write(msg)
	file.close()
	print('Done')

#text_create('hello','hello')

def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
	return word.replace(censored_word, changed_word)

#print (text_filter('Python is lame!'))

def censored_text_create(name,msg):
	clean_msg = text_filter(msg)
	text_create(name,clean_msg)

censored_text_create('Try','lame!lame!lame!')