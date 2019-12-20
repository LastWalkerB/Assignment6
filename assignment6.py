#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Car:
    def __init__(self, company,name, model, color, weight, rating):
        self.company = company
        self.name = name
        self.model = model
        self.color = color
        self.weight = weight
        self.rating = rating
    
    def tellColor(self):
        print("The color of your car is " + self.color)
        
    def tellWeight(self):
        print("Weight of your car is " + self.weight)
        
    def tellNameAndModel(self):
        print("Name: " + self.name + " Model: " + self.model)
        

O1 = Car("Suzuki", "Alto", "2009", "Red", "200", "5")
O2 = Car("Corolla", "GLI", "2015", "Blue", "500", "4")
O3 = Car("Honda", "City", "2015", "White", "500", "3.5")
O4 = Car("Suzuki", "Swift", "2015", "Black", "400", "3.5")
O5 = Car("Toyota", "Aqua", "2016", "Black", "300", "5")
O1.tellNameAndModel()
O2.tellNameAndModel()
O3.tellNameAndModel()
O4.tellNameAndModel()
O5.tellNameAndModel()
        


# In[ ]:




