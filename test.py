#! /usr/bin/python
# -*- coding: utf-8 -*-


class Employee:
    empCount = 0

    def __init__(self, name, salary, age, sex, tall):
        '''

        :param name:
        :param salary:
        :param age:
        :param sex:
        :param tall:
        '''
        self.name = name
        self.salary = salary
        self.age = age
        self.sex = sex
        self.tall = tall
        Employee.empCount += 1

    @staticmethod
    def displaycount():
        '''

        :return:
        '''
        print('total Employee {:d}'.format(Employee.empCount))


    def displayemployee(self):
        '''

        :return:
        '''
        print('Name: ', self.name, ', Salary: ', self.salary)


def print_h(a, b, c):
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''
    print('hello, world! ')


if __name__ == "__main__":
    emp = Employee('wang', 23, 25, 'm', 178)
    print(emp.tall)
