#library management system
import datetime as dt
def home():
    a =1
    while a:
        print("Library Management System".center(120,'='))
        a = input('''Select a choice
1.Admin Signup
2.Student Signup
3.Admin Login
4.Student Login
0.Exit\n''')
        if a is '1':
            adminsign()
        elif a is '2':
            stdsign()
        elif a is '3':
            adminlog()
        elif a is '4':
            stdlogin()
        elif a is '0':
            print("Thank u for Using Library Management system".center(120,"="))
            quit()
        else:
            print("Enter a valid choice")
            home()

def adminsign():
    print("Admin Signin".center(50,'*'))
    b="%s,%s\n"%(input("Enter the new admin username: "),input("Enter the new admin password: "))
    c=0
    try:
        if b.split(",")[0].isspace():
            raise ValueError("Enter the Valid Username".center(120,"~"))
        elif len(b.split(",")[0].split(" "))>1:
            raise ValueError("Space is not allowed".center(120,"~")) 
        elif b.split(",")[0].isalnum()==False or len(b.split(",")[0])<5:
            raise ValueError("Enter the Username Only Containing Alphabet and Numeric Digits and mini lenght must be 5".center(120))
    except Exception as e:
        print(e)
    else:
        slist = open("d:/batch30/admin.txt").read().split("\n")
        for t in range(len(slist)-1):
            s = slist[t].split(",")
            if b.split(",")[0] ==s[0]:
                print("Users Already Exist".center(120,"="))
                c=1
        if c==0:
            open("d:/batch30/admin.txt","a").write(b)
            adminlog()
    
def adminlog():
    print("admin login".center(60,'*'))
    b="%s,%s\n"%(input("Enter the admin username: "),input("Enter the admin password: "))
    if b in  open("d:/batch30/admin.txt").read():
        print("You succesfully Logged in".center(120,"="))
        a =1
        while a:
            a = input('''\nSelect a choice
1.Add the Books
2.Update the quantity of Books
3.Show Library Avilable Books
4.Show Issued Books
5.Show The Details Of The Students Which Are Signined in Library Management System
0.For Logout\n''')
            if a is '1':
                addBooks()
            elif a is '2':
                updateBook()
            elif a is '3':
                showlbooks()
            elif a is '4':
                showibooks()
            elif a is '5':
                showdstudents()
            elif a is '0':
                print("Thank u for Your Work Admin".center(120,"="))
                a=0
            else:
                print("Enter a valid choice")
                
    else:
        print("Invalid Credentials")
        adminlog()

def stdsign():
    print("Student signup".center(120,'='))
    q = "%s %s"%(input("Enter the First name: "),input("Enter the Last Name: "))
    b="%s,%s,%s\n"%(q,input("Enter the rollno: "),input("Enter the new student password: "))
    c=0
    try:
        if b.split(",")[0].isspace()  or b.split(",")[1].isspace() :
            raise ValueError("Enter the Valid Credentials".center(120,"~"))
        elif q.split(" ")[0].isalpha()==False or q.split(" ")[1].isalpha()==False:
            raise ValueError("Only alphabets are allowed".center(120,"~"))
        elif b.split(",")[1].isdigit()==False or len(b.split(",")[1])<5:
            raise ValueError("Enter the Name Only Containing Alphabet and RollNO containing atleast 5 Numeric Digits".center(120))
    except Exception as e:
        print(e)
    else:
        slist = open("d:/batch30/student.txt").read().split("\n")
        for t in range(0,len(slist)-1):
            s = slist[t].split(",")
            if b.split(",")[1] ==s[1]:
                print("Users Already Exist".center(120,"="))
                c=1
        if c==0:
            open("d:/batch30/student.txt","a").write(b)
            stdlogin()
def stdlogin():
    print("Student login".center(120,'='))
    b="%s,%s,%s"%(input("Enter the name: "),input("Enter the Roll no: "),input("Enter the password: "))
    if b in open("d:/batch30/student.txt").read():
        print("You succesfully Logged in".center(120,"="))
        s = b.split(",")
        name = s[0]
        roll = s[1]
        a =1
        while a:
            a = input('''\nSelect a choice
1.List the Available Books in Library
2.Search And Place the order of Books
3.List the Issued Books On Your Id
4.Return the Book
0.For Logout\n''')
            if a is '1':
                listbook()
            elif a is '2':
                SearchBooks(name,roll)
            elif a is '3':
                listibook(name,roll)
            elif a is '4':
                returnBook(name,roll)
            elif a is '0':
                a=0
                print("thanks\n")
            else:
                print("Enter a valid choice")
    else:
        print("Invalid Credentials".center(120,"="))
        stdlogin()
            
