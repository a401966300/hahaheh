import sys
from config import config_data

receive_data = ' '.join(sys.argv[1:])
if receive_data:
    data = dict(x.split('=') for x in receive_data.split(' '))
    print(data)

for key,value in config_data.items():
    if key in data.keys():
        config_data[key] = data[key]

cmake = 'cmake .. -dargqq=%s -dargww=%s -dargee=%s ' % (config_data['flash'],config_data['uttype'],config_data['processname'])

if receive_data:
    qq = data.get('flash','gg')
    ww = data.get('uttype',0)

else:
    qq = 'gg'
    ww = 0
