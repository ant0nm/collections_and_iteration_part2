import math

def display_cohorts(c):
    for cohort_name, num_students in c.items():
        print("{} : {} students".format(cohort_name, num_students))

def sum_students(c):
    sum = 0
    for num_students in c.values():
        sum += num_students
    return sum

students = {
    'cohort1': 34,
    'cohort2': 42,
    'cohort3': 22
}

print()
display_cohorts(students)

# add a new cohort
students['cohort4'] = 43
print()
display_cohorts(students)

# print all the cohort names
print()
for cohort_name in students.keys():
    print(cohort_name)

# classrom expansion
for cohort_name, num_students in students.items():
    students[cohort_name] = math.ceil(num_students * 1.05)
print()
display_cohorts(students)

# remove cohort 2 from the dictionary
students.pop('cohort2')
print()
display_cohorts(students)

# total number of students
number_of_students = sum_students(students)
print()
print("The total number of students is {}.".format(number_of_students))
