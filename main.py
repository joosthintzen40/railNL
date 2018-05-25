# Hintzen, Joost - 10434143
# Heijningen, Rutger van - 10272224
# Kemmere, Simon - 10798250
#
# Script that calls every needed algorithm as per the input of the user.
# Main.py is in such a way defined that there should be no need for the user
# to look in the algorithm files and make changes. Main.py (and all other files)
# should be compatible for every OS.

from Python_files.Greedy import graph_Simon2, run_greedy
from Python_files.Dijkstra import dijkstra, run_greedy_dijkstra
from Data.datastructuur_graph import Graph
from Python_files.Random import run_random_algorithm, random_algorithm
from Python_files.Hillclimber import run_hillclimbing_algorithm, hillclimber_algorithm
import csv
from itertools import chain
import copy
import sys
import random
import os


print('-'*100)
print('Welcome to the RailNL case, please fill in the following options.')
print('-'*100)
print('\n\n')


# files that are to be loaded
connectionsHolland = 'Data/ConnectiesHolland.csv'
connectionsNationaal = 'Data/ConnectiesNationaal.csv'
stationsHolland = 'Data/StationsHolland.csv'
stationsNationaal = 'Data/StationsNationaal.csv'
train_north = 'How many trains do you want to use? It is only possible to choose a number between 1 and 7'
train_holland = 'How many trains do you want to use? It is only possible to choose a number between 1 and 20'
text_maps = 'Which map do you want to use? \n For the map of North and South Holland choose "North" \n For the map of whole of the Netherlands choose "NL"'


# the way main.py is run
while True:
    print('please fill in which algorithm you want to choose: \n\
    ' + '-'*100 + '\n For the Dijkstra Algorithm choose "a" \n For the Greedy Algorithm \
    choose "b" \n For the Hillclimber Algorithm choose "c" \n For the Random Algorithm choose "d" \n ')
    algorithm = input()

    # based on input certain functions from helperfiles are called
    # to let the chosen algorithm run
    if algorithm == "a":
        print(text_maps)
        while True:
            maps = input()
            if maps == 'North':
                print(train_north)
                while True:
                    train_dijkstra = int(input())
                    if train_dijkstra > 7 or train_dijkstra < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        holland = dijkstra.Holland(train_dijkstra, connectionsHolland)
                        run_greedy_dijkstra.run_greedy(connectionsHolland, holland)
                        break

                break

            # based on input certain functions from helperfiles are called
            # to let the chosen algorithm run
            elif maps == 'NL':
                print(train_holland)
                while True:
                    train_dijkstra = int(input())
                    if train_dijkstra > 20 or train_dijkstra < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        nationaal = dijkstra.Holland(train_dijkstra, connectionsNationaal)
                        run_greedy_dijkstra.run_greedy(connectionsNationaal, nationaal)
                        break

                break
            else:
                print('try again')
                continue

    # based on input certain functions from helperfiles are called
    # to let the chosen algorithm run
    elif algorithm == "b":
        print(text_maps)
        while True:
            maps = input()
            if maps == 'North':
                print(train_north)
                while True:
                    train_greedy = int(input())
                    if train_greedy > 7 or train_greedy < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        holland = graph_Simon2.Holland(train_greedy, connectionsHolland)
                        run_greedy.run_greedy(connectionsHolland, holland)
                        break

                break

            # based on input certain functions from helperfiles are called
            # to let the chosen algorithm run
            elif maps == 'NL':
                print(train_holland)
                while True:
                    train_greedy = int(input())
                    if train_greedy > 20 or train_greedy < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        nationaal = graph_Simon2.Holland(train_greedy, connectionsNationaal)
                        run_greedy.run_greedy(connectionsNationaal, nationaal)
                        break

                break
            else:
                print('try again')
                continue

    # based on input certain functions from helperfiles are called
    # to let the chosen algorithm run
    elif algorithm == "c":
        print(text_maps)
        while True:
            maps = input()
            if maps == 'North':
                print(train_north)
                while True:
                    train_hillclimber = int(input())
                    if train_hillclimber > 7 or train_hillclimber < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        totaal = run_hillclimbing_algorithm.load_map(connectionsHolland)
                        hillclimber_algorithm.main(maps, train_hillclimber, totaal)
                        break

                break

            # based on input certain functions from helperfiles are called
            # to let the chosen algorithm run
            elif maps == 'NL':
                print(train_holland)
                while True:
                    train_hillclimber = int(input())
                    if train_hillclimber > 20 or train_hillclimber < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        totaal = run_hillclimbing_algorithm.load_map(connectionsNationaal)
                        hillclimber_algorithm.main(maps, train_hillclimber, totaal)
                        break

                break
            else:
                print('try again')
                continue

    # based on input certain functions from helperfiles are called
    # to let the chosen algorithm run
    elif algorithm == "d":
        print(text_maps)
        while True:
            maps = input()
            if maps == 'North':
                print(train_north)
                while True:
                    train_random = int(input())
                    if train_random > 7 or train_random < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        totaal = run_random_algorithm.load_map(connectionsHolland)
                        random_algorithm.main(maps, train_random, totaal)
                        break

                break

            # based on input certain functions from helperfiles are called
            # to let the chosen algorithm run
            elif maps == 'NL':
                print(train_holland)
                while True:
                    train_random = int(input())
                    if train_random > 20 or train_random < 1:
                        print('try again')
                        continue
                    else:
                        os.system('cls')
                        os.system('clear')
                        totaal = run_random_algorithm.load_map(connectionsNationaal)
                        random_algorithm.main(maps, train_random, totaal)
                        break
                break

            else:
                print('try again')
                continue
