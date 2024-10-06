# Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.

# Note: Perform case insensitive string comparison wherever necessary.

# Sample Input

# Expected Output

# Jet on the Mat but mat is too long

# False

# mat jet Jet Mat

# True




def check_occurence(string):  
    count=0 
    count1=0
    s=string.split()
    for i in s:
          if (i=='jet' or i=='Jet'):
               count=count+1
          elif (i=='mat' or i=='Mat'):
               count1=count1+1
    print(count,count1)
    if(count==count1): 
        return True 
    else: 
        return False
            
    #start writing your code here
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))