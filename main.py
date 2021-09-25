from flask import Flask
from flask import render_template
from flask import request
from block import write_block, check_integrity
import time

app = Flask(__name__)

transac = [] # string string int

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        lender = request.form.get('lender')
        amount = request.form.get('amount')

        transtime = time.ctime()
        transac.append({'borrower' : borrower, 'lender' : lender, 'amount' : amount, 'transtime' : transtime})

#        write_block(borrower = borrower,lender=lender, amount=amount)

    return render_template('index.html', transax = transac)

@app.route('/mine')
def mine():
    if request.method == 'GET':
        for x in transac:
            write_block(borrower = x.get('borrower'), lender = x.get('lender'), amount = x.get('amount'))
    transac.clear()
    return render_template('index.html')
    
    
    


@app.route('/checking')
def check():
    results= check_integrity()
    return render_template('index.html', checking_results=results)


if __name__ == '__main__':
    app.run(debug=True, port=5000)




