from flask import Flask
from flask import render_template
from flask import request
from block import write_block, check_integrity
import time

app = Flask(__name__)

"""
transac = {
    'data': [],
    'hash_details': {}
}
"""
transac = {
    'data': [],
}                                                                   # a list to store unverified transactions


# Standard method of flask to get input from the page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        lender = request.form.get('lender')
        amount = request.form.get('amount')

        transtime = time.ctime()
        # storing transaction details with transaction time into the list
        transac['data'].append(
            {'borrower': borrower, 'lender': lender, 'amount': amount, 'transtime': transtime})

    return render_template('index.html', transax=transac)


# function for mine button to call mine function
@app.route('/mine')
def mine():
    if request.method == 'GET':
        # adding new blocks to the blockchain , verifying unconfirmed transactions
        write_block(transac)
    transac['data'].clear()
    return render_template('index.html')


# integrity check for already verified blocks
@app.route('/checking')
def check():
    results = check_integrity()
    return render_template('index.html', checking_results=results)


# web page works on localhost port 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
