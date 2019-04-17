# paillier encryption
from paillier.paillier import *
from load_key import load_key
import pickle
# Import socket module
import socket               
from SignMsg import *

def main():
    # Create a socket object
    s = socket.socket()         
 
    # Define the port on which you want to connect

    port = 12345               
    prod_list = []

    # load key
    priv = load_key('priv')
    pub = load_key()
    #HW = Pyfhel()
    #filename = 'Hekey'
    #HW.restoreEnv(filename)
    #print "I'm ready"

    # connect to the server on local computer
    s.connect(('127.0.0.1', port))

    input1 = open('Secretshare/share'+ sys.argv[1] + '.pkl', 'r+') #difffff
    share_list = pickle.load(input1)
    input1.close()
    Path_Sign = "Signkey/Sign_private_" + sys.argv[1] + ".pem" #difffff
    Path_Verfy = "Signkey/Sign_public.pem"

    while True:
     
        # receive command from the server
        operation_msg = s.recv(1024)
        print "****************************************************************"
        operation = unPackandVerify(Path_Verfy, operation_msg)
        if operation == 'pls send me a number for sum:':
            print " "
            print "SUMMATION:"
            print " "
            print operation
            # input the number
            x_input = input()
            for cc in range (0,9):
                if share_list[2*cc] == 0:
                    share = share_list[2*cc+1]
                    share_list[2*cc] = 1
                    break
                elif cc == 9:
                    print("pls renew the shares")
            x = (x_input + share) % 255
            cx = encrypt(pub, x)
            msg = SignandPack(Path_Sign, str(cx))
            s.send(msg)
            # output result
            cr_msg = s.recv(1024)
            print "Result received ..."
            cr = unPackandVerify(Path_Verfy, cr_msg)
            print ("Sum:", decrypt(priv, pub, long(cr)) % 255)
        
            # close the connection
            # close the connection

        elif operation == 'pls send me a number for mean:':
            print " "
            print "MEAN:"
            print " "
            print operation
            # input the number
            x_input = input()
            for cc in range (0,9):
                if share_list[2*cc] == 0:
                    share = share_list[2*cc+1]
                    share_list[2*cc] = 1
                    break
                elif cc == 9:
                    print("pls renew the shares")
            x = (x_input + share) % 255
            cx = encrypt(pub, x)
            msg = SignandPack(Path_Sign, str(cx))
            s.send(msg)
            # output result
            cr_msg = s.recv(1024)
            print "Result received ..."
            cr = unPackandVerify(Path_Verfy, cr_msg)
            print ("Mean:", float(decrypt(priv, pub, long(cr)) % 255)/3)

        elif operation == 'pls send me a number for variance:':
            print " "
            print "VARIANCE:"
            print " "
            print operation
            # input the number
            x_input = input()
            for cc in range (0,9):
                if share_list[2*cc] == 0:
                    share = share_list[2*cc+1]
                    share_list[2*cc] = 1
                    break
                elif cc == 9:
                    print("pls renew the shares")
            x = (x_input + share) % 255
            cx = encrypt(pub, x)
            msg = SignandPack(Path_Sign, str(cx))
            s.send(msg)
            # output result
            cr_msg = s.recv(1024)
            print "Result received ..."
            cr = unPackandVerify(Path_Verfy, cr_msg)
	    mean = float(decrypt(priv, pub, long(cr)) % 255)/3
            print ("Mean:", mean, round(100*mean))
            x_mu_sq = (100 * x_input - int(round(100*mean))) * (100 * x_input - int(round(100*mean)))
            for cc in range (0,9):
                if share_list[2*cc] == 0:
                    share = share_list[2*cc+1]
                    share_list[2*cc] = 1
                    break
                elif cc == 9:
                    print("pls renew the shares")
            x = (x_mu_sq + share * 10000) % 2550000
            cx = encrypt(pub, x)
            msg = SignandPack(Path_Sign, str(cx))
            s.send(msg)
            # output result
            cr_msg = s.recv(1024)
            print "Result received ..."
            cr = unPackandVerify(Path_Verfy, cr_msg)
	    variance = float(decrypt(priv, pub, long(cr)) % 2550000)/30000
            print ("Variance:", variance)
        elif operation == 'Bye!':
            print operation
            s.close()
            break


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "enter client No"
    else:
        main()
