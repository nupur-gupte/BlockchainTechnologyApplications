import datetime
import hashlib

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    proof=0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) +"\nPrevious Hash: "+ str(self.previous_hash)+"\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nNonce: " + str(self.nonce) +"\nProof: "+str(self.proof)+ "\n--------------"

class Blockchain:

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def proof_of_work(self, block, difficulty):
        block.nonce = 0
        computed_hash = block.hash()
        while not computed_hash.startswith('0' * difficulty):
            block.nonce += 1
            computed_hash = block.hash()
        return computed_hash
   
    def mine(self,new_block):
        new_block.proof = self.proof_of_work(new_block,4)
        self.add(new_block)

   

blockchain = Blockchain()

for n in range(5):
    data=input('Enter the data to be stored in block '+str(n+1)+' ')
    blockchain.mine(Block(data))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
