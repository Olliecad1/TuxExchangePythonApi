
import subprocess
import json

get = subprocess.check_output('curl https://tuxexchange.com/api?method=get24hvolume', shell=True)

get = str(get)

s = json.loads(get)

getETH = s['BTC_ETH']['ETH']
print '\n'

getBTC = s['BTC_ETH']['BTC']

print 'ETH 24H Volume: ' + getETH 

print 'BTC 24H Volume: ' + getBTC 
