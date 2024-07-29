"""
MCQ TEST CREATION SOFTWARE
STUDENT NAME: RUPESH SINGH
CLASS: 12 
SECTION: A
ROLL NO. : 12125
"""
#MCQ TEST GENERATOR

import os.path
#above library to check existence of file
def checker():                #checks whether the user is a student or teacher
    print("WHO ARE YOU:")
    print("1.TEACHER")
    print("2.STUDENT")
    interface=input("ENTER 1 OR 2 : ")
    if(interface=='1'):
        teacher()
    elif(interface=='2'):
            student()
    else:
        print("!INVALID INPUT! \n PLEASE RE-ENTER \n  ENTER ONLY 1 OR 2 \n")
        checker()

def linereader(file):                   #to read file
    read=file.readlines()
    print("""FORMAT IS \n 
          QNO,QUESTION,OPTION A,OPTION B,OPTION C,OPTION D,CORRECT,MARKS""")
    for line in read:
        c=line.split("~")
        print(c)

def qdeletor(name,qno):                         #To delete a question
        a=open(name,"r+")
        b=a.readlines()
        a.close()
        print("FORMAT \n questionumber,question,A,B,C,D,CORRECT,MARKS")
        l=len(b)
        for i in range(0,l,1):
            d=b[i]
            c=d.split("~")
            if(c[0]==qno):
                b[i]=""
                break
            else:
                continue
        new=open(name,"w+")
        for line in b:
            if(len(line)==0 or len(line)==1):
                continue
            else:
                new.write(line)
                new.write("\n")
        new.close()

def qeditor(name):                  #function to edit a question
    file=open(name,"r") 
    s=file.readlines()
    file.close()
    for i in s:
        print(i)
    qno=input("ENTER QUESTION NUMBER WHICH YOU WANT TO EDIT: ")
    q=input("ENTER QUESTION: ")
    optiona=input("ENTER OPTION A: ")
    optionb=input("ENTER OPTION B: ")
    optionc=input("ENTER OPTION C: ")
    optiond=input("ENTER OPTION D: ")
    correct=input("ENTER CORRECT OPTION A/B/C/D:")
    mark=input("ENTER MARKS FOR CORRECT ANSWER: ")
    line=qno+"~"+q+"~"+optiona+"~"+optionb+"~"+optionc+"~"+optiond+"~"+correct+"~"+mark
    h=""
    for i in s:
        c=i.split("~")
        if(c[0]==str(qno)):
            j=line+"\n"
            h=h+j
        else:
            h=h+i
    file=open(name,"w")
    file.write(h)
    file.close()
    print("QUESTION EDIT SUCCESSFUL")
    m=input("WANT TO EDIT MORE QUESTION(Y/N): ")
    if(m=="Y" or m=="y"):
        qeditor(name)
    else:
        print("THANK YOU")

def timediff(starthour,startminute):                #to calculate how many minutes completed
    from datetime import datetime
    x=datetime.now().time()
    hour=int((str(x)[0:2]))
    min=int((str(x))[3:5])
    if(starthour==hour):
        print(min-startminute,"MINUTES COMPLETED.")
        return min-startminute
    elif(hour>starthour):
        print((60-startminute)+min+(60*((hour-starthour)-1)),"MINUTES COMPLETED.")
        z=(60-startminute)+min+(60*((hour-starthour)-1))
        return z

