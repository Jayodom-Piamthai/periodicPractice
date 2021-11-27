import random

a3 = ['a','b','c']
sampled_list = str(random.sample(a3,1))
print(sampled_list)
correctAnswer = 0
if sampled_list in a3 :
    correctAnswer = correctAnswer+1
print(correctAnswer)