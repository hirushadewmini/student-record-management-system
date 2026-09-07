import os
from colorama import Fore,Back,Style
#function decralations
def main():
    while True:
        ans=menu()
        #print('ans=',ans)
        if ans=='1':
            insertarecord()
        if ans=='2':
            displayarecord()
        if ans=='3':
            displayallrecord()
        if ans=='4':
            updaterecords()
        if ans=='5':
            deleterecords()
        if ans=='6':
            if exit() in 'Yy':
                break
    print('Bye....')

def menu():
    os.system('cls')
    print('+----------------------+')
    print('|         MENU         |')
    print('+----------------------+')
    print('|1.Insert a record.    |')
    print('|2.Display a record.   |')
    print('|3.Dispaly all records.|')
    print('|4.Update records.     |')
    print('|5.Delete record.      |')
    print('|6.Exit.               |')
    print('+----------------------+')
    print(Fore.YELLOW+'Enter your choice:[123456]:'+Style.RESET_ALL,end="")
    return input()

def getcon_insert(a,b,c,d):
    import mysql.connector
    from mysql.connector import Error

    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='grade11',
            user='hirusha',
            password='hirusha1128'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            
            #Insert_query = "INSERT INTO grade10 VALUES ('1122','osada',200,102)"
            i_query=f"INSERT INTO student VALUES('{a}','{b}',{c},{d})"
            cursor.execute(i_query)
            connection.commit()

            if cursor.rowcount == 1:
                print(Fore.GREEN+"The record inserted successfully."+Fore.RESET)
            else:
                print(Fore.LIGHTRED+"Error in inserting the record..."+Fore.RESET)

    except Error as e:
        print("ERROR:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def insertarecord():
    #print('still under construction-insertarecord()')
    os.system('cls')
    st_index=getindex()
    #print('st_index',st_index)
    #pause
    ans1,ans2=wrong_in(st_index)
    if ans1==False:
        print('Enter Student Name\t\t:',end='')
        st_name=isname_correct()
        print('Enter Practical Marks\t:',end='')
        p_m=ismarks_correct()
        print('Enter Theory Marks\t:',end='')
        t_m=ismarks_correct()
        getcon_insert(st_index,st_name,p_m,t_m) 
    else:
        print(Fore.LIGHTRED_EX+"Index already exist"+Fore.RESET)
    pause()

def ismarks_correct():
    while True:
        try:
            marks=int(input())          
        except:
            print(Fore.LIGHTRED_EX+'Enter only digits from 0 to 100:'+Fore.RESET,end='')
            continue
        if 0<=marks<=100:
            return marks
            break
        else:
            print(Fore.LIGHTRED_EX+'The range should be between o and 100:'+Fore.RESET,end='')
            continue

def isname_correct():
    letters = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    " "]
    l1=[]
    while True:
        name=input()
        name_l=list(name)
        #print(name_l)
        for n in name_l:
            #print(n)
            for l in letters:
                #print(l)
                if n==l:
                    l1.append(n)
                continue
        #print(l1)
        if l1!=name_l:
            print(Fore.LIGHTRED_EX+'Enter a correct name:'+Fore.RESET,end='')
            l1.clear()
            continue
        else:
            return name
            break

def displayarecord():
    os.system('cls')
    index=getindex()
    ans1,ans2=wrong_in(index)
    if ans1:
        for row in ans2:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    else:
        print(Fore.LIGHTRED_EX+"SORRY! No such record in the database."+Fore.RESET)      
    pause()

def displayallrecord():
    os.system('cls')
    #print('still under construction-displayallrecord()')
    import mysql.connector
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="hirusha",
            password="hirusha1128",
            database="grade11"
        )
        cursor = con.cursor()
        cursor.execute("SELECT * FROM student")
        rows = cursor.fetchall()
        #print('Rows=',rows)
        for row in rows:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

    except Exception as e:
        print("ERROR:", e)

    finally:
        con.close()
    pause()

