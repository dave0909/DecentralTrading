from inspect import signature
from web3 import Web3
from datetime import datetime,timedelta,time
from datetime import datetime
import pytz
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

class DTauthenticator():

    def __init__(self, *args, **kw):
        self.w3=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
    def rounded_to_the_last_30th_minute_epoch(self,unix_time):
        date_time = datetime.fromtimestamp(unix_time)
        now = date_time
        rounded = now - (now - datetime.min) % timedelta(minutes=5)
        return rounded.timestamp()

    def get_time_in_rome(self):
        rome_tz= pytz.timezone("Europe/Rome") 
        time_in_rome = datetime.now(rome_tz)
        return time_in_rome

    def encode_unsigned(self,resource,time):
        msg_to_hash=resource+":*:*:"+time
        msghash = encode_defunct(text=msg_to_hash)
        return msghash

    def authenticate_signature(self,signature,msg_hash,claim):
        return claim==self.w3.eth.account.recover_message(msg_hash, signature=signature)
    

    def authenticate(self,resource,signature,claim):
        time_in_rome=self.get_time_in_rome()
        rounded=self.rounded_to_the_last_30th_minute_epoch(int(time_in_rome.timestamp()))
        msg_hash=self.encode_unsigned(resource,str(rounded))
        bytes_signature=HexBytes(signature)
        print("is authenticated: "+str(self.authenticate_signature(signature,msg_hash,claim)))
        return self.authenticate_signature(signature,msg_hash,claim)
