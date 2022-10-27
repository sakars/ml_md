import random
###########################
########### setup
###########################
# Ideja: https://www.youtube.com/watch?v=pKO9UjSeLew&ab_channel=JomaTech
n=7
s = set(range(1,n ))
l=[random.randint(1, n-1) for x in range(n)]
print(l)


###########################
########### atrodi dubultos
###########################
# Atrodi visus dubultos skaitļus un ievieto tos doubles listē
# l ir 7 gara liste ar numuriem 1-6 => būs vienmēr situacija
# kad būs dubulti skaitļi
# s ir set ar numuriem 1-6
doubles=[l[i] for i in range(0,n) for i2 in range(i+1,n) if l[i]==l[i2]]
# TODO
print(doubles)


    