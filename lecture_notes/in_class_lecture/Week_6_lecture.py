"""

Why have more than one type of data structure??
- dictionary --> mutable 
- tuple --> immutable 
- list --> mutable, orderable and sortable

"""

# kinda holds related variables 
#aka holds key-value pairs
fruits_calories = {'apple':10,'banana':30}


#ordered collection of items
vegetables = ('broccoli','leek','potato')

meats = ['beef','chicken','pork']

"""
Accessing data within the data structures 
"""
apple_calories = fruits_calories['apple']

first_vegetable = vegetables[0]

"""
Why have ordered data?
"""

file_size_list_mb = [10,11,14,16,70,900]

smallest_file = file_size_list_mb[0]
largest_file = file_size_list_mb[-1]
largest_file = file_size_list_mb[len(file_size_list_mb)-1]

"""
When values need names, reach for a dictionary!
"""

files_named_size = {
    'tuples_dictionaries.py':12,
    'sample.py':8,
}

sample_file_size = files_named_size['sample.py']

#hello_world_size = files_named_size['hello world!.py']

#will succeed, but return none
files_named_size.get('hello_world!.py', None)

ordered_machines = [
    {
        'id':'CNC_1',
        'status':'running',
        'temperature': 45.2
    },
    {
        'id':'CNC_2',
        'status':'idle',
        'temperature': 38.7
     },
    {
        'id':'robot_1',
        'status':'fault',
        'temperature': 52.4
    },
]

nested_machines = {
    'CNC_1': {
        'status':'running',
        'temperature':45.2
    },
    'CNC_2': {
        'status':'idle',
      'temperature':[38.7,45.2]
    },
    'robot_1': {
        'status':'fault',
        'temperature':52.4
    }
}

ordered_machines[1]['status']

for machine in ordered_machines:
    if machine['machine'] == 'CNC_2':
        stauts = machine['status']


nested_machines['CNC_2']['status']
print(nested_machines['CNC_2']['temperature'][0])

cnc_tools = ('parting','end_mill') 