def bracket_pattern(input_str): 
    if(input_str[0]==')' or input_str[-1]=='('):
        return False 
    else:
        count=0 
        count1=0
        for i in input_str:
            if(i==')'):
                count=count+1 
            elif(i=='('):
                count1=count1+1 
        if(count==count1):
            return True 
        else: 
            return False
            
    #Remove pass and write your code her
    
input_str="(())("
print(bracket_pattern(input_str))