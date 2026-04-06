
data ={
    
    "student":["ram","shyam","hari"],
    "marks":[90,80,70],
}

import pandas  
newdf=pandas.DataFrame(data)

print(newdf)

# data frame using methods to perform  statistical analysis 

print(newdf["marks"].mean())
print(newdf["marks"].median())
print(newdf["marks"].max())
print(newdf["marks"].min())
print(newdf["marks"].std())
print(newdf["marks"].var())
