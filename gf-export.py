from Robinhood import Robinhood
import shelve
import json
import csv

logged_in = False

def get_symbol_from_instrument_url(rb_client, url, db):
    instrument = {}
    if type(url) != str:
        url = url.encode('utf8')
    if url in db:
        instrument = db[url]
    else:
        db[url] = fetch_json_by_url(rb_client, url)
        instrument = db[url]
    return instrument['symbol']


def fetch_json_by_url(rb_client, url):
    return rb_client.session.get(url).json()


def order_item_info(order, rb_client, db):
    #side: .side,  price: .average_price, shares: .cumulative_quantity, instrument: .instrument, date : .last_transaction_at
    symbol = get_symbol_from_instrument_url(rb_client, order['instrument'], db)
    return {
        'Transaction Type': order['side'],
        'Purchase price per share': order['average_price'],
        'Shares': order['cumulative_quantity'],
        'Symbol': symbol,
        'Date Purchased': order['last_transaction_at'],
        'Commission': order['fees']
    }


def get_all_history_orders(rb_client):
    orders = []
    past_orders = rb_client.order_history()
    orders.extend(past_orders['results'])
    while past_orders['next']:
        print("{} order fetched".format(len(orders)))
        next_url = past_orders['next']
        past_orders = fetch_json_by_url(rb_client, next_url)
        orders.extend(past_orders['results'])
    print("{} order fetched".format(len(orders)))
    return orders

robinhood = Robinhood()

# fetch order history and related metadata from the Robinhood API
past_orders = get_all_history_orders(robinhood)

instruments_db = shelve.open('instruments.db')
orders = [order_item_info(order, robinhood, instruments_db) for order in past_orders]
keys = ['Purchase price per share', 'Date Purchased', 'Commission', 'Shares', 'Symbol', 'Transaction Type']
with open('orders.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(orders)
