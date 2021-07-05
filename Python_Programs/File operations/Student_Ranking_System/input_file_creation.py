# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:22:13 2020
@author: gshambul
"""


#to create a list of students & subjects names if it known to user
def creation_subject_and_student_name():
    for i in range(1,student_count+1):
        student_name  = str(input("Enter the {} student name : ".format(i)))
        student_name_list.append(student_name)
    for i in range(1,subject_count+1):
        subject_name = str(input("Enter the {} subject name : ".format(i)))
        subject_name_list.append(subject_name)



#craeting a student_database by having all proper input data 
def student_database():
    if( student_count >= 1 and subject_count >= 1 ):
        with open('student_database.txt','a+') as  database_file:
            if('yes' == (str(input("Type 'Yes' if you know the students name & subject names on this academic year : "))).lower()):
                #function calling
                creation_subject_and_student_name()
                
                for i in range(0,len(student_name_list)):
                    database_file.write(student_name_list[i]+'-'+str(i+1))
                    
                    for j in range(0,len(subject_name_list)):
                        database_file.write(',')
                        subject_mark = int(input("Enter the mark which {} has scored on {} out of 100 : ".format(student_name_list[i],subject_name_list[j])))
                        database_file.write(subject_name_list[j]+'-'+str(subject_mark))
                        
                    database_file.write('\n')
            
            
            else:
                print(" \n Default names & subjects will taken into considaration \n")
                for i in range(1,student_count+1):
                    database_file.write('Student-'+str(i))
                    for j in range(1,subject_count+1):
                        database_file.write(',')
                        subject_mark = int(input("Enter the mark which student {} obtained for subject {} out of 100 : ".format(i,j)))
                        database_file.write('Subject'+str(j)+'-'+str(subject_mark))
                    database_file.write('\n')
                        
            
            
            
    else:
        print("Please do provide us the proper input count for student count & subject count , and Retry ...")
        
    

if __name__ == "__main__":
    student_count = int(input("Enter the students count in a class : "))
    subject_count = int(input("Enter the subjects count which each student has on this academic year : "))
    student_name_list = list()
    subject_name_list = list()
    student_database()
