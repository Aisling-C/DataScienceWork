/* Welcome to the SQL mini project. You will carry out this project partly in
the PHPMyAdmin interface, and partly in Jupyter via a Python connection.

This is Tier 1 of the case study, which means that there'll be more guidance for you about how to 
setup your local SQLite connection in PART 2 of the case study. 

The questions in the case study are exactly the same as with Tier 2. 

PART 1: PHPMyAdmin
You will complete questions 1-9 below in the PHPMyAdmin interface. 
Log in by pasting the following URL into your browser, and
using the following Username and Password:

URL: https://sql.springboard.com/
Username: student
Password: learn_sql@springboard

The data you need is in the "country_club" database. This database
contains 3 tables:
    i) the "Bookings" table,
    ii) the "Facilities" table, and
    iii) the "Members" table.

In this case study, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */


/* QUESTIONS 
/* Q1: Some of the facilities charge a fee to members, but some do not.
Write a SQL query to produce a list of the names of the facilities that do. */

SELECT name
FROM Facilities
WHERE membercost =0;

>>>
Badminton Court
Table Tennis
Snooker Table
Pool Table


/* Q2: How many facilities do not charge a fee to members? */
SELECT COUNT(*)
FROM Facilities
WHERE membercost =0;

>>>
4

/* Q3: Write an SQL query to show a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost.
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */
SELECT facid, name, membercost, monthlymaintenance
FROM Facilities
WHERE membercost >0
AND membercost < monthlymaintenance * .2;

>>>
(0, 'Tennis Court 1', 5.0, 200),
(1, 'Tennis Court 2', 5.0, 200),
(4, 'Massage Room 1', 9.9, 3000),
(5, 'Massage Room 2', 9.9, 3000),
(6, 'Squash Court', 3.5, 80);


/* Q4: Write an SQL query to retrieve the details of facilities with ID 1 and 5.
Try writing the query without using the OR operator. */
SELECT *
FROM Facilities
WHERE facid
IN ( 1, 5 )

>>>
(1, 'Tennis Court 2', 5.0, 25.0, 8000, 200),
(5, 'Massage Room 2', 9.9, 80.0, 4000, 3000);


/* Q5: Produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100. Return the name and monthly maintenance of the facilities
in question. */

SELECT name, monthlymaintenance, 
CASE WHEN monthlymaintenance>=100 THEN 'expensive'
ELSE 'cheap' END AS 'costcategory'
FROM Facilities;

>>>
('Tennis Court 1', 200, 'expensive'),
('Tennis Court 2', 200, 'expensive'),
('Badminton Court', 50, 'cheap'),
('Table Tennis', 10, 'cheap'),
('Massage Room 1', 3000, 'expensive'),
('Massage Room 2', 3000, 'expensive'),
('Squash Court', 80, 'cheap'),
('Snooker Table', 15, 'cheap'),
('Pool Table', 15, 'cheap');

/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Try not to use the LIMIT clause for your solution. */
SELECT firstname, surname
FROM Members
WHERE MONTH( joindate ) =9

>>
('Ramnaresh', 'Sarwin'),
('Douglas', 'Jones'),
('Henrietta', 'Rumney'),
('David', 'Farrell'),
('Henry', 'Worthington-Smyth'),
('Millicent', 'Purview'),
('Hyacinth', 'Tupperware'),
('John', 'Hunt'),
('Erica', 'Crumpet'),
('Darren', 'Smith');

/* Q7: Produce a list of all members who have used a tennis court.
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */

SELECT name, CONCAT(firstname,' ',surname) AS Fullname
FROM Bookings as b
JOIN Facilities as f
	USING (facid)
JOIN Members 
	USING (memid)
ORDER BY memid DESC;

