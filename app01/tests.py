from django.test import TestCase


# Create your tests here.

class T1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def plus_def(self, item):
        item += 1
        print(item)


t1  = T1('humu','32')
print(t1)