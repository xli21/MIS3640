from twython import Twython
import string

def process_data():
    # Replace the following strings with your own keys and secrets
    TOKEN = '2176923597-qdCRmTUOtKpxJlXCgQtOxXCsxogwISEsrL95SrJ'
    TOKEN_SECRET = 'TRTY85MwEYyf2Hi1KocCmul4tiCObrRodOeQJSn6hNB40'
    CONSUMER_KEY = 'WTjWq39CmXN88VPX5OJag277k'
    CONSUMER_SECRET = 'WfpiLlItfqZIynTTLVqYeigs1ExhlpqpY4hBZFvKZhB0IpjOwR'

    t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
    TOKEN, TOKEN_SECRET)

    data = t.search(q="Manchester united", count=200)
    return data
    

def process_file(data):
    hist = {}

    for status in data['statuses']:
        line = status['text'].replace("-", " ")
        strippables = string.punctuation + string.whitespace 
        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1 
    return hist

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t    


def print_most_common(hist, num=30):
    print('Most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def main():
    data = process_data()
    hist = process_file(data)
    print(hist)

    t = most_common(hist)
    print('Most common words are:')
    for freq, word in t[0:30]:
        print(word, '\t', freq)


if __name__ == '__main__':
    main()