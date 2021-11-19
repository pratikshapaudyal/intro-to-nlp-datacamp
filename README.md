# intro-to-nlp-datacamp

This repo contains the notes and exercises from the Introduction to Natural Language Processing course I am completing in Datacamp.

## Regex

- use the `re` library
- Format is always the pattern first, followed my the string:

e.g.:

``` python
(re.split(sentence_endings, my_string))
```

### Useful methods

    - `Findall`
    - `split`

## Tokenize

- removing unwanted tokens
- determine meaning from text
- `nltk` liibrary
- `sent_tokenize` The sent_tokenize function will split a document into individual sentences.
- The `regexp_tokenize` uses regular expressions to tokenize the string, giving you more granular control over the process.
- `tweettokenizer` does neat things like recognize hashtags, mentions and when you have too many punctuation symbols following a sentence.
