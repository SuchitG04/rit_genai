
### kickstart
- count vectorizer, BoW, tfidf, hamming distance, cosine similarity
- word vectors
- resources:
	- https://victorzhou.com/blog/bag-of-words/
	- http://vision.stanford.edu/teaching/cs131_fall1718/files/14_notes.pdf
	- https://people.seas.harvard.edu/~madhusudan/courses/Spring2017/scribe/lect01.pdf

### meet 1 - 22/06/24
- fasttext, glove, google ngrams viewer
- counter (python lib), word2vec, cosine similarity, tsne (converting to 2d space?)
- scikit-learn nearest neighbour, spotify annoy
- optimization of nearest search: first bucketing, finding the relevant bucket, and then doing a full search in that bucket only (read: annoy)
- resources:
	- https://www.projectpro.io/article/10-nlp-techniques-every-data-scientist-should-know/415
- TF-IDF:
	- tf - term frequency, idf - inverse document frequency
	- tf: number of times a word `w` occurs in a document d. func: `tf(w,d)` where `w` is the word and `d` is the document
	- idf: first, `df` gives the occurrences of a word `w` in a corpus of N documents. func: `df(w) = num_occurrences of w in the corpus or N docs`. `idf` essentially measures the usefulness or the specificity of a word to a given document. func: `idf(w) = N / df(w)`. seems like this technique is useful for keyword extraction as well, in that it can highlight words that are important in a given document compared to the whole corpus.
	- **moral of the story**: there's just too much abstraction given by many "ready-made" models. its good to learn the foundations.
	- cosine similarity is just normalized dot product.