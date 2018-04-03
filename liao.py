#! /usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    pass


if __name__ == '__main__':
    bart = Student('shiwei', 24)
    print(bart.name)