def addBooks():
    s="%s,%s,%s,0\n"%(input("Enter the Book name: "),input("Enter the ISBN number: "),input("Enter the Quantity of book: "))
    slist = open("d:/batch30/addandupdate.txt").read().split("\n")
    num = int(s.split(",")[2])
    if num >0:
        for t in range(0,len(slist)-1):
            st = slist[t].split(",")
            if s.split(",")[0] ==st[0]:
                print("Book is already Exist")
                addBooks()
        else:
            open("d:/batch30/addandupdate.txt","a").write(s)
            print("Your Book is Suucesfully Added")
    else:
        print("Enter the valid quantity".center(120,"="))
        addBooks()

def updateBook():
    s="%s"%(input("Enter the Book name which u want to update: "))
    slist = open("d:/batch30/addandupdate.txt").read().split("\n")
    c=0
    for t in range(0,len(slist)-1):
        j = slist[t].split(",")
        if s ==j[0]:
            num = int(j[2])
            print("The present Quantity of The BOOK is ",num)
            try:
                number =int(input("Enter the quantity which u want to increase: "))
            except:
                print("Please Enter The Integer only".center(120,"="))
                c=1
            else:
                num = num+number
                k = j[0]+","+j[1]+","+str(num)+","+j[3]
                st = open("d:/batch30/addandupdate.txt").read().replace(slist[t],k)
                open("d:/batch30/addandupdate.txt","w").write(st)
                print("Your Book is Suucesfully updated and quantity is now ",num)
                c=1
                break
    if c==0:
        print("Book is Not found")
        

    

def showlbooks():
    st = open("d:/batch30/addandupdate.txt").readlines()
    print("Library Books".center(115,"="))
    print()
    print("{:13}||{:10}||{:10}||{:10}".format("Book_Name","ISBN NO","Quantity","No of times issue").center(120))
    print("{:15}{:12}{:12}{:10}".format("---------","-------","--------","-----------------").center(120))
    for i in st:
        t = i.split(",")
        print("{:15}{:12}{:12}{:10}".format(t[0][:10],t[1],t[2],t[3]).center(120))
    print("".center(120,"="))

def showibooks():
    st = open("d:/batch30/orderRecord.txt").readlines()
    print("Issued Books".center(115,"="))
    print()
    print("{:13}||{:10}||{:10}||{:10}".format("User_Name","ROLL NO","Book_Name","Issued Date").center(120))
    print("{:15}{:12}{:12}{:10}".format("---------","-------","---------","-----------").center(120))
    for i in st:
        t = i.split(",")
        print("{:15}{:12}{:12}{:10}".format(t[0],t[1],t[2][:10],t[3]).center(120))
    print("".center(120,"="))

def showdstudents():
    st = open("d:/batch30/student.txt").readlines()
    gt = open("d:/batch30/orderRecord.txt").readlines()
    print("Students Details".center(115,"="))
    print()
    print("{:13}||{:10}||{:10}".format("Name","ROLL NO","NO of Issued").center(120))
    print("{:15}{:12}{:12}".format("---------","-------","------------").center(120))
    for i in st:
        count =0
        g = i.split(",")
        s = "%s,%s"%(g[0],g[1])
        for j in gt:
            if s in j:
                count = count+1
        print("{:15}{:12}{:12}".format(g[0][:10],g[1],count).center(120))
    print("".center(120,"="))

def listbook():
    st = open("d:/batch30/addandupdate.txt").readlines()
    print("Avilable Books".center(115,"="))
    print("--------------".center(115))
    for i in st:
        s = i.split(",")
        n = int(s[2])-int(s[3])
        if n!=0:
            print(s[0].center(115))
    print("".center(120,"="))

def listibook(name,roll):
    st = open("d:/batch30/orderRecord.txt").readlines()
    s = "%s,%s"%(name,roll)
    count =0
    print(" Book_Name".center(115,"="))
    print("----------".center(115))
    for i in st:
        gt = i.split(",")
        if s in i:
            count = count+1
            print("%s"%(gt[2]).center(115))
    print("No of issued book on your account is {}".format(count).center(115))
    print("".center(120,"="))

