import pprint, pickle
from random import *
import math

share_list1=[]
share_list2=[]
share_list3=[]
for c in range (1,10):
    x1 = randint(0, 255)
    x2 = randint(0, 255)
    x3 = (- x1 - x2) % 255
    share_list1.append(0)
    share_list1.append(x1)
    share_list2.append(0)
    share_list2.append(x2)
    share_list3.append(0)
    share_list3.append(x3)
output1 = open('Secretshare/share1.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(share_list1, output1)
output1.close()
input1 = open('Secretshare/share1.pkl', 'rb')
data1 = pickle.load(input1)
pprint.pprint(data1)
input1.close()
output2 = open('Secretshare/share2.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(share_list2, output2)
output2.close()
input2 = open('Secretshare/share2.pkl', 'rb')
data2 = pickle.load(input2)
pprint.pprint(data2)
input2.close()
output3 = open('Secretshare/share3.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(share_list3, output3)
output3.close()
input3 = open('Secretshare/share3.pkl', 'rb')
data3 = pickle.load(input3)
pprint.pprint(data3)
input3.close()
