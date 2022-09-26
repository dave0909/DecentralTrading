from inspect import signature
from web3 import Web3
from datetime import datetime,timedelta,time
from datetime import datetime
import pytz
from hexbytes import HexBytes

from eth_account.messages import encode_defunct

w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
#abi='[{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getFinancialPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getMedicalPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"getResource","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"url","type":"bytes"},{"internalType":"int256","name":"podId","type":"int256"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Resource","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getSocialPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes","name":"newReference","type":"bytes"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"}],"name":"registerPod","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"podId","type":"int256"},{"internalType":"bytes","name":"newReference","type":"bytes"},{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"registerResource","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"nonpayable","type":"function"}]'
#address='0x88bA9f707a4E4e455a02862C9158ee0898d6b0Fb'
#contract_instance = w3.eth.contract(address=address, abi=abi)
#print(contract_instance.functions.getFinancialPods(2).call())
from eth_account import Account
import secrets
from WorldTimeAPI import service as serv

#priv = secrets.token_hex(32)
#private_key = "0x" + priv
#print ("SAVE BUT DO NOT SHARE THIS:", private_key)
#acct = Account.from_key(private_key)
#print("Address:", acct.address)

#contract_instance.functions.registerPod('0x66616e63756c6f2064696f',0).send
def rounded_to_the_last_30th_minute_epoch(unix_time):
    date_time = datetime.fromtimestamp(unix_time)
    now = date_time
    rounded = now - (now - datetime.min) % timedelta(minutes=5)
    return rounded.timestamp()
def get_time_in_rome():
    rome_tz= pytz.timezone("Europe/Rome") 
    time_in_rome = datetime.now(rome_tz)
    return time_in_rome
def encode_unsigned(resource,time):
    msg_to_hash=resource+":*:*:"+time
    msghash = encode_defunct(text=msg_to_hash)
    return msghash
def authenticate_signature(signature,msg_hash,claim):
    return claim==w3.eth.account.recover_message(msg_hash, signature=signature)

time_in_rome=get_time_in_rome()
print(str(int(time_in_rome.timestamp())))
rounded=rounded_to_the_last_30th_minute_epoch(int(time_in_rome.timestamp()))



msg_hash=encode_unsigned("/",str(rounded))
print(msg_hash)

#msghash = encode_defunct(text=msg)
#msghash2 = encode_defunct(text=msg2)
key="4f2481596b2240fdca059e5ea5271f7b0a0c3e0fdf0593c16e1668908db2f7e0"
#acct = Account.from_key(key)
singed_message=Account.sign_message(msg_hash,key)
#singed_message2=Account.sign_message(msghash2,key)
#print(singed_message.signature)
#bytes_signature=HexBytes(hex_signature)
#print(bytes_signature)

#tx_hash=contract_instance.functions.registerPod('0x6576766976612073616e20676975736570706521',0).transact()
#print(tx_hash)
#recovered_from_signed=w3.eth.account.recoverHash(singed_message.messageHash, signature=singed_message.signature)
claim=Account.from_key(key).address
#print("CLAIM: "+claim)
#print(hex_signature)
addr_recovered=recovered_from_unsigned=w3.eth.account.recover_message(msg_hash, signature=singed_message.signature)
print("TOKEN",singed_message.signature)
#print("RECOVERED ADDRESS from  unsigned message: ",str(authenticate_signature(bytes_signature,msg_hash,claim)))

#firmo il messaggio contenente  e ti mando la signature e la richiesta di risorsa
#prendi la signature
#hashi la richiesta di risorsa
#
print(bytes("ciaooooooo", 'utf-8'))