pip install merkle
pip install pymerkle
from pymerkle import *

tree=MerkleTree()
tree

tree=MerkleTree(hash_type='sha256', encoding='utf-8', raw_bytes=True, security=True)
tree

tree=MerkleTree(b'first record',b'second record',b'third record',b'fourth record',b'fifth record',b'sixth record',b'seventh record',b'eigth record',b'ninth record',b'tenth record')
tree
print(tree)

with open('current state','w') as f:
  f.write(tree.__repr__())
 
tree.export('backup.json')
loaded_tree=MerkleTree.loadFromFile('backup.json')

#Single Record Encryption
tree.encryptRecord('txn record')
print(tree)

#Bulk file encryption
tree.encryptFileContent('sampletree.txt')

#Per Log file encryption
tree.encryptFilePerLog('../../var/log/boot.log')

#Direct JSON encryption
tree.encryptJSON({'b':0,'a':1})

#File Based JSON encryption
tree.encryptJSONFromFile('tree.json')

#Proof Generation
merkle_proof=tree.merkleProof({'checksum':hashvalue})
merkle_proof=get_validation_params()
validateProof(merkle_proof)
receipt=validateProof(merkle_proof,get_receipt=True)

subhash=tree.rootHash
tree.inclusionTest(subhash)
