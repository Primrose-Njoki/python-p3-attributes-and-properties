#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name="rose"):
        self.name=name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if isinstance(value,str) and 1 <=len(value) <=25:
                self._name =value.title()

        else:
            #print("Name must be string between 1 and 25 character.")
            self._name = "Name must be string between 1 and 25 character."
p1=Person("cate")
print(p1.name)

p2= Person("")
print(p2.name)
