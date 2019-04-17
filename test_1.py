
from SignMsg import *
import time
import datetime


print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

t = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

message = "asdadadadasdasdasd"

"""msg=[]

t_msg = []

msg.append(message)
msg.append(t)

trans_msg = jsonpickle.encode(msg)

sk = SigningKey.from_pem(open("Signkey/Sign_private_1.pem").read())

sig = sk.sign(trans_msg)
#open("signature","wb").write(sig)

t_msg.append(trans_msg)
t_msg.append(sig)

tt_msg = jsonpickle.encode(t_msg)


"""
Path = "Signkey/Sign_private_1.pem"
tt_msg = SignandPack(Path, message)

Pathc = "Signkey/Sign_public_1.pem"
cipher = unPackandVerify(Pathc, tt_msg)

print "Cipher:", cipher

'''
t_msg = jsonpickle.decode(tt_msg)
vk = VerifyingKey.from_pem(open("Signkey/Sign_public_1.pem").read())

trans_msg = t_msg[0]
mmsg = jsonpickle.decode(trans_msg)

sig = t_msg[1]

#sig = open("signature","rb").read()



try:
    vk.verify(sig, trans_msg)
    print "good signature"
    time = mmsg[1]
    print "sign time:", t
    print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%M'))
except BadSignatureError:
    print "BAD SIGNATURE"
'''
