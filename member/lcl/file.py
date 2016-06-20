# coding: utf-8 
3 
 
4 # In[26]: 
5 
 
6 # check missing value function 
7 def missingcheck(obj): 
8     flag="No missing!" 
9     for bool in obj: 
10         if bool==True: 
11           flag="missing entry detected!"   
12     print(flag)   
13 
 
14 
 
15 # In[2]: 
16 
 
17 # step 2: modify dataframe 
18 se=pd.Series(ds["uid"]) 
19 ds.index=se 
20 ds=ds.drop("uid",axis=1) 
21 print(ds) 
22 
 
23 
 
24 # In[2]: 
25 
 
26 ##step 1 : import original data 
27 import pandas as pd 
28 import json as js 
29 
 
30 path = r"C:\Users\Changlin Li\Desktop\user.json\user.json" 
31 record=[js.loads(line) for line in open(path)] 
32 ds=pd.DataFrame(record) 
33 print(ds) 
34 
 
35 
 
36 # In[35]: 
37 
 
38 # step 3: check null values 
39 counter=pd.isnull(ds) 
40 missingcheck(counter["app"])  
41 missingcheck(counter["appfile"]) 
42 missingcheck(counter["activity_time"]) 
43 missingcheck(counter["label"]) 
44 missingcheck(counter["category_id"]) 
45     
46 
 
47 
 
48 # In[20]: 
49 
 
50 # step 4 check duplicate UID 
51 ds1=pd.DataFrame(ds.index) 
52 booleans=ds1.duplicated() 
53 flag="No duplicated!" 
54 for bool in booleans: 
55     if bool==True: 
56       flag="duplicate entry detected!"   
57 print(flag) 
58 
 
59 
 
60 # In[3]: 
61 
 
62 # step 5 sort dataframe accroding to uid 
63 ds=ds.sort_index(axis=0) 
64 print(ds) 
65 
 
66 
 
67 # In[17]: 
68 
 
69 # step 6 sort dataframe accroding to activity_time 
70 ds=ds.sort_values(by="activity_time") 
71 print(ds) 
72 
 
73 
 
74 # In[16]: 
75 
 
76 # step 7, sub-step 1： get total entries, training sets , 
77 ds_sample=ds[:300].label 
78 print(len(ds_sample)) 
79 print(ds.app.describe()) 
80 
 
81 
 
82 # In[ ]: 
83 
 
84 # compute the weight of non-empty category_id user (unfinished!) 
85 import pandas as pd 
86 def compWeight(ds): 
87     counter=0 
88     list=[] 
89     se=pd.DataFrame(ds["category_id"]) 
90     se1=pd.DataFrame(ds["label"]) 
91     print(se) 
92 #     print(ds["category_id"][10] == []) 
93 #     list=[x for x in ds["category_id"] if x==[]] 
94 
 
95     for value in se: 
96         if not any(value) : 
97             counter+=1 
98             list.append(counter) 
99     print(list) 
100 compWeight(ds) 
101 
 
102 
 
103 
 
