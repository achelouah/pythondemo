import logging
import time
import os

logfile=os.environ.get('LOGFILE')
result=os.environ.get('RESULT')
wait=os.environ.get('WAIT')

if logfile is not None:
    logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, encoding='utf-8', level=logging.DEBUG)
else:
    print(f'Environment variable LOGFILE is not set')
    logging.basicConfig(format='%(asctime)s %(message)s', filename='python.log', encoding='utf-8', level=logging.DEBUG)

if wait is not None:
    w=int(wait)
else:
    w=30

i=1
while i <=w:
    k=w+1-i
    print('{0:2d} sec remaining ...'.format(k))
    logging.info('Waiting for %s sec', k)
    time.sleep(1)
    i+=1

if result is None:
    result="/tekton/results/exists"

if w <= 5:
    with open(result, 'w') as f:
        f.write('no')
else:
    with open(result, 'w') as f:
        f.write('yes')

