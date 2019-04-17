from paillier.paillier import *
import pickle

print "Generating keypair..."
priv, pub = generate_keypair(128)

with open('key.pkl', 'wb') as fid:
    pickle.dump([priv, pub], fid)


