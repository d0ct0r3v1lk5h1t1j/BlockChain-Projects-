# BlockChain Project 1 
Language Used - Python 
Framework Used - Flask 
Pre- Requisites for running : 
1. Flask and Python 3

Instructions to run :
execute main.py and click on the generated link on the terminal to access or go to http://127.0.0.1:5000/

#Assignment 1 .... 

A web application for a basic Blockchain that stores the transacton data of the coffee shop inclduing the time of transation.
The blockchain can only be modified by its owner who can add/edit transactions and also mine them.
Transaction details consists of :
1. Customer name 
2. Order placed
3. Amount of Transaction
4. Time of transaction 

Whenever a new order is placed its details are stored in an unverified list and only the owner has the authority to verify/ mine them.

When a transaction is mined it is placed in a new block with the follwing properties:
1. Transaction details( customer name, order, amount of transaction)
2. Hash value of previous block and its file name 
3. Timestamp of the Verification

Block data is stored in json format for each order placed.

To ensure security of the blockchain, the owner can check its integrity to make sure if any of the transactions were modified maliciously.

#Assignment 2 ....

Implemented Proof Of Stake Consensus Algorithm to elect a node for block creation in the PoS.py file 

Summary of Algorithm : 
    1. Sum of stakes of all validators are taken and they sum is segemented based on the proportion of their stakes.
    2. A random number is generated from 1 to the sum of stakes and the validator is selected based on the segment in which the number generated lies
    3. The above ensures that the validator selection is random and probability of selection is proportional to the stakes.
    4. On successful creation of a block the validator is rewarded.