def qdisplay(mcqname):                  #DISPLAYS QUESTIONS TO THE STUDENT
    from datetime import datetime
    import time                      
    file=open(mcqname,"r")
    s=file.readlines()
    file.close()
    a=datetime.now().time()
    b=str(a)
    starthour=int(b[0:2])
    startminute=int(b[3:5])
    points=0
    print("CURRENT TIME IS",starthour,"HOURS AND",startminute,"MINUTES.\n \n")
    time.sleep(1)
    print("TEST STARTS NOW")
    for i in s:
        y=i.split("~")
        if(len(y)==0):
            continue
        else:
            print("QUESTION: ",y[1],"\n")
            print("OPTION A:",y[2])
            print("OPTION B:",y[3])
            print("OPTION C",y[4])
            print("OPTION D:",y[5])
            answer=input("ENTER ONLY OPTION IN CAPITAL LETTER: ")
            if(answer not in ["A","B","C","D","a","b","c","d"]):
                print("CHOOSE CORRECT OPTION,RETRY ONE MORE TIME.")
                answer=input("ENTER ONLY OPTION: ")
                if(answer==y[6] or answer==y[6].upper()):
                    points=points+int(y[7])
                    timediff(starthour, startminute)
                else:
                    timediff(starthour,startminute)
                    continue
            else:
                if(answer==y[6]):
                    points=points+int(y[7])
                else:
                    continue
            if(timediff(starthour,startminute)>len(s)):
                print("TIME IS OVER.")
                print("TEST OVER.THANK YOU STUDENT.")
                break
            else:
                continue
    print("DISPLAYING YOUR MARKS IN:")
    for i in range(5,0,-1):
        print(i,end=" ")
        time.sleep(1)
    print("YOUR MARKS IS",points)
    return points
            

def refiner(name):                  #rearrange questions so as to remover whitespaces and empty line
    r=open(name,"r")
    s=r.readlines()
    r.close()
    l=len(s)
    t=open(name,"w+")
    for i in range(0,l,1):
        s[i]=s[i].lstrip()
        s[i]=s[i].rstrip()        
        if(len(s[i])==1 or len(s[i])==0):
            continue
        else:
            t.write(s[i])
            t.write("\n")
    t.close()



            
def teacher():                                          #starts teacher interface 
    print("WELCOME TO MCQ TEST GENERATOR")
    tname=input("DEAR TEACHER, PLEASE ENTER YOUR NAME:")
    subname=input("ENTER THE NAME OF SUBJECT: ")
    task=input(""""ENTER THE TASK,CHOOSE FROM BELOW: \n 
               1.CREATE A NEW MCQ TEST \n 
               2.EDIT AN MCQ TEST \n 
               3.SHOW MARKS OF STUDENTS \n
               4.EXIT
               ENTER ONLY THE RESPECTIVE NUMBER: \n""")
    def questionmaker(file):                    #function to add a new question
                    qno=input("ENTER QUESTION NUMBER")
                    q=input("ENTER QUESTION: ")
                    optiona=input("ENTER OPTION A: ")
                    optionb=input("ENTER OPTION B: ")
                    optionc=input("ENTER OPTION C: ")
                    optiond=input("ENTER OPTION D: ")
                    correct=input("ENTER CORRECT OPTION A/B/C/D:")
                    mark=input("ENTER MARKS FOR CORRECT ANSWER: ")
                    line=qno+"~"+q+"~"+optiona+"~"+optionb+"~"+optionc+"~"+optiond+"~"+correct+"~"+mark
                    file.write(line)
                    file.write('\n')
                    a=input("WANT TO ENTER MORE QUESTIONS(Y/N): ")
                    if(a=="y" or a=="Y"):
                        questionmaker(file)
                    else:
                        file.close()
                        print("YOUR MCQ HAS BEEN SAVED")
    if(task=='1'):
        def new():          #function to create a new mcq file
            name=input("ENTER THE NAME OF MCQ TEST: ")
            filename=name+"_"+tname+"_"+subname+".txt"
            if os.path.exists(filename)==True:          #so that previous file is not deleted
                print("MCQ WITH THE SAME NAME ALREADY EXISTS \n PLEASE USE ANOTHER NAME")
                new()
            else:
                print("THE NEW MCQ FILE IS CREATED WITH NAME:",filename)
                file=open(filename,"w+")
                questionmaker(file)                         #adds a new question
            rep=input("WANT TO CREATE ANOTHER MCQ TEST? : Y/N")
            if(rep=="Y" or rep=="y"):
                new()
        new()                                           #creates a new mcq file
    elif(task=='2'):            #edit an existing mcq file
        def edit():
            name=input("ENTER THE FULL NAME OF MCQ TEST WHICH YOU WANT TO EDIT WITH .txt EXTENSION: ")
            if os.path.exists(name)==False:
                print("THIS FILE DOES NOT EXIST, PLEASE RE-ENTER THE FILE NAME:")
                edit()
            else:
                choose=input("""SELECT THE TASK: \n 
                             1.EDIT A QUESTION \n 
                             2.ADD MORE QUESTIONS \n 
                             3.DELETE A QUESTION \n   
                             ENTER ONLY 1 OR 2: \n""")
                if(choose=="1"):                    #edit a question
                    qeditor(name)
                elif(choose=="2"):              #add more questions 
                    file=open(name,"a+")
                    questionmaker(file)
                elif(choose=="3"):              #deletes a question
                    file=open(name,"r+")
                    linereader(file)
                    delno=input("ENTER THE QUESTION NUMBER YOU WANT TO DELETE: ")
                    qdeletor(name, delno)
                    print("DELETED.")
                    m=input("WANT TO EDIT MORE QUESTION(Y/N): ")
                    if(m=="Y" or m=="y"):
                        qeditor()
                    else:
                        print("THANK YOU")
            refiner(name)                        
        edit()
    elif(task=="3"):
        stumark=open("studentmarks.csv","r")
        r=stumark.readlines()
        for line in r:
            o=line.split(",")
            print("STUDENT NAME: ",o[0])
            print("CLASS: ",o[1])
            print("SECTION: ",o[2])
            print("ROLL NO.: ",o[3])
            print("MCQ NAME:",o[4])
            print("MARKS:",o[5])
    elif(task=="4"):
        print("THANK YOU")
    else:
        print("! INVALID INPUT !\n   RE-ENTER CORRECT NUMBER")
        teacher()
    ask=input("WANT TO GO TO MAIN MENU? : (Y/N)")
    if(ask=="Y" or ask=="y"):
        teacher()
    else:
        print("THANK YOU")
        
        
