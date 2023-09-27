from example import SingletonExample as SE1
from example import SingletonExample as SE2

the_one_instance = SE1.get_instance()
print(the_one_instance)

the_same_instance = SE2.get_instance()
print(the_same_instance)

print(SE1())