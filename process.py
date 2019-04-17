from paillier.paillier import *


def load_key():
    import pickle
    with open('key.pkl') as fid:
        return pickle.load(fid)


def encrypt(priv, pub, x):
    cx = encrypt(pub, x)
    
    
def decrypt
    
