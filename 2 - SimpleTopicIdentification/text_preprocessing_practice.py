# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
from collections import Counter
import topic
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

english_stops = stopwords.words("english")

# Retain alphabetic words: alpha_only
alpha_only = [t for t in topic.lower_tokens if t.isalpha()]

# Remove all stop words: no_stops
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))
