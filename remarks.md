# Pentomino Tiling Solver

solve.py is a python script that finds all rectangular tilings using one set of pentominos ([Wikipedia link](https://en.wikipedia.org/wiki/Pentomino#Tiling_puzzle_(2D)))

Earlier this year, I wrote some python code while trying to learn how to use functional programming techniques.  See https://github.com/wusui/pent_func

Later, I thought that I should try to remove some of the functions by using lambda expressions.  Well, I got a little carried away and ended up with a one-liner piece of code which is now the only assignment statement in solve.py.  This is mostly a bunch of lambda expressions with recursion implemented using Y-combinator constructs.

So I decided to unleash this on the rest of the world.  I refer to it as "lambda expressions on steroids."  I had one colleague review it who said it was "lambda calculus on LSD."

I have run this on Ubuntu 20.04.6 using version 3.10.1 of python, and on Windows 11 Version 23H2 using version 3.11.1 of python.

It only requires json and itertool libraries to be imported.

To run, cd to the directory where solve.py has been downloaded and enter 'python solve.py'

The output is a file named obf_pentominos.json.

My email address is warrenusui@gmail.com.  Please do not forward this code to any authorities who are trying to collect evidence that I should be locked up...
