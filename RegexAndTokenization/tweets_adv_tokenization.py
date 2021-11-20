# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer


# tweets
tweets = [
    "This is the best #nlp exercise ive found online! #python",
    "#NLP is super fun! <3 #learning",
    "Thanks @datacamp :) #nlp #python",
]


# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@|#]\w+)"  # r"#\w+"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)


# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)