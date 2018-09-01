
# coding: utf-8

# In[78]:


import requests
import json
import os
from tqdm import tqdm


# In[7]:


wl_dir_url = "https://wolnelektury.pl/api/books/"


# In[14]:


books_dir = requests.get(wl_dir_url)
books_json = books_dir.json()


# In[66]:


def get_epoch_tag(epoch):
    return epoch.split()[0].replace(',', '').lower()


# In[69]:


epochs = []
for book in books_json:
    epochs += [get_epoch_tag(book['epoch'])]
epochs = set(epochs)


# In[71]:


data_dir = "./data"
for ep in epochs:
    os.mkdir(os.path.join(data_dir, ep))


# In[94]:


for book in tqdm(books_json):
    title = book['url'].split('/')[-2]
    url = "https://wolnelektury.pl/media/book/txt/" + title + ".txt"
    #print(url)
    book_content = requests.get(url)
    with open(os.path.join(data_dir, get_epoch_tag(book['epoch']), title + ".txt"), 'wt') as f:
        f.write(book_content.text)


# In[95]:


print(epochs)


# In[97]:


json.dump(books_json, open('./data/books.json', "wt"))

