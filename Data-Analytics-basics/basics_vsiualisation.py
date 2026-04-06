
data ={
    
    "student":["ram","shyam","hari"],
    "marks":[90,80,70],
}



import pandas  
newdf=pandas.DataFrame(data)
print(newdf)

import matplotlib.pyplot as plt

# using function bar passing data frame column's 

plt.bar(newdf["student"],newdf["marks"])
plt.xlabel("students")
plt.ylabel("marks")
plt.title("marks of students")
plt.show()
