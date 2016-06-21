# coding: utf-8

# In[26]:

# check missing value function, needed in step 3
def missingcheck(obj):
    flag="No missing!"
    for bool in obj:
        if bool==True:
          flag="missing entry detected!"  
    print(flag)  


# In[2]:

# step 2: modify dataframe
se=pd.Series(ds["uid"])
ds.index=se
ds=ds.drop("uid",axis=1)
print(ds)


# In[1]:

##step 1 : import original data
import pandas as pd
import json as js

path = r"C:\Users\Changlin Li\Desktop\user.json\user.json"
record=[js.loads(line) for line in open(path)]
ds=pd.DataFrame(record)
print(ds)


# In[34]:

# step 3: check null values, use fun in the beginning
counter=pd.isnull(ds)
missingcheck(counter["app"]) 
missingcheck(counter["appfile"])
missingcheck(counter["activity_time"])
missingcheck(counter["label"])
missingcheck(counter["category_id"])
   


# In[35]:

# step 4 check duplicate UID
ds1=pd.DataFrame(ds.index)
booleans=ds1.duplicated()
flag="No duplicated!"
for bool in booleans:
    if bool==True:
      flag="duplicate entry detected!"  
print(flag)


# In[3]:

# step 5 sort dataframe accroding to uid
ds=ds.sort_index(axis=0)
print(ds)


# In[17]:

# step 6 sort dataframe accroding to activity_time
ds=ds.sort_values(by="activity_time")
print(ds)


# In[6]:

# step 7, sub-step 1： get total entries, training sets , small sample test(300 units)
ds_sample=ds[:300]
ds_sample=ds_sample[ds_sample["label"]>0]
ds_sample=ds_sample.dropna() 
length=len(ds_sample)
# clear na value
ds_sample.sort_values(by="category_id")
count1=0
print(ds_sample["category_id"])
for ele in ds_sample["category_id"]:
    if ele==[]:
        count1+=1
print(count1)
appPerc=count1/length
print(appPerc)


# In[4]:

# sub-step2: compute the weight of non-empty category_id user in all VIP-purchase group
ds=ds[ds["label"]>0]
ds=ds.dropna()  
# clear na value
length=len(ds) 
ds=ds.sort_values(by="category_id")
count1=0
for ele in ds["category_id"]:
    if ele==[]:
        count1+=1
appPerc=count1/length
print(appPerc)
# conclusion: there is no possibility to remove empty category_id users.



 
