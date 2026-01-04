
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
# signed and unsigned : 

# what is the difference between char and varchar 

# constraint : specified rules in table column ensure data consistency integrity
primary key ,foreign key, unique,not null ,default, check 

# What is Primary Key and Foreign Key?
* primary key : it is the column in table which uniquely identifies each row, There can be only 1 PK and it should be not null
* Foreign Key : it is a cloumn in one table that is link to the primary key of another table and it ensure consistency and integrity of data.
FK can have dublicate and null value
it can be self-referencing.

# Where clause : filters rows based on one or more conditions so your query returns (or modifies) only the records that match.

# operator:
* Between : select for given Range inclusive ```sql select * from table_name WHERE marks BETWEEN 80 AND 100;```
* And: check both the conditions to be true
* OR: check either one of the condition to be true
* IN:
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