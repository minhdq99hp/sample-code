'''
The `subprocess` mudle allows you to spawn new processes, 
connect to their input/output/error pipes, 
and obtain their return codes.

References:
- https://docs.python.org/2/library/subprocess.html
'''

import subprocess 
import time


subprocess.call(['python', 'temp.py'])
# subprocess.call('python temp.py', shell=True)

# Note: using shell=True can be a security hazard.


# subprocess.check_call('exit 1', shell=True)

# If the return code was 0 then return, otherwise raise CalledProcessError


# output = subprocess.check_output(['python', 'temp.py'])
# print(output)
# print(output.decode('utf-8'))

# return as byte string. Decode to string if needed.

# output = subprocess.check_output('python temp.py', stderr=subprocess.STDOUT, shell=True)


# A better way is to use to Popen class.