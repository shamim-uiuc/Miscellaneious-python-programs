#!/usr/bin/python
#Author: Md Shamimuzzaman
#Date: Jan 4, 2018
#Counting words from a text file

#Importing module for regular expression (re)
import re

#input: a txt file
#output: a txt file
#Function: counts the occurance/frequency of individual word in the file and writes into a output txt file


def Freq_individual_words(name_of_input_file, name_of_output_file):
    #opening an input file using a file object and acessing mode as read (r)
    fo_input=open(name_of_input_file,"r")
    #reading entire contents of file into a string
    str1=fo_input.read()
    #Must need to close the file with the file object
    fo_input.close()
    #print str1
    
    #Keeping only alphanumeric characters plus underscores(_)
    str1=re.sub("[^a-zA-Z0-9_]"," ", str1)
    #Removing leading and trailing whitespaces
    str1=str1.strip()
    #converting strings into list of words
    list1=re.split('\W+', str1)     #if needed to convert strings into list of letters # list1=list(str1): can be found entire program below as function name 'Free_Individual_Letters'
    #print list1
    
    #Creating an empty dictionary
    freq_dict1={}
    #Converting a list to a dictionary where words within a list are used as key and frequencies are used as value
    freq_dict1=dict([i,list1.count(i)]for i in list1)
    #print freq_dict1
    #print freq_dict1.items()
    
    
    #Opneing a new file in order to write the output
    fo_output=open(name_of_output_file, "wb")
    #Listing all the dictionary keys
    key_list=freq_dict1.keys()
    #Writing output for each key:value pairs using for loop 
    for keys in key_list:
        fo_output.write(keys + " : " + str(freq_dict1[keys])+"\n")
    fo_output.close()
    
    return





#####For Counting alphabets from a txt file##########################

def Freq_individual_letters(name_of_input_file, name_of_output_file):
    #opening an input file using a file object and acessing mode as read (r)
    fo_input=open(name_of_input_file,"r")
    #reading entire contents of file into a string
    str1=fo_input.read()
    #Must need to close the file with the file object
    fo_input.close()
    #print str1
    
    #Keeping only alphanumeric characters
    str1= re.sub("[^a-zA-Z]","", str1)
        
    #Converting strings into list of letters
    list1=list(str1)
    #list2=['#', '!', ' ', ':', '/', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #list1 = [x for x in list1 if x not in list2] #list1-list2
    
    #print list1
    
    
    #Creating an empty dictionary
    freq_dict1={}
    #Converting a list to a dictionary where letters within a list are used as key and frequencies are used as value
    freq_dict1=dict([i,list1.count(i)]for i in list1)
    #print freq_dict1
    #print freq_dict1.items()
    
    
    #Opneing a new file in order to write the output
    fo_output=open(name_of_output_file, "wb")
    #Listing all the dictionary keys
    key_list=freq_dict1.keys()
    #Writing output for each key:value pairs using for loop 
    for keys in key_list:
        fo_output.write(keys + " : " + str(freq_dict1[keys])+"\n")
    fo_output.close()
    
    return
###################################################################  
   
#To get maximum from a list (we may have a built in list.max() function as well)   
'''def get_max_from_list(lst):
    my_max=0;
    for x in lst:
        if x>my_max:
            my_max=x
    return my_max'''        
   
    
#input: a txt file
#output: a txt file
#function1: counts the number of words per line in a text file and writes output into a text file
#function2: Print the line with maximum number of words
  
def no_words_per_line(name_of_input_file,name_of_output_file):
    #open a text file for reading
    fo_input=open(name_of_input_file,"r")
    #Reading each line separately into a list; each line become a list element
    line_list=fo_input.readlines()
    #print line_list
    fo_input.close()
    
    #Open an output file for writing
    fo_output=open(name_of_output_file, "wb")
    
    #Initializing variable for finding maximum counts and corresponding line
    max_count=0
    max_line=""
    #Operate on each line using for loop
    for line in line_list:
        ##Keeping only alphanumeric characters plus underscores(_)
        line=re.sub("[^a-zA-Z0-9_]"," ", line)
        line=line.strip()
        #converting strings into list of words
        word_list=re.split('\W+', line)
        #print word_list
        
        #Counting number of words in a line
        count = len(word_list)
        #If a line is empty (new line), then count is equivalent to zero
        if word_list[0]=="":
            count=0
        
        #Converting list into string for specfic output purposes
        word_string=' '.join(word_list)
        #Writing each line and corresponding word count, then new line after each output line
        fo_output.write(word_string+"-"+str(count)+"\n")
        
        #Finding the line with maximum number of word counts
        if count>max_count:
            max_count=count
            max_line=word_string        
        
    fo_output.close()
    
    print max_line, " : ", max_count
    
    return
   


#############Main##########
Freq_individual_words("test.txt", "output.txt")
#name_of_input_file=raw_input("Enter input file name: ")
#name_of_output_file=raw_input("Enter output file name: ")
#no_words_per_line(name_of_input_file,name_of_output_file)

#max1=get_max_from_list([1,23,45,12,4,78,9,13])
#print max1

