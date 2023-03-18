# CURD Operation  C:Create, U:Update, R:Read, D:Delete
import os
z=1
while(True):
    print("\n 1. Add Record:")
    print("\n 2. Display All Record")
    print("\n 3. Search Student Record By Name")
    print("\n 4. Search Student Record By Rollno")
    print("\n 5. Delete Student Record By Name")
    print("\n 6. Update Student Record")
    print("\n 7. Exit")

    n=int(input("Enter your choice:"))
    if n==7:
        break
    elif n==1:
        print("\nEnter Student Details\n")
        name=input("Enter Name: ")
        r=input("Enter Rollno: ")
        cl=input("Enter Class: ")
        fees=input("Enter Fees: ")
        per=input("Enter Percentage: ")
        f=open("developers.txt","a")
        f.write(name+"-"+r+"-"+cl+"-"+fees+"-"+per+"\n")
        f.close()
    elif n==2:
        print("\n\n List of present records\n\n")
        print("NAME-ROLLNO-CLASS-FEES-PERCENTAGE")
        f=open("developers.txt","r")
        while(True):
            d=f.readline()
            l=len(d)
            if(l==0):
                break
            print(d.strip())
        f.close()
    elif n==3:
        search=input("Enter Student Name: ")
        f=open("developers.txt","r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if(g[0]==search):
                print("\n Record Found")
                print("Name is: ",g[0])
                print("Rollno is: ",g[1])
                print("Class is: ",g[2])
                print("Fees is: ",g[3])
                print("Percentage is: ",g[4])
                flag=1
                break
        if (flag==0):
           print("Record not found")
        f.close()
    elif n==4:
        search=input("Enter Student Rollno: ")
        f=open("developers.txt","r")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if(g[1]==search):
                print("\n Record Found")
                print("Name is: ",g[0])
                print("Rollno is: ",g[1])
                print("Class is: ",g[2])
                print("Fees is: ",g[3])
                print("Percentage is: ",g[4])
                flag=1
                break
        if (flag==0):
           print("Record not found")
        f.close()
    elif n==5:
        search = input("Enter Student Name : ")
        f = open("developers.txt","r")
        temp=open("temp.txt","w")
        h=0
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if (g[0]!=search):
                temp.write(t)
            if(g[0]==search):
                h=1
        f.close()
        temp.close()
        if(h==1):
            print("Record Deleted Successfully")
            os.remove("developers.txt")
            os.rename("temp.txt","developers.txt")
        elif h==0:
            print("Record Not Found!! Deletion Unsuccessful")
    elif n==6:
        h=0
        search=input("Enter Student Name: ")
        f=open("developers.txt","r")
        temp=open("temp.txt","w")
        flag=0
        while(True):
            t=f.readline()
            l=len(t)
            if(l==0):
                break
            g=t.split("-")
            if(g[0]=="search"):
                print("Current Deletion is\n",t)
                print("------------------------")
                newroll=input("Want to change rollno? Enter new detail or press enter to continue")
                newclass=input("Want to change class? Enter new detail or press enter to continue")
                newfees=input("Want to change fees? Enter new detail or press enter to continue")
                newper=input("Want to change percentage? Enter new detail or press enter to continue")
                if(len(newroll)==0):
                    newroll=g[1]
                if(len(newclass)==0):
                    newclass=g[2]
                if(len(newfees)==0):
                    newfees=g[3]
                if(len(newper)==0):
                    newper=g[4]
                temp.write("\n"+g[0]+"-"+newroll+"-"+newclass+"-"+newfees+"-"+newper)
                h=1
            else:
                temp.write(t)
        f.close()
        temp.close()
        if(h==1):
            print("Record Updated Successfully")
            os.remove("developers.txt")
            os.rename("temp.txt","developers.txt")
        elif(h==0):
            print("No Such Record Exist.For Updation Process")



        



