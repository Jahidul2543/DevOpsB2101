import base


def get_info():
    my_dict = {
        'name': 'John',
        'City': 'New York',
        'Zip Code': 12453,
        'Country': 'USA'
    }
    print(type(my_dict))
    print(my_dict.get('name'))

    for k, v in my_dict.items():
        print(k, v)


def function2():
    print('Function 2')

# get_info()
# function2()

# double under = dunder


def main():
    # function2()
    # base.my_helper()
    get_info()


if __name__ == "__main__":
    main()



