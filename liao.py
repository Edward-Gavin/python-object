#! /usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('{:d}'.format(self.score))

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
