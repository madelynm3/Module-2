# Overview

A SQL relational database designed for student to store user course data. Users can track their completed courses and their planned courses, as well as total credits completed and planned. Course data includes academic year, semester, course code, grade, and credits. 

How to use: A menu is displayed that allows the user to add courses into their completed or planned tables, and store course data such as: grades, credit, academic year, and semester. User can update completed and planned tables with any changes, and can also view total credits and courses taken, and when. 

Purpose: Manage courseload and make academic planning simple.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

MySQL

There are 2 tables, "planned" and "completed." "Planned" stores user's future courses and "completed" stores user's past courses. There are 5 columns in each: year, semester, course code, grade, and credits. 

# Development Environment

[Git] (https://git-scm.com)

[Github] (https://github.com/madelynm3)

[Visual Studio Code] (https://code.visualstudiocode.com)

[SQLite] (https://pypi.org/project/pysqlite3/#files)

Python 3.9.2

# Useful Websites

* [Geeks for Geeks - SUM values in SQL](https://www.geeksforgeeks.org/how-to-compute-the-sum-of-all-rows-of-a-column-of-a-mysql-table-using-python/)
* [Geeks for Geeks - COUNT function](https://www.geeksforgeeks.org/count-sql-table-column-using-python/)

# Future Work

* GPA calculator for completed courses
* User friendly interface
* Mark a course as complete in the "planned" table and have it automatically added to the "completed" table and deleted from "planned."
* Add logic for repeated/retake courses