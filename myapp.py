import logging
import time
import os

logfile=os.environ.get('LOGFILE')
result=os.environ.get('RESULT')
wait=os.environ.get('WAIT')
waittreshold=os.environ.get('WAIT_TRESHOLD')

if logfile is None:
    print(f'Environment variable LOGFILE is not set')
    logging.basicConfig(format='%(asctime)s %(message)s', filename='python.log', encoding='utf-8', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile, encoding='utf-8', level=logging.DEBUG)

if wait is None:
    w=30
else:
    w=int(wait)

#
if waittreshold is None:
    wt=10
else:
    wt=int(waittreshold)

i=1
while i <=w:
    k=w+1-i
    print('{0:2d} sec remaining ...'.format(k))
    logging.info('Waiting for %s sec', k)
    time.sleep(1)
    i+=1

if result is None:
    result="/tekton/results/exists"

os.makedirs(os.path.dirname(result), exist_ok=True)

if w <= wt:
    with open(result, 'w') as f:
        f.write('no')
else:
    with open(result, 'w') as f:
        f.write('yes')

