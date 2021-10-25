from flask import Flask
from flask import render_template
from flask import request
from PoS import Consensus
from block import write_block, check_integrity
import time

app = Flask(__name__)

#   class for a node / validator ---- 
class validator :
       def __init__(self , name , stakes):
             self.name = name
             self.stakes = stakes

#   list to keep track of the validators present ---- 
valid_identites = []

#   creating some validators ----
valid_identites.append(validator("Node1" , 200))
valid_identites.append(validator("Node2" , 100)) 
valid_identites.append(validator("Node3" , 400))



#   a list to store unverified transactions ----
transac = {
    'data': [],
}                                                                  

#   click-action call to integrity check for already verified blocks ----
@app.route('/checking')
def check():
    results = check_integrity()
    results.reverse()
    return render_template('index.html', checking_results=results, transax=transac)


#   click-action standard method of flask to get transaction input from the page ----
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        lender = request.form.get('lender')
        amount = request.form.get('amount')

        transtime = time.ctime()

#   storing transaction details with transaction time into the list ----
        transac['data'].append(
            {'borrower': borrower, 'lender': lender, 'amount': amount, 'transtime': transtime})

    return render_template('index.html', transax=transac)


#   function for mine button to call mine function ----
@app.route('/mine')
def mine():
    if request.method == 'GET':

#   Running the consensus algortihm, adding new blocks to the blockchain ----

        validator_name = Consensus(valid_identites) 
        write_block(transac)
    transac['data'].clear()
    return render_template('index.html', validator_name = validator_name)


#   web page works on localhost port 5000 ----
if __name__ == '__main__':
    app.run(debug=True, port=5000)