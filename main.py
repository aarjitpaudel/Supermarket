from time import sleep
import sqlite3 as sq
mycon=sq.connect("Shop.db")
cursor=mycon.cursor()
cursor.execute('create table if not exists items(SNO integer primary key,PNAME char(20),PRICE Float,QUANTITY FLOAT)')
def add():
    print("Loading.....")
    sleep(1)
    print()
    print("Provide the details of the product")
    print()
    ans='y'
    while ans.lower()=='y':
        sno=int(input("Enter SNO of product: "))
        pname=input("Enter product name: ")
        price=float(input("Enter price: "))
        quantity=eval(input("Enter quantity: "))
        q="insert into items values({},'{}',{},{})".format(sno,pname,price,quantity)
        cursor.execute(q)
        mycon.commit()
        print("="*20)
        print('Record added successfully')
        print('='*20)
        ans=input("Do you want to add more elements(y/n): ")
        print()
	
	    
def update():
    print("..Loading..")
    sleep(2)
    global cursor
    global mycon
    ans="y"
    print()
    while ans.lower()=="y":
        print("Please provide the sno of the product you want to  update " )
        print()
        sleep(1)
        s=int(input("Enter the the sno of product which you want to update: "))
        cursor.execute("select *from items where sno={}".format(s))
        data=cursor.fetchall()
        count=cursor.rowcount
        if data!=[]:
            print("Enter what factor of the particular product you want to update")
            sleep(1)
            print("1.serial number\n2.Product name\n3.Price\n4.Quantity")
            sleep(2) 
            c=int(input("Enter the choice: ")) 
            done="N"
            if c==1:
                s1=int(input("Enter the new serial number: "))
                print()
                q1="Update items set sno={} where sno={}".format(s1,s)
                cursor.execute(q1)
                mycon.commit()
                done='S'
            elif c==2:
                p1=input("Enter new product name: ")
                q2="Update items set pname='{}' where sno={}".format(p1,s)
                cursor.execute(q2)
                mycon.commit()
                done='S'
            elif c==3:
                pr1=eval(input("Enter the new price of the product: "))
                q3="update items set price={} where sno={}".format(pr1,s)
                cursor.execute(q3)
                mycon.commit()
                done='S'
            elif c==4:
                qu1=eval(input("Enter new quantity of product: "))
                q4="Update items set quantity={} where sno={}".format(qu1,s)
                cursor.execute(q4)
                mycon.commit()
                done="S"
            else:
                print("Invalid choice\n Try again")            
            if done.upper()=='S':
                print("="*45)
                print("--Record updated successfully--")
                print("="*45)
                sleep(1)
            ans=input("Do you want to update more(y/n):")
        else:
            print()
            print('------No such record------')
            print()
            ans=input("Do you want to try again to update enter(y/n): ")
            print()
       
	
def delete():
    print()
    print("Loading...")
    sleep(1)
    print()
    ans='y'
    while ans.lower()=='y':
        print("Provide the serial number of the product you want to delete" )
        sn=int(input("Enter sno of product you want to delete: "))
        cursor.execute("select *from items where sno={}".format(sn))
        data=cursor.fetchall()
        count=cursor.rowcount
        if data!=[]:
            cursor.execute("delete from items where sno=:sn",{'sn':sn})
            mycon.commit()
            print('='*20)
            print("Record deleted successfully")
            print('='*20)
            ans=input("Do you want to delete more(y/n): ")
        else:
            print('='*20)
            print("No such record found")
            print('='*20)
            print("Try again")
            ans=input("Do you want to try again(y/n): ")
            
	
