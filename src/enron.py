# Use this module to read the enron spam data

import os
import pickle

ENRON_PATH = 'data/Enron/'
CACHE_PATH = 'data/cache/'

def load_text(enron_id, cache=True):
    """
    Reads all the files for `enron_id` dataset and
    returns a tuple of the form ([ham, spam]) where
    `ham` is a list of strings containing one ham email
    and `spam` is a list of strings each containing
    one spam email

    params
    enron_id : an integer from 1 to 6
    cache : A bool. If true, try loading the data from cache.
    If data is not stored in cache, load it and save it
    to the cache. If False, don't cache or load cache

    returns:
    (ham, spam) : list of strings of ham and spam
    """

    if not (isinstance(enron_id, int) and 1<=enron_id<=6):
        raise ValueError('enron_id must be an int from 1 to 6')

    if not (isinstance(cache, bool)):
        raise ValueError('cache must be True or False')

    cache_path = CACHE_PATH+'enron{}'.format(enron_id)
    if cache and os.path.isfile(cache_path):
        with open(cache_path, 'rb') as fd:
            ham, spam = pickle.load(fd)
        return ham, spam

    ham = []
    spam = []

    ham_path = ENRON_PATH+'enron{}/ham/'.format(enron_id)
    for filepath in os.listdir(ham_path):
        try:
            with open(ham_path+filepath, 'r') as fd:
                txt = fd.read()
                ham.append(txt)
        except UnicodeDecodeError:
            print('utf-8 error. Skipping file {}'.format(ham_path+filepath))

    spam_path = ENRON_PATH+'enron{}/spam/'.format(enron_id)
    for filepath in os.listdir(spam_path):
        try:
            with open(spam_path+filepath, 'r') as fd:
                txt = fd.read()
                spam.append(txt)
        except UnicodeDecodeError:
            print('utf-8 error. Skipping file {}'.format(spam_path+filepath))

    if cache:
        with open(cache_path, 'wb') as fd:
            pickle.dump((ham, spam), fd)

    return (ham, spam)
