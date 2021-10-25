import json
import os
import hashlib
import time

#   path for file directory of json file of blocks ----
block_direc = 'blockchain/'                                 

#   function to get hash for previous block ----
def get_hash(prev_block):                                   
    
#   reading the previous block in binary format ----
    with open(block_direc + prev_block, 'rb') as f:
        content = f.read()
    
#   hashlib library to return hash of binary content of previous block ----
    return hashlib.md5(content).hexdigest()

#   function to check if any previous verified data was overwritten ----
def check_integrity():                                      
    files = sorted(os.listdir(block_direc), key=lambda x: int(x))
    results = []

#   comparing hashes of a block in iterative fashion ----
    for file in files[1:]:
        with open(block_direc + file) as f:
            block = json.load(f)
            print(block)

#   obtaining hash of previous block from current block ----
            prev_hash = block['prev_block']['hash']
            prev_filename = block['prev_block']['filename']
            timest = block['timestamp']

#   hashing the block to get current hash ----
            actual_hash = get_hash(prev_filename)

#   comparing hash value of current block with the hash value stored in next block ----
            if prev_hash == actual_hash:                   
                res = 'OK'
            else:
                res = 'Was Changed'

            print(f'block {prev_filename} : {res} : {timest}')
            results.append(
                {'block': prev_filename, 'result': res, 'timestamp': timest})

    return results


#   function to verify uncomfirmed transaction and store them in our blockchain ----
def write_block(transactions, time=time.ctime()):
    block_count = len(os.listdir(block_direc))


#    storing the block data in json format,
#    as well as adding timestamp and hash of previous block ----

    prev_block = str(block_count)                           
    transactions['prev_block'] = {
        "hash": get_hash(prev_block),
        "filename": prev_block
    }
    transactions['timestamp'] = str(time)

    current_block = block_direc + str(block_count + 1)
    data = json.dumps(transactions, indent=4)            

    with open(current_block, 'w') as f:                
        f.write(data)


def main():
    check_integrity()


if __name__ == '__main__':
    main()
