#!/usr/bin/env python
# encoding: utf-8
import json
import sqlite3
from flask import Flask, request, make_response

app = Flask(__name__)

def process_data(arg1, arg2):
    try:
        sqliteConnection = sqlite3.connect('data.db')
        query = ""
        j = ""
        if arg1 == 'customers':
            query = """ select * from customers; """
        elif arg1 == 'customer_id':
            query = f""" select * from customers where customerid={arg2[0]};"""
        elif arg1 == 'orders':
            print("printing orders")
            query = f""" select product, orderid from orders where customerid={arg2[0]}; """
        elif arg1 == 'order_id':
            print("order_id")
            query = f""" select product, orderid from orders where customerid={arg2[0]} and orderid={arg2[1]};"""
        else:
            print("error in args %s".format(str(arg1) + str(arg2) ) )
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite3")
        cursor.execute(query)
        res = cursor.fetchall()
        l = dict(zip(list(range(len(res))), res))
        j = json.dumps( l )
        #print(j)
        cursor.close()

    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
        return j


@app.route("/")
def index():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Home page. Try with routes!',
        200
    )

@app.route('/customers', methods=['GET'])
def customers():
        j = process_data('customers', () )
        return j

@app.route('/customers/<customer_id>', methods=['GET'])
def customer_id(customer_id=0):
        j = process_data('customer_id', (customer_id, '') )
        return  j


@app.route('/customers/<customer_id>/orders', methods=['GET'])
def orders(customer_id=0):
        j = process_data('orders', (customer_id, ''))
        return  j

@app.route('/customers/<customer_id>/orders/<order_id>/', methods=['GET'])
def order_id(customer_id=0, order_id=0):
        j = process_data('order_id', (customer_id, order_id))
        return  j


#app.run()
app.run(host="0.0.0.0")
