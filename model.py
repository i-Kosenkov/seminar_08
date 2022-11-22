import sys
import pandas
import interface
import controller
import logger


def view_file():
    logger.logging.info("Просмотр базы данных")
    data = pandas.read_csv('db.csv')
    interface.view_data(data)


def add_new_row():
    pass


def delete_row():
    pass


def menu(data):
    if data == '1':
        view_file()
    elif data == '2':
        add_new_row()
    elif data == '3':
        delete_row()
    else:
        sys.exit()
