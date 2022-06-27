import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s', filename='message.log', encoding='utf-8', level=logging.DEBUG)

i=1
while i <=30:
    k=31-i
    print('{0:2d} sec remaining ...'.format(k))
    logging.info('Waiting for %s sec', k)
    time.sleep(1)
    i+=1

with open('readme.txt', 'w') as f:
    f.write('Create a new text file!')


