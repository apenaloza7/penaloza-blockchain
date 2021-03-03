import datetime
import hashlib

class Block:
    block_number = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = None

    def hash(self):
        hash_generation = hashlib.sha256()
        hash_generation.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.block_number).encode('utf-8')
        )
        return hash_generation.hexdigest()
    
    def __str__(self):
        return 'Block Hash: {} \nBlock Number: {} \nBlock Data: {} \nBlock Hashes: {} \n----------------'.format(self.hash(), str(self.block_number), str(self.data), str(self.nonce))

class Blockchain:
    diff = 20
    max_nonce = 2**32
    target = 2 ** (256 - diff)

    block = Block('Genesis')
    dummy = head = block

    def add_block(self, block):

        block.previous_hash = self.block.hash()
        block.block_number = self.block.block_number + 1

        self.block.next = block
        self.block = self.block.next

    def mine_block(self, block):
        for n in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add_block(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()

for n in range(10):
    blockchain.mine_block(Block('Block ' + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next