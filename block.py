import json
import os
import hashlib
import time

block_direc = 'blockchain/'  # constant path for file directory of json file of blocks


def get_hash(prev_block):  # function to get hash for previous block
    # reading the previous block in binary format
    with open(block_direc + prev_block, 'rb') as f:
        content = f.read()
    # hashlib library to return hash of binary content of previous block
    return hashlib.md5(content).hexdigest()


def check_integrity():  # function to check if any previous verified data was overwritten
    files = sorted(os.listdir(block_direc), key=lambda x: int(x))
    results = []

    for file in files[1:]:
        with open(block_direc + file) as f:
            block = json.load(f)
            print(block)

            prev_hash = block['prev_block']['hash']
            prev_filename = block['prev_block']['filename']
            timest = block['timestamp']
            actual_hash = get_hash(prev_filename)
            if prev_hash == actual_hash:  # comparing hash value of current block with the hash value stored in next block
                res = 'OK'
            else:
                res = 'Was Changed'

            print(f'block {prev_filename} : {res} : {timest}')
            results.append(
                {'block': prev_filename, 'result': res, 'timestamp': timest})

    return results


# function to verify uncomfirmed transaction and store them in our blockchain
def write_block(transactions, time=time.ctime()):
    block_count = len(os.listdir(block_direc))

    prev_block = str(block_count)
    transactions['prev_block'] = {
        "hash": get_hash(prev_block),
        "filename": prev_block
    }
    transactions['timestamp'] = str(time)
    
#    data =  {                                                                          #storing data in json format
#     "borrower" : borrower ,
#     "lender" : lender ,
#     "amount" : amount ,
#     "prev_block" : {
#         "hash" : get_hash(prev_block) ,
#         "filename" : prev_block
#     },
#     "timestamp": str(time)
#     }

    current_block = block_direc + str(block_count + 1)
    data = json.dumps(transactions, indent=4)

    with open(current_block, 'w') as f:
        f.write(data)
    #  json.dump(data, f, indent = 4, ensure_ascii = False)                          #ensuring encyption of the json file with 4 bytes of indent
        # newline for stroing next data


def main():
    check_integrity()


if __name__ == '__main__':
    main()