def search():
    print('..Loading..') 
    sleep(1) 
    global cursor
    global mycon
    ans='y'
    while ans.lower()=='y':
        print("Please give any one of the details of the product you want to search for")
        sleep(4)
        print("Enter the correct choice corresponding to the column heading which you know about the product you want to search")
        sleep(5.3)
        print("Enter choice which you know about the product\n1.serial number\n2.Product name\n3.Price\n4.Quantity")
        sleep(2) 
        cs=int(input("Enter the choice: ")) 
        done="N"
        cursor.execute('select * from items')
        if cs==1:
            s1=int(input("Enter the serial number of the product to search for: "))
            data=cursor.fetchall()
            for row in data:
                if row[0]==s1:
                    print()
                    print("#"*25)
                    print()
                    print(row[0],row[1],row[2],row[3])
                    print()
                    print("#"*25)
                    print()
                    sleep(1.2)
                    done="S"
                    break                             
        elif cs==2:
            p1=input("Enter product name of the product you want to search for: ")
            data1=cursor.fetchall()
            for row in data1:
                if row[1]==p1:
                    print()
                    print("#"*30)
                    print()
                    print("  ",row[0],row[1],row[2],row[3])
                    print()
                    print("#"*30)
                    print()
                    sleep(1.2)
                    done="S"
                    break       
        elif cs==3:
            pr1=eval(input("Enter price of the product that you want to search for: "))
            data2=cursor.fetchall()
            for row in data2:
                if row[2]==pr1:
                    print()
                    print("#"*30)
                    print()
                    print("  ",row[0],row[1],row[2],row[3])
                    print()
                    print("#"*30)
                    print()
                    sleep(1)
                    done="S"
                    break                                      
        elif cs==4:
            qu1=eval(input("Enter the quantity of the  product you want to search for: "))
            data3=cursor.fetchall()
            for row in data3:
                if row[3]==qu1:
                    print()
                    print("#"*30)
                    print()
                    print("  ",row[0],row[1],row[2],row[3])
                    print()
                    print("#"*30)
                    print()
                    sleep(1)
                    done="S"
                    break                               
        else:
            print("Invalid choice")  
            done="E"          
        if done.upper()=='S':
            print("...Search process completed ...")
            print("="*45)
            print("--Record found successfully--")
            print("="*45)
            sleep(1)
        elif done.upper()=='N':
            print("Search process failed")
            print(".."*19)
            print("No such record exist in table items")
            print("="*45) 
            sleep(1)
        elif done.upper()=="E":
            print("Please enter valid choice ,to search for an item based on the column headings")
            print('='*45)       
        ans=input("Do you want to search more(y/n): ")

	
def display():
    print()
    print("Loading....")
    sleep(1)
 
    cursor.execute("select * from items")
    data=cursor.fetchall()
    count=cursor.rowcount
    if data==[]:
        print('='*20)
        print("No records in the table")
        print('='*20)
    else: 
        print("="*20)
        print('Downloading the content..' )
        print("="*20)
        for i in data:
            print()
            print("   ",i[0]," ",i[1]," ",i[2]," ",i[3])
            sleep(1.5)
        sleep(2)
        print("-"*20)
        print("All content displayed")
        print("-"*20)
	
def bill():
    print('Loading......')
    sleep(1)
    print('Provide product name that you purchased and also the quantity of product from the shop  ')
    sleep(2)
    print()
    n=int(input('Enter the no of items you purchased: '))
    print()
    l=[]
    sum=0
    for i in range(n):
    	pn=input('Enter product name you purchased: ')
    	am=eval(input('Enter the amount you purchased: '))
    	print()
    	cursor.execute('select price from items where pname="{}"'.format(pn))
    
    	pr=cursor.fetchall()
    	if pr!=[]:
    		tot=pr[0][0]*am
    		sum+=tot
    		l.append([pn,am,tot])
    	else:
    		l.append(['-','-','-'])
    print()
    print('Bill is printing...')
    print()
    sleep(2)
    print('+','-'*38,'+')
    print(' SNO','%10s'%"PRODUCT",'%10s'%'QUANTITY','%10s'%'PRICE')
    print('+','-'*38,'+')
    for i in l:
    	s=1
    	print(' ',s,'%9s'%i[0],'%9s'%i[1],"%13s"%i[2])
    	s+=1
    print('-'*42)
    print(' TOTAL','%30s'%sum)
    print('-'*42)
    print()
    print(' '*11,'Pay Fast!')
    sleep(3)
    print()
print('-'*25)
print("%20s"%"AKM SUPERMARKET")
print('-'*25)
print("Welcome to shop database")
print()
while True:
    print('Enter choice')
    print()
    print('1.Add item\n2.Update item\n3.Delete item\n4.Search item\n5.Display full item\n6.Bill printing\n7.exit')
    print()
    ch=int(input("Enter your choice: "))
    if ch==1:
        add()
    elif ch==2:
        update()
    elif ch==3:
        delete()
    elif ch==4:
        search()
    elif ch==5:
        display() 
    elif ch==6:
    	bill()
    elif ch==7:
        break
    else:
        print("Entered invalid choice\n .TRY AGAIN")
        sleep(2)
name=input("Enter your name: ")
print()
print('.........................')
print("Thanks for visiting .")  
print('.........................')
print()

print(' ',name,' '*(25-len(name)),'A.K')
print('Name of user',' '*13,'CEO ,AKM')
