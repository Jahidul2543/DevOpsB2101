
doc_string = """

Hello this is a paragraph
And it is another string

"""

first_name = 'John'
last_name = 'Jack'
age = 34
print('MyName ' + first_name)
print('My Full Name: {} {}, Age: {} Years'.format(first_name, last_name, age))
x = 4
print(x)
print(type(x))
f = 5.666666666666667
print(type(f))

course_name = 'aws devops aa'
print('Total letters: {}'.format(course_name.count(' ', 0, 4)))
v = course_name.find('aa', 0, 14)
v2 = course_name.index('d')
print(v2)

# tuple
tuple_demo = (12, 23, 4,'a')
print(tuple_demo)
print('Count: '.format(tuple_demo.count(4))) # Count: + 1

print(type(tuple_demo))

my_list = [12, 23, 4,'a']
my_list.append('Jack')
# my_list.insert(2, 400)
# my_list.pop(0)
my_list.remove(12)
print('MyList: {}'.format(my_list))
print(type(my_list))

# List, Dict, Set, if else, foreach



