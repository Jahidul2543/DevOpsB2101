letters = ['a', 'b', 'c', 'd', 'e']
letters[1:2] = ['B', 'C']
print(letters)
letters[:] = []
print(letters)

questions = ['name', 'quest', 'favorite color', 'name']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions,answers):
    print(q, a)

for i in sorted(questions):
    print('sorted list {}'.format(i))

for i in set(questions):
    print(i)
