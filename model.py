
import os
import pickle

import tflearn
from tflearn.data_utils import *


char_idx_file = 'charmap.pickle'
char_idx = pickle.load(open(char_idx_file, 'rb'))

epochs = ['średniowiecze', 'współczesność', 'modernizm', 'romantyzm', 'barok', 'oświecenie', 'renesans', 'pozytywizm', 'dwudziestolecie', 'starożytność']

maxlen = 25
len_chars = len(char_idx)
len_epochs = len(epochs)
vector_len = len_chars + len_epochs


g = tflearn.input_data([None, maxlen, vector_len])
g = tflearn.lstm(g, 768, return_seq=True)
g = tflearn.dropout(g, 0.25)
g = tflearn.lstm(g, 768, return_seq=True)
g = tflearn.dropout(g, 0.25)
g = tflearn.lstm(g, 768)
g = tflearn.dropout(g, 0.25)
g = tflearn.fully_connected(g, len_chars, activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path='pl_model')


def get_dataset(q, epochs):
    import h5py
    import numpy as np

    SAMPLE_SIZE = 20000
    Xlist = []
    Ylist = []
    for epoch in epochs:
        print("Sampling from ", epoch)
        hdf_file = h5py.File('dataset_'+epoch+'.h5f', "r") 
        xs = hdf_file['X']
        ys = hdf_file['Y']
        idx = np.random.randint(0, xs.shape[0] - SAMPLE_SIZE)
        print("Sampling from idx ", idx)
        Xlist.append(xs[idx:idx+SAMPLE_SIZE])
        Ylist.append(ys[idx:idx+SAMPLE_SIZE])        
    out = (np.concatenate(Xlist, axis=0), np.concatenate(Ylist, axis=0))
    q.put(out)

from multiprocessing import Process, Queue

q = Queue()
    
    
get_dataset(q, epochs)
newX, newY = q.get()
for i in range(1000):    
    X, Y = newX, newY
    p = Process(target=get_dataset, args=(q, epochs))
    print("Sampling new dataset")
    p.start()
    
    m.fit(X, Y, validation_set=0.1, batch_size=256,
          n_epoch=1, shuffle=True, run_id='pl_model')
    
    newX, newY = q.get()
    p.join()