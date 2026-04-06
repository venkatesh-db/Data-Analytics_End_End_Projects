


# detailed explanation of sql and how to use it in python with example
#https://chatgpt.com/share/69b8ef42-1d7c-8002-80b8-c610f7256ac0


# sql - data structure 

# create data structure for darshan booking
# initalising data structure for darshan booking
# sql - create table 


specialentrydarshan = [ 
   {"booking date time ":"feb 24","booking no":"IDJ2436687666","booking status":"sucess" , "no of pililigrims":"2","total amount":"600"},
   {"booking date time ":"dec 24","booking no":"IDJ3436687666","booking status":"failed" , "no of pililigrims":"2","total amount":"600"},
   {"booking date time ":"mar 24","booking no":"IDJ9436687666","booking status":"sucess" , "no of pililigrims":"2","total amount":"600"},
   {"booking date time ":"apr 24","booking no":"IDJ7743668766","booking status":"sucess" , "no of pililigrims":"2","total amount":"600"},
]

# append data to data structure for darshan booking
specialentrydarshan.append({"booking date time ":"june 24","booking no":"IDJ9743668766","booking status":"sucess" , "no of pililigrims":"2","total amount":"600"})

print(specialentrydarshan)

# search data in data structure for darshan booking
findresult = [x for x in specialentrydarshan if x["booking no"] == "IDJ7743668766"]
print("found data",findresult)


# update 
for booking in specialentrydarshan:
    if booking["booking no"] == "IDJ3436687666":
        booking["booking status"] = "sucess"
   
   
#SELECT ALL     
print(specialentrydarshan)

#COUNT
print(len(specialentrydarshan))


#7️⃣ GROUP BY Example

from collections import Counter

status_count = Counter(x["booking status"] for x in specialentrydarshan)
print(status_count)


'''

| SQL    | Python               |
| ------ | -------------------- |
| Table  | List of dictionaries |
| Row    | Dictionary           |
| Column | Dictionary key       |
| SELECT | List comprehension   |
| INSERT | `append()`           |
| UPDATE | Modify dict          |
| DELETE | List filtering       |


'''


# JOIN

users = [
 {"id":1, "name":"Ram"},
 {"id":2, "name":"Krishna"},
 {"id":3, "name":"Shiva"}
]

darshan = [
 {"booking_no":"IDJ101","user_id":1,"amount":600},
 {"booking_no":"IDJ102","user_id":2,"amount":600},
 {"booking_no":"IDJ103","user_id":1,"amount":600},
 {"booking_no":"IDJ104","user_id":3,"amount":600}
]


for d in darshan:
    for u in users:
        if d["user_id"] == u["id"]:
            print("inner join ", d, u)
            
    
'''

| Operation | Python             | MySQL        |
| --------- | ------------------ | ------------ |
| Create    | list               | CREATE TABLE |
| Insert    | append()           | INSERT       |
| Select    | list comprehension | SELECT       |
| Update    | loop               | UPDATE       |
| Delete    | filter             | DELETE       |
| Count     | len()              | COUNT        |
| Group     | Counter            | GROUP BY     |
| Sort      | sorted()           | ORDER BY     |
| Join      | nested loops       | JOIN         |


'''
