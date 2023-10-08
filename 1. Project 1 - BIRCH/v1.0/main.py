contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

contact_name = input()

for i in range(len(contacts)):
    if (contacts[i][0] == contact_name):
        print(contact_name, "is", contacts[i][1])
    else:
        print("Not Found")