def SearchBooks(name,roll):
    s=input("Enter the name of book which u want to search: ")
    slist = open("d:/batch30/addandupdate.txt").read().split("\n")
    c=0
    d=0
    for t in range(0,len(slist)-1):
        j = slist[t].split(",")
        if s ==j[0]:
            try:
                q = int(input("Press 1 If you want to Place The order: "))
            except:
                print("Enter a Valid Number".center(120,"="))
                c=1
            else:
                if q==1:
                    sli = open("d:/batch30/orderRecord.txt").read().split("\n")
                    p = "%s,%s,%s"%(name,roll,s)
                    for l in range(0,len(sli)-1):
                        if p in sli[l]:
                            print("You can't place this book,You Already Have this book".center(120,"="))
                            d=1
                    if d==0:
                        inum = int(j[3])
                        num = int(j[2])-inum
                        if num ==0:
                            print("OUT OF STOCK".center(120,"="))
                        else:
                            inum = inum+1
                            print("".center(120,"="))
                            print("Your Book Name is %s (ISBN no = %s)"%(j[0],j[1]))
                            curr_date = str(dt.date.today())
                            x = curr_date.split("-")
                            y = int(x[2])+1
                            z =dt.date(int(x[0]),int(x[1]),y)
                            ret_date= str(z)
                            print("Your Book Is Issued at the date %s"%(curr_date))
                            print("You Must return this book to Library on the date %s"%(ret_date))
                            k = j[0]+","+j[1]+","+j[2]+","+str(inum)+"\n"
                            st = open("d:/batch30/addandupdate.txt").read().replace(slist[t],k)
                            open("d:/batch30/addandupdate.txt","w").write(st)
                            s = "%s,%s,%s,%s\n"%(name,roll,j[0],curr_date)
                            open("d:/batch30/orderRecord.txt","a").write(s)
                            print("".center(120,"="))
                            c=1
                            break
                else:
                    print("Enter a valid number".center(120,"~"))
                    c=1
    if c==0 and d==0:
        print("Book is Not found".center(120,"="))


    
def returnBook(name,roll):
    s = "%s"%(input("Enter Your Book Name: "))
    try:
        num = 0
        glist = open("d:/batch30/orderRecord.txt").read().split("\n")
        for z in range(0,len(glist)-1):
            if "%s,%s,%s"%(name,roll,s) in glist[z]:
                j = glist[z].split(",")
                if j[2] == s:
                    m=open("d:/batch30/orderRecord.txt").read().index("%s,%s,%s"%(name,roll,s))
                    num=1
                    break
        if num ==0:
            raise ValueError("You Can't return this book because you didn't issued this book")
    except Exception as e:
        print(e)
    else:
        b = open("d:/batch30/orderRecord.txt")
        slist = open("d:/batch30/orderRecord.txt").read().split("\n")
        for t in range(len(slist)-1):
            if "%s,%s,%s"%(name,roll,s) in slist[t]:
                b.seek(m+t)
        ordstr ="%s"%(b.readline())
        b.close
        n = ordstr.split(",")
        issued = n[3]
        i=open("d:/batch30/addandupdate.txt").read().find(s)
        a=open("d:/batch30/addandupdate.txt")
        slist = open("d:/batch30/addandupdate.txt").read().split("\n")
        for t in range(len(slist)-1):
            if s in slist[t]:
                a.seek(i+t)
        string = "%s"%(a.readline())
        a.close
        j = string.split(",")
        inum = int(j[3])
        inum = inum-1
        k = j[0]+","+j[1]+","+j[2]+","+str(inum)+"\n"
        st = open("d:/batch30/addandupdate.txt").read().replace(string,k)
        open("d:/batch30/addandupdate.txt","w").write(st)
        print("Your Book Is succesfully returned")
        x = issued.split("-")
        y = int(x[2])+1
        w = dt.date.today()
        z = str(w)
        p = z.split("-")
        q = int(p[2])
        sdate = q-y
        if sdate<0:
            fine = 0
        else:
            fine  = sdate*100
        print("Your Fine Of the Book is Rs ",fine)
        sq = open("d:/batch30/orderRecord.txt").read().replace(ordstr,"")
        open("d:/batch30/orderRecord.txt","w").write(sq)      

if __name__=='__main__':
    home()
