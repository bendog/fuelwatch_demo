from jinja2 import Template, Environment, FileSystemLoader, select_autoescape
from get_feed import get_feed

feed = get_feed()

entries = feed['entries']

new_data_set = []
for x in entries:
    new_data_set.append({
        'name': x['trading-name'],
        'price': x['price']
    })

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html'])
)

template = env.get_template('fuellist.html')

print(template.render(data_set=new_data_set))
