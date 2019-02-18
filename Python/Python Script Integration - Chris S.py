#____________________________________________________________________________________
#
#                   Python MySQL Demo Integration with PyMySQL
#          Uses the excellent "classicmodels" sample database available at
#           https://www.richardtwatson.com/dm6e/Reader/ClassicModels.html
#____________________________________________________________________________________

########################## IMPORTS AND TICKER FUNCTION ########################################

import pymysql                  # enable MySQL connectivity
import warnings                 # import warnings library (exception subclass)
import getpass                  # enable accepting password silently / entry hiding
warnings.simplefilter("ignore") # ignore warnings (to allow for reducing Decimal values)

def yesNo(question):            # Simple and tolerant mechanism to take yes/no from user
    while True:
        reply = str(input(question + ' (Y/N): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

########################## CONNECTION LOGIC ###################################################

while True:     # start a loop which repeats until there is no problem with login
    try:
        db_user = input("Please Enter Valid DB Credentials.\nUsername: ")  # Get username
        db_password = getpass.getpass('Password: (hidden) ')               # Get password
        conn   = pymysql.connect(host='localhost',           # Connect to the local MySQL server
                                 port=3306,
                                 user=str(db_user),          # Use the value we just grabbed
                                 passwd=str(db_password),    # Same for password
                                 db='classicmodels',         # Indicate which schema to use
                                 charset='utf8')
        cur = conn.cursor()                                  # Open a cursor on active connection
        cur.connection.autocommit(False)                     # Turn off automatic DB commitment
        break                                                # DB login worked, break out of try loop.
    except pymysql.OperationalError as error:                # BUT if there was a logon problem,
        code, message = error.args
        print ("\n::: ERROR", code,":::", message, "\n")     # let the user know about it before retrying

########################## DATABASE OPERATION (DISCOUNT APPLICATION) ##########################

try:                                                         # Open a transaction with MYSQL for DB safety
    with conn.cursor() as cur:
        input("\nYou have logged in and connected to the database successfully." +
        "\nPress [ENTER] to Perform Deduction on December Transaction Amts (1% markdown): ")

        # SQL query to grab original December payment amounts
        sql_fetchAmounts = """
        SELECT amount, paymentDate FROM payments
        WHERE MONTH(paymentDate) = 12;
        """
        cur.execute(sql_fetchAmounts)                        # Run query and dump resulting rows to var
        output = cur.fetchall()

        date, result_original, result_after = ([],[],[])     # Create lists to store row results internally

        for row in output:                                   # Append dumped rows from cursors to lists
            result_original.append(float(row[0]))            # by column, for original amt and post discount
            date.append(str(row[1]))                         # amt

        # SQL query to reduce payment amounts from DECEMBER by 1%
        sql = """
        UPDATE payments
        SET amount = (amount * 0.99)
        WHERE MONTH(paymentDate) = 12 AND checkNumber IS NOT NULL;
        """

        cur.execute(sql)                                     # Run query
        cur.execute(sql_fetchAmounts)                        # Re-run fetch query

        output = cur.fetchall()                              # Dump resulting row to var
        for row in output:
            result_after.append(float(row[0]))               # Append updated amounts to list we prepared

        print("\nOPERATION COMPLETE. RESULTS :::\n\n",       # Begin tabulated results display
        "{0:<10}".format("DATE"),"{0:>13}".format("ORIG. AMT"),'   ',"{0:<13}".format("AFTER DISC."), sep='',end='')
        for date, a, b in zip(date, result_original, result_after):
            print ("\n","{0:<10}".format(date),"{0:>13}".format(a),'   ',"{0:<13}".format(b), sep='',end='')
        ticker = yesNo("\n\nWould you like to COMMIT these changes? (CANNOT BE UNDONE)")  # TO COMMIT, OR NOT TO COMMIT
        if ticker:
            conn.commit()                                    # Write the visualized changes to DB permanently
            print('\nChanges to database have been saved.')  # Confirm operation successful
        else:
            conn.rollback()                                  # Roll back the visualized changes (DB not altered)
            print('\nChanges to database have been rolled back.')  # Confirm no changes made
    # conn.commit()
except (pymysql.OperationalError, pymysql.ProgrammingError) as error:  # Exception Handling,
    code, message = error.args                               # If error encountered, cancel changes to DB and inform user
    conn.rollback()
    cur.close()
    conn.close()
    print ("\n::: ERROR", code,":::", message, "\nChanges were rolled back, where possible.", '\n')
finally:                                                     # In any case,
    cur.close()                                              # Close the DB cursor and connection after we're finished
    conn.close()                                             # using them. Report this to user.
    input("\nConnection Closed. ((ENTER)) ")

########################## POST OPERATIONS ####################################################

input("\nPROGRAM COMPLETED SUCCESSFULLY {{ENTER}} ")         # Everything is finished, wait for keypress to close
quit()
