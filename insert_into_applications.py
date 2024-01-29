import psycopg2
from psycopg2 import sql

def main():
    try:
        # Database Connection Parameters
        database = 'job_applications'
        user = 'brittany'
        password = ''
        db_table = 'applications'

        # Csonnect to the Postgres database
        conn = psycopg2.connect(database=database, user=user, password=password)
        conn.autocommit = True

        # Create a cursor object
        cur = conn.cursor()

        # Ask User for input
        contactid = input("Enter the contact id:")
        jobtitle = input("Enter the job title: ")
        companyid = input("Enter the company id: ")
        applicationdate = input("Enter the application date (YYYY-MM-DD)")
        status = input("Enter the application status (Pending, Accepted, Interviewing, Rejected): ")
        status = status.upper()

        # Checking to see if all fields have something in them.
        if not any ([ contactid, jobtitle, companyid, applicationdate, status]):
            print(f"Nothing was added to {db_table}.")
            return

        # Inserting into application table
        insert_query = sql.SQL(
            "Insert INTO {} (Contactid, jobtitle, companyid, applicationdate, status) VALUES (%s, %s, %s, %s, %s);".format('applications')
        )

        # Adding data to  insert
        data = (contactid or None, jobtitle or None, companyid or None, applicationdate or None, status or None)

        # Execute query
        cur.execute(insert_query, data)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        print("Record added...")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cur.close()
        conn.close()
        print("The script shut down gracefully.")

if __name__== "__main__":
    main()
