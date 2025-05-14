#class Human:
#     species ='Homo sapiens' #class attribute
#     def __init__(self,name):
#       self.name=name # instance attribute 
#         pass
# cate = Human("cate")
# # rose.species="rat"
# # rose.name="mouse"
# print(rose.name)

# rose.nationality="dutch"
#print(rose.nationality)
# 

#my_attr = "is_a_friend"
#getattr(cate,my_attr,false)

class Human:
    species = "Homo sapiens"
    def __init__(self,age):
        self.age = age
    def get_age(self):
        print('RETRIEVING AGE.')
        return self._age 
    def set_age(self,age):
         if (type(age) in (int, float)) and (0 <= age <= 120):
             print(f'setting age to {age}')
             self._age = age
         else:
             print('ooo')

    age = property(get_age,set_age)

rose = Human(age=67)

rose.age = 0 
rose.age= False