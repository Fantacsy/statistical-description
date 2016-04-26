
# coding: utf-8

# In[1]:


import csv
import collections
from collections import Counter

with open("/Users/FAN/Desktop/cars_price_miles.data.txt") as data:
    reader = csv.reader(data, delimiter="\t")
    data = list(reader)


# In[2]:

#question 1
print "The total records number is: " + str(len(data))


# In[3]:

#question 2
unique_make = {d[0] for d in data}
# I check the set "unique_make", find there's an element does not have name, so I delete it.
print "The unique make number is: " + str(len(unique_make) - 1)

from collections import Counter
make_counts = Counter()
for d in data:
    make_counts[d[0]] += 1
print "The top five most common makes is:"
print make_counts.most_common(5) # gives you a list of top five [(player_id, num_injuries), ...]


# In[4]:

#question 3
invalid_data = [d for d in data if d[2] == "Missing"]
print "The number of item which price is Missing is: " + str(len(invalid_data))


# In[5]:

# question 4
data2 = [d for d in data if d[0] == "LAMBORGHINI"]
number_lambo = len(data2)
print "The total of lambo makes model is: " + str(number_lambo)


unique_lambo = {d[1] for d in data2}
number_unique = len(unique_lambo)

make_counts_lambo = Counter()
for d in data2:
    make_counts_lambo[d[1]] += 1

lambo_model = list(collections.Counter(make_counts_lambo.items()))

for i in range(0, number_unique):
    print "The number of model named " + str(lambo_model[i][0]) + " is: " + str(lambo_model[i][1]/float(number_lambo))


# In[6]:

#question5 Miles
# I check the database data2, find there exists some item which the miles elements is "-"
# I delete these invalid data.

miles_valid = [d[3] for d in data2 if d[3] != '-']
print "The number of item in Lambo which miles is - is: " + str(len(data2) - len(miles_valid))
print "The number of item in Lambo which miles is valid is: " + str(len(miles_valid))

sum_miles = 0
for element in miles_valid:
    sum_miles = sum_miles + int(element)

print "The avg miles of each Lamborghini model is: " + str(sum_miles/len(miles_valid))


# In[7]:

#question5 Price
# I check the database data2, find there exists some item which the Price elements is "Missing"
# I delete these invalid data.
price_valid = [d for d in data2 if d[2] != 'Missing']
print "The number of item in Lambo which price is missing is: " + str(len(data2) - len(price_valid))
print "The number of item in Lambo which price is valid is: " + str(len(price_valid))


sum_price = 0
for element in price_valid:
    sum_price = sum_price + int(element[2])
    
print "The avg price of each Lamborghini model is: " + str(sum_price/len(price_valid))


# In[8]:

#question6 distribution of cars by price
price_valid2 = [d for d in data if d[2] != "Missing"]
num_interval = (50000 - 0)/2000 + 1

price_bin = []
for i in xrange(0,num_interval):
    price_bin.append(0)
    

for d in price_valid2:
    i = int(d[2])/2000
    if i < num_interval:
        price_bin[i] = price_bin[i] + 1
    else:
        price_bin[num_interval - 1 ] = price_bin[num_interval - 1 ] + 1

percent_bin = []
for i in range(0, num_interval):
    percent_bin.append(price_bin[i]/float(len(price_valid2)))

print "The price distribution percentage can be written as a set as below"    
print percent_bin


# In[9]:

#question7 smooth the chart in question6

smooth_bin = []
smooth_bin.append((3*percent_bin[0] + percent_bin[1])/4.0)

for i in range(1, num_interval - 1):
        smooth_bin.append((percent_bin[i-1] + 2*percent_bin[i] + percent_bin[i+1])/4.0)

smooth_bin.append((3*percent_bin[num_interval - 1] + percent_bin[num_interval-2])/4.0)

print "The smooth distribution percentage can be written as a set as below"    
print smooth_bin

