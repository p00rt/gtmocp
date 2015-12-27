from os import system

def next(wid):
	system("mocp --next")

def prev(wid):
	system("mocp --previous")

def togg(wid):
	system("mocp --toggle-pause")
	

