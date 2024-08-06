import os
import platform
import mysql.connector

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database='parking'
)
mycursor = mydb.cursor()


def clear_screen():
    """Clears the terminal screen."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def input_int(prompt):
    """Helper function to get an integer input with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Function to add parking details
def Add_Record():
    try:
        id1 = input_int("Enter the parking number: ")
        pname1 = input("Enter the Parking Name: ").strip()
        level1 = input("Enter level of parking: ").strip()
        psize1 = input_int("Enter parking size: ")

        stud = (id1, pname1, level1, psize1, 0)  # Initial payment is 0
        sql = 'INSERT INTO parkmaster (pid, pnm, level, AVSPACE, payment) VALUES (%s, %s, %s, %s, %s)'
        mycursor.execute(sql, stud)
        mydb.commit()  # Commit changes to the database
        print("Parking record added successfully.")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Function to view parking details
def Rec_View():
    print("1. Parking Number")
    print("2. Parking Name")
    print("3. Level No")
    print("4. All")
    ch = input_int("Enter your choice: ")

    if ch == 1:
        s = input_int("Enter Parking number: ")
        sql = "SELECT * FROM parkmaster WHERE pid = %s"
        mycursor.execute(sql, (s,))
    elif ch == 2:
        s = input("Enter Parking Name: ").strip()
        sql = "SELECT * FROM parkmaster WHERE pnm = %s"
        mycursor.execute(sql, (s,))
    elif ch == 3:
        s = input_int("Enter Level of Parking: ")
        sql = "SELECT * FROM parkmaster WHERE level = %s"
        mycursor.execute(sql, (s,))
    elif ch == 4:
        sql = "SELECT * FROM parkmaster"
        mycursor.execute(sql)
    else:
        print("Invalid choice.")
        return

    res = mycursor.fetchall()
    if res:
        print("Details about Parking are as follows: ")
        print("(Parking Id, Parking Name, Level, Available Space, Payment)")
        for x in res:
            print(x)
    else:
        print("No records found.")
    print('Task completed.')


# Function to add car details to a parking spot
def Add_Car():
    try:
        pid1 = input_int("Enter Parking Number (pid must match a Parking No): ")

        # Check if the entered pid exists in parkmaster
        sql_check = "SELECT pid, AVSPACE, payment FROM parkmaster WHERE pid = %s"
        mycursor.execute(sql_check, (pid1,))
        result = mycursor.fetchone()

        if result:
            parkid, available_space, current_payment = result

            if available_space > 0:
                Vid1 = input_int("Enter Vehicle Number: ")
                vnm1 = input("Enter Vehicle Name/Model Name: ").strip()
                dateofpur1 = input("Enter Year-Month-Date of purchase (YYYY-MM-DD): ").strip()
                nod1 = input_int("Enter total number of days for parking: ")
                Payment1 = 20 * nod1

                vdt = (Vid1, vnm1, dateofpur1, parkid, nod1, Payment1)
                sql = "INSERT INTO vehicle (Vid, vnm, dateofpur, parkid, Period, pay) VALUES (%s, %s, %s, %s, %s, %s)"
                mycursor.execute(sql, vdt)

                # Update available space and payment after adding vehicle
                available_space -= 1
                new_payment = current_payment + Payment1
                sql_update_space_payment = "UPDATE parkmaster SET AVSPACE = %s, payment = %s WHERE pid = %s"
                mycursor.execute(sql_update_space_payment, (available_space, new_payment, pid1))

                mydb.commit()
                print("Car details added to parking successfully.")
            else:
                print(f"No space available in Parking Number {pid1}.")
        else:
            print(f"Error: Parking Number {pid1} does not exist. Please enter a valid Parking Number.")
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Function to view vehicle details
def Vehicle_View():
    try:
        vid1 = input_int("Enter the vehicle number of the vehicle whose details are to be viewed: ")
        sql = 'SELECT * FROM vehicle WHERE Vid = %s'
        mycursor.execute(sql, (vid1,))

        res = mycursor.fetchall()
        if res:
            print('The following are the details you wanted:')
            for x in res:
                print(x)
        else:
            print("No records found.")
        print('Task completed.')
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Function to remove vehicle records
def remove():
    try:
        vid1 = input_int("Enter the vehicle number of the vehicle to be deleted: ")
        sql = "DELETE FROM vehicle WHERE Vid = %s"
        mycursor.execute(sql, (vid1,))
        mydb.commit()
        print('Vehicle record removed successfully.')
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Function to display menu options
def Menu():
    while True:
        print("\nMenu:")
        print("1: Add Parking Detail")
        print("2: View Parking Detail")
        print("3: Add Car to Parking")
        print("4: Remove Vehicle Record")
        print("5: View Vehicle Details")
        print("6: Exit")

        input_dt = input_int("Please select an option: ")
        if input_dt == 1:
            Add_Record()
        elif input_dt == 2:
            Rec_View()
        elif input_dt == 3:
            Add_Car()
        elif input_dt == 4:
            remove()
        elif input_dt == 5:
            Vehicle_View()
        elif input_dt == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        runAgain()


# Function to run the menu again
def runAgain():
    runAgn = input('\nDo you want to perform another operation (Y/n)? ')
    if runAgn.lower() == 'n':
        exit()
    clear_screen()


if __name__ == "__main__":
    Menu()
