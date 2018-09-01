
# coding: utf-8

# In[1]:


import os
from tqdm import tqdm
import pickle
import numpy as np
import h5py


# In[2]:


data_dir = "./data"
epochs = ['średniowiecze', 'współczesność', 'modernizm', 'romantyzm', 'barok', 'oświecenie', 'renesans', 'pozytywizm', 'dwudziestolecie', 'starożytność']


# In[3]:


sizes = get_ipython().getoutput('du ./data')
epoch_sizes = {}
for s in sizes:
    size = s.split()[0]
    name = s.split()[1].split('/')[-1]
    epoch_sizes[name] = int(size)
epoch_sizes


# In[4]:


m = min(epoch_sizes.values())
skips = 2*np.log(np.array(list(epoch_sizes.values())) / m)
epoch_skips = {a: int(np.floor(b)) for a,b in zip(epoch_sizes.keys(),skips)}
epoch_skips


# In[5]:


get_ipython().system('cd data; cat */*.txt > big_blob.txt')
with open('./data/big_blob.txt', 'r', encoding="utf-8") as blob:
    b = blob.read()
    chars = set(b)
    freq = {c: 0 for c in chars}
    for c in list(b):
        freq[c] +=1
        
    del b
    
freq_sorted = sorted(freq.items(), key=lambda x: x[1])
freq_filtered = [x[0] for x in freq_sorted if x[1] > 1000]
print("".join(sorted(freq_filtered)))
freq_filtered += ["NULL"]

char_idx = {c: i for i, c in enumerate(sorted(freq_filtered))}
pickle.dump(char_idx, open('charmap.pickle','wb'))


# In[15]:


def process_text_with_epochs(files_dir, epochs, char_idx, epoch_skips, hdf_path ="./dataset.h5f", seq_maxlen=25, redun_step=3):
    def map_char(char):
        idx = char_idx.get(char)
        if idx is None:
            return char_idx['NULL']
        else:
            return idx
        
    len_chars = len(char_idx)
    len_epochs = len(epochs)
    vector_len = len_chars + len_epochs
    
    with h5py.File(hdf_path, "a") as hdf5_file:
        Xt = hdf5_file.create_dataset('X', (0, seq_maxlen, vector_len), 
                                        maxshape=(None, seq_maxlen, vector_len),
                                        dtype='bool')
        
        Yt = hdf5_file.create_dataset('Y', (0, len_chars), 
                                        maxshape=(None, len_chars),
                                        dtype='bool')
        

        for epoch in epochs:
            print("Processing: ",epoch, 'step=',redun_step+epoch_skips[epoch])
            epoch_path = os.path.join(files_dir, epoch)
            txt_files = [os.path.join(epoch_path, f) for f in os.listdir(epoch_path) if os.path.isfile(os.path.join(epoch_path, f))]

            for file in tqdm(txt_files):
                with open(file, 'rt') as txt:
                    string = txt.read()

                    sequences = []
                    next_chars = []
                    step = redun_step + epoch_skips[epoch]
                    for i in range(0, len(string) - seq_maxlen, redun_step):
                        sequences.append(string[i: i + seq_maxlen])
                        next_chars.append(string[i + seq_maxlen])

                    x = np.zeros((len(sequences), seq_maxlen, vector_len), dtype=np.bool)
                    y = np.zeros((len(sequences), len_chars), dtype=np.bool)
                    for i, seq in enumerate(sequences):
                        for t, char in enumerate(seq):
                            x[i, t, map_char(char)] = 1
                            x[i, t, len_chars + epochs.index(epoch)] = 1
                        y[i, map_char(next_chars[i])] = 1

                    x_len = x.shape[0]
                    Xt.resize(Xt.shape[0]+x_len, axis=0)   
                    Xt[-x_len:] = x
                    
                    y_len = y.shape[0]
                    Yt.resize(Yt.shape[0]+y_len, axis=0)   
                    Yt[-y_len:] = y
                
        shapes = (Xt.shape, Yt.shape)
                
    return shapes


# In[17]:


#shapes = process_text_with_epochs(data_dir, ['średniowiecze'], char_idx, epoch_skips)


# In[18]:


from multiprocessing import Pool
pool = Pool()

for epoch in epochs:
    pool.apply_async(process_text_with_epochs, [data_dir, [epoch], 
                                                char_idx, epoch_skips,
                                                "dataset_"+epoch+".h5f",
                                                25, 3])
    

