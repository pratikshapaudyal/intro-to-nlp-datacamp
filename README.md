# intro-to-nlp-datacamp

This repo contains the notes and exercises from the Introduction to Natural Language Processing course I am completing in Datacamp.

## Chapter 1 - Regular Expressions and Word Tokenisation

## Regex

- use the `re` library
- Format is always the pattern first, followed by the string:

``` python
(re.split(sentence_endings, my_string))
```

### Useful methods

`Findall`
`split`
`search`
`match`

## Tokenize

- used to remove unwanted tokens.
- determine meaning from text.
- import the `nltk` library.
- `word_tokenize` - add description here.
- `sent_tokenize` - the sent_tokenize function will split a document into individual sentences.
- The `regexp_tokenize` - uses regular expressions to tokenize the string, giving more granular control over the process.
- `tweettokenizer` - recognises hashtags, mentions and punctuation symbols following a sentence.

## Chapter 2 - Simple Topic Identification

## Bag-of-words

`from collections import Counter`

### punkt not installed error

To fix this error:

``` python
import nltk
nltk.download('punkt')
```

## Preprocessing

- Tokenisation
- Lowercasing words
- Lemmatisation/Stemming - shorten words to their root stems
- Remove "the", punctuation and other filler tokens
- Good to experiment with different preprocessing examples to best suit individual needs.

`from nltk.corpus import stopwords`

- Use list comprehension to lower words

``` python
tokens = [w for w in word_tokenize(text.lower())
                  if w.isalpha()]
```

`isalpha` will return alphabetical characters only. It will strip out numbers/punctuation.

``` python
no_stops = [t for t in tokens
                  if t not in stopwords.words('english')]
```

Then can use Counter to return the most common words:

``` python
Counter(no_stops).most_common(2)
```
