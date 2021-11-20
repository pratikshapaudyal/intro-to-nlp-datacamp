from gensim.models.tfidfmodel import TfidfModel
import gensim_bag_of_words
import create_corpus_gensim

doc = create_corpus_gensim.corpus[4]
dictionary = create_corpus_gensim.dictionary
corpus = create_corpus_gensim.corpus

# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]
print(tfidf_weights)

# Print the first two weights
print(tfidf_weights[0:1])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)