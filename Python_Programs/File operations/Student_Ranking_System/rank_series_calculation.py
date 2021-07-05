#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:04:58 2021

@author: giri
"""


import input_file_creation

#Creating input.txt file from the below module & its method.
input_file_creation.student_database()

#total score calculation for each student who has scored on 'n' subjects
def total_marks_calculation(total_mark_list):
    with open('student_database_ranking.txt','w+') as out_file:
        with open('student_database.txt','r') as in_file:
            lines = in_file.readlines()
            for line in lines:
                new_line_remover = line.rstrip('\n')
                
                stripped_data_on_line = new_line_remover.split(',')
                total_score = 0
                for i in range(1,len(stripped_data_on_line)):
                     subject_marks = (stripped_data_on_line[i].split('-'))[1]
                     total_score+=int(subject_marks)
                
                total_mark_list.append(total_score)
                
                out_file.write(new_line_remover+','+'TotalScore-'+str(total_score)+'\n')
                
                        
#calculating the ranking series for the student based on their total score
def rank_series_calculation(total_mark_list):
    
    with open('student_database_ranking.txt','r+') as out_file:
        lines = out_file.readlines()
        with open('student_database_ranking.txt','w') as file:
            for line in lines:
                new_line_remover = line.rstrip('\n')
                
                stripped_data_on_line = new_line_remover.split(',')
                
                total_mark_for_rank = int((stripped_data_on_line[len(stripped_data_on_line)-1]).split('-')[1])
                
                rank_indexing = total_mark_list.index(total_mark_for_rank)+1
                
                file.write(new_line_remover+','+'Rank-'+str(rank_indexing)+'\n')
                
                
            
if __name__ == "__main__":
    #to store total marks of each students on all subjects 
    total_mark_list = list()
    total_marks_calculation(total_mark_list)
    total_mark_list = list(set(total_mark_list))
    total_mark_list.sort(reverse=True)
    rank_series_calculation(total_mark_list)
