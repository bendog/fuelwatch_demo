from flask import Flask, escape, request
from get_feed import get_feed

feed = get_feed()

entries = feed['entries']

print(len(entries))

new_data_set = []
for x in entries:
    new_data_set.append({
        'name': x['trading-name'],
        'price': x['price']
    })

new_data_set = [{'name':x['trading-name'], 'price':x['price']} for x in entries]


def munge_data(item):
    """ convert my data to a new format """
    return {
        'name': item['trading-name'],
        'price': item['price']
    }

new_data_set = []
for x in entries:
    new_data_set.append(munge_data(x))

new_data_set = [munge_data(x) for x in entries]

app = Flask(__name__)

@app.route('/')
def fuel_price():
    return render_template('fuellist.html', data_set=new_data_set)

output = """
<html>
<body>
<table>
    <tr>
        <th>name</th>
        <th>price</th>
    </tr>
"""

for x in new_data_set:
    output += f"""
    <tr>
        <td>{x['name']}</td>
        <td>{x['price']}</td>
    </tr>
    """

output += """
</table>
</body>
</html>
"""

with open('output.html', 'w') as file_obj:
    file_obj.write(output)
