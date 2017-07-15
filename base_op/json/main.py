import json
from datetime import datetime

with open('in.json') as jfile:
    jdata = json.load(jfile)

# convert to date
begin_shelf_date = datetime.strptime(jdata['begin_shelf_date'], '%d.%m.%Y').date()
print(begin_shelf_date)

# iter from all elm
for item in jdata.items():
    print('{0}: {1}'.format(item[0], item[1]))

# iter deep el
for mech in jdata['promo_mechanics']:
    print('id={0} value={1}'.format(mech['id'], mech['value']))
    for att in mech.get('attachments', []):
        print('\tid={0}, name={1}'.format(att['id'], att['name']))

# convert to json and save
sales_plan = jdata['sales_plan']
with open('out.json', 'w') as jfile:
    js = json.dumps(sales_plan, indent=4)
    jfile.write(js)
