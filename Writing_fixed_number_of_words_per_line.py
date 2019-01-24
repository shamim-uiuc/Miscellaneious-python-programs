#!/usr/bin/python
#Author: Md Shamimuzzaman
#Date: Jan 3, 2018

import re

#Taking string as a input, convert to list and sorting words. Finally return as a string 
def raw_input_string_sort(str):
    list=str.split(',');
    list.sort();
    str=','.join(list);
    return str;

#Taking string as a input, convert to list and sorting words. Finally return as a string. Taking delim varible as a std input 
def raw_input_string_sort_advance(str, delim):
    list=str.split(delim);
    list.sort();
    str=delim.join(list)
    return str

#Taking string as a input, convert to list and sorting words. Finally return as a string. Taken care of multiple delimiters (,.;:_)
def raw_input_string_sort_advance2(str):
    #str=str.replace(';',' ').replace(',',' ').replace('_',' ').replace('-',' ').split()
    list = re.split('\W+|_', str)
    list.sort()
    str=','.join(list)
    return str


def file_string_sort_and_writing_fixed_words_per_line(input_file_name, output_file_name, no_words_line):
    input_fo=open(input_file_name,"r")
    str1=input_fo.read()
    #Keeping only alphanumeric characters plus underscores(_)
    str1=re.sub("[^a-zA-Z0-9_]"," ", str1)
    #Removing leading and trailing whitespaces
    str1=str1.strip()
    #converting strings into list of words
    list1=re.split('\W+', str1)
    #print list1

    #Intilizing variable for number of words per line
    i=0
    output_fo = open(output_file_name, "wb")
    #the operation will continue until it reaches the value less than lenth of the list
    while i<len(list1):
        #Creating a small list(equivalent to line in output file) with fixed number of words by providing the number from the keyboard as input
        small_list=list1[i:i+no_words_line]
        #Converting the list into strings
        str1=' '.join(small_list)
        #Writing the output into txt file
        output_fo.write(str1+"\n");
        #loop will continue 
        i=i+no_words_line
        
    output_fo.close()
    return
 

############################## Main begins here  #######################################################################
#handles comma seperated string
#str=raw_input("Enter comma separated string: [world,hello,my,name,abc,python]:   ") # str=world,hello,my,name,abc,python
#str=raw_input_string_sort(str)
#print str #str=abc,hello,my,name,python,world

#handles string with specific delimeter
#str=raw_input("Enter string: ") # str=world,hello,my,name,abc,python  str=world hello my name abc python str=world_hello_my_name_abc_python str=world;hello;my;name;abc;python
#delim=raw_input("Enter delimeter: [,  _ ;]:   ")
#str=raw_input_string_sort_advance(str, delim)
#print str #str=abc,hello,my,name,python,world str=abc hello my name python world str=abc_hello_my_name_python_world str=abc;hello;my;name;python;world 

#handles any delimeter string
#str=raw_input("Enter string: ") # str=world,hello,my,name,abc,python  str=world hello;my_name,abc-python str=world_hello_my_name_abc_python str=world;hello;my;name;abc;python
#str=raw_input_string_sort_advance2(str)
#print str #str=abc,hello,my,name,python,world


#handles raw strings from a file
input_file_name=raw_input("Enter name of input file: ") # fo=test.txt
output_file_name=raw_input("Enter name of output file: ") # fo=output.txt
no_words_line=input("Enter no of words per line: ") # 10
file_string_sort_and_writing_fixed_words_per_line(input_file_name, output_file_name, no_words_line)
#output_file: 3,2018,author,bin,Date,import,Jan,md,python,re,shamimuzzaman,user


