def SignandPack(Path, Cipher):
    import pickle
    from ecdsa import (NIST192p, SigningKey, VerifyingKey, BadSignatureError)
    from ecdsa.util import randrange_from_seed__trytryagain
    import time
    import datetime
    import jsonpickle
    
    msg_list = []
    trans_list = []
    t = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    msg_list.append(Cipher)
    msg_list.append(t)

    msg = jsonpickle.encode(msg_list)
    sk = SigningKey.from_pem(open(Path).read())
    sig = sk.sign(msg)
    trans_list.append(msg)
    trans_list.append(sig)
    trans = jsonpickle.encode(trans_list)

    return trans


def unPackandVerify(Path, trans):
    import pickle
    from ecdsa import (NIST192p, SigningKey, VerifyingKey, BadSignatureError)
    from ecdsa.util import randrange_from_seed__trytryagain
    import time
    import datetime
    import jsonpickle

    trans_list = jsonpickle.decode(trans)
    msg = trans_list[0]
    sig = trans_list[1]
    msg_list = jsonpickle.decode(msg)
    vk = VerifyingKey.from_pem(open(Path).read())

    try:
        vk.verify(sig, msg)
        print "Signature verification passed"
        time = msg_list[1]
        print "sign time:", time, "current time", (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        Cipher = msg_list[0]
        return Cipher
    except BadSignatureError:
        print "Signature verification failed"
