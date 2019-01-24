#!/usr/bin/python

#Author: Md Shamimuzzaman
#Date: Jan 2, 2018
#Handling List in python

def myInsert(list, index, value):
    list.insert(index, value);
    return list;


def myPrint(list):
    print list;


def myRemove(list, value):
    list.remove(value);
    return list;


def myAppend(list, value):
    list.append(value);
    return list;


def mySort(list):
    list.sort();
    return list;

#Remove last element
def myPop(list):
    list.pop();
    return list;

def myReverse(list):
    list.reverse();
    return list;

#Insering multiple emements into a list
def myAdvanceInsert(list, index1, index2, value1, value2):
    list.insert(index1, value1);
    list.insert(index2,value2);
    return list;
    
#Printing absolute value of elements
def myAdvancePrint(list):
    #print map(abs, list)
    for x in list:
        print "abs value of " , x, " is ", abs(x);
    
#Input valiadity checking        
'''def myAdvanceInsert2(list, indexList, valueList):
    if len(indexList)!=len(valueList):
        print "Different lengths of index and values!!!"
        return list
        
    for i in range(len(indexList)):
        if indexList[i]>=len(list):
            print "Out of range index!!!"
            return list;
        list.insert(indexList[i],valueList[i]);
    return list;'''

#Inserting new elements based on the provided indexlist and valuelist
def myAdvanceInsert2(list, indexList, valueList):
    #Handling list elemnts according to list position(i)
    for i in range(len(indexList)):
        list.insert(indexList[i],valueList[i]);
    return list;
     

############################ Main Function Begins Here ######################
list=[];
list=myInsert(list, 0, 5)
list=myInsert(list,1, 10)
list=myInsert(list, 0, 6)
myPrint(list) 
list=myRemove(list,6)
myPrint(list)

list=myAppend(list,9)
list=myAppend(list, 1)
myPrint(list);
list=mySort(list) 
myPrint(list)
list=myPop(list)
myPrint(list)
list=myReverse(list)
myPrint(list)


list=myAdvanceInsert(list, 2, 1, -20, -3)
myPrint(list)
myAdvancePrint(list)
myPrint(list)

list=myAdvanceInsert2(list, [2, 4, 1, 0, 1, 1], [23, -23, 30, 4, 1000, -33])
myPrint(list)











