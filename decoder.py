
import os
import pickle

import tflearn
from tflearn.data_utils import *

from generator import SequenceGeneratorWithClasses


char_idx_file = 'charmap.pickle'
char_idx = pickle.load(open(char_idx_file, 'rb'))

epochs = ['średniowiecze', 'współczesność', 'modernizm', 'romantyzm', 'barok', 'oświecenie', 'renesans', 'pozytywizm', 'dwudziestolecie', 'starożytność']

#maxlen = 25
maxlen = 100
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

m = SequenceGeneratorWithClasses(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              extra_vect_len = len_epochs,
                              checkpoint_path='pl_model')

# m.load('pl_model-169664')
m.load('pl_model2-39424')

seed = random_sequence_from_string("Wlazł kotek na płotek. Ala ma kota, a kot ma Alę. Skąd Litwini wracali? Z wycieczki wracali! Nocnej, nawiasem mówiąc.", maxlen)
for i, epoch in enumerate(epochs):
	print("EPOCH: ", epoch)
	print(m.generate(2000, temperature=0.8, extra_class = i, seq_seed=seed))