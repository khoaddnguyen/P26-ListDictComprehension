#LOOPING THROUGH DATAFRAME

student_dict = {
    "student": ["Cece", "Nana", "Bento"],
    "score": [77, 97, 55]
}


# Looping through dictionaries:
#for (key, value) in student_dict.items():
#    print(value)

# Looping through and print a DF
import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

print(student_data_frame)

# Looping through a DF column
for (key, value) in student_data_frame.items():
    print(key)
    print(value)

# Looping through a DF row
for (index, row) in student_data_frame.iterrows():
    #print(row)
    #print(row.student)
    #print(row.score)
    if row.student == "Bento":
        print(row.score)
