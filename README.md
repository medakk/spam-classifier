# Spam Classification using a Neural Network

This project uses neural networks trained on the [Enron Email Dataset](http://www.edrm.net/resources/data-sets/edrm-enron-email-data-set) to classify emails as either *SPAM* or *NOT SPAM*. The current method used is:
* Identify `n` most frequent words in the corpus
* Create a vector for each email in the corpus denoting whether or not the `n` words appear in it. (0 if the word does not exist, 1 if the word exists)
* Train a neural network on the vectorized data using stochastic gradient descent.

The training data and test data are 75% and 25% respectively of the loaded corpus. A classification accuracy of 98.14% is obtained on the test data using approximately 20000 emails.

The [NLTK](https://pypi.python.org/pypi/nltk) library is used to tokenize and create a frequency distribution of the words in the corpus. [Theano](https://pypi.python.org/pypi/Theano) is used to build a computational graph of the network and run it. The theano-specific code in this program is based on [Michael Nielsen's book](http://neuralnetworksanddeeplearning.com/) on Deep Learning.

### Obtaining the data
The instructions for obtaining the data will be added to the repo soon.

### Running the program
Run
```
python src/spam_classifier.py
```
An interactive session opens, where you can train and check the accuracy of the model, or enter custom text to test the model. Currently, the only way to modify the model(ie: add new layers, change the activation function, etc.) is to edit the source for this file.

The first run will take some time, but from the second time onwards a lot of things will be cached, so it will run much quicker.
