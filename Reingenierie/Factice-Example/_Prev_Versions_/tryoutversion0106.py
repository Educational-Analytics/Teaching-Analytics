import random
import numpy as np
from math import *

"""
test = 1
test2 = 2
c1a = [test == 0, test == 1, test == 2]
c1b = [test2 == 0, test2 == 1, test2 == 2]
c2 = [0, 1, 2]
conditions_predict1 = np.select(c1a, c2)
conditions_predict2 = np.select(c1b, c2)
conditions_predict = [conditions_predict1, conditions_predict2]
print(conditions_predict)

c3 = [[0,1], [0,2], [0,3], [0,4], [0,5], []]

#Slip, guess, B
def test(type, level):
     #Define some conditions and associated values to determine the slip, guess per Quiz
    conditions_sgb = [type == 'QCU' and level == 'Trop Facile', type == 'QCU' and level == 'Facile', type == 'QCU' and level == 'Adapte', type == 'QCU' and level == 'Difficile', type == 'QCU' and level == 'Trop Difficile',
                      type == 'QCM' and level == 'Trop Facile', type == 'QCM' and level == 'Facile', type == 'QCM' and level == 'Adapte', type == 'QCM' and  level == 'Difficile', type == 'QCM' and  level == 'Trop Difficile',
                      type == 'QROC' and level == 'Trop Facile', type == 'QROC' and level == 'Facile', type == 'QROC' and level == 'Adapte', type == 'QROC' and  level == 'Difficile', type == 'QROC' and  level == 'Trop Difficile',
                      type == 'QO' and level == 'Trop Facile', type == 'QO' and level == 'Facile', type == 'QO' and level == 'Adapte', type == 'QO' and  level == 'Difficile', type == 'QO' and  level == 'Trop Difficile']
    choice_sgb = [ [round(random.uniform(0, 0.10), 2), round(random.uniform(0.90, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.75, 0.90), 2)], [round(random.uniform(0, 0.30), 2), round(random.uniform(0.40, 0.70), 2)], [round(random.uniform(0, 0.40), 2), round(random.uniform(0.30, 0.40), 2)], [round(random.uniform(0, 0.75), 2), round(random.uniform(0.20, 0.30), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.80, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.70, 0.80), 2)], [round(random.uniform(0, 0.30), 2), round(random.uniform(0.40, 0.70), 2)], [round(random.uniform(0, 0.50), 2), round(random.uniform(0.30, 0.40), 2)], [round(random.uniform(0, 0.75), 2), round(random.uniform(0.20, 0.30), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.50, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.40, 0.75), 2)], [round(random.uniform(0.20, 0.50), 2), round(random.uniform(0.25, 0.40), 2)], [round(random.uniform(0.50, 0.75), 2), round(random.uniform(0.15, 0.25), 2)], [round(random.uniform(0.75, 1), 2), round(random.uniform(0, 0.15), 2)],
                   [round(random.uniform(0, 0.10), 2), round(random.uniform(0.50, 1), 2)], [round(random.uniform(0, 0.20), 2), round(random.uniform(0.30, 0.75), 2)], [round(random.uniform(0.20, 0.75), 2), round(random.uniform(0.15, 0.30), 2)], [round(random.uniform(0.75, 0.90), 2), round(random.uniform(0, 0.15), 2)], [round(random.uniform(0.90, 1), 2), round(random.uniform(0, 0.10), 2)],

    ]
    true_ratio = 2
    slip, guess= np.select(conditions_sgb, choice_sgb), true_ratio
    return slip, guess, b
red = test('QO', 'Trop Difficile')
print(red)
"""

"""
def QCU_PrdCct_level(type, level_array, rand_num):
    conditions_type = [type == 'QCU', type == 'QCM', type == 'QROC', type == 'QO'] #Define the conditions.
    choices_type = [
        [rand_num <= 0.20, 0.20 < rand_num < 0.45,  0.45 <= rand_num <= 0.55, 0.55 < rand_num <= 0.80, 0.80 < rand_num <= 1],  #QCU
        [rand_num <= 0.15, 0.15 < rand_num < 0.35,  0.35 <= rand_num <= 0.50, 0.50 < rand_num <= 0.80, 0.80 < rand_num <= 1],  #QCM
        [rand_num <= 0.10, 0.10 < rand_num < 0.25,  0.25 <= rand_num <= 0.40, 0.40 < rand_num <= 0.75, 0.75 < rand_num <= 1],  #QROC
        [rand_num <= 0.05, 0.05 < rand_num < 0.15,  0.15 <= rand_num <= 0.25, 0.25 < rand_num <= 0.65, 0.65 < rand_num <= 1],  #QO
    ]
    conditions_predict = np.select(conditions_type, choices_type)
    choices_predict = ['Trop Facile', 'Facile', 'Adapte', 'Difficile', 'Trop Difficile'] #Define the values corresponding to the connditions.
    predict_level = choices_predict[np.asarray([index for index in range(len(conditions_predict)) if conditions_predict[index] == 1]).item()]

    ran = random.random()
    condition_correct = [ran >= 0.33, ran < 0.33] #Define the conditions.
    choices_correct = [predict_level, random.choice(list(filter((predict_level).__ne__, choices_predict)))] #Define the values corresponding to the connditions.
    correct_level = np.select(condition_correct, choices_correct) #Select a value depending on the above conditions and values.

    #Return the predicted and correct level of difficulty of the Quiz.
    return predict_level, correct_level

pred_level = ['Trop Facile'] + ['Facile']  + ['Adapte']  + ['Difficile'] +  ['Trop Difficile']  
predict, correct = QCU_PrdCct_level('QCU', pred_level, 0.76)
print(predict, correct)

"""

