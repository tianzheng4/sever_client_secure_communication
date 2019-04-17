def main():
    
    # first of all import the socket library
    import socket 
    import sys, select
    import pickle
    from load_key import load_key
    from SignMsg import *
 
    # next create a socket object
    s = socket.socket()
         
    print "Socket successfully created"
 
    port = 12345              
    
    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests 
    # coming from other computers on the network
    s.bind(('', port))        
    print "socket binded to %s" %(port)
 
    # put the socket into listening mode
    s.listen(5)     
    print "socket is listening"           
    priv = load_key('priv') # colluded case
    

    ctr = 0
    client_list = []
    addr_list = []
    result = -1
    Path_Sign = "Signkey/Sign_private.pem"
    Path_Verfy1 = "Signkey/Sign_public_1.pem"
    Path_Verfy2 = "Signkey/Sign_public_2.pem"
    Path_Verfy3 = "Signkey/Sign_public_3.pem"
    #HW = Pyfhel()
    #filename = 'Hekey'
    #HW.restoreEnv(filename)
    #base_list = [0]
    #recv_list = [0]
    #base_plain = PyPtxt(base_list, HW)
    #recv_plain = PyPtxt(recv_list, HW)
    #base_cipher = HW.encrypt(base_plain)
    #recv_cipher = HW.encrypt(recv_plain)
    #rr = HW.decrypt(recv_cipher)
    #print ("ids:", recv_cipher._PyCtxt__ids)
    #print ("rr:", rr)
    while True:
        # Establish connection with client.
        try:
            s.settimeout(0.5) 
            c, addr = s.accept()
        
            print 'Got connection from', addr

            client_list.append(c)
            addr_list.append(addr)

            print 'Currently connected clients  ', addr_list
        except socket.timeout:
            print 'Next round'
            pass
            
        except:
            raise
            
            
        ##
            
        try:
            keyinput = 'None'
            print 'What do you want to do: '
            ready, _, __ = select.select([sys.stdin], [],[], 10)
            
            if (ready):
                keyinput = sys.stdin.readline().strip()
                print keyinput
            else:
                pass
            
            if keyinput == 'summation':
                for c in client_list:
                    operation = 'pls send me a number for sum:'
                    operation_send = SignandPack(Path_Sign, operation)
                    c.send(operation_send)
                    cx_recv = c.recv(1024)
                    if ctr == 0:
                        Path_Verfy = Path_Verfy1
                    elif ctr == 1:
                        Path_Verfy = Path_Verfy2
                    elif ctr == 2:
                        Path_Verfy = Path_Verfy3
                    cx = unPackandVerify(Path_Verfy, cx_recv)
                    ctr = ctr + 1
                    if result == -1:
                        result = long(cx)
                    else:
                        result = e_add(pub, result, long(cx))
                    print 'encrypted result:  ', result
                    print 'plaintext result( if S colluded with C ):' , decrypt(priv, pub, long(result)) % 255
                for c in client_list:
                    result_send = SignandPack(Path_Sign, str(result))
                    c.send(result_send)
                result = -1
                ctr = 0

            elif keyinput == 'mean':
                for c in client_list:
                    operation = 'pls send me a number for mean:'
                    operation_send = SignandPack(Path_Sign, operation)
                    c.send(operation_send)
                    cx_recv = c.recv(1024)
                    if ctr == 0:
                        Path_Verfy = Path_Verfy1
                    elif ctr == 1:
                        Path_Verfy = Path_Verfy2
                    elif ctr == 2:
                        Path_Verfy = Path_Verfy3
                    cx = unPackandVerify(Path_Verfy, cx_recv)
                    ctr = ctr + 1
                    if result == -1:
                        result = long(cx)
                    else:
                        result = e_add(pub, result, long(cx))
                    print 'encrypted result:  ', result
                    print 'plaintext result( if S colluded with C ):' , decrypt(priv, pub, long(result)) % 255
                for c in client_list:
                    result_send = SignandPack(Path_Sign, str(result))
                    c.send(result_send)
                result = -1
                ctr = 0

            elif keyinput == 'variance':
                for c in client_list:
                    operation = 'pls send me a number for variance:'
                    operation_send = SignandPack(Path_Sign, operation)
                    c.send(operation_send)
                    cx_recv = c.recv(1024)
                    if ctr == 0:
                        Path_Verfy = Path_Verfy1
                    elif ctr == 1:
                        Path_Verfy = Path_Verfy2
                    elif ctr == 2:
                        Path_Verfy = Path_Verfy3
                    cx = unPackandVerify(Path_Verfy, cx_recv)
                    ctr = ctr + 1
                    if result == -1:
                        result = long(cx)
                    else:
                        result = e_add(pub, result, long(cx))
                    print 'encrypted result:  ', result
                    print 'plaintext result( if S colluded with C ):' , decrypt(priv, pub, long(result)) % 255
              	"""
                for c in client_list:
                    result_send = SignandPack(Path_Sign, str(result))
                    c.send(result_send)

                result = -1
                ctr = 0
		"""
                result_s = result
	        result = -1
		ctr = 0
                for c in client_list:
                    if ctr ==0:
                        result_send = SignandPack(Path_Sign, str(result_s))
                    c.send(result_send)
                    cx_recv = c.recv(1024)
                    if ctr == 0:
                        Path_Verfy = Path_Verfy1
                    elif ctr == 1:
                        Path_Verfy = Path_Verfy2
                    elif ctr == 2:
                        Path_Verfy = Path_Verfy3
                    cx = unPackandVerify(Path_Verfy, cx_recv)
                    ctr = ctr + 1
                    if result == -1:
                        result = long(cx)
                    else:
                        result = e_add(pub, result, long(cx))
                    print 'encrypted result:  ', result
                print 'plaintext variance result( if S colluded with C ):' , (float(decrypt(priv, pub, long(result))) % 2550000) /30000
                result_s = result
	        result = -1
		ctr = 0
                for c in client_list:
                    result_send = SignandPack(Path_Sign, str(result_s))
                    c.send(result_send)

            elif keyinput == 'bye':
                for c in client_list:
                    operation = 'Bye!'
                    operation_send = SignandPack(Path_Sign, operation)
                    c.send(operation_send)         
                s.close()
                break
            """	    elif keyinput == 'production':
                for c in client_list:
                    c.send('pls send me a number for prod:')
                    str_recv = c.recv(1024)
                    recv_cipher._PyCtxt__ids = pickle.loads(str_recv)
                    if result == -1:
                        base_cipher._PyCtxt__ids = recv_cipher._PyCtxt__ids
                        result = 1
                    else:
                        base_cipher %= recv_cipher
                    #print 'encrypted:  ', result
                str_send = pickle.dumps(base_cipher._PyCtxt__ids)
                for c in client_list:
                    c.send(str_send)
                break"""
        except socket.timeout:
            pass
            
        except:
            raise

            
 
            
            
if __name__ == '__main__':
    from paillier.paillier import *
    from load_key import load_key
    pub = load_key()
    main()

   
        
    

