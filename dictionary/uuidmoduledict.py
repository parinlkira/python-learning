# Importing and using the UUID module in Python

import uuid
# Generate a random UUID but it shows time and MAC address (UUID1)
id = uuid.uuid1()
print(id)

# Generate a random UUID without revealing time and MAC address (UUID4)
id = uuid.uuid4()
print(id)

# Generate a UUID using UUID3 (based on MD5 hash of a namespace and name)
id = uuid.uuid3(uuid.NAMESPACE_OID, 'laptop')
print(id)

# Generate a UUID using UUID5 (based on SHA-1 hash of a namespace and name)
id = uuid.uuid5(uuid.NAMESPACE_OID, 'laptop')
print(id)

# challenge is to generate uuid and assign the items from the list as values to it

items = [['laptop', 1200], ['mouse', 200], ['keyboard', 500], ['tablet', 1500]]

item_data = {}
for item in items:
    id = uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key = id.hex[:6] # Use the first 6 characters of the UUID 
    # as the key and typecast them to hexadecimal using the hex attribute
    item_data[key] = item

print('Item data with UUID keys:')

for k, v in item_data.items():
    print(f'{k}: {v}')
