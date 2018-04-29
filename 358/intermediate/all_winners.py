#!/usr/bin/env python

import csv
from collections import defaultdict


lost_against = defaultdict(list)

with open('scores.csv', 'rb') as csvfile:
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
