from paillier.paillier import *
import pickle

print "Generating keypair..."
priv, pub = generate_keypair(128)

with open('priv_key.pkl', 'wb') as fid:
    pickle.dump(priv, fid)
    
with open('pub_key.pkl', 'wb') as fid:
    pickle.dump(pub, fid)


