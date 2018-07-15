import hashlib
from utils import next_string

class Block():

    REPEAT_NUMBER = 3
    SPECIAL_CHARACTER = '0'

    def __init__(self, content=None, previous_block_hash=None):
        self.block_hash = None
        self.nonce = None
        self.content = content
        self.previous_block_hash = previous_block_hash


    def __str__(self):
        block_repr = ""
        block_repr += "-------------------------------------------------\n"
        block_repr += "My hash: {}\n".format(self.block_hash)
        block_repr += "My contents: {}\n".format(self.content)
        block_repr += "My nonce: {}\n".format(self.nonce)
        block_repr += "My previous block hash: {}\n".format(
                                                      self.previous_block_hash)
        block_repr += "-------------------------------------------------\n"
        return block_repr


    def hash_block(self, nonce=''):
        payload = ((self.nonce or nonce) + (self.content or '') + 
                   (self.previous_block_hash or ''))
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()


    def valid_nonce(self, nonce):
        hashed_payload = self.hash_block(nonce)        
        return hashed_payload.startswith(
                                self.SPECIAL_CHARACTER * self.REPEAT_NUMBER)


    def mine_block(self):

        nonce = 'starting nonce to find a valid hash'

        valid = False
        while not valid:
            nonce = next_string(nonce)
            valid = self.valid_nonce(nonce)

        self.nonce = nonce
        self.block_hash = self.hash_block()


    def valid_block(self):
        return self.valid_nonce(self.nonce)