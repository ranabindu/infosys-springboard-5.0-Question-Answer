#Freight Pvt. Ltd, a cargo company, forwards cargos/freights between its customers.
# Freight charges are applied based on weight and distance of the shipment.
# Write a python program to implement the class diagram given below.



# Method description:

# Initialize counter variable to 198 in Freight class
# All validate methods should return true, if validation succeeds. Else it should return false
# validate_customer_id(): Customer id should be 6 digits and should begin with digit 1
# validate_weight(): Weight should be a multiple of 5
# validate_distance(): Distance should be between 500kms and 5000kms (both inclusive)
# forward_cargo():
# Validate from_customer.customer_id, recipient_customer.customer_id, distance and weight of the freight
# If valid,
# auto-generate freight_id starting from 200 and initialize it. freight_id should be even
# calculate freight_charge based on weight (Rs.150/kg) and distance (Rs.60/km)
# Else, set freight_charge to 0

# For testing:

# Create objects of Customer and Freight class
# Invoke forward_cargo() method on Freight object
# Display freight id and freight charge
# In case of error/invalid data, display appropriate error message




class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address
        
    def validate_customer_id(self):
        # customer_id=str(self.__customer_id)
        if len(str(self.__customer_id))==6 and (str(self.__customer_id))[0]=='1':
            return True
        return False
        
    def get_customer_id(self):
        return self.__customer_id
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_address(self):
        return self.__address
        
class Freight:
    counter=198
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__freight_id=None
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_charge=None
        
    def get_freight_id(self):
        return self.__freight_id 
    
    def get_recipient_customer(self):
        return self.__recipient_customer
        
    def get_from_customer(self):
        return self.__from_customer
        
    def get_weight(self):
        return self.__weight
        
    def get_distance(self):
        return self.__distance
        
    def get_freight_charge(self):
        return self.__freight_charge
        
    def validate_weight(self):
        if self.__weight%5==0:
            return True
        return False
        
    def validate_distance(self):
        if self.__distance>=500 and self.__distance<=5000:
            return True
        return False
        
    def forward_cargo(self):
        if self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_weight() and self.validate_distance():
            Freight.counter+=2
            self.__freight_id=Freight.counter
            self.__freight_charge=(self.__weight*150)+(self.__distance*60)
        else:
            self.__freight_charge=0