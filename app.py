
from flask import Flask, escape, request, render_template
from get_feed import get_feed

feed = get_feed()

entries = feed['entries']

new_data_set = []
for x in entries:
    new_data_set.append({
        'name': x['trading-name'],
        'price': x['price']
    })

app = Flask(__name__)

@app.route('/')
def fuel_price():
    return render_template('fuellist.html', data_set=new_data_set)

