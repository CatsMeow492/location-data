# search for a contact from a list of tuples

contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

x = input()

for i in range(len(contacts)):
    if x in contacts[i]:
        print(f'{contacts[i][0]} is {contacts[i][1]}')
    