import sys
import json

def hw(sent_file,tweet_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" mean
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        response = json.loads(line)
        if 'text' in response:
            text = response['text']
            score = 0.0
            terms = text.split(' ')
            for term in terms:
                if term in scores:
                    score += scores[term]
            for term in terms:
                if term not in scores:
                    print '%s %d' %(term,score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)

if __name__ == '__main__':
    main()
