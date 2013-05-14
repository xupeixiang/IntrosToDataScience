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

def hw(tweet_file):
    hashtags = collections.defaultdict(lambda:0.0)
    
    for line in tweet_file:
        response = json.loads(line)
        if 'entities' in response and response['entities'] != None:
            tags = response['entities']['hashtags']
            for tag in tags:
                hashtags[tag['text']] += 1.0
    top_tags = sorted(hashtags.items(),key = lambda x:x[1],reverse = True)[0:10]
    for tag in top_tags:
        print '%s %.1f' %(tag[0],tag[1])

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
