import mysql.connector

#CONNECTION TO THE DATABASE USING MYSQL#
connection = mysql.connector.connect(host="localhost", user="root", passwd="narag", database="atmdatabase")
print(connection)

#CHECK IF THERE'S A DATA SAVED IN THE DATABASE AND INSERT IT TO THE LIST#
acc = []

conn = connection.cursor()
conn.execute("select name, password, money from accounts")
gather = conn.fetchall()

for x in gather:
    data1 = x[0]
    data2 = x[1]
    data3 = x[2]
    acc.append([data1, data2, data3])

while True:
    print('ATM MACHINE')
    print('1.Create an Account')
    print('2.Log-in')
    print('3.View Accounts')
    pick = input("Choose a number for your transction:")

    if pick == '1':
        name = input("Input Name:")
        password = input("Input Password:")
        confirm = input("Confirm Password:")
        if password != confirm:
            print('Password not Match')
            name = input("Input Name:")
            password = input("Input Password:")
            confirm = input("Confirm Password:")
        else:
            # SELECT PROMPT FOR THE DATA IF THE DATA IS ALREADY EXISTED#
            conn = connection.cursor()
            query = "SELECT * FROM accounts where name=%s and password=%s;"
            data = (name, password)
            conn.execute(query,data)
            chk = conn.fetchall()
            comp = len(chk)
            if comp > 0:
                print("Data is Already Registered!")
            else:
                acc.append([name, password, 0])
                # INSERT PROMPT FOR THE DATA'S NEEDED#
                query1 = "INSERT INTO accounts(name,password,money) VALUES(%s,%s,%s);"
                data1 = (name, password, 0)
                conn.execute(query1,data1)
                print("Successfully Created an Account!")
                connection.commit()

    elif pick == "2":
        name1 = input("Enter your Name:")
        pass1 = input("Enter your Password:")
        for i in range(len(acc)):
            namee=acc[i][0]
            passs=acc[i][1]
            amount1=acc[i][2]
            if name1 == namee:
                pass
                if pass1 == passs:
                    print('1.Withdraw')
                    print('2.Deposit')
                    print('3.Balance Inquiry')
                    print('4.Back')
                    response=input("Choose a transaction:")
                    if response == "4":
                        pass
                    elif response =="2":
                        amount=int(input('Insert how much money:'))
                        if amount <= 0:
                            print('Please enter valid amount')
                        else:
                            conn = connection.cursor()
                            compute = amount + amount1
                            acc[i][2]=compute
                            print(amount,'is succesfully deposited in your account')
                            print('Your New Balance is',compute)

                            # UPDATE PROMPT FOR THE DATA OF MONEY#
                            query2 = "UPDATE accounts SET money=%s WHERE name=%s "
                            data2 = (compute, name1)
                            conn.execute(query2,data2)
                            connection.commit()

                    elif response == "1":
                        withdraw=int(input('Enter Amount to withdraw:'))
                        if withdraw <=0:
                            print('Please enter valid amount')

                        elif withdraw > amount1:
                            print('Your Money in the Bank is insufficient')

                        else:
                            conn = connection.cursor()
                            calc=amount1 - withdraw
                            acc[i][2]=calc
                            print(withdraw, 'is succesfully withdrawn from your account')
                            print('Your New Balance is', calc)

                            # UPDATE PROMPT FOR THE DATA OF MONEY#
                            query3 = "UPDATE accounts SET money=%s WHERE name=%s "
                            data3 = (calc, name1)
                            conn.execute(query3, data3)
                            connection.commit()

                    elif response == "3":
                        print(namee,'Your balance is',amount1)
                    else:
                        print('Response is Invalid')
                elif passs !=pass1:
                    print('Invalid Credentials')
            elif len(acc) == 0:
                print('Invalid Credentials')
    elif pick == "3":
        if len(acc) == 0:
            print('There is no registered acc yet')
        else:
            for i in range(len(acc)):
                print(acc)
                print('1.Delete Account')
                print('2.Back')
                enter=input('Choose the transaction you want:')
                if enter =='2':
                    break
                elif enter == '1':
                    
                    # SELECT PROMPT FOR A SPECIFIC DATA TO DETECT IF IT IS IN THE DATA#
                    search = input("Search the name you want to delete:")
                    conn = connection.cursor()
                    check = "SELECT * FROM accounts where name=%s;"
                    data = (search,)
                    conn.execute(check, data)
                    go = conn.fetchall()
                    c = len(go)
                    
                    if c > 0:
                        # DELETE PROMPT FOR A SPECIFIC DATA TO BE INSERTED#
                        conn = connection.cursor()
                        query4 = "DELETE from accounts WHERE name=%s;"
                        data4 = (search,)
                        conn.execute(query4, data4)
                        connection.commit()
                        print("Successfully Deleted")
                        for i in range(len(acc)):
                            cheking = acc[i][0]
                            if cheking == search:
                                del acc[i][:3]
                        break
                        
                    else:
                        print("Account not exist")
    else:
        print('Response is Invalid')

