# Import spacy
import spacy
import ner_nltk_practice

# Instantiate the English model: nlp
nlp = spacy.load("en", tagger=False, parser=False, matcher=False)

# Create a new document: doc
doc = nlp(ner_nltk_practice.article)

# Print all of the found entities and their labels
for ent in doc.ents:
    print(ent.label_, ent.text)