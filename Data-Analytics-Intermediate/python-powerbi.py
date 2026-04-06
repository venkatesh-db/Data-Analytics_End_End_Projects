

Darshan =
DATATABLE(
    "booking date time", STRING,
    "booking no", STRING,
    "booking status", STRING,
    "no of pililigrims", STRING,
    "total amount", STRING,
{
    {"feb 24","IDJ2436687666","success","2","600"},
    {"dec 24","IDJ3436687666","failed","2","600"},
    {"mar 24","IDJ9436687666","success","2","600"},
    {"apr 24","IDJ7743668766","success","2","600"},
    {"may 24","IDJ7743668766","success","2","600"}
}
)

FilteredBookings =
FILTER(
    Darshan,
    Darshan[booking no] = "IDJ7743668766"
)

'''
| Python      | Power BI              |
| ----------- | --------------------- |
| append()    | DATATABLE / Load data |
| list filter | FILTER()              |
| print()     | Visual (Table/Chart)  |


'''


INSERT (append)

SELECT (filter)

UPDATE

DELETE

COUNT

GROUP BY


Darshan =
UNION(
    ExistingTable,
    ROW(
        "booking date time", "june 24",
        "booking no", "IDJ9743668766",
        "booking status", "success",
        "no of pililigrims", "2",
        "total amount", "600"
    )
)

FilteredBookings =
FILTER(
    Darshan,
    Darshan[booking no] = "IDJ7743668766"
)

UpdatedStatus =
IF(
    Darshan[booking no] = "IDJ3436687666",
    "success",
    Darshan[booking status]
)

FilteredTable =
FILTER(
    Darshan,
    Darshan[booking no] <> "IDJ2436687666"
)

TotalRows = COUNTROWS(Darshan)

StatusSummary =
SUMMARIZE(
    Darshan,
    Darshan[booking status],
    "Count", COUNTROWS(Darshan)
)

'''

| Operation | Python             | Power BI          |
| --------- | ------------------ | ----------------- |
| Insert    | append()           | UNION / ROW       |
| Select    | list comprehension | FILTER()          |
| Update    | loop modify        | Calculated column |
| Delete    | list filter        | FILTER()          |
| Count     | len()              | COUNTROWS()       |
| Group By  | Counter            | SUMMARIZE()       |


'''


''' Interviewer Expectations 

Primary Key 
Foreign Key
Indexing. 
Transactions.
Join. ,
GROUP BY + AGGREGATION.
INNER JOIN. 
ORDER BY HAVING 
DISTINCT 
WINDOW FUNCTION
SUBQUERY  
INDEX  
TRANSACTIONS  
CTE. 
Recursive Queries. 
Window Functions. 
Partitioning 
Materialized Views 
Query Optimization. 
Stored Procedures 
Triggers 
OLTP vs OLAP 
Star Schema

'''


'''

                   python           sql       vs                 power bi

      
memory acessing    arr["c"].      select * from table where col = "c"  

SUMMARIZE(
    Darshan,
    Darshan[booking status],
    "TotalAmount", SUM(Darshan[total amount])
)

                  Loop acessing     few functions  values         majority functions 
                                    keyword based acessing
                                    

| Concept            | SQL | Power BI                 | Exists in Power BI?   |
| ------------------ | --- | ------------------------ | --------------------- |
| Primary Key        | Yes | Relationship uniqueness  | ⚠️ Partial            |
| Foreign Key        | Yes | Relationships            | ✅ Yes                 |
| Indexing           | Yes | VertiPaq compression     | ⚠️ Internal only      |
| Transactions       | Yes | No concept               | ❌ No                  |
| JOIN               | Yes | Relationships / DAX      | ✅ Yes                 |
| GROUP BY           | Yes | SUMMARIZE                | ✅ Yes                 |
| INNER JOIN         | Yes | Relationships            | ✅ Yes                 |
| ORDER BY           | Yes | Sorting                  | ✅ Yes                 |
| HAVING             | Yes | Filter after aggregation | ⚠️ Partial            |
| DISTINCT           | Yes | DISTINCT()               | ✅ Yes                 |
| WINDOW FUNCTION    | Yes | RANKX, etc.              | ⚠️ Partial            |
| SUBQUERY           | Yes | Nested DAX               | ⚠️ Partial            |
| INDEX              | Yes | Internal engine          | ❌ Not user-controlled |
| CTE                | Yes | Variables in DAX         | ⚠️ Partial            |
| Recursive Query    | Yes | No                       | ❌ No                  |
| Partitioning       | Yes | Incremental refresh      | ⚠️ Partial            |
| Materialized View  | Yes | Cached model             | ⚠️ Partial            |
| Query Optimization | Yes | Auto engine              | ⚠️ Internal           |
| Stored Procedure   | Yes | No                       | ❌ No                  |
| Trigger            | Yes | No                       | ❌ No                  |
| OLTP               | Yes | No                       | ❌ No                  |
| OLAP               | Yes | Yes (Power BI is OLAP)   | ✅ Yes                 |
| Star Schema        | Yes | Yes (recommended)        | ✅ Yes                 |


'''
#🔹 GROUP BY + AGGREGATION

Summary =
SUMMARIZE(
    Darshan,
    Darshan[booking status],
    "TotalAmount", SUM(Darshan[total amount])
)

UniqueStatus = DISTINCT(Darshan[booking status])


🔹 ORDER BY (Sorting)

Sorted =
TOPN(100, Darshan, Darshan[total amount], DESC)

🔹 INNER JOIN (via relationship)

Merged =
NATURALINNERJOIN(Darshan, Users)

🔹 FILTER (HAVING equivalent)

FilteredSummary =
FILTER(
    SUMMARIZE(Darshan, Darshan[booking status], "cnt", COUNTROWS(Darshan)),
    [cnt] > 1
)

WINDOW FUNCTION (RANKX)

RankColumn =
RANKX(
    ALL(Darshan),
    Darshan[total amount],
    ,
    DESC
)

🔹 SUBQUERY (Nested DAX)
AboveAvg =
FILTER(
    Darshan,
    Darshan[total amount] > AVERAGE(Darshan[total amount])
)

'CTE'

Result =
VAR AvgAmt = AVERAGE(Darshan[total amount])
RETURN
FILTER(Darshan, Darshan[total amount] > AvgAmt)


PARTITION

PartitionRank =
RANKX(
    FILTER(
        Darshan,
        Darshan[booking status] = EARLIER(Darshan[booking status])
    ),
    Darshan[total amount]
)

powerbi :
https://chatgpt.com/share/69ba4767-d8a8-8002-8a32-9422104dbcbb


🔷 1️⃣ Data Modeling
🔷 2️⃣ DAX Advanced Concepts
🔷 3️⃣ Time Intelligence
🔷 4️⃣ Power Query
🔷 5️⃣ Visualization Layer
🔷 6️⃣ Performance Optimization
🔷 7️⃣ Security (RLS)
🔷 8️⃣ Incremental Refresh
🔷 9️⃣ Deployment & Service
🔷 🔟 Real Business Use Cases
Sales dashboard
Banking analytics
Customer segmentation
Fraud detection dashboards