# Royal Orchid is a florist. They want to be alerted when stock of a flower goes below a particular level. 
# The flowers are identified using name, price per kg and stock available (in kgs).
# Write a Python program to implement the above requirement.

# Details of Flower class are given below:

# Class name: Flower

# Attributes
# (private)

# flower_name
# price_per_kg
# stock_available

 

# Methods
# (public)

# __init__()

# Create and initialize all instance variables to None

# validate_flower()

# Return true, if flower name is valid. Else, return false
# (Refer table for valid flower names)

# validate_stock(required_quantity)

# Accept the quantity required. Return true, if stock is available.
# Else return false.

# sell_flower(required_quantity)

# Accept the quantity required.
# Validate flower name and stock.
# If both are valid, update stock available based on the quantity required

# check_level()

# Check if available stock is below the order level
# If so, return true. Else, return false
# (Refer table for order level of each flower)

# setter methods

# Include setter methods for all instance variables to set its values

# getter methods

# Include getter methods for all instance variables to get its values

 

 

# Flower Name

# Level(in Kgs)

# Orchid

# 15

# Rose

# 25

# Jasmine

# 40

# Note: Perform case insensitive string comparison
# Represent few flowers, initialize instance variables using setter methods, invoke appropriate methods and test your program.

 

class Flower:
    # flowers=
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
        
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name.lower()
        
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
        
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
        
    def get_flower_name(self):
        return self.__flower_name
        
    def get_price_per_kg(self):
        return self.__price_per_kg
        
    def get_stock_available(self):
        return self.__stock_available
        
    def validate_flower(self):
        if self.__flower_name in ["orchid","rose","jasmine"]:
            return True
        return False
        
    def validate_stock(self,required_quantity):
        if required_quantity<=self.__stock_available:
            return True
        return False
        
    def sell_flower(self,required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available-=required_quantity
    
    def check_level(self):
        if (self.__flower_name=="orchid" and self.__stock_available<15) or (self.__flower_name=="rose" and self.__stock_available<25) or (self.__flower_name=="jasmine" and self.__stock_available<40):
            return True
        return False
        