import socket

def start():
    print("Would you like to listen or connect? type \"listen\" or \"connect\": ")
    cmdConn = input()
    if cmdConn.split(' ')[0] == "connect":
        connection()
    elif cmdConn.split(' ')[0] == "listen":
        print("Please wait for a friend to connect.")
        listen()
    else:
        print("Invalid command")
        print("--------------------")
        start()

def connection():
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connectFriend(server, port, client2):
        client2.connect((server, port))

    print("Please type: \"connect <IP Address> <Port Number>\" ")
    connectflag = False
    while True:
        cmdInput = input()
        if cmdInput.split(' ')[0] == "connect" and connectflag == False:
            connectFriend(cmdInput.split(' ')[1], int(cmdInput.split(' ')[2]), client2) 
            connectflag = True
            print('You have connected to your friend! Type \"quit\" to exit')
            message = input(" -> ")
            while message != 'quit':
                    print("You: " + message)
                    client2.send(message.encode())
                    data = client2.recv(4096).decode()
                    if not data:
                        break
                    print ('Friend: ' + data)
                        
                    message = input(" -> ")
            print("Connection has been terminated.")
            exit(0)
        else:
            print('Invalid, please try again')

def listen():
    host = "127.0.0.1"
    port = 1000
        
    client1 = socket.socket()
    client1.bind((host,port))
        
    client1.listen(1)
    conn, addr = client1.accept()
    print ("Your friend connected from: " + str(addr) + ". Type \"quit\" to exit")
    while True:
            data = conn.recv(4096).decode()
            if not data:
                    break
            print ("Friend: " + str(data))
            message = input(" -> ")
            print ("You: " + str(message))
            if message == "quit":
                print("Connection has been terminated.")
                exit(0)
            conn.send(message.encode())
                
    print("Connection has been terminated.")
    exit(0)

start()