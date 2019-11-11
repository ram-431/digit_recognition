#for loading data 
import numpy as np
import gzip
import pickle as cPickle



def load_data():






    with gzip.open('mnist.pkl.gz', 'rb') as f:
        data = cPickle._Unpickler(f)
        data.encoding = 'latin1'  # set encoding
        train, valid, test = data.load()
    return(train,valid,test)

        
""" 
f = gzip.open('mnist.pkl.gz', 'rb')
training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
f.close()
"""
"""   with gzip.open('mnist.pkl.gz','rb') as ff :
    u = cPickle._Unpickler( ff )
    u.encoding = 'latin1'
    train, val, test = u.load()
return (train,val,test) """

def load_data_wrapper():
    
    tr_d, va_d, te_d = load_data()
    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

def vectorized_result(j):
    
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

