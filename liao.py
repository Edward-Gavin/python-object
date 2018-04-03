#! /usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, gender, score):
        """
        设置私有（private）变量，只有内部可以访问，外部不可访问
        :param name:
        :param score:

        """
        self.__gender = gender
        self.__name = name
        self.__score = score

    def set_score(self, score):
        self.__score = score

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def get_score(self):
        return self.__score

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


if __name__ == '__main__':
    bart = Student('shiwei', 24)
    print(bart.get_grade())
