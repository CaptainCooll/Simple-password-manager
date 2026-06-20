import pickle as p
import random as r
def gen():
    al='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#'
    y=''
    x=int(input("Enter number of characters (between 8 and 128): "))
    if x>=8 and x<=128:
        for i in range(x):
            y+=al[r.randint(0,len(al)-1)]
        return y
    else:
        print("Password must be at least 8 characters and less than 128 characters")
        gen()
accounts={}
f=open("accounts.dat",'ab')
f.close()
def login():
    x=input("\nEnter username: ")
    y=search(x)
    if y:
        pword=int(input("\nEnter 4 digit PIN: "))
        while y['pword']!=pword:
            print("Incorrect Pin, please try again")
            pword=int(input("\nEnter 4 digit PIN: "))
        else:
            print("\nSuccesfully logged in")
            global user
            user=y['user']+'.dat'
            return True
    else:
        print("\nUser not found, try creating account instead")
        return False
def search(x):
    file=open("accounts.dat",'rb')
    found=0
    try:
        while True:
            data=p.load(file)
            if data['user']==x:
                found=data
                break
    except EOFError:
        file.close()
    if found==0:
        return False
    else:
        return found
def new():
    acc=open("accounts.dat",'ab+')
    user=input("Enter your username: ")
    if search(user):
        print("Account already exists, try logging in instead")
    else:
        p1=int(input("Enter 4 digit PIN: "))
        p2=int(input("Confirm 4 digit PIN: "))
        while p1!=p2:
            print("PIN does not match, please try again")
            p2=int(input("Confirm 4 digit PIN: "))
        else:
            print("Your account with username {} has been created".format(user))
            accounts['user']=user
            accounts['pword']=p1
            p.dump(accounts,acc)
d={}
def view():
    f=open(user,'rb')
    try:
        while True:
            d=p.load(f)
            print("\nWebsite: ",d['site'],"\nUsername: ",d['user'],"\nPassword: ",d['pword'],"\n")
    except EOFError:
        f.close()    
def serch(x):
    f=open(user,'rb')
    try:
        while True:
            l=f.tell()
            o=p.load(f)
            if o['site']==x:
                ret=(True,o,l)
                break
    except EOFError:
        ret=(False,"RECORD NOT FOUND")
    f.close()
    return ret
def add():
    j=input("Enter name of website: ")
    y=serch(j)[0]
    if y:
        print("You have already saved a password for this website.")
    else:
        f=open(user,'ab')
        d['site']=j
        d['user']=input("Enter username: ")
        ch=input("Enter 1 to generate a password, any other number to skip ")
        if ch.isdigit() and int(ch)==1:
            x=gen()
            print("Your password is",x)
            d['pword']=x
        else:
            d['pword']=input("Enter password: ")
        p.dump(d,f)
        f.close()
def delete():
    x=input("Enter the website name for the password you want to delete: ")
    f=open(user, 'rb')
    records=[]
    try:
        while True:
            record=p.load(f)
            records.append(record)
    except EOFError:
        f.close()
    for record in records:
        if record['site']==x:
            records.remove(record)
            print("Password for '{x}' has been deleted.")
            break
    else:
        print("No record found for '{x}'.")
    f=open(user, 'wb')
    for record in records:
        p.dump(record, f)
    f.close()
def update():
    x=input("Enter the site for which you want to update credentials: ")
    f=open(user,'rb+')
    records=[]
    try:
        while True:
            record=p.load(f)
            records.append(record)
    except EOFError:
        pass
    finally:
        f.close()
    for index,record in enumerate(records):
        if record['site']==x:
            print("Current details:")
            print("Website: {record['site']}")
            print("Username: {record['user']}")
            print("Password: {record['pword']}")
            print("What do you want to update?")
            print("1. Username")
            print("2. Password")
            print("3. Both")
            choice=input("Enter your choice: ")
            if choice.isdigit():
                choice=int(choice)
                if choice==1:
                    new_username=input("Enter new username: ")
                    records[index]['user']=new_username
                    print("Username updated successfully.")
                elif choice==2:
                    new_password=input("Enter new password: ")
                    records[index]['pword']=new_password
                    print("Password updated successfully.")
                elif choice==3:
                    new_username=input("Enter new username: ")
                    new_password=input("Enter new password: ")
                    records[index]['user']=new_username
                    records[index]['pword']=new_password
                    print("Username and password updated successfully.")
                else:
                    print("Invalid choice, no updates made.")
            else:
                print("Invalid choice, no updates made.")
            break
    else:
        print("No record found for the specified site.")
    f=open(user,'wb')
    for record in records:
        p.dump(record,f)
    f.close()
def pword():
    f=open(user,'ab')
    f.close()
    while True:
        print("Menu")
        print("1.View passwords")
        print("2.Search")
        print("3.Add password")
        print("4.Update password")
        print("5.Delete password")
        print("6.Generate a password")
        print("7.Logout")
        ch=input("Enter choice: ")
        if ch.isdigit():
            ch=int(ch)
            if ch==1:
                view()
            elif ch==2:
                x=serch(input("Enter site to search: "))
                if x[0]:
                    print("\nWebsite: {}\nUsername: {}\nPassword: {}".format(x[1]['site'],x[1]['user'],x[1]['pword']))
                else:
                    print(x[1])
            elif ch==3:
                add()
            elif ch==4:
                update()
            elif ch==5:
                delete()
            elif ch==7:
                print("Successfully logged out")
                break
            elif ch==6:
                print("Password generated is",gen())
            else:
                print("Invalid choice, try again")
        else:
            print("Invalid choice, try again")
def main():
    while True:
        print("1. Create account to manage passwords")
        print("2. Login to account")
        print("3. Generate a password")
        print("4. Exit")
        ch=input("Enter action: ")
        if ch.isdigit():
            ch=int(ch)
            if ch==1:
                new()
            elif ch==2:
                if login():
                    pword()
            elif ch==3:
                print("Password generated is",gen())
            elif ch==4:
                print("Exiting")
                break
            else:
                print("Invalid choice, try again")
        else:
            print("Invalid choice, try again")
main()

