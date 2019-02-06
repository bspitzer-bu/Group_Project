BF768 Biological Databases
Spring 2019
Database Project Proposal
See second page for the requirements of your project. See third page for evaluation.
Proposal Draft due date Feb 28, 2019.
Final Proposal due date March 31, 2019.
Include the following in the proposal draft. Your information may change before the final Proposal is due.
1. Name of project
	GPCR Allosteric Sites 

2. Names of members of group working on project <br />
	Amanda Wakefield <br />
	Lucas Schiffer <br />
	Brian  <br />
	
3. Name of professor or other person supervising this work and contact information <br />
	Sandor Vajda <br />
	BME Dept. <br />
	vajda@bu.edu <br />

4. Brief description of project (250 word max). Include the principle aims of your project. <br />

5. Three examples of questions (broadly speaking) that will be answered by your database. <br />
Which GPCRs have ligands in their allosteric site? <br />
Which allosteric ligands are associated with class X? <br />
Where is the allosteric site on a given GPCR? <br />

6. Description of user accessibility (i.e., who can use it, who can’t use it, will there be password protection). <br />
	This database will have two user types: admin and guest. There will be no restricitions on who can be a guest. Guest access will be limited to viewing and downloading data. Guests will not be able to add or remove data from the database. 

7. Description of data (what are the data objects, where do the data come from). <br />
	The data will consist of PDB IDs, FTMap mapping results for allosteric sites, Ligand IDs, Binding affinities.

8. List of any special software that is not currently on bioed, but which you would like to use for the project (if your project will be on bioed). <br />
	The database will not be hosted on Bioed


The following will be required in the final proposal. Any and all of this may be included in the draft. <br />
9. A specific list of tasks that you expect to accomplish. <br />
10. ER model (diagram) including key and participation constraints. <br />
11. Description of tables: What tables are used. For each table <br />
• Which fields are keys. <br />
• Which fields are foreign keys and to which other tables do they refer. <br />
• Which fields are indexed. What type of index. <br />
12. Three sample SQL queries for common functions of the database. <br />
13. Description of data processing, scheduled or performed by the user interface <br />
program, but which is external to the database (e.g. BLAST searches, statistical analysis, SOAP queries, etc.) if any. <br />
14. List of other databases to which this database provides links. <br />
15. Description of graphical output of the database. Include examples. <br />
16. Description of the data download function of the database (i.e., what data comes out and in what format).


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
