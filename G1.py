import random
import sys
import time
def mengetik (s):
    for c in s + '\n':
	sys.stdout.write(c)
	sys.stdout.flush()
	time.sleep(random.random() * 0.3)

mengetik('irfan fermanto  \n181100165 \nUnversitas Metamedia')
