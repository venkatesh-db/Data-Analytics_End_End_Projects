
data ={
    
    "student":["ram","shyam","hari"],
    "marks":[90,80,70],
}

# dict is transformed to dataframe data structure
# dict data is tranformed to dataframe using pandas library

import pandas  
newdf=pandas.DataFrame(data)
print(newdf)