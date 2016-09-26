import nltk
import random
import os


def nltkify(path):
        """
        Using nltk, make a text. We might not really need this,
        as the really only purpose is to find the most common words.
        """
        with open(path, 'r+') as f:
            line = f.read()
            tokens = nltk.word_tokenize(line)
            text = nltk.Text(tokens)
            return text

def remove_random_crap(user_text):
        """
        Get rid of common things found on twitter, we won't want our
        sentences to just be gibberish.
        """
        new_text = []
        remove = ['//', 'http', ':', '\'\'']
        for word in user_text:
            if word not in remove:
                new_text.append(word)
        return new_text

def create_word_pairs(text):
        """
        Go through the supplied text and create our 'word pairs',
        its actually a dictinary of: 'word:[list of words]'' pairs, but you
        get the idea.
        """
        all_pairs = {}

        for word in range(len(text) - 1):
            if text[word] not in all_pairs:
                all_pairs[text[word]] = [text[word + 1]]
            else:
                all_pairs[text[word]] += [text[word + 1]]
        return all_pairs

def get_next_word(word, pairs):
        """
        Depending on how many words come after a word,
        either just grab one if it's the only one, or
        randomly select a word if there exists multiples within the list.
        """
        if len(pairs[word]) == 1:
            return ''.join(pairs[word])
        else:
            _range = len(pairs[word])
            selection = generate_random(_range)
            return ''.join(pairs[word][selection])

def generate_random(_range):
        """
        Using SystemRandom, generate a random number.
        """
        return random.randrange(_range)

def make_sentence(text, pairs, length):
        """
        Given the text, the pairs of words, and the length, we create a sentence.
        The starting word will be one of most common words the user has used, so
        hopefully it doesn't sound too random.
        """
        sentence = []
        fd = nltk.FreqDist(text)
        most_common = fd.most_common(75)

        starting_place = generate_random(len(most_common))
        word = text[starting_place]

        sentence.append(text[starting_place])

        for i in range(length):
            word = ''.join(word)
            word = get_next_word(word, pairs)
            sentence.append(word)
        return sentence

def get_most_common(request, text):
    fd = nltk.FreqDist(text)
    request.session['trump_common'] = fd.most_common(70)

def get_tweet(request):
    sentence = []
    starting_place = generate_random(70)
    word = request.session['trump_common'][starting_place][0]
    sentence.append(word)

    for i in range(10):
        word = ''.join(word)
        word = get_next_word(word, request.session['trump_pairs'])
        sentence.append(word)
    return sentence

def format_sentence(sentence):
        """
        We iterate through the words and make any modifications needed, namely
        the format of the sentence. This means we put '@' in front of the word, and the
        other puncuation marks behind the words.
        """
        put_in_front = ['@', '#']
        put_in_back = ['.', ',', '\'re', '\'nt', '\'', '\'t', '\'s', '!', '\'m', '?', '!?','?!']
        for word in range(len(sentence)):
            try:
                if sentence[word] in put_in_front:
                    sentence[word + 1] = sentence[word] + sentence[word + 1]
                    del sentence[word]
                elif sentence[word] in put_in_back:
                    sentence[word - 1] = sentence[word - 1] + sentence[word]
                    del sentence[word]
            except IndexError:
                pass
        return ' '.join(sentence)

def get_random_likes_retweets(tweet):
    tweet['likes'] = random.randrange(50, 25000)
    tweet['retweets'] = random.randrange(50, 25000)
    return tweet

def get_random_date(tweet):
    hour = random.randrange(1, 12)
    minute = random.randrange(1, 60)
    if len(str(minute)) == 1:
        minute = "{}{}".format(0, minute)
    day = random.randrange(1, 31)
    time = ['AM', 'PM'][random.randrange(0, 2)]
    months = ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug']
    month = months[random.randrange(0, 11)]
    tweet['date'] = "{}:{} {} - {} {} 2016".format(
            hour, minute, time, day, month)
    return tweet

def trumpify(request):
    tweet = {}
    try:
        request.session['trump_pairs']
        request.session['trump_common']
    except:
        user_text = nltkify('trumpify/user_tweets.txt')
        clean_text = remove_random_crap(user_text)
        request.session['trump_pairs'] = create_word_pairs(clean_text)
        get_most_common(request, clean_text)
    tweet = get_random_likes_retweets(tweet)
    tweet = get_random_date(tweet)
    tweet['sentence'] = format_sentence(get_tweet(request))
    return tweet
