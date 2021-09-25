import json
import os
import hashlib
import time

block_direc = 'blockchain/'

def get_hash(prev_block) :
    with open(block_direc + prev_block, 'rb') as f:
        content  = f.read()
    return hashlib.md5(content).hexdigest()


def check_integrity() : 
    files = sorted(os.listdir(block_direc), key = lambda x : int(x))
    
    results = []

    for file in files[1:] :
        with open(block_direc + file ) as f:
            block = json.load(f)

            prev_hash = block.get('prev_block').get('hash')
            prev_filename = block.get('prev_block').get('filename')
            timest = block.get('timestamp')
            actual_hash = get_hash(prev_filename)
            if prev_hash == actual_hash :
               res = 'OK'
            else :
                res = 'Was Changed'
              
            print(f'block {prev_filename} : {timest}')
            results.append({'block' : prev_filename ,  'timestamp' : timest})

    return results


def write_block(borrower, lender, amount, time=time.ctime()):
   block_count =  len(os.listdir(block_direc))

   prev_block = str(block_count)
   data =  {  
    "borrower" : borrower ,
    "lender" : lender ,
    "amount" : amount ,
    "prev_block" : {
        "hash" : get_hash(prev_block) ,
        "filename" : prev_block
    },
    "timestamp": str(time)
    }
    
   current_block = block_direc +  str(block_count + 1)

   with open(current_block, 'w') as f :
     json.dump(data, f, indent = 4, ensure_ascii = False)
     f.write('\n')

def main():
    write_block(borrower= "Kshitij", lender= "Gaurvit", amount= 100)
    check_integrity()

if __name__ == '__main__' :
    main()