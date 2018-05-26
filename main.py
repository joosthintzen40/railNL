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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear && printf "\e[3j"')

print('-'*100)
print('Welcome to the RailNL case, please fill in the following options.')
print('-'*100)


# files that are to be loaded
openings_text = '\nPlease fill in which algorithm you want to choose: \n' + '-'*100 + '\nFor the Dijkstra Algorithm choose "a" \nFor the Greedy Algorithm choose "b" \nFor the Hillclimber Algorithm choose "c" \nFor the Random Algorithm choose "d" \nTo exit type exit \n '
connectionsHolland = 'Data/ConnectiesHolland.csv'
connectionsNationaal = 'Data/ConnectiesNationaal.csv'
stationsHolland = 'Data/StationsHolland.csv'
stationsNationaal = 'Data/StationsNationaal.csv'
train_north = '\nHow many trains do you want to use? It is only possible to choose a number between 1 and 7\n'
train_holland = '\nHow many trains do you want to use? It is only possible to choose a number between 1 and 20\n'
text_maps = '\nWhich map do you want to use? \n For the map of North and South Holland choose "North" \n For the map of whole of the Netherlands choose "NL"\n'
text_iterations = '\nHow many iterations would you like to run?\n'


def choose_algorithm(algorithm):
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
                    while True:
                        print(text_iterations)
                        iterations = int(input())
                        clear_screen()
                        if algorithm == 'a':
                            holland = dijkstra.Holland(train_dijkstra, connectionsHolland)
                            run_greedy_dijkstra.run_greedy(connectionsHolland, holland, iterations)
                            break
                        elif algorithm == 'b':
                            holland = graph_Simon2.Holland(train_greedy, connectionsHolland)
                            run_greedy.run_greedy(connectionsHolland, holland, iterations)
                            break
                        elif algorithm == 'c':
                            totaal = run_hillclimbing_algorithm.load_map(connectionsHolland)
                            hillclimber_algorithm.main(maps, train_hillclimber, totaal, iterations)
                            break
                        elif algorithm == 'd':
                            totaal = run_random_algorithm.load_map(connectionsHolland)
                            random_algorithm.main(maps, train_random, totaal, iterations)
                            break
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
                    while True:
                        print(text_iterations)
                        iterations = int(input())
                        clear_screen()
                        if algorithm == 'a':
                            nationaal = dijkstra.Holland(train_dijkstra, connectionsNationaal)
                            run_greedy_dijkstra.run_greedy(connectionsNationaal, nationaal, iterations)
                            break
                        elif algorithm == 'b':
                            nationaal = graph_Simon2.Holland(train_greedy, connectionsNationaal)
                            run_greedy.run_greedy(connectionsNationaal, nationaal, iterations)
                            break
                        elif algorithm == 'c':
                            totaal = run_hillclimbing_algorithm.load_map(connectionsNationaal)
                            hillclimber_algorithm.main(maps, train_hillclimber, totaal, iterations)
                            break
                        elif algorithm == 'd':
                            totaal = run_random_algorithm.load_map(connectionsNationaal)
                            random_algorithm.main(maps, train_random, totaal, iterations)
                            break
                    break

            break
        else:
            print('try again')
            continue

# the way main.py is run
while True:
    print(openings_text)
    algorithm = input()
    if algorithm == 'a' or algorithm == 'b' or algorithm == 'c' or algorithm == 'd':
        choose_algorithm(algorithm)

    elif algorithm == 'exit':
        break
