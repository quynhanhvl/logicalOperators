'''
For this assignment you should look at the code created below and find the error.
For each task, there will be one error that you must find and correct.
Sometimes there will be an explanation of the problem and/or tips that can help you
complete the tasks.
EXAMPLE TASK:
'''
#EX)
#  )Broken: make the code return False
#  )5 == 5 and 4 == 4
#  )Correct:
#  )5 == 5 and not(4 == 4)
#  This is just one way to do it. There is more that one way to make this false.

'''
END EXAMPLE
'''

'''
START HERE
'''

#1)
# )Broken: Change the code so it returns True
# )4 !== 4 and 3 == 3 
# )Correct:
f = (4==4) and (3==3)
print(f)

#2)
# )Broken: Change the code so it returns True
# )3**2 == 3+2 or 1+2 <= 3 and !True
# )Correct:
g = (3*2==3+2) or (1+2<=3) and (True)
print(g)

#3)
# )Broken: Change it so it returns False
# )(True and False) or (True or false)
# )Correct:
h = (True and False) and (True or False)
print(h)

#4)
# )Broken: Make the code return True
# )((5==5) and 4<3) and not(True and 8**2 >= 64)
# )Correct:
i = ((5==5) and 2<3) and not(True and 8*2>=64)
print(i)

#5)
# )Broken:Make the code return False
# )a = True
# )b = False
# )((a or b) and a) or (a or b)
# )Correct:
a = True
b = False
j = ((a or b) and a) and (a and b)
print(j)

#6)
# )Broken: make the code return True
# )a = True
# )b = False
# )not(a or b) and a
# )Correct:
a = True
b = False
k = not(a or b) or a 
print(k)
