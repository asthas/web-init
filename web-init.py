#!/usr/local/bin/python3

from os import system as run
from os import chdir as cd
from sys import argv

user = input('Enter github username: ')

if len(argv) == 1:
	name = input('Enter name of project: ')
else:
	name = argv[1]

def setup_bower():
	bowerrc = open('app/.bowerrc', 'w+')
	bowerrc.write('{"directory": "lib"}\n')

def setup_gitignore():
	cd('app')
	run('curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Node.gitignore')	
	gitignore = open(name + '.gitignore', 'a')
	gitignore.write('lib\n')

commands = [
	"curl -u '" + user + "' https://api.github.com/user/repos -d '{\"name\":\"" + name + "\"}'",
	'mkdir app',
	'touch README'
	'git init',
	"git remote add origin https://github.com/" + user + "/" + name + ".git",
	'touch app/.bowerrc'
	'touch app/index.html'
	'mkdir app/css',
	'touch app/css/main.css',
	'mkdir app/js',
	'touch app/js/main.js',
	'mkdir app/lib',
	'mkdir app/img',
]

run('mkdir ' + name)
cd(name)

for command in commands:
	print(command)
	run(command)

setup_bower()
setup_gitignore()

