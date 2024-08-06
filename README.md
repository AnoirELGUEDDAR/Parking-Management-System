# **Features**
Add Parking Details: Easily add new parking spaces with their ID, name, level, and initial available space.
View Parking Details: Search and view parking space details by ID, name, level, or see all available spaces at once.
Add Cars to Parking: Assign vehicles to parking spaces, specifying their details and parking duration.
Remove Vehicle Records: Clear out vehicle information from the system when they leave the parking lot.
View Vehicle Details: Look up details of parked vehicles by their ID.
# **Prerequisites**
Python (3.x recommended): Make sure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

MySQL Server: You'll need a MySQL database server up and running.  Instructions for installing and setting up MySQL can be found on their website: https://www.mysql.com/.

mysql-connector-python: This library is used to connect Python to MySQL. Install it using pip:
*pip install mysql-connector-python*
# **Database Setup**
Create Database: In your MySQL server, create a database named parking.
Create Tables: Execute the following SQL commands in your MySQL client to create the necessary tables:<br>
*CREATE TABLE parkmaster ( <br>
    pid INT PRIMARY KEY,   -- Parking space ID (unique)  <br>
    pnm VARCHAR(255),      -- Parking name (e.g., "North Lot") <br>
    level VARCHAR(255),    -- Level of the parking (e.g., "Ground", "1st Floor") <br>
    AVSPACE INT,           -- Available spaces in the parking lot <br>
    payment FLOAT          -- Total payments received for this lot <br>
);*
<br>
*CREATE TABLE vehicle ( <br>
    Vid INT PRIMARY KEY,    -- Vehicle ID (unique) <br>
    vnm VARCHAR(255),      -- Vehicle name/model <br>
    dateofpur DATE,        -- Purchase date of the vehicle <br>
    parkid INT,            -- Foreign key referencing parkmaster.pid <br>
    Period INT,            -- Number of days parked <br>
    pay FLOAT,             -- Payment for parking <br>
    FOREIGN KEY (parkid) REFERENCES parkmaster(pid) <br>
);*<br>
# **Configuration**
### **Environment Variables:**

Before running the application, set the following environment variable to your MySQL root password:

Windows: set MYSQL_PASSWORD=your_password
macOS/Linux: export MYSQL_PASSWORD=your_password <br>
**Replace:**

Replace the host, user, and password parameters in the code with your specific MySQL credentials.
# **Running the Project** <br>
1-Make sure your MySQL server is running.<br>
2-Open your terminal or command prompt.<br>
3-Navigate to the project directory.<br>
4-Run the script:<br>
*python main.py*<br>
You'll be presented with the menu options to start managing your parking.