>>>
Badminton Court;"Erica Crumpet"
Massage Room 1;"Erica Crumpet"
Badminton Court;"Erica Crumpet"
Massage Room 1;"Erica Crumpet"
Tennis Court 1;"Erica Crumpet"
Table Tennis;"Erica Crumpet"
Table Tennis;"Erica Crumpet"
Tennis Court 1;"John Hunt"
Tennis Court 2;"John Hunt"
Tennis Court 1;"John Hunt"
Massage Room 1;"John Hunt"
Tennis Court 2;"John Hunt"
Table Tennis;"John Hunt"
Tennis Court 2;"John Hunt"
Tennis Court 2;"John Hunt"
Massage Room 1;"John Hunt"
Massage Room 1;"John Hunt"
Tennis Court 1;"John Hunt"
Tennis Court 1;"John Hunt"
Badminton Court;"John Hunt"
Badminton Court;"John Hunt"
Squash Court;"John Hunt"

/* Q8: Produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30. Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */

SELECT name, CONCAT(firstname,' ',surname) AS fullname,
(CASE WHEN memid=0 AND slots*guestcost>30 THEN slots*guestcost
	 WHEN memid>0 AND slots*membercost>30 THEN slots*membercost
	 END) AS cost
FROM Bookings as b
JOIN Facilities as f
	USING (facid)
JOIN Members 
	USING (memid)
WHERE DATE(starttime)='2012-09-14' AND 
CASE WHEN memid=0 AND slots*guestcost>30 THEN slots*guestcost
	 WHEN memid>0 AND slots*membercost>30 THEN slots*membercost
	 END IS NOT NULL
ORDER BY cost DESC;

>>>
Massage Room 2;"GUEST GUEST";"320.0"
Massage Room 1;"GUEST GUEST";"160.0"
Massage Room 1;"GUEST GUEST";"160.0"
Massage Room 1;"GUEST GUEST";"160.0"
Tennis Court 2;"GUEST GUEST";"150.0"
Tennis Court 1;"GUEST GUEST";"75.0"
Tennis Court 1;"GUEST GUEST";"75.0"
Tennis Court 2;"GUEST GUEST";"75.0"
Squash Court;"GUEST GUEST";"70.0"
Massage Room 1;"Jemima Farrell";"39.6"
Squash Court;"GUEST GUEST";"35.0"
Squash Court;"GUEST GUEST";"35.0"


/* Q9: This time, produce the same result as in Q8, but using a subquery. */
>>>
SELECT name AS facilityname, CONCAT(m.firstname,' ',m.surname) AS fullname, cost
FROM 
	(SELECT
		name,
        memid,
     	starttime,
		(CASE WHEN memid=0 THEN slots*guestcost
	 	WHEN memid>0 THEN slots*membercost
	 	END) AS cost
		FROM Bookings as b
		JOIN Facilities as f
			USING (facid)) AS Subquery
JOIN Members as m
	USING (memid)
WHERE DATE(starttime)='2012-09-14' AND cost>30
ORDER BY cost DESC;

>>>
Massage Room 2;"GUEST GUEST";"320.0"
Massage Room 1;"GUEST GUEST";"160.0"
Massage Room 1;"GUEST GUEST";"160.0"
Massage Room 1;"GUEST GUEST";"160.0"
Tennis Court 2;"GUEST GUEST";"150.0"
Tennis Court 1;"GUEST GUEST";"75.0"
Tennis Court 1;"GUEST GUEST";"75.0"
Tennis Court 2;"GUEST GUEST";"75.0"
Squash Court;"GUEST GUEST";"70.0"
Massage Room 1;"Jemima Farrell";"39.6"
Squash Court;"GUEST GUEST";"35.0"
Squash Court;"GUEST GUEST";"35.0"

/* PART 2: SQLite
/* We now want you to jump over to a local instance of the database on your machine. 

Copy and paste the LocalSQLConnection.py script into an empty Jupyter notebook, and run it. 

Make sure that the SQLFiles folder containing thes files is in your working directory, and
that you haven't changed the name of the .db file from 'sqlite\db\pythonsqlite'.

You should see the output from the initial query 'SELECT * FROM FACILITIES'.

Complete the remaining tasks in the Jupyter interface. If you struggle, feel free to go back
to the PHPMyAdmin interface as and when you need to. 

You'll need to paste your query into value of the 'query1' variable and run the code block again to get an output.
 
QUESTIONS:
/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */

/* Q11: Produce a report of members and who recommended them in alphabetic surname,firstname order */


/* Q12: Find the facilities with their usage by member, but not guests */


/* Q13: Find the facilities usage by month, but not guests */

