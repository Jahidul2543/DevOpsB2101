
def if_demo():
    character = False
    if character:
        print('Jahiudl is a good boy')
    elif character == False:
        print('We dont know')
    else:
        print('Jahiudl Is a bad boy')


def while_demo():
    count = 6
    while count < 5:
        print('Iteration {}'.format(count))
        count = count + 1
    else:
        print('While condition is false')


def for_demo():
    fruits = ['apple', 'banana', 'grape']
    for f in range(2):
        print(fruits[f+1]) # 0-1, 1-1=0

for_demo()