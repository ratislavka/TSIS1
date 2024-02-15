import json

# Load the data from the JSON file
with open('sample-data.json') as f:
    data = json.load(f)

# Check if the data is a list
if isinstance(data, list):
    # Print the header
    print('Interface Status')
    print('=' * 80)
    print('{:<50} {:<20} {:<6} {:<6}'.format('DN', 'Description', 'Speed', 'MTU'))
    print('-' * 80)

    # Parse and print the data
    for item in data:
        # Check if the item is a dictionary
        if isinstance(item, dict):
            dn = item.get('dn', '')
            description = item.get('descr', '')
            speed = item.get('speed', '')
            mtu = item.get('mtu', '')
            print('{:<50} {:<20} {:<6} {:<6}'.format(dn, description, speed, mtu))
        else:
            print('Error: Item is not a dictionary:', item)
else:
    print('Error: Data is not a list:', data)
