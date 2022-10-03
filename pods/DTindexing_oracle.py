from web3 import Web3
from eth_account import Account
import secrets
from DTaddress_generator import DTaccount_generator
import web3
class DTindexing_oracle:


    def __init__(self, *args, **kw):
        self.indexing_address=args[0]
        self.contract_abi='[{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"deactivateResource","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"int256","name":"idPod","type":"int256"},{"indexed":false,"internalType":"address","name":"obligationAddress","type":"address"}],"name":"NewPod","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"int256","name":"idResource","type":"int256"}],"name":"NewResource","type":"event"},{"inputs":[{"internalType":"bytes","name":"newReference","type":"bytes"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"podAddress","type":"address"}],"name":"registerPod","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"int256","name":"podId","type":"int256"},{"internalType":"bytes","name":"newReference","type":"bytes"},{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"registerResource","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getFinancialPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"podAddress","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getMedicalPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"podAddress","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"pod_id","type":"int256"},{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getPodResources","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"url","type":"bytes"},{"internalType":"int256","name":"podId","type":"int256"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Resource[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"int256","name":"idResource","type":"int256"}],"name":"getResource","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"bytes","name":"url","type":"bytes"},{"internalType":"int256","name":"podId","type":"int256"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Resource","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"idSubscription","type":"uint256"}],"name":"getSocialPods","outputs":[{"components":[{"internalType":"int256","name":"id","type":"int256"},{"internalType":"enumDTIndexing.PodType","name":"podType","type":"uint8"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"podAddress","type":"address"},{"internalType":"bytes","name":"baseUrl","type":"bytes"},{"internalType":"bool","name":"isActive","type":"bool"}],"internalType":"structDTIndexing.Pod[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"}]'
        self.private_key=args[1]
        self.account= Account.from_key(self.private_key)
        self.provider=Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
        self.contract_instance = self.provider.eth.contract(address=self.indexing_address, abi=self.contract_abi)
        print(self.provider.eth.accounts)
        
    def deactivate_resource(self,resource_id):
        tx=self.contract_instance.functions.deactivateResource(resource_id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        receipt=self.provider.eth.waitForTransactionReceipt(tx)
        if receipt:
            return True
        else:
            return False


    def register_resource(self,reference,pod_id):
        tx=self.contract_instance.functions.registerPod(reference,pod_id).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        return Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
    
    def add_resource(self,reference,podId,subscription):
        print("ECCOLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",podId,self.account.address)
        tx=self.contract_instance.functions.registerResource(podId,reference,subscription).buildTransaction({'from': self.account.address,'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(self.account.address)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=self.private_key)
        print(self.private_key,self.account.address)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        #tx=self.provider.eth.sendRawTransaction(signed_txn.rawTransaction)
        print(tx)
        retVal = self.provider.eth.waitForTransactionReceipt(tx)#['logs'][0]['data']
        gino=self.contract_instance.events.NewResource().processReceipt(retVal)
        print(gino)
        id=gino[0]['args']['idResource']
       # obligation_address=gino[0]['args']['obligationAddress']
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",id)
        return id
       
    def get_resource_information(self,resourece_id):
        contract_instance = self.provider.eth.contract(address=self.indexing_address, abi=self.contract_abi)
        return contract_instance.functions.getPodResources(resourece_id,0).call()

    def register_Pod(self,pod_reference,pod_type,public_key_owner,private_key_owner):
        public_key_pod,private_key_pod=DTaccount_generator().generate_account()
        tx=self.contract_instance.functions.registerPod(pod_reference,pod_type,Web3.toChecksumAddress(public_key_pod)).buildTransaction({'gasPrice': Web3.toWei(21, 'gwei'),'nonce': self.provider.eth.getTransactionCount(public_key_owner)})
        signed_txn = self.provider.eth.account.sign_transaction(tx, private_key=private_key_owner)
        tx=Web3.toHex(self.provider.eth.sendRawTransaction(signed_txn.rawTransaction))
        retVal = self.provider.eth.waitForTransactionReceipt(tx)
        processed_receipt=self.contract_instance.events.NewPod().processReceipt(retVal)
        id=processed_receipt[0]['args']['idPod']
        obligation_address=processed_receipt[0]['args']['obligationAddress']
        return id,public_key_pod,private_key_pod,obligation_address