"""
attempts = 12
type = 'QO'


conditions = [
   type == 'QCU',
   type == 'QCM',
   type == 'QROC',
   type == 'QO'
]

choices = [random.randint(ceil(attempts/3), attempts),
           random.randint(ceil(attempts/4), attempts),
           random.randint(ceil(attempts/2.5), attempts),
           random.randint(ceil(attempts/2), attempts)
           ]

learners = np.select(conditions, choices)


print(learners)
"""


"""
a = [1,2,3]
c = a[0]
b = a

b.remove(c)
correct_level = random.choice(b)

print(correct_level)

x = 20
b = []
for i in range(0, 100):
    a = random.choice(list(range(round(x*0.85), round(x*1.15)+1)))
    b.append(a)

print(b)




def Level_Percent(type, level, attempts):
    learners = random.randint(ceil(attempts/4), attempts)

    if level == 'Trop Facile':
        success = round(random.uniform(learners*0.86, learners))
    elif level == 'Facile':
        success = round(random.uniform(learners*0.75, learners*0.85))
    elif level == 'Adapte':
        success = round(random.uniform(learners*0.60, learners*0.75))
    elif level == 'Difficile':
        success = round(random.uniform(learners*0.20, learners*0.60))
    elif level == 'Trop Difficile':
        success = round(random.uniform(learners*0, learners*0.20))
    failure = learners - success
    percent_success = round((success / learners) * 100, 2) 

    avg_attempts = round(attempts / learners, 2) #Require to be modified
    
    return learners, success, failure, percent_success, avg_attempts


def QCU_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.20:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.20 < rand_num < 0.45:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.45 <= rand_num <= 0.55:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.55 < rand_num <= 0.80:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.80 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

def QCM_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.15:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.15 < rand_num < 0.30:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.30 <= rand_num <= 0.50:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.50 < rand_num <= 0.80:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.80 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###


###

def QROC_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.10:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.10 < rand_num < 0.25:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.25 <= rand_num <= 0.40:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.40 < rand_num <= 0.75:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.75 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

###

def QO_PrdCct_level(rand_num, level_array):
    if rand_num <= 0.5:
        predict_level = 'Trop Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.5 < rand_num < 0.15:
        predict_level = 'Facile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.15 <= rand_num <= 0.25:
        predict_level = 'Adapte'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)


    elif 0.25 < rand_num <= 0.65:
        predict_level = 'Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)

    elif 0.65 < rand_num <= 1:
        predict_level = 'Trop Difficile'
        if random.random() >= 0.25:
            correct_level = predict_level
        else:
            level_array = list(filter((predict_level).__ne__, level_array))
            correct_level = random.choice(level_array)
                
    return predict_level, correct_level

###

def TyLvl_ScsFlr(type, rand_num, level_array, attempts):
    if type == 'QCU':
        predict_level, correct_level = QCU_PrdCct_level(rand_num, level_array)
    elif type == 'QCM':
        predict_level, correct_level = QCM_PrdCct_level(rand_num, level_array)
    elif type == 'QROC':
        predict_level, correct_level = QROC_PrdCct_level(rand_num, level_array)
    elif type == 'QO':
        predict_level, correct_level = QO_PrdCct_level(rand_num, level_array)

    learners, success, failure, success_percent, avg_attempts  = Level_Percent(type, correct_level, attempts)

    return predict_level, correct_level, learners, success, failure, success_percent, avg_attempts 


pred_level_QCU = ['Trop Facile'] * 20 + ['Facile'] * 30 + ['Adapte'] * 20  + ['Difficile'] * 20 +  ['Trop Difficile'] * 10

predict_level, correct_level, learners, success, failure, success_percent, avg_attempts = TyLvl_ScsFlr('QCU', random.random(),  pred_level_QCU, 17)
print(predict_level, correct_level, learners, success, failure, success_percent, avg_attempts)

"""

