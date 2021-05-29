data = [
  {
    'name':'Sam',
    'service':'Driver' 
  },
  {
    'name':'Ram',
    'service':'Capenter' 
  },
  {
    'name':'Sam',
    'service':'Delivery' 
  },
  {
    'name':'Ram',
    'service':'Cook' 
  }
]

new_data_set = []
for i in data:
  for j in new_data_set:
    if j['name'] == i['name']:
      j['service'].append(i['service'])
      break
  else:
    cur = {
      "name" : i['name'],
      'service' : [i['service']]
    }
    new_data_set.append(cur)
  
print(new_data_set)
