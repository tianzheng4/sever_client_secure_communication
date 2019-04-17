def load_key(key_name = 'pub'):
    import pickle
    
    if key_name == 'priv':
        with open('priv_key.pkl', 'rb') as fid:
            return pickle.load(fid)
    else:
        with open('pub_key.pkl', 'rb') as fid:
            return pickle.load(fid)
