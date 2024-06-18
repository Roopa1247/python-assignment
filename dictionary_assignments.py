"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""

student_info={'student_name':"Roopa",'age':23,'roll_no':280071,'class':"btech",'section':'A','percentage':90,'college_name':'vignan',}
print(student_info['percentage'])

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
students_info={'student_names': ['roopa', 'laxmi', 'durga'], 'ages': [19, 23, 27],
                 'roll_nos':[101, 102,103],'classes': ['lkg','UKG',"btech"],
                 'sections': ['A','B','C'],'percentages':[65.6, 78.9, 99.1],
                  'university':["vignan","githam","gayathri"]
                 }
print(students_info['classes'][2])



"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employees={
    "emp_1":{"name":'pinky','salary':30000,"designation":'testing'},
    "emp_2":{"name":'roopa','salary':30000,"designation":'jE'},
    "emp_3":{"name":'durgs','salary':30000,"designation":'automation'},
    "emp_4":{"name":'vinny','salary':30000,"designation":'SE'}
           }
print(employees["emp_3"]["designation"])


