# Spam-detection

0x102 will include spam detection. The spam detection works by feeding the a machine learning model some data, being:

- the average time taken for the message to be sent over the last x amount of messages
- the message length

This model has sofar been written in jupyter notebook, but will be written in c++. C++ is a fast language that will be able to run the model very quickly. The model will be able to detect if a user is spamming and will silence the member for 20 seconds.

# More information on the model

The model is a combination of 4 lists:

- spam intervals
- spam lengths

- normal intervals
- normal lengths

The reason for the normal lists is so that the model does not think that all messages are spam.
The model is implemented in the KNN algorithm. The k-nearest-neighbors algorithm.

Once a large sample size has been gathered, I will use a different model which should be faster.
