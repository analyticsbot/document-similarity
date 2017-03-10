from pyemd import emd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import euclidean_distances
import os
from gensim.models.word2vec import Word2Vec
from text_unidecode import unidecode

d1 = "Obama speaks to the media in Illinois"
d2 = "The President addresses the press in Chicago"

if not os.path.exists("data/embed.dat"):
    print("Caching word embeddings in memmapped format...")
    
    wv = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        binary=True)
    wv.init_sims(replace=True)
    fp = np.memmap("data/embed.dat", dtype=np.double, mode='w+', shape=wv.syn0norm.shape)
    fp[:] = wv.syn0norm[:]
    with open("data/embed.vocab", "w") as f:
        for _, w in sorted((voc.index, word) for word, voc in wv.vocab.items()):
            #print(w, file=f)
            print >>f, unidecode(w)
    del fp
wv = Word2Vec.load_word2vec_format(
        "data/GoogleNews-vectors-negative300.bin.gz",
        binary=True)
W = np.memmap("data/embed.dat", dtype=np.double, mode="r", shape=wv.syn0.shape)

with open("data/embed.vocab") as f:
    vocab_list = map(str.strip, f.readlines())

vocab_dict = {w: k for k, w in enumerate(vocab_list)}

def similarity(d1, d2):
    vect = CountVectorizer(stop_words="english").fit([d1, d2])
    W_ = W[[vocab_dict[w] for w in vect.get_feature_names()]]
    D_ = euclidean_distances(W_)

    v_1, v_2 = vect.transform([d1, d2])
    v_1 = v_1.toarray().ravel()
    v_2 = v_2.toarray().ravel()

    # pyemd needs double precision input
    v_1 = v_1.astype(np.double)
    v_2 = v_2.astype(np.double)
    v_1 /= v_1.sum()
    v_2 /= v_2.sum()
    D_ = D_.astype(np.double)
    D_ /= D_.max()  # just for comparison purposes
    return emd(v_1, v_2, D_))

