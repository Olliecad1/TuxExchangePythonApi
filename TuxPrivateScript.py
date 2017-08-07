import json
import requests
import hmac
import hashlib
import urllib


#Tuxexchange info
PublKey = ""
PrivKey = ""
tuxURL = "https://tuxexchange.com/api"

query = {"method":"getmybalances"}

newquery = {"method":"getmytradehistory"} 

encoded = urllib.urlencode(query)

signature = hmac.new(PrivKey,encoded,hashlib.sha512).hexdigest()

TuxexchangeHeader = {'Sign':signature, 'Key': PublKey}

tuxgetbalance = requests.post(tuxURL, data=query, headers=TuxexchangeHeader,timeout=15).json()

encodeurl = urllib.urlencode(newquery)

signature1 = hmac.new(PrivKey,encodeurl,hashlib.sha512).hexdigest()

TuxexchangeHeader1 = {'Sign':signature1, 'Key': PublKey}

tuxgetaddresses = requests.post(tuxURL, data=newquery, headers=TuxexchangeHeader1, timeout=15).json()

print tuxgetbalance

#print 'Btc balance: ' + tuxgetbalance['BTC']['balance']

#print 'Eth Balance: ' + tuxgetbalance['ETH']['balance']

print tuxgetaddresses

#print '\n' + '\n'

#ethTotal = tuxgetaddresses[0]['total']

#xcpTotal = tuxgetaddresses[1]['total']



