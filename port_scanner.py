from socket import *



def conScan(targetHost, targetPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost,targetPort))
        print("[*] tcp open"+ targetHost + targetPort)
        connskt.close()
    except:
        print("[*] tcp closed "+ targetHost + " "+ targetPort)



if __name__ == "__main__":
    conScan("127.0.0.1","80")


#https://www.youtube.com/watch?v=bH-3PuQC_n0