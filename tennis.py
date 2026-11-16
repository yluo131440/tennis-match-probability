from random import random
import matplotlib.pyplot as plt

def win_point(level_a,level_b):
    return random()<level_a/(level_a+level_b)

def win_game(level_a, level_b,advantage=True):
    pa = 0
    pb = 0
    while (pa < 4 and pb <4) or (abs(pa-pb) < 2):
        if win_point(level_a,level_b):
            pa += 1
        else:
            pb += 1
    return pa > pb 

def win_set(level_a,level_b,set_advantage=True,game_advantage=True):
    ga = 0
    gb = 0
    while (ga < 6 and gb < 6) or (abs(ga-gb) < 2):
        if win_game(level_a, level_b,advantage=True):
            ga += 1
        else:
            gb += 1
    return ga > gb

def win_match(level_a, level_b, nb_sets,set_advantage=True,game_advantage=True):
    sets_a = 0
    sets_b = 0
    while sets_a < nb_sets and sets_b < nb_sets:
        if win_set(level_a,level_b,set_advantage=True,game_advantage=True):
            sets_a += 1
        else:
            sets_b += 1
    return sets_a > sets_b

levels = []
for i in range(40,61):
    levels.append(i)

def match_win_rate(level_a,level_b,nb_sets,set_advantage,game_advantage,nb_runs=1000):
    ma = 0
    for i in range(nb_runs):
        if win_match(level_a, level_b, nb_sets,set_advantage=True,game_advantage=True):
            ma += 1
    return ma/nb_runs


def main():
    nb_runs=2000
    stats_simple=[]
    stats_one_advantage=[]
    stats_two_advantages=[]
    stats_three_advantages=[]
    
    for level_a in levels:
        level_b = 100 - level_a

        stats_simple.append(match_win_rate(level_a,level_b,2,False,False,nb_runs))
        stats_one_advantage.append(match_win_rate(level_a,level_b,2,False,True,nb_runs))
        stats_two_advantages.append(match_win_rate(level_a,level_b,2,True,True,nb_runs))
        stats_three_advantages.append(match_win_rate(level_a,level_b,3,True,True,nb_runs))



    plt.plot(levels, stats_simple, label='No advantage')
    plt.plot(levels, stats_one_advantage, label='1 advantage')
    plt.plot(levels, stats_two_advantages, label='2 advantages')
    plt.plot(levels, stats_three_advantages, label='3 advantages')
    plt.legend()
    plt.xlabel('Probability of winning a point for player A')
    plt.ylabel('Probability of winning the match for player A')
    plt.title('Match win probability for player A with different advantage rules')
    plt.show()


main()