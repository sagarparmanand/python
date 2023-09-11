# main file
'''
fp = open("data.txt","w")
print(fp)
print(type(fp))
fp.close()
'''
#write data in file                               .write()
'''
fp = open("data.txt","w")
#d="good morning buddy"
d="good boy"
fp.write(d)
fp.close()
'''
#write data                                 mod = a
'''
fp = open("data.txt","a")
name = input("enter your name: ")
mob = input("enter your mobile number:")
d=name+":"+mob+"\n"
fp.write(d)
fp.close()
'''

#                             CRUD  Project

def searchByName():
    n=input("enter name: ")
    fp=open("data.txt","r")
    data=fp.readlines()
    for x in data:
        s=x.split(":")
        if n==s[0]:
            print("found ",x)
            break
        
    else:
        print("name not found")
        
    fp.close()

def searchByNumber():
    mob=input("enter mobile number: ")
    fp=open("data.txt","r")
    data=fp.readlines()
    #print(data)
    for x in data:
        s=x.split(':')
        #print(s)
        if mob+"\n"==s[1]:
            print("No. ==",x)
            break
    else:
        print("not found")
    fp.close()

def update_contact():
    print("1. for mobile number update: ")
    print("2. for name update: ")
    ch=input("enter your choice: ")
    if ch=="1":
        mob=input("enter mobile number: ")
        fp=open("data.txt","r")
        data=fp.readlines()
        for x in data:
            s=x.split(":")
            if mob+"\n"==s[1]:
                newmob=input("enter new mobile number: ")
                s[1]=newmob+"\n"
                data.remove(x)
                temp=":".join(s)
                data.append(temp)
                fdata="".join(data)
                fp1=open("data.txt","w")
                fp1.write(fdata)
                fp1.close()
                print("Record updated successfully")
        fp.close()     
    elif ch=="2":
        nam=input("enter name: ")
        fp=open("data.txt","r")
        data=fp.readlines()
        for x in data:
            s=x.split(':')
            if s[0]==nam:
                newName=input("enter  new name: ")
                s[0]=newName
                data.remove(x)
                temp=":".join(s)
                data.append(temp)
                fdata="".join(data)
                fp1=open("data.txt","w")
                fp1.write(fdata)
                fp1.close()
                print("Record updated successfully")
                
    else:
        print("please enter valid choice")

def delete_contact():
        mob=input("enter mobile number to delete: ")
        fp=open("data.txt","r")
        data=fp.readlines()
        for x in data:
            s=x.split(":")
            if mob+"\n"==s[1]:
                data.remove(x)
                fp1=open("data.txt","w")
                newdata="".join(data)
                fp1.write(newdata)
                print("deleted")
                fp.close()
                break
        else:
            print("number not found")
        fp.close()
while True:
    print()
    print("1.Add Contact")
    print("2.View Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search by name")
    print("6.Search by mobile number")
    print("7.Exit")
    ch = input("enter your choice: ")

    if ch=="1":
        fp=open("data.txt","a");
        n=input("enter your name: ")
        mob=input("enter your mobile number: ")
        d=n+":"+mob+"\n"
        fp.write(d)
        fp.close()
    elif ch=="2":
        fp=open("data.txt","r")
        view = fp.read()
        print("----------------------------------------------")
        print(view)
        print("----------------------------------------------")
    elif ch=="3":
        update_contact()
    elif ch=="4":
        delete_contact()
    elif ch=="5":
        searchByName()
    elif ch=="6":
        searchByNumber()
        
    elif ch=="7":
        print("thank you for using our application!!!")
        break
    else:
        print("please enter valid number!!")
    



















