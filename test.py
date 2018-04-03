#! /usr/bin/python
# -*- coding: utf-8 -*-


class Man:

    def __init__(self, name, age, sex, tall):
        """

        :param name:
        :param age:
        :param sex:
        :param tall:
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.tall = tall

    @staticmethod
    def eat(self):
        print('eat food')

    @staticmethod
    def sleep(self):
        print('run ')


class Employee(Man):
    empCount = 0

    def __init__(self, salary):
        self.salary = salary

        Employee.empCount += 1

    @staticmethod
    def displaycount():
        """

        :return:
        """
        print('total Employee {:d}'.format(Employee.empCount))

    def displayemployee(self):
        """

        :return:
        """
        print('Name: ', self.name, ', Salary: ', self.salary)


def print_h(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    d = a+b+c
    print('hello, world! {:d}'.format(d))


if __name__ == "__main__":
    man = Man('wang', 23, 'M', 178)
    emp = Employee(23)
    pass

