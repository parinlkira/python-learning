# A simple login tracker using a dictionary to COUNT login attempts for list of users

users = ['alice', 'bob', 'charlie', 'alice', 'bob', 'alice', 'charlie', 'bob',
 'dave', 'eve', 'eve']

# declaring empty dict 
logins = {}

# for looping the logic
for username in users:
    if username in logins:
        logins[username] += 1
    else:
        logins[username] = 1

# now printing the dict output in formatted way

for user, numbertimes in logins.items():
    print(f" {user:8} : {numbertimes} logins")