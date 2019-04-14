**Setup:** <br>
Clone repository: <br>
```https://github.com/Amanda-Wakefield/Group_Project.git```

Install requirements files (on local or in virtual env): <br>
```pip install -r requirements/development.txt ```

Apply migrations to start database: <br>
```python manage.py migrate```

Any time you modify the database (ie. add table or column) you need to make migrations: <br>
```python manage.py makemigrations```
```python manage.py migrate```

Run server: <br>
```python manage.py runserver```

Create super user: <br>
```python manage.py createsuperuser```

Database Project Requirements
1. Design the database, i.e. produce an annotated E-R diagram of data entities and the relations between the entities. <br />
2. Implement the schema using SQL, Python (or another programming language), and the MySQL database management systems. <br /> Implementations on the class computer/server bioed.bu.edu using Python will be supported in terms of making
software available and helping you with problems. For other programming language/server combinations, you are on your own. <br />
3. Draw up a set of common questions that will be asked by a user of your database and design a set of efficient queries (in SQL) that answer those questions. <br />
4. Create a Web interface for your database using HTML, javascript, and CGI. <br />
Make this easy to use and intuitive. <br />
5. Create informative ways to view the results of a database query. At least one of your views should use a graphics display based on a file produced and saved by your CGI program. <br />
6. Create a data download function for your database that stores output for the user to download. <br />
7. Create a series of help pages for your database. <br />
8. Implement AJAX javascript in your CGI. <br />
9. Present your database to the class at the end of the semester and demonstrate the database to me in my office during exam week. <br />

Database Project Evaluation <br />
Each group will receive a group grade on the DB project. My evaluation will be based on four elements: <br />
1. A class presentation (powerpoint) to be given on April 30 or May 2, 2019. It should last 20-25 minutes and each student in your group must give part of the presentation. This will not be a “live” presentation. You should instead prepare
screenshots to show your database features. <br />
2. A demonstration in my office on May 7 or 8, 2019. Exact times will be determined later. <br />
3. A letter of evaluation (attached) from the supervising faculty member or other person. This letter must be in my hands when you do you demonstration, either May 7 or 8, 2019. <br />
4. A group summary, in narrative form, describing what you wanted to accomplish (list of tasks), what you actually did accomplish, and the limitations and difficulties you encountered. No more than one page. Please include a percentage effort by each group member on the major design and programming tasks. All group members must sign the summary. <br />

In my evaluation, I will be looking for implementation of the following: <br />
1. A pleasing uniform appearance for the HTML interface. <br />
2. An introduction page with the names of the project, student developers, faculty advisor, and a statement that the project was developed at Boston University as part of BF768, Spring 2019, G. Benson instructor. This page should also include
a brief abstract of the purpose of the database. <br />
3. A general help page with links from your HTML forms explaining what the page does, the format of input, and other necessary information to correctly use the database. <br />
4. Linked sample data or javascript filling of forms (where necessary) for trying out database features anywhere data input is required. <br />
5. A menu driven selection of data from your database. <br />
6. Links for additional information, on data output pages, to at least one external database. <br />
7. Data download into a file, supporting one or more formats. <br />
8. A graphical plot for data presentation. <br />
9. Javascript usage. <br />
10. AJAX usage. <br />
Additionally, I will check that you have implemented the tasks and queries outlined in your project proposal.
