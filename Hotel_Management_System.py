import mysql.connector

# Global variable declaration
myConnnection = ""
cursor = ""
userName = ""
password = ""
cid = ""


# Module to check MYSQL Connectivity
def connectionCheck():
    global myConnection
    global userName
    global password
    userName = input("\nEnter MYSQL Server's Username: ")
    password = input("\nEnter MYSQL Server's Password: ")
    myConnection = mysql.connector.connect(host="localhost", user=userName,
                                           passwd=password,
                                           auth_plugin='mysql_native_password')
    if myConnection:
        print("\nYOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor = myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print('''\nERROR ESTABLISHING MYSQL CONNECTION. ENTER AGAIN !''')


# Module to Estabalished MYSQL Connnection
def connection():
    global userName
    global password
    global myConnection
    global cid
    myConnection = mysql.connector.connect(host="localhost", user=userName,
                                           passwd=password, database="HMS",
                                           auth_plugin='mysql_native_password')
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()


# Modulle to create and insert Customer data
def userEntry():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        createTable = """CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),
        C_NAME VARCHAR(30),C_ADDRESS VARCHAR(30),C_AGE VARCHAR(30),
        C_COUNTRY VARCHAR(30) ,P_NO VARCHAR(30),C_EMAIL VARCHAR(30))"""
        cursor.execute(createTable)
        cid = input("Enter Customer's Identification Number : ")
        name = input("Enter Customer's Name : ")
        address = input("Enter Customer's Address : ")
        age = input("Enter Customer's Age : ")
        nationality = input("Enter Customer's Country : ")
        phoneno = input("Enter Customer's Contact Number : ")
        email = input("Enter Customer's Email : ")
        sql = "INSERT INTO C_Details VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (cid, name, address, age, nationality, phoneno, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        print("\nNew Customer Entered In The System Successfully !")
        cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# Module to create and insert booking record
def bookingRecord():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = '''CREATE TABLE IF NOT EXISTS BOOKING_RECORD(CID
             VARCHAR(20),CHECK_IN DATE ,CHECK_OUT DATE)'''
            cursor.execute(createTable)
            checkin = input("\n Enter Customer CheckIN Date [YYYY-MM-DD]: ")
            checkout = input("\n Enter Customer CheckOUT Date [YYYY-MM-DD]: ")
            sql = "INSERT INTO BOOKING_RECORD VALUES(%s,%s,%s)"
            values = (cid, checkin, checkout)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("\nCHECK-IN AND CHECK-OUT ENTRY MADED SUCCESSFULLY !")
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# Module to create Room_rent table
def roomRent():
    global cid
    customer = searchCustomer()
    if customer:

        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS ROOM_RENT(CID
             VARCHAR(20),ROOM_CHOICE INT,NO_OF_DAYS INT,ROOMNO INT ,
             ROOMRENT INT)"""
            cursor.execute(createTable)
            print("\n ##### We have The Following Rooms For You #####")
            print(" 1. Ultra Royal ----> 10000 Rs.")
            print(" 2. Royal ----> 5000 Rs. ")
            print(" 3. Elite ----> 3500 Rs. ")
            print(" 4. Budget ----> 2500 Rs. ")
            roomchoice = int(input("Enter Your Option : "))
            roomno = int(input("Enter Customer Room No : "))
            noofdays = int(input("Enter No. Of Days : "))
            if roomchoice == 1:
                roomrent = noofdays * 10000
                print("\nUltra Royal Room Rent : ", roomrent)
            elif roomchoice == 2:
                roomrent = noofdays * 5000
                print("\nRoyal Room Rent : ", roomrent)
            elif roomchoice == 3:
                roomrent = noofdays * 3500
                print("\nElite Royal Room Rent : ", roomrent)
            elif roomchoice == 4:
                roomrent = noofdays * 2500
                print("\nBudget Room Rent : ", roomrent)
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input!!! ")
                return
            sql = "INSERT INTO ROOM_RENT VALUES(%s,%s,%s,%s,%s)"
            values = (cid, roomchoice, noofdays, roomno, roomrent,)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Your Room Has Been Booked For : ", noofdays, "Days")
            print("Your Total Room Rent is : Rs. ", roomrent)
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# Module to create Restaurent Table
def Restaurent():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS RESTAURENT(CID
             VARCHAR(20),CUISINE VARCHAR(30),QUANTITY VARCHAR(30),
             BILL VARCHAR(30))"""
            cursor.execute(createTable)
            print("1. Vegetarian Combo -----> 300 Rs.")
            print("2. Non-Vegetarian Combo -----> 500 Rs.")
            print("3. Vegetarian & Non-Vegetarian Combo -----> 750 Rs.")
            choice_dish = int(input("Enter Your Cusine : "))
            quantity = int(input("Enter Quantity : "))
            if choice_dish == 1:
                print('''\nSO YOU HAVE ORDER:''')
                print('''Vegetarian Combo ''')
                restaurentbill = quantity * 300
            elif choice_dish == 2:
                print('''\nSO YOU HAVE ORDER:''')
                print('''Non-Vegetarian Combo ''')
                restaurentbill = quantity * 500
            elif choice_dish == 3:
                print('''\nSO YOU HAVE ORDER:''')
                print('''Vegetarian & Non-Vegetarian Combo ''')
                restaurentbill = quantity * 750
            else:
                print("Sorry ,May Be You Are Giving Me Wrong Input!!! ")
                return
            sql = "INSERT INTO RESTAURENT VALUES(%s,%s,%s,%s)"
            values = (cid, choice_dish, quantity, restaurentbill)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            print("Your Total Bill Amount Is : Rs. ", restaurentbill)
            print("\n\n**** WE HOPE YOU WILL ENJOY YOUR MEAL ***\n\n")
            cursor.close()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# Module to calculate total amount of bill
def totalAmount():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            createTable = """CREATE TABLE IF NOT EXISTS TOTAL(CID VARCHAR(20),
             C_NAME VARCHAR(30),ROOMRENT INT(5) ,RESTAURENTBILL INT(5) ,
             TOTALAMOUNT INT(5))"""
            cursor.execute(createTable)
            sql = "INSERT INTO TOTAL VALUES(%s,%s,%s,%s,%s)"
            cursor.execute('''select c_name from c_details
                                   where cid=''' + str(cid))
            name = cursor.fetchone()[0]
            cursor.execute('''select roomrent from room_rent
                                where cid=''' + str(cid))
            roomrent = int(cursor.fetchone()[0])
            cursor.execute('''select bill from restaurent
                               where cid=''' + str(cid))
            restaurentbill = int(cursor.fetchone()[0])
            grandTotal = roomrent + restaurentbill
            values = (cid, name, roomrent, restaurentbill, grandTotal)
            cursor.execute(sql, values)
            cursor.execute("COMMIT")
            cursor.close()
            print('***************************************************')
            print("\n **** HOTEL SHIV **** CUSTOMER BILLING ****")
            print("\n CUSTOMER NAME : ", name)
            print("\nROOM RENT : Rs. ", roomrent)
            print("\nRESTAURENT BILL : Rs. ", restaurentbill)
            print("___________________________________________________")
            print("\nTOTAL AMOUNT : Rs. ", grandTotal)
            print('***************************************************')
            cursor.close()
        else:
            print("\nERROR ESTABLISHING MYSQL CONNECTION !")


# Module to search for old bills
def searchOldBill():
    global cid
    customer = searchCustomer()
    if customer:
        if myConnection:
            cursor = myConnection.cursor()
            sql = "SELECT * FROM TOTAL WHERE CID= %s"
            cursor.execute(sql, (cid,))
            data = cursor.fetchall()
            if data:
                print('')
                print('***************************************************')
                print("\n **** HOTEL SHIV **** CUSTOMER BIILING ****")
                print('Customer Details:')
                print('CustomerName:', data[0][1])
                print('\nROOM RENT : Rs. ', data[0][2])
                print('\nRESTAURENT BILL : Rs. :', data[0][3])
                print("___________________________________________________")
                print('\nTOTAL AMOUNT : Rs. ', data[0][4])
                print('***************************************************')
            else:
                print("Record Not Found Try Again !")
                cursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


# Module to search data about customers)
def searchCustomer():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        cid = input("ENTER CUSTOMER ID : ")
        sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        print(data)
        if data:
            print('')
            print('Customer Details:')
            print('CustomerID:', data[0][0])
            print('CustomerName:', data[0][1])
            print('Adress:', data[0][2])
            print('Age:', data[0][3])
            print('Phone Number:', data[0][5])
            print('Email:', data[0][6])
            print('Country:', data[0][4])
            return True
        else:
            print("Record Not Found Try Again !")
            return False
        cursor.close()

    else:
        print("\nSomthing Went Wrong ,Please Try Again !")


# MODULE To Update Customer Record
def update_user():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        updatestat = '''UPDATE C_DETAILS
                      SET C_NAME=%s,C_ADDRESS=%s,C_AGE=%s,C_COUNTRY=%s,
                      P_NO=%s,C_EMAIL=%s
                      WHERE cid = %s'''
        cid = int(input("Enter Customer's Identification Number : "))
        name = input("Enter Customer's Name : ")
        address = input("Enter Customer's changed Address : ")
        age = input("Enter Customer's changed Age : ")
        nationality = input("Enter Customer's Country : ")
        phoneno = input("Enter Customer's Contact Number : ")
        email = input("Enter Customer's Email : ")
        x = (name, address, age, nationality, phoneno, email, cid)
        cursor.execute(updatestat, x)
        cursor.execute('commit')
        print('RECORD UPDATED')
        print('UPDATED RECORD:')
        sql = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql, (cid,))
        data = cursor.fetchall()
        if data:
            print('')
            print('Customer Details:')
            print('CustomerID:', data[0][0])
            print('CustomerName:', data[0][1])
            print('Adress:', data[0][2])
            print('Age:', data[0][3])
            print('Phone Number:', data[0][5])
            print('Email:', data[0][6])
            print('Country:', data[0][4])


