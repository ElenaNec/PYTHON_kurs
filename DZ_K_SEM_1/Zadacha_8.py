# Задача 8: 
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input("Введите размер шоколадки по вертикали m = "))
n = int(input("Введите размер шоколадки по горизонтали n = "))
k = int(input("Введите количество долек k = "))

if  k % m == 0 or k % n == 0 :
    print("От шоколадки можно отделить {} кусочка одним разломом".format(k))
else :
    print("От шоколадки нельзя отделить {} кусочка одним разломом".format(k))
    