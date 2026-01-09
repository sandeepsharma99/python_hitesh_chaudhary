
# Database : 
Database is a collection of data in a format that csn be easily accessed(Digital)
A software that is used to manage our database is called DBMS (Database Management System) for ex: MYSql workbench
# Type of Database :
* Relation database (RDBMS) : data stored in table for example : MySql, oracle, sqlserver PostgreSql 
* No relational database NoSql : data not stored in table
# SQL/SEQUEL
Structure Query Language is a programming language used to interact with relational databases.
it is used to perform crud operations: Create , Read , Update , Delete.
- Not case Sensitive
- created by IBM
``` sql
    tinyint unsigned (0 to 256)
```

# Type of sql command
* DDL (data defination language) : create , alter(modifies the structure), drop(Permanently deletes), truncate( Removes all records from a table), rename
* DQL (data query language) : Select
* DML (data manipulation language) : insert update delete
* DCL (data control language) : Grant and revoke
* TCL (Transaction control language ) :commit(save), rollback(undoes all the change made in the current transaction sice the last commit) savepoint(Sets a point within a transaction to which you can later roll back, without rolling back the entire transaction.)

# what is schema ?
# datatypes(what type of value is stored in column) : int, varchar(), primary key, Tinyint (-127 to 127),float, date 
# signed and unsigned : signed numbar can be positive and negative while unsigned can only be positive. allow large range of same no.of bit  

# what is the difference between char and varchar 
Ans : CHAR is a datatype it always use the specified number of byte regarless of the length of the store string where VARCHAR occupies the space require for actual data

# Constraint
Ans : specified rules in table column. ensurig data consistency integrity
primary key ,foreign key, unique,not null ,default, check 

# What is Primary Key and Foreign Key?
* primary key : it is the column in table which uniquely identifies each row, There can be only 1 PK and it should be not null
* Foreign Key : it is a cloumn in one table that is link to the primary key of another table and it ensure consistency and integrity of data.
FK can have dublicate and null value
it can be self-referencing.

# Q: what is the difference between where and Having clause ?
* Where clause : filters rows based on one or more conditions so your query returns (or modifies) only the records that matchs the condition.
* HAVING Clause : similar to where clause applies some condition on row .it is  Used when we want to apply condition after grouping. ``` select city column_name table_name group by city having avg(marks)>80; ```

# Limit clause : used to control the number of records returned by a query
# ORDER BY Clause : to sort in ascending and descending order
# GROUP BY Clause : groups the row that have same value ``` select city, count(name) from table_name group by city; ``` It is ofently used with aggregate functions (like COUNT(), SUM(), AVG(), MAX(), and MIN()) 

# Q: What is the difference between drop truncate and delete ?
Ans: 
* Delete : remove specific rows from a table based on a given condition syntax :```DELETE FROM table_name WHERE condition```
* Drop : used to remove  completely table permanentely, its structure, and all its data from the database. suntax :``` DROP table <table_name>;```
* Truncate :  used to remove all rows from a table efficiently, without deleting the table’s structure or schema. ``` TRUNCATE table <table_name>;```


# operator:
* Between : select for given Range inclusive ``` select * from table_name WHERE marks BETWEEN 80 AND 100;```
* And: check both the conditions to be true
* OR: check either one of the condition to be true
* IN: matches any value in the list ``` select * from table_name WHERE CITY IN ("DELHI","MUMBAI","BANGALORE","PUNE","NOIDA")```
* NOT IN:

# create command syntax
```sql
create database db_name;
use database
create table table_name(
    col_name dataype constraint,
    .
    .
    .
);
```
# what is Aggregate Function ?
Ans : Aggregate function perform a calculation on set of value , and return a single value.
- count() , max(), min(), avg(), sum()

# update query :update and set
``` update TB_name set grade = "A+" where grade = "A" ```
# Set sql_safe_updates = 0; -> enables updation on exiting table

# Delete query : to delete existing row
``` delete from table_name Where condition;```

# ON update cascade, ON delete cascade 
Ans : automatically update to match the new value from parent(primary key) table to child(foreign key) table  ensuring data integrity, consistency ensuring related data stays consistent by keeping related records synchronized   
# Alter : to change the  schema of table

* Add Column ``` ALTER Table table_name add column_name datatype contraint;```
* Remove Column``` ALTER Table table_name drop column_name;```
* Modify Column``` ALTER Table table_name modify column_name datatype constraint;```
* Change Column ``` ALTER Table table_name change old_column_name new_column_name datatype constraint;```
``` ALTER Table table_name rename to new_Table_name;```

# Sql Joins : 
#### Ans: join is used to combine row from two or more tables, based on related column between them ad pick only common or matching data/row.

#### INNER JOIN 
INNER JOIN : combines rows from two or more tables, returning only the rows where the specified condition (usually matching values in a common column) is true in both tables, effectively showing the intersection of the data
```sql 
SELECT Products.ProductName, Categories.CategoryName
FROM Products
INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;
```
#### OUTER JOIN :
### left join : return all record from the left table, and the match record from the right table.
```sql
SELECT columns
FROM left_table
LEFT JOIN right_table
ON left_table.common_column = right_table.common_column;
```

### right join : return all record from the right table, and match record from the left table
```sql
    SELECT *
FROM LeftTable
RIGHT JOIN RightTable
ON LeftTable.CommonColumn = RightTable.CommonColumn;
```
### full join : return all record from both left and right table ,It is basically the combination of LEFT JOIN and RIGHT JOIN
```sql
    SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```
### left exclusive : retrieves all records from the left table that have no matching records in the right table
```sql
SELECT C.CustomerName, O.OrderID
FROM Customers C
LEFT JOIN Orders O ON C.CustomerID = O.CustomerID
WHERE O.CustomerID IS NULL;
```

### Right exclusive : a relational database concept used to retrieve only the records present in the right table that do not have a match in the left table
```sql
SELECT B.* -- Select all columns from the right table
FROM TableA A
RIGHT JOIN TableB B ON A.matching_column = B.matching_column
WHERE A.matching_column IS NULL; -- Filter where there was no match in the left table
```
# full exclusive join :

# Union :
# union all : 

# Q: what is sub query ?
Ans : sub query or inner query or a nested query is a query within another query 
A subquery must always be enclosed within parentheses ()
```sql
-- Subquery to find employees with salary greater than the average salary
SELECT name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
# Q: My Sql view : view is the virtual table based on the result statement. view always show up-to-date data. the database engine every recreates the view, every time user query it. Enhance Security

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


```sql

```