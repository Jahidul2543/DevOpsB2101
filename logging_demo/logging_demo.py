import logging
from self import self

logging.basicConfig(filename='log/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)
self.logger = logging.getLogger('urbanGUI')


def logging_demo():
    logging.info('Let\'s read from a JSON file')
    logging.info('This is debug level')
    # logging.error('Error level logging')

    while True:
        try:
            logging.info('User Input')
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            logging.error("Oops!  That was no valid number.  Try again...")


def main():
    logging_demo()


if __name__ == '__main__':
    main()