def student():                      #starts student interface
    print("WELCOME STUDENT")
    sname=input("DEAR STUDENT,ENTER YOUR NAME: ")
    sclass=input("ENTER YOUR CLASS IN DIGITS: ")
    ssec=input("ENTER SECTION IN CAPITAL LETTERS: ")
    sroll=input("ENTER YOUR ROLL NUMBER IN DIGITS: ")
    mcqname=input("ENTER FULL FILE NAME OF THE MCQ TEST YOU WANT TO GIVE WITH .txt EXTENSION: ")
    if os.path.exists(mcqname)==False:
        print("MCQ FILE WITH NAME",mcqname,"DOES NOT EXISTS \n ENTER ANOTHER NAME")
        student()
    else:
        import time
        file=open(mcqname,"r")
        s=file.readlines()
        file.close()
        print("\n GENERAL INSTRUCTIONS FOR THE TEST \n")
        time.sleep(1)
        print("1.THE PAPER CONSIST OF",len(s),"QUESTIONS \n")
        time.sleep(1)
        print("2.YOU HAVE",len(s),"MINUTES TO COMPLETE THIS TEST.\n")
        time.sleep(1)   
        print("3.ONE MARKS WILL BE DEDUCTED FOR EACH EXTRA MINUTE TAKEN TO COMPLETE THIS TEST.\n")
        time.sleep(1)
        print("4.CHECK THE TIME THROUGH THE SYSYEM CLOCK.\n")
        time.sleep(1)
        print("5.NO NEGATIVE MARKING.\n")
        time.sleep(1)
        print("6.OPTION ONCE CHOSEN WILL NOT BE CHANGED,BE CAREFUL.\n")
        time.sleep(1)
        print("7.BEST OF LUCK FOR THE TEST.\n")
        time.sleep(1)
        ready=input(""""ARE YOU READY FOR THE TEST(Y/N)\n  
                    YOUR TIME START AS SOON AS YOU ENTER Y : """)
        if(ready=="Y" or ready=="y"):            
            print("YOUR TEST STARTS IN:")
            for i in range(5,0,-1):
                print(i,end=" ")
                time.sleep(1)
            print("0")
            time.sleep(1)
        marks=qdisplay(mcqname)
        stufile=open("studentmarks.csv","a")
        p=str(sname+","+sclass+","+ssec+","+sroll+","+mcqname+","+str(marks))
        stufile.write(p)
        stufile.write("\n")
        print("YOUR MARKS IS SAVED")
        
checker()                              #STARTS THE PROGRAM     