##############################################################
#
# Copyright (c) 2013, Peixiang Xu(peixiangxu@gmail.com)
#
# This program is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public 
# License as published by the Free Software Foundation.
#
##############################################################

import sys
import json
import collections

def hw(sent_file,tweet_file):
    states_scores = collections.defaultdict(lambda:0.0)
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" mean
        scores[term] = int(score)  # Convert the score to an integer.
    
    for line in tweet_file:
        response = json.loads(line)
        if 'place' in response and response['place'] != None and response['place']['country_code'] \
            == 'US' and 'text' in response:
            text = response['text']
            score = 0.0
            for term in text.split(' '):
                if term in scores:
                    score += scores[term]
            state_fullname = response['place']['full_name']
            states_scores[state_fullname[len(state_fullname) - 2:]] += score

    print sorted(states_scores.items(), key=lambda x: x[1],reverse = True)[0][0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
