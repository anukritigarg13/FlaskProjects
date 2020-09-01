import sys
import random
import string
m=sys.argv[1]		#size of each file in MB
n=sys.argv[2]
l=[]		#no. of files
size=m*1024*1024

for i in range(0:n):
	chars=''.join([random.choie(list(string.ascii_letters)) for i in range(size)])
	with open('myfile%s.txt'%i,'w') as f:
		f.write(chars)
	



