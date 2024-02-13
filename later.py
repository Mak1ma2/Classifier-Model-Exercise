import csv 
import random 
from faker import Faker 

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

#creating 2nd dataset (standard deviation) 
    
data2 = [['Name', 'Student id', 'sex', 'overall gpa', 'grade on recent exam', 'letter grade on recent exam', 'gym_exam_score']]

for i in range(260): 
    name = fake.name() 
    id = f"{i+260}".zfill(3) 
    sex = random.choice(sex_list) 
    overall_gpa = format(random.uniform(2.0, 4.0), '.2f') 
    