import csv 
import random 
from faker import Faker 

"""
This code is used only for creating the csv files for the exercise. 
I will make changes to this later in the future for a neater algorithm + code, will be developing this file to end up generating csv datasets based on prompts
"""

fake = Faker() 

grade_scale = { 
    "A+": 97, 
    "A": 93, 
    "A-": 90, 
    "B+": 87, 
    "B": 83, 
    "B-": 80, 
    "C+": 77, 
    "C": 73, 
    "C-": 70, 
    "D+": 67, 
    "D": 63, 
    "D-": 60, 
    "F": 0 
}

#overall data
data = [['Name', 'Student id', 'sex', 'overall gpa', 'grade on recent exam', 'letter grade on recent exam', 'gym_exam_score']]

#do not take variable naming seriously 
sex_list = ["male", "female"]
grades = ["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]

#total dataset will have 260 values 
#creating first dataset (equal relation between each letter grade) 
# 20 values for each scale 

for i in range(260): 
    name = fake.name() 
    id = f"{i}".zfill(3) 
    sex = random.choice(sex_list) 
    overall_gpa = format(random.uniform(2.0, 4.0), '.2f') 
    index = (int)(i / 20) 
    letter = grades[index] 
    lower_bound = grade_scale[letter]
    if index == 12: 
        upper_bound = 100 
    else: 
        upper_bound = grade_scale[grades[index + 1]] - 1
    recent_exam = f"{random.randint(lower_bound, upper_bound)}"
    gym_score = f"{random.randint(0, 100)}" 

    data.append([name, id, sex, overall_gpa, recent_exam, letter, gym_score]) 
    
with open('teacher1.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(data) 

csvfile.close() 

#creating 2nd dataset (bell curve) 
#normal distribution of grades: 2% A, 14% B, 68% C, 14% D, 2% F 
#5.2 A, F 
#176.8 C
#36.4 B, D
# if we go by whole numbers then we'll get 258, the remaining 2 students will go to B and D to follow equal distribution over the bell curve 
    
data2 = [['Name', 'Student id', 'sex', 'overall gpa', 'grade on recent exam', 'letter grade on recent exam', 'gym_exam_score']]

for i in range(260): 
    name = fake.name() 
    id = f"{i+260}".zfill(3) 
    sex = random.choice(sex_list) 
    overall_gpa = format(random.uniform(2.0, 4.0), '.2f') 
    if i < 5: 
        recent_exam = random.randint(grade_scale['A-'], 100)
    elif i >= 5 and i < 41: 
        recent_exam = random.randint(grade_scale['B-'], grade_scale['A-'] - 1)
    elif i >= 41 and i < 218:
        recent_exam = random.randint(grade_scale['C-'], grade_scale['B-'] - 1)
    elif i >= 218 and i < 255: 
        recent_exam = random.randint(grade_scale['D-'], grade_scale['C-'] - 1)
    else: 
        recent_exam = random.randint(grade_scale['F'], grade_scale['D-'] - 1)
    letter = "A+" 
    for letters in grade_scale.__reversed__(): 
        if grade_scale[letters] <= recent_exam: 
            letter = letters 
    gym_score = f"{random.randint(0, 100)}" 
    recent_exam = f"{recent_exam}"

    data2.append([name, id, sex, overall_gpa, recent_exam, letter, gym_score]) 

with open('teacher2.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(data2) 

csvfile.close()

#creating the 3rd dataset 
# full randomization
data3 = [['Name', 'Student id', 'sex', 'overall gpa', 'grade on recent exam', 'letter grade on recent exam', 'gym_exam_score']]

for i in range(260): 
    name = fake.name() 
    id = f"{i+520}".zfill(3) 
    sex = random.choice(sex_list) 
    overall_gpa = format(random.uniform(2.0, 4.0), '.2f') 
    score = random.randint(0, 100) 
    letter = "A+" 
    for letters in grade_scale.__reversed__(): 
        if grade_scale[letters] <= score: 
            letter = letters 
    recent_exam = f"{score}"
    gym_score = f"{random.randint(0, 100)}" 

    data3.append([name, id, sex, overall_gpa, recent_exam, letter, gym_score]) 

with open('teacher3.csv', 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(data3) 

csvfile.close()