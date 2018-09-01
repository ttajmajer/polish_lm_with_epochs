
# coding: utf-8

# In[ ]:


import os
import pickle

import tflearn
from tflearn.data_utils import *


char_idx_file = 'charmap.pickle'
char_idx = pickle.load(open(char_idx_file, 'rb'))
hdf_file = h5py.File('dataset_średniowiecze.h5f', "r") 

epochs = ['średniowiecze', 'współczesność', 'modernizm', 'romantyzm', 'barok', 'oświecenie', 'renesans', 'pozytywizm', 'dwudziestolecie', 'starożytność']

maxlen = 25
len_chars = len(char_idx)
len_epochs = len(epochs)
vector_len = len_chars + len_epochs


X = hdf_file['X']
Y = hdf_file['Y']


g = tflearn.input_data([None, maxlen, vector_len])
g = tflearn.lstm(g, 512, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 512, return_seq=True)
g = tflearn.dropout(g, 0.5)
g = tflearn.lstm(g, 512)
g = tflearn.dropout(g, 0.5)
g = tflearn.fully_connected(g, len_chars, activation='softmax')
g = tflearn.regression(g, optimizer='adam', loss='categorical_crossentropy',
                       learning_rate=0.001)

m = tflearn.SequenceGenerator(g, dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path='pl_model')

for i in range(50):
    seed = random_sequence_from_string("Bywało też to u mnie myślistwo z podziwieniem ludzkim. Począwszy od ptaków, zawsze mi[e]wałem bardzo dobre sokoły, jastrzęby, drzemliki, kobuzy, kruki, co do berła chodziły i kuropatwy pod nimi olegały, zająca zalatowały, jako raróg; wszystko to ptastwo praktykowało swoję powinność. Jastrzębia raz miałem takiego, który był zbyt rosły, a tak rączy, że kożdego ptaka uganiał i do najmniejszej ptaszyny nie lenił się, okraczywszy go owymi srogimi szponami, i zawszem żywiusieńkiego odebrał. Rzuciłeś go też do największego ptaka — i tego się nie wstydził; gęsi, kaczki, czaple, kanie, kruki uganiał tak jako przepiórki, bo ich i kilka na dzień ugonił. Tak był mocny, że z zającem starym, związawszy się i udusiwszy, to czasem poprawił się, i na drugi zagon podlatując sobie z nim, podnosząc go od ziemie jak kuropatwę. Miałem go ośm lat, póko mi nie zdechł. Do myślistwa zaś, z charty mówiąc, rozmnożyłem był sobie gniazdo chartów od brata mego, pana Stanisława Paska z ziemie sochaczowskiej; które charty były i piękne, i rosłe, a przy tym tak rącze, że nie trzeba było nigdy [dwu] zmykać do zająca i do liszki, tylko jedno którekolwiek alternatą, jednak do kożdego zająca insze, a nigdy zając nie uciekł; do wilka zaś to już pospolitym ruszeniem. I takie to bywało przysłowie u myśliwych sąsiadów moich, że to nieszczęśliwy zwierz, który się z panem Paskiem potka, bo mu się już nie dostanie uciec.",maxlen)
    m.fit(X, Y, validation_set=0.1, batch_size=512,
          n_epoch=1, run_id='pl_model')
    print("-- TESTING...")
    print("-- Test with temperature of 1.0 --")
    print(m.generate(600, temperature=1.0, seq_seed=seed))
    print("-- Test with temperature of 0.5 --")
    print(m.generate(600, temperature=0.5, seq_seed=seed))