def getcon_update(a):
    import mysql.connector
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="hirusha",
            password="hirusha1128",
            database="grade11"
        )
        cursor = con.cursor()
        print('+----------------------------+')
        print('|          SUB MENU          |')
        print('+----------------------------+')
        print('|1.Update the Name           |')
        print('|2.Update the Practical Mark |')
        print('|3.Update the Theory Mark    |')
        print('+----------------------------+')
        print('Enter your choice:[123]:',end="")
        ans=input()
        if ans=='1':
            print('Enter the updated Name\t:',end='')
            u_value=isname_correct()
            u_query =f"UPDATE student SET st_name='{u_value}' WHERE st_index ='{a}'"
        if ans=='2':
            print('Enter the updated Practical Mark\t:',end='')
            u__value=ismarks_correct()
            u_query =f"UPDATE student SET p_m='{u_value}' WHERE st_index ='{a}'"
        if ans=='3':
            print('Enter the updated Theory Mark\t:',end='')
            u__value=ismarks_correct()
            u_query =f"UPDATE student SET t_m='{u_value}' WHERE st_index ='{a}'"
        ans=getanswer('Do you want to update[YyNn]:')
        if ans in 'Yy':
            cursor.execute(u_query)
            con.commit()

            if cursor.rowcount == 1:
                print(Fore.GREEN+"The record updated successfully."+Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX+"Error in updating the record..."+Fore.RESET)

    except Exception as e:
        print("ERROR:", e)
    
    finally:
        con.close()

def updaterecords():
    os.system('cls')
    #print('still under construction-updaterecords()')
    index=getindex()
    ans1,ans2=wrong_in(index)
    if ans1:
        getcon_update(index)
    else:
        print(Fore.LIGHTRED_EX+"SORRY! No such record in the database."+Fore.RESET)
    
    pause()

def getcon_delete(a):
    import mysql.connector
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="hirusha",
            password="hirusha1128",
            database="grade11"
        )
        cursor = con.cursor()
        #query = "DELETE FROM grade10 WHERE st_index = 'senaka'"
        dl_query=f"DELETE from student where st_index='{a}'"
        cursor.execute(dl_query)
        con.commit()  
        if cursor.rowcount == 1:
            print(Fore.GREEN+"The record deleted successfully."+Fore.RESET)
        else:
            print(Fore.LIGHTRED_EX+"Error in deleting the record..."+Fore.RESET)

    except Exception as e:
        print("ERROR:", e)
    
    finally:
        con.close()

def deleterecords():
    os.system('cls')
    #print('still under construction-deleterecords()')
    index=getindex()
    ans1,ans2=wrong_in(index)
    if ans1:
        ans=getanswer('Do you want to delete[YyNn]:')
        if ans in 'Yy':
            getcon_delete(index)
    else:
        print(Fore.LIGHTRED_EX+"SORRY! No such record in the database."+Fore.RESET)      
    pause()

def exit():
    return getanswer('Do you want to exit[YyNn]:')
    
def getanswer(args):
    print(args,end='')
    ans=''
    while True:
        ans=input()
        if ans not in 'YyNn':
            print(Fore.LIGHTRED_EX+"Wrong input,Enter[YyNn]:"+Fore.RESET,end='')
        else:
            break
    return ans

def getindex(): 
    index=None
    while True:
        index=input('Enter Index Number\t\t:')
        if len(index)!=4:
            print(Fore.LIGHTRED_EX+'Wrong length,only 4 digits'+Fore.RESET)
            continue
        try:
            int(index)
        except:
            print(Fore.LIGHTRED_EX+'Enter only digits'+Fore.RESET)
            continue
        if index=='0000':
            print(Fore.LIGHTRED_EX+'The range should be 0001 to 9999'+Fore.RESET)
            continue
        break
    return index    

def wrong_in(a):
    import mysql.connector
    rows=None
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="hirusha",
            password="hirusha1128",
            database="grade11"
        )
        cursor = con.cursor()
        d_query=f"SELECT * FROM student WHERE st_index='{a}'"
        cursor.execute(d_query)
        rows = cursor.fetchall() 
        
    except Exception as e:
        print("ERROR:", e)

    finally:
        con.close()
        #print("Database was closed")
    if not rows:
        return False,None
    else:
        return True,rows
        
def pause():
    input("Press 'Enter' to Continue.... ")


#calling the main programme
main()