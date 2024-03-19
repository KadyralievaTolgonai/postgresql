class Person:
    def __init__(self):
        self.__name=None
        self.__last_name=None
        self.__age=None
        self.__email=None
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name=new_name
       
    @property
    def last(self):
        return self.__last_name
    @last.setter
    def last(self,new_last):
        self.__last_name=new_last
       
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,new_age):
        self.__age=new_age
       
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,new_email):
        self.__email=new_email
        
    
john = Person()
print(john.name) # None
print(john.last) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com

class Dog:
    def voice(self):
        return "gav"
class Cat:
    def voice(self):
        return "mya"
def to_pet(voice):
    print(voice.voice())
    # print(voice.voice())
barsik=Dog()
rex=Cat()

to_pet(barsik)
to_pet(rex)




# 1) Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.
# У класса должен быть один метод set_deadline, который принимает дату дедлайна (в
# виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.
# Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin,
# DeleteMixin, UpdateMixin, ReadMixin:
# в классе CreateMixin определите метод create, который принимет в себя задачу todo и
# ключ key по которому нужно добавить задачу в словарь todos, если ключ уже
# существует верните "Задача под таким ключём уже существует".
# класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу
# key, который передается как аргумент, и возвращает сообщение 'удалили название
# задачу', где вместо слова название должно быть название задачи.
# класс UpdateMixin должен содержать метод update, который принимает в себя ключ key
# и новое значение new_value и заменяет задачу под данным ключом на новое значение.
# класс ReadMixin должен





    
    
    
    






