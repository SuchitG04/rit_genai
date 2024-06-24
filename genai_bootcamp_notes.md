
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
	- https://www.kaggle.com/code/harshsinghal/rit-bootcamp-june-2024-goal-1
	- 
- TF-IDF:
	- tf - term frequency, idf - inverse document frequency
	- tf: number of times a word `w` occurs in a document d. func: `tf(w,d)` where `w` is the word and `d` is the document
	- idf: first, `df` gives the occurrences of a word `w` in a corpus of N documents. func: `df(w) = num_occurrences of w in the corpus or N docs`. `idf` essentially measures the usefulness or the specificity of a word to a given document. func: `idf(w) = N / df(w)`. seems like this technique is useful for keyword extraction as well, in that it can highlight words that are important in a given document compared to the whole corpus.
	- **moral of the story**: there's just too much abstraction given by many "ready-made" models. its good to learn the foundations.
- "Efficient Estimation of Word Representations in Vector Space" by Mikolov et al. - introduced cbow and skip-gram
	- continuous bag of words (cbow): a prediction setting using a 2 layered neural network (1 input layer and 1 hidden layer and 1 softmax layer, but considered 2 layers coz the hidden layer and the softmax layers are merged. read more about hierarchical softmax - https://leimao.github.io/article/Hierarchical-Softmax/ and negative sampling - https://arxiv.org/pdf/1402.3722v1 and https://stackoverflow.com/a/41319421/15368987) for a word given some context. in the paper, the authors use 4 words as the context. in other, simpler, words, consider the example "this is fine, i am fine, said the poor dog". the model will be given "this is fine i" and "fine said the poor" as the context and will be tasked to predict "am".
	- i did some reading and negative sampling kinda aims to remove the softmax layer and model the training task as binary classification. it involves sampling words randomly from out of the context. two scores are generated `pos_score` and `neg_score`. `neg_score` is negated (`-neg_score`) to make the model minimize the dot product similarity between the `w` (the word to predict given `c` the context) and the words out of the context (i.e., "negatively" sampled words).
	- skip gram: this is the inverse of cbow, in the sense that the model is tasked to predict the context given a word.
	- unigram (random term that was interesting): unigram distribution is just the probability of finding a word in a data corpus. in other words, its the non-contextual probability of finding a specific word in a corpus. it can also be thought of as the frequency of the word in the corpus. no points for guessing that ;)
- cosine similarity is just normalized dot product.
- 