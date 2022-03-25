from typing import List
import typing
import hashlib
 
class Node:
    def __init__(self, left, right, value: str,content)-> None:
        self.left: Node = left
        self.right: Node = right
        self.value = value
        self.content = content
   
    @staticmethod
    def hash(val: str)-> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()
    def __str__(self):
      return (str(self.value))
 
class MerkleTree:
    def __init__(self, values: List[str])-> None:
        self.__buildTree(values)
 
    def __buildTree(self, values: List[str])-> None:
 
        leaves: List[Node] = [Node(None, None, Node.hash(e),e) for e in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0])
        self.root: Node = self.__buildTreeRec(leaves)
   
    def __buildTreeRec(self, nodes: List[Node])-> Node:
        half: int = len(nodes) // 2
 
        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.hash(nodes[0].value + nodes[1].value), nodes[0].content+"+"+nodes[1].content)
       
        left: Node = self.__buildTreeRec(nodes[:half])
        right: Node = self.__buildTreeRec(nodes[half:])
        value: str = Node.hash(left.value + right.value)
        content: str = self.__buildTreeRec(nodes[:half]).content+"+"+self.__buildTreeRec(nodes[half:]).content
        return Node(left, right, value,content)
   
    def printTree(self)-> None:
        self.__printTreeRec(self.root)
 
    def __printTreeRec(self, node)-> None:
        if node != None:
            if node.left != None:
             print("Left: "+str(node.left))
             print("Right: "+str(node.right))
            else:
             print("Input")
            print("Value: "+str(node.value))
            print("Content: "+str(node.content))
            print("")
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)
   
    def getRootHash(self)-> str:
        return self.root.value
       
       
       
def mixmerkletree(elements)-> None:
    elems = elements
    mtree = MerkleTree(elems)
    return mtree
   

import datetime
import hashlib

class Block:
    blockNo = 0
    next = None
    hash = None
    nonce = 0
    root=Node(None, None, Node.hash(''),'')
    previous_hash = 0x0
    proof=0
    timestamp = datetime.datetime.now()

    def __init__(self, elements):
        self.root=mixmerkletree(elements)

    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')+
        str(self.root).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) +"\nPrevious Hash: "+ str(self.previous_hash)+"\nBlockNo: " + str(self.blockNo) +  "\nNonce: " + str(self.nonce) +"\nProof: "+str(self.proof)

class Blockchain:

    block = Block([''])
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
        new_block.proof = self.proof_of_work(new_block,5)
        self.add(new_block)

   

blockchain = Blockchain()

for n in range(3):
    elements=list(input('Enter the elements to be stored in block '+str(n+1)+' ').split(' '))
    blockchain.mine(Block(elements))

while blockchain.head != None:
    print(blockchain.head)
    print("Root Hash: "+blockchain.head.root.getRootHash()+"\n")
    print(blockchain.head.root.printTree())
    print('\n----------------------------------------')
    blockchain.head = blockchain.head.next

