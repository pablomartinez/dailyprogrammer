#!/usr/bin/env python

import os
import csv
from collections import defaultdict


scores_dir = os.path.dirname(os.path.realpath(__file__))
scores_file = os.path.join(scores_dir, 'scores.csv')

lost_against = defaultdict(list)

with open(scores_file) as csvfile:
    games = csv.reader(csvfile)
    for game in games:
        if int(game[1]) > int(game[3]):
            lost_against[game[2]].append(game[0])

def transitive_winners(team):
    winners = set()
    teams = set([team])
    while teams:
        new_winners = set()
        for t in teams:
            new_winners.update(lost_against[t])
        teams = new_winners - winners
        winners.update(teams)
    return winners
