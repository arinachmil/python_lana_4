#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # загрузка формы в py-скрипт

        self.setWindowTitle('Работа с визуальными табличными данными в Python')

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0

        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 20)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                item = self.tableWidget.item(row, col).text()
                col += 1
            row += 1
            col = 0

        # [0] - число единиц, [1] - 1-ый максимум, [2] - строка 1-ого максимума,
        # [3] - 2-ой максимум, [4] - столбец 2-ого максимума
        list_information_max_num = finder(self.tableWidget)

        if not list_information_max_num:
            self.label_error.setStyleSheet("QLabel { color : red}")
            self.label_error.setText('Введены неправильные данные!')
        else:
            # выводим на кэран информацию о расположении максимального числа
            self.label_max_el.setText(
                'Количество единиц в 3-ей строке: ' + str(list_information_max_num[0]) + ' \nМаксимум 1-ого столбца: ' +
                str(list_information_max_num[1]) + ' [' + str(list_information_max_num[2]) + '][0]' +
                '\nМаксимум 2-ого столбца: ' + str(list_information_max_num[3]) +
                ' [' + str(list_information_max_num[2]) + '][1]')

    def solve(self):
        try:
            list_information_max_num = finder(self.tableWidget)

            self.label_error.setText('')
            if not list_information_max_num:
                self.label_error.setText('Введены некорректные данные!')
            else:
                self.label_max_el.setText(
                    'Количество единиц в 3-ей строке: ' + str(
                        list_information_max_num[0]) + ' \nМаксимум 1-ого столбца: ' +
                    str(list_information_max_num[1]) + ' [' + str(list_information_max_num[2]) + '][0]' +
                    '\nМаксимум 2-ого столбца: ' + str(list_information_max_num[3]) +
                    ' [' + str(list_information_max_num[2]) + '][1]')

                count = list_information_max_num[0]
                max_num1 = list_information_max_num[1]
                row_max_number1 = list_information_max_num[2]
                max_num2 = list_information_max_num[3]
                row_max_number2 = list_information_max_num[4]

                # -*- решение задания -*-
                if count != 5:
                    self.label_error.setStyleSheet("QLabel { color : red}")
                    self.label_error.setText(
                        '3-я строка не только из единиц.\n'
                        'Задание не будет выполнено.'
                    )
                else:
                    self.tableWidget.setItem(row_max_number1, 0, QTableWidgetItem(str(max_num1 * 2)))
                    self.tableWidget.setItem(row_max_number2, 1, QTableWidgetItem(str(max_num2 * 3)))
                    self.label_error.setStyleSheet("QLabel { color : green}")
                    self.label_error.setText('Выполнено!')
        except:
            self.label_error.setText('Введены некорректные данные!')


def finder(table_widget):
    """
    находим два максимума и их координаты и проверяем 3-ю строку из таблицы
    :param table_widget: таблица
    :return: [count, max_num1, row_max_number1, max_num2, row_max_number2], если выкинуто исключение,
            то None
    """

    row_max_number1 = 0  # номер строки, в котором находится максимальне число 1-ого столбца
    max_num1 = int(table_widget.item(row_max_number1, 0).text())  # Максимальное значение 1-ого столбца

    row_max_number2 = 0  # номер строки, в котором находится максимальне число 2-ого столбца
    max_num2 = int(table_widget.item(row_max_number2, 1).text())  # Максимальное значение 2-ого столбца

    count = 0
    row = 0
    col = 0

    try:
        while col < table_widget.columnCount():
            number = int(table_widget.item(2, col).text())
            if number == 1:
                count += 1
            col += 1
        while row < table_widget.rowCount():
            number1 = int(table_widget.item(row, 0).text())
            number2 = int(table_widget.item(row, 1).text())
            if number1 > max_num1:
                max_num1 = number1
                row_max_number1 = row
            if number2 > max_num2:
                max_num2 = number2
                row_max_number2 = row
            row += 1
        return [count, max_num1, row_max_number1, max_num2, row_max_number2]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
