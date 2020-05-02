import mysql.connector
import random
from tabulate import tabulate
from prettytable import PrettyTable
import csv


class Bullpass():

    def __init__(self):
        self.string = "abcdefghijklmnopqrstuvwxyx1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&1234567890"
        self.newpass = ""


    def add_new_pass(self):
        if user_input.lower() == "b":
            pass
        length = int(input("\n\rEnter password length: "))
        for c in range(length):
            self.newpass += str(random.choice(self.string))
        x = PrettyTable()
        x.field_names = ["-- OK? --", "--"]
        x.add_row(["New Password", f"{self.newpass}"])
        print(x)
        ok = str(input("\n[Y/n]"))
        if ok.lower() == "y":
            name_of_the_site = str(input("\n\rEnter the website's name: "))
            user_name = str(input("\n\rEnter the user name: "))
            sql = "INSERT INTO general_passwords (website, user_name, password) VALUES (%s, %s, %s)"
            val = (name_of_the_site, user_name, self.newpass)
            cursor.execute(sql, val)
            db.commit()
            cursor.execute(f"SELECT * FROM general_passwords WHERE website = '{name_of_the_site}' ")
            result = cursor.fetchall()
            for i in result:
                print(f"Row added -\n{i}")
        elif ok.lower() == "n":
            pass

    def add_old_pass(self):
        if user_input.lower() == "b":
            pass
        the_password = str(input("\n\rType your password: \n\r"))
        name_of_the_site = str(input("\n\rEnter the website's name: "))
        user_name = str(input("\n\rEnter the user name: "))
        sql = "INSERT INTO general_passwords (website, user_name, password) VALUES (%s, %s, %s)"
        val = (name_of_the_site, user_name, the_password)
        cursor.execute(sql, val)
        db.commit()
        cursor.execute(f"SELECT * FROM general_passwords WHERE website = '{name_of_the_site}' ")
        result = cursor.fetchall()
        for i in result:
            print(f"Row added -\n{i}")


    def search_pass(self):
        x = PrettyTable()
        x.field_names = ["Site", "User", "Password"]
        x.add_row(["1", "2", "3"])
        print(x)
        user_input = str(input(">> Enter Your Choice: "))
        if user_input.lower() == "1":
            site = str(input(">> Enter SITE name: "))
            sql = f"SELECT * FROM general_passwords WHERE website LIKE '{site}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(tabulate(result, tablefmt='psql'))
            if user_input.lower() == "b":
                pass
        elif user_input.lower() == "2":
            user = str(input(">> Enter USER name: "))
            sql = f"SELECT * FROM general_passwords WHERE user_name LIKE '{user}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(tabulate(result, tablefmt='psql'))
            if user_input.lower() == "b":
                pass
        elif user_input.lower() == "3":
            passw = str(input(">> Enter PASSWORD name: "))
            sql = f"SELECT * FROM general_passwords WHERE user_name LIKE '{passw}'"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(tabulate(result, tablefmt='psql'))
            if user_input.lower() == "b":
                pass


    def show_pass(self):
        sql = "SELECT * FROM general_passwords"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(tabulate(result, tablefmt='psql'))
        pass


    def delete_pass(self):
        sql = "SELECT * FROM general_passwords"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Choose row to delete by ID -")
        print(tabulate(result, tablefmt='psql'))
        user_id = str(input(">> Enter id: "))
        sql2 = f"SELECT * FROM general_passwords WHERE id = {user_id}"
        cursor.execute(sql2)
        result2 = cursor.fetchall()
        sql1 = f"DELETE FROM general_passwords WHERE id = {user_id}"
        cursor.execute(sql1)
        db.commit()
        for x in result2:
            print(f"Row Deleted -\n{x}")
        if user_input.lower() == "b":
            pass


    def export_pass(self):
        try:
            cursor.execute(f"SELECT * FROM general_passwords")
            with open(f"passwords.csv", "w") as outfile:
                writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(col[0] for col in cursor.description)
                for row in cursor:
                    writer.writerow(row)
        except mysql.connector.errors.Error as e:
            print(f"Mysql Error: {e}")
        finally:
            print(f"File passwords.csv created!")
            pass

    def update_pass(self):
        x = PrettyTable()
        x.field_names = ["Site", "User", "Password"]
        x.add_row(["1", "2", "3"])
        print(x)
        user_input = str(input(">> Enter Your Choice: "))
        if user_input.lower() == "1":
            site = str(input(">> Enter SITE name to change: "))
            new_site = str(input(">> Enter new SITE name: "))
            sql = f"UPDATE general_passwords SET website = '{new_site}' WHERE website = '{site}'"
            cursor.execute(sql)
            db.commit()
            cursor.execute(f"SELECT * FROM general_passwords WHERE website = '{new_site}' ")
            result = cursor.fetchall()
            for i in result:
                print(f"Row Updated -\n{i}")
            if user_input.lower() == "b":
                pass
        elif user_input.lower() == "b":
            pass
        elif user_input.lower() == "2":
            user = str(input(">> Enter USER name to change: "))
            new_user = str(input(">> Enter new USER name: "))
            sql = f"UPDATE general_passwords SET user_name = '{new_user}' WHERE user_name = '{user}'"
            cursor.execute(sql)
            db.commit()
            cursor.execute(f"SELECT * FROM general_passwords WHERE user_name = '{new_user}' ")
            result = cursor.fetchall()
            for i in result:
                print(f"Row Updated -\n{i}")
            if user_input.lower() == "b":
                pass
        elif user_input.lower() == "3":
            passw = str(input(">> Enter PASSWORD name to change: "))
            new_passw = str(input(">> Enter new PASSWORD name: "))
            sql = f"UPDATE general_passwords SET password = '{new_passw}' WHERE password = '{passw}'"
            cursor.execute(sql)
            db.commit()
            cursor.execute(f"SELECT * FROM general_passwords WHERE password = '{new_passw}' ")
            result = cursor.fetchall()
            for i in result:
                print(f"Row Updated -\n{i}")
            if user_input.lower() == "b":
                pass


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Idanid1",
  database="idan_passwords")
cursor = db.cursor()

while True:
    test = Bullpass()
    x = PrettyTable()
    x.field_names = ["NEW", "OLD", "Search", "Show", "Delete", "UPDATE", "Export"]
    x.add_row(["1", "2", "3", "4", "5", "6", "7"])
    print(x)
    user_input = str(input(">> Enter Your Choice (b = back): "))
    if user_input.lower() == "1":
        test.add_new_pass()
    elif user_input.lower() == "2":
        test.add_old_pass()
    elif user_input.lower() == "3":
        test.search_pass()
    elif user_input.lower() == "4":
        test.show_pass()
    elif user_input.lower() == "5":
        test.delete_pass()
    elif user_input.lower() == "6":
        test.update_pass()
    elif user_input.lower() == "7":
        test.export_pass()
