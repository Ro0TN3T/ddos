import random
import os
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

text1 = B+"""
                                                                                 
,--.  ,--. """+F+'Author: '+W+'Ro0T@N3T'+B+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
"""+E
text2 = G+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
 """+E
text3 = F+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
"""+E
text4 = O+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################
                                                                                                                                                                                                                                                                                     
"""+E
text5 = W+"""
###########################################
#             ACEH CYBER TEAM             #
#             $ DDOS ATTACK $             #
#             $ VERSION 1.0 $             #
###########################################                                              
"""+E

ran = random.randrange(1,6)

if ran == 1:
	print(text1)
elif ran == 2:
	print(text2)
elif ran == 3:
	print(text3)
elif ran == 4:
	print(text4)
elif ran == 5:
	print(text5)