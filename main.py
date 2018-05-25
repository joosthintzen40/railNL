
from Python_files import Dijkstra, Greedy, Hillclimber, Random
from Python_files.Greedy import graph_Simon2
from Python_files.Greedy.critical_connections_simon import check_list
from Python_files.Data.datastructuur_graph import graph
import csv
from itertools import chain
import copy
import sys
import random



print('-'*100)
print('Welcome to the RailNL case, please fill in the following options.')
print('-'*100)
print('\n\n')


connectionsHolland = 'Data/ConnectiesHolland.csv'
connectionsNationaal = 'Data/ConnectiesNationaal.csv'
stationsHolland = 'Data/StationsHolland.csv'
stationsNationaal = 'Data/StationsNationaal.csv'


print('please fill in which algorithm you want to choose: \n\
' + '-'*100 + '\n For the Dijkstra Algorithm choose "a" \n For the Greedy Algorithm \
choose "b" \n For the Hillclimber Algorithm choose "c" \n For the Random Algorithm choose "d" \n ')
while True:
    algorithm = input()

    if algorithm == "a":
        print('a')
        break
    elif algorithm == "b":
        print('Which map do you want to use? \n For the map of North and South Holland \
choose "North" \n For the map of whole of the Netherlands choose "NL"')
        while True:
            maps = input()
            if maps == 'North':
                print('How many trains do you want to use? It is only possible to \
choose a number between 1 and 7')
                while True:
                    train_greedy = int(input())
                    if train_greedy > 10 or train_greedy < 1:
                        print('try again')
                        continue
                    else:
                        graph_Simon2.Holland(maps, train_greedy)
                        break

                    break
                break
            elif maps == 'NL':
                print('How many trains do you want to use?')
                train_greedy = input()
                break
            else:
                print('try again')
                continue



        break
    elif algorithm == "c":
        print('c')
        break
    elif algorithm == "d":
        print('d')
        break
    else:
        print('invalid answer, try again!')
        continue