def del_cus():
    global cid
    if myConnection:
        cursor = myConnection.cursor()
        stat = 'delete from c_details where cid=%s'
        cid = int(input("Enter Customer's Identification Number for deletion : "))
        cursor.execute(stat, (cid,))
        cursor.execute('commit')
        print('RECORD DELETED')


myConnection = connectionCheck()
if myConnection:
    connection()
    while (True):
        print('')
        print('1--->Enter Customer Details')
        print('2--->Booking Record')
        print('3--->Calculate Room Rent')
        print('4--->Calculate Restaurant Bill')
        print('5--->Display Customer Details')
        print('6--->GENERATE TOTAL BILL AMOUNT')
        print('7--->GENERATE OLD BILL')
        print('8--->UPDATE CUSTOMER DETAILS')
        print('9--->DELETE CUSTOMER DETAILS')
        print('10--->EXIT')
        choice = int(input("Enter Your Choice:"))
        if choice == 1:
            userEntry()
        elif choice == 2:
            bookingRecord()
        elif choice == 3:
            roomRent()
        elif choice == 4:
            Restaurent()
        elif choice == 5:
            searchCustomer()
        elif choice == 6:
            totalAmount()
        elif choice == 7:
            searchOldBill()
        elif choice == 8:
            update_user()
        elif choice == 9:
            del_cus()
        elif choice == 10:
            print('COME BACK SOON')
            break
        else:
            print("Sorry ,May Be You Are Giving Me Wrong Input!!! ")
else:
    print("\nERROR ESTABLISHING MYSQL CONNECTION !")


