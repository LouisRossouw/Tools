import os
from time import sleep

# Script to quickly copy files from windows to raspberry pi,
# Copy script into directory with the files you want to copy over.
# the win cmd it uses: scp path/filename pi@10.0.0.102:~/Desktop/path

script_file = os.path.basename(__file__)
directory = os.path.dirname(__file__)

raspberry = 'pi@10.0.0.102:'
raspberry_dir = '~/Desktop/Dump'

files = os.listdir(directory)

print ('copy to Raspberry Pi started')

response = input(f'\nDelete {script_file} after it is done? Y/N : ')

data = []

for f in files:
    if f != script_file:
        data.append(f)
        all_files = (' '.join(data))

os.system(f'cd {directory}')
os.system(f'scp -r {all_files} {raspberry}{raspberry_dir}')

print (f'Done copying: {all_files}')

sleep(5)

# Delete script if user inputs y/Y
if response == 'y' or response == 'Y':
    os.remove(script_file)
else:
    pass
