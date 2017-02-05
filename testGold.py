"""
train and test the model on a hand categorized gold standard
"""
import transact as ts
import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle

modelname = 'transaction_logreg'
train_in = '/home/eli/Data/Narmi/train_cat.csv'
train_out = '/home/eli/Data/Narmi/train_cat.csv'
cv_in = '/home/eli/Data/Narmi/cv.csv'
cv_out = '/home/eli/Data/Narmi/cv_cat.csv'
test_in = '/home/eli/Data/Narmi/test.csv'
test_out = '/home/eli/Data/Narmi/test_cat.csv'

# glove's pretrained model, loaded into dictionary
try:
    cat = embeddings['cat']
except:
    embedding_name = '/home/eli/Data/Narmi/glove_embeddings'
    embeddingFileLoad = open(embedding_name, 'rb')
    embeddings = pickle.load(embeddingFileLoad)

# our best middle of the road
# TODO this should be with a separate test set, with the parameter selection
#      runs using a cv set
# seed = 42, very dependent on seed
# best accuracy = 82%
# best precision = 90%
# no difference between log and modified_huber losses
# no difference between averaged and not
# no difference between l2 and elasticnet
prec = ts.run_test(train_in, train_out, test_in, test_out, modelname, embeddings, 
                  model_type='logreg',run_parse=False,
            alpha=1.0, cutoff=0.50, n_iter=1)

"""
alphas = [10., 1., 0.1, 0.01, 0.001, 0.0001]
cutoffs = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
n_iters = [1, 5, 10]

# effect of alpha
prec = np.empty(len(alphas))
idx = 0
for alpha in alphas:
    prec[idx] = ts.run_test(train_in, train_out, cv_in, cv_out, modelname, embeddings, run_parse=False,
                           alpha=alpha, cutoff=0.50, n_iter=1)
    idx+=1
plt.plot(alphas,prec,'ro')
plt.xscale('log')
plt.show()

# effect of cutoff
prec = np.empty(len(cutoffs))
idx = 0
for cutoff in cutoffs:
    prec[idx] = ts.run_test(train_in, train_out, cv_in, cv_out, modelname, embeddings, run_parse=False,
                           alpha=1., cutoff=cutoff,n_iter=1)
    idx+=1
plt.plot(cutoffs,prec,'ro')
plt.show()

# effect of n_iter
prec = np.empty(len(n_iters))
idx = 0
for n_iter in n_iters:
    prec[idx] = ts.run_test(train_in, train_out, cv_in, cv_out, modelname, embeddings, run_parse=False,
                           alpha=1., cutoff=0.50, n_iter=n_iter)
    idx+=1
plt.plot(n_iters,prec,'ro')
plt.show()
"""
