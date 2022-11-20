import base64
import configparser
import logging
from datetime import datetime

config = configparser.ConfigParser()
config.read('config.ini')


def encode_str(regular_string):
    return base64.b64encode(regular_string.encode('ascii'))


def generate_file_name(extension, prefix):
    now = datetime.now()  # current date and time

    year = now.strftime("%Y")
    # print("year:", year)

    month = now.strftime("%m")
    day = now.strftime("%d")

    # time = now.strftime("%H:%M:%S")
    # print("time:", time)

    # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    return prefix+day+"-"+month+"-"+year+extension


def saveLog(message):

    filename = "logs/" + generate_file_name(".logs", "logs-")
    with open(filename, mode='a') as file:
        # f = open(filename, "a")
        file.close()

    logging.basicConfig(filename=filename, filemode='a', datefmt='%H:%M:%S',
                    level=logging.DEBUG, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')
    logging.info(message)
