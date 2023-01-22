#!/usr/bin/env python
# coding: utf-8

# In[8]:


#sorting the list of ages
import statistics 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorts age list in ascending order by default
ages.sort()
print ("Sorted age:", ages) 
# Displays min value as we used min() method
print ("Min age of the given list:", min(ages)) 
# Displays max value as we used max() method
print ("Max age of the given list:", max(ages)) 
# Adding again min and max values 
ages.append(min(ages)) 
ages.append(max(ages))
print ("Adding the min and max values again:",ages) #Displays the list again with new values
# Median
mdn_age = statistics.median(ages)
print ("Median age of the list:", mdn_age)
# Average age
average= sum(ages)/len(ages)
print ("Avg of the given list = ", average)
# Range
rng=max(ages)-min(ages)
print ("Range of the list = ", rng)


# In[13]:


# Dog dictionary is created with given key and values
dog = {'name':'Lucky','color':'Brown','breed':'German Shepard','legs':'4','age':'5'}
print ("Dog Dictionary Created:",dog)
# Student dictionary is created with given key and values
student ={'first_name':'Manoj','last_name':'Sarakanam','Gender':'male','age':'23','marital_status':'single',
'skills':'dancer','Country':'India','City':'Hyderabad','Address':'5/2/19'}
print ("Student Dictionary Created:",student)
# Create another dictionary for skills
skills = {'dancer':'1','technical knowledge':'2','coder':'3'}
print ("Skills Dictionary Created:",skills)
# Find the length of student dictionary
print ("Length of student dictonery:", len(student))
# Check the datatype of skills
print ("Datatype of skills:",type(skills))
# Get values of skills dictionary
print ("Values of skills:",skills.values())
# Add one item to skills
skills['creativity'] = 4
print ("New skill added:",skills)
# Get dog and student key and values
print ("Dog keys:",dog.keys())
print ("Student values:",student.values())


# In[22]:


my_sisters = ('Mounika','Bhavana','Padma','Usha Kiran') 
my_brothers = ('Sai Sunil','Avinash','Vamshi','Harshith')
# Create another tuple as siblings and join the sister’s and brother’s tuple
siblings = my_sisters + my_brothers
# Displays siblings’ output and length of siblings
print("Siblings:", siblings)
print("Length of Siblings:", len(siblings))
# Create another tuple as family_members and add father and mother name to it
family_members = siblings + ('Satyanarayana','Kumari')
# Displays family_members output
print("Family_members:",family_members)


# In[25]:


#Length of the set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Length of it_companies:", len(it_companies))
#Add twitter
it_companies.add('Twitter')
print("After adding another it_company:",it_companies)
#Add multiple it_companies
it_companies.update({'Infosys','Capgemini','Wipro','TCS'})
print("After adding multiple items:",it_companies)
#Remove
it_companies.remove('TCS')
print("After removing one company:",it_companies)
#Discard
it_companies.discard('TCS')
print("After discarding company:",it_companies)
#Discard doesn't raise any error if any item is not present in the set
#Join A & B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27} 
print("Join A and B:", A.union(B))
#Intersection
print("Intersection of A and B:", A.intersection(B))
#Subset
print("Subset of A and B:", A.issubset(B))
#Disjoint
print("Disjoint:", A.isdisjoint(B))
#Convert list to set
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Converting list to set:", set(age))
#Length of set
print("Length of set:",len(set(age))) 
#Length of list
print("Length of list:",len(age))
#Symmetric diff- returns values which are not in common with other set
print("Symmetric diff:",A.symmetric_difference(B))
#delete set 
A.clear()
print(A) 
B.clear()
print(B)


# In[28]:


# Initialise r where r value can be read from user inpt
r = int(input("enter raduis:"))
# Calculate area of circle and circumference of circle
area_of_circle = 3.14*r*r 
circum_of_circle = 2*3.14*r
# Display area of circle and circumference of circle
print("Area of Circle:",area_of_circle)
print("Circumference of Circle:",circum_of_circle)


# In[48]:


# Unique
str= "I am a teacher and I love to inspire and teach people"
print(str)
# Use split method to separate the words and set to get the unique values
set_str=set(y)
print(set_str)
print ("number of unique words in given sentence is: %s"% len(set_str))


# In[55]:


a= "Name\t Age\t Country\t City\t \nAsabeneh 250\t Finland\t Helsinki"
print(a)


# In[41]:


#Using String format method
print(f'radius = 10')
print(f'area = 3.14*radius**2')
print(f'"The area of circle with radius {r} is {3.14*r*r} meters square"')


# In[42]:


#Creating a list(L1) for weights(lbs) of N students
L1=[int(num) for num in input().split(" ")]
#Creating another list called W_kg
W_kg=[] 
#Using for loop to iterate the values and appending the list
for i in L1:
 W_kg.append(round(i/2.205,2))
#Displaying the values in kgs after conversion
print ("Values are:",W_kg)


# In[ ]:




