from  classes import *
import pickle
                
# Function to add a book into the pickle file (Book_data).
def addBook():                          
    l=[]
    b_name=input("Enter name of the book: ")
    quantity=int(input("Number of copies: "))
    isbn=int(input("Enter ISBN number: "))
    with open("Book_data.pkl",'rb') as f:
        l=pickle.load(f)
    with open("Book_data.pkl",'wb') as f:
        s=Book_details(b_name,quantity,isbn)
        l.append(s)
        pickle.dump(l,f)

# Function to display all the books from Book_data.pkl.
def showBook():
    with open("Book_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            i.display()

# Function to add a student into the pickle file (student_data.pkl).
def addStudent():
    student_name=input("Enter student name: ")
    student_year=(input("Enter year of admission: 20"))
    student_id=(input("Student id number: "))
    student_branch=int(input("Select one-\n1.CSE\n2.EC\n3.EX\n4.ME\n5.CE\n"))
    if student_branch==1:
        roll_no='0187'+'CS'+student_year+'1'+student_id
    if student_branch==2:
        roll_no='0187'+'EC'+student_year+'1'+student_id
    if student_branch==3:
        roll_no='0187'+'EX'+student_year+'1'+student_id
    if student_branch==4:
        roll_no='0187'+'ME'+student_year+'1'+student_id
    if student_branch==5:
        roll_no='0187'+'CE'+student_year+'1'+student_id
    with open("student_data.pkl",'rb') as f1:
        l1=pickle.load(f1)
        for i in l1:
            if i.roll_no==roll_no:
                print("Student already exists")
                return 
        else:
            with open("student_data.pkl",'wb') as f:
                s=Student(student_name,student_year,student_id,student_branch,roll_no)
                l1.append(s)
                pickle.dump(l1,f)
                   
# Function to display all the students from student_data.pkl.
def showStudents():
    with open("student_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            i.display()
    
# Function to add a faculty into the pickle file (faculty_data.pkl).        
def addFaculty():
    fname=input("Enter Faculty name: ")
    fid=int(input("Enter Faculty Id: "))
    with open("faculty_data.pkl",'rb') as f1:
        l1 = pickle.load(f1)
        for i in l1:
            if i.fid==fid:
                print("Faculty already exists")
        else:
            with open("faculty_data.pkl",'wb') as f:
                fobj=Faculty(fname,fid)
                l1.append(fobj)
                pickle.dump(l1,f)
                
# Function to display all the faculties from faculty_data.pkl.                
def showFaculties():
    with open("faculty_data.pkl",'rb') as f:
        obj=pickle.load(f)
        #obj.display()
        for i in obj:
            i.display()

# Function to issue a book (Student).
def Book_issue_S(issued_books,issued_rolls):
    s_roll=input("Enter enrollment number: ")
    with open("student_data.pkl",'rb') as f1:
        l1 = pickle.load(f1)
        for i in l1:
            if i.roll_no==s_roll:
                showBook()
                isb=int(input("Enter ISBN of required book: "))
                with open("Book_data.pkl",'rb') as f:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.isbn==isb:
                            if i.quantity==0:
                                print("Copies exhausted")                         
                            issued_books.append(isb)
                            issued_rolls.append(s_roll)
                            i.quantity-=1
                            with open("Book_data.pkl",'wb') as f:
                                    pickle.dump(obj,f)
                break
        else:
            print("Student doesn't exist")

# Function to issue a book (Faculty).
def Book_issue_F(issued_fbooks,issued_fid):
    f_id=int(input("Enter Employee ID: "))
    with open("faculty_data.pkl",'rb') as f1:
        l1 = pickle.load(f1)
        for i in l1:
            if i.fid==f_id:
                showBook()
                isb=int(input("Enter ISBN of required book: "))
                with open("Book_data.pkl",'rb') as f:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.isbn==isb:
                            if i.quantity==0:
                                print("Copies exhausted")
                            issued_fbooks.append(i.isbn)
                            issued_fid.append(f_id)
                            i.quantity-=1
                            with open("Book_data.pkl",'wb') as f:
                                    pickle.dump(obj,f)
                break
        else:
            print("Faculty doesn't exist")        

#Function to return a book (Student).
def return_book_S(issued_books,issued_rolls):
    s_roll=input("Enter enrollment number: ")
    with open("student_data.pkl",'rb') as f1:
        l1 = pickle.load(f1)
        for i in l1:
            if i.roll_no==s_roll:
                showBook()
                isb=int(input("Enter ISBN of book to be returned: "))
                for i in issued_books:
                    for j in issued_rolls:
                        if i==isb and j==s_roll:
                            issued_books.remove(i)
                            issued_rolls.remove(j)
                            with open("Book_data.pkl",'rb') as f:
                                obj=pickle.load(f)
                                for z in obj:
                                    if z.isbn==isb:
                                        z.quantity+=1
                                    with open("Book_data.pkl",'wb') as f:
                                        pickle.dump(obj,f)    
                break
        else:
            print("Student doesn't exist")

# Function to return a book (Faculty).
def return_book_F(issued_fbooks,issued_fid):
    eid=int(input("Enter Employee ID: "))
    with open("faculty_data.pkl",'rb') as f1:
        l1 = pickle.load(f1)
        for i in l1:
            if i.fid==eid:
                showBook()
                isb=int(input("Enter ISBN of book to be returned: "))
                for i in issued_fbooks:
                    for j in issued_fid:
                        if i==isb and j==eid:
                            issued_fbooks.remove(i)
                            issued_fid.remove(j)
                            with open("Book_data.pkl",'rb') as f:
                                obj=pickle.load(f)
                                for z in obj:
                                    if z.isbn==isb:
                                        z.quantity+=1
                                    with open("Book_data.pkl",'wb') as f:
                                        pickle.dump(obj,f)    
                break
        else:
            print("Faculty doesn't exist")
    
# Function to display number of books issued by a particular student. 
def display_records_S(issued_books,issued_rolls):
    s_roll=input("Enter roll no.: ")
    with open("student_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.roll_no==s_roll:
                i.display()
                for z in range(0,len(issued_books)):
                    for j in range(0,len(issued_rolls)):
                        if issued_rolls[j]==s_roll:
                            z=j
                            print(f"Book Issued (ISBN): {issued_books[z]}")
                    break
                break
        else:
            print("Not Found")

# Function to display number of books issued by a particular faculty.
def display_records_F(issued_fbooks,issued_fid):
    eid=int(input("Enter Emlpoyee ID: "))
    with open("faculty_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.fid==eid:
                i.display()
                for z in range(0,len(issued_fbooks)):
                    for j in range(0,len(issued_fid)):
                        if issued_fid[j]==eid:
                            z=j
                            print(f"Book Issued (ISBN): {issued_fbooks[z]}")
                    break
                break
        else:
            print("Not Found")

# Function to search a paricular student from student_data.pkl.
def search_S():
    s_roll=input("Enter roll no.: ")
    with open("student_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.roll_no==s_roll:
                print("Student Found")
                i.display()
                break
        else:
            print("Student not Found")
            
# Function to search a paricular faculty from faculty_data.pkl.
def search_F():
    eid=int(input("Enter Faculty ID: "))
    with open("faculty_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.fid==eid:
                print("Faculty Found")
                i.display()
                break
        else:
            print("Faculty not Found")

# Function to search a paricular book from Book_data.pkl.
def search_B():
    isb=int(input("Enter Book ISBN: "))
    with open("Book_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.isbn==isb:
                print("Book Found")
                i.display()
                break
        else:
            print("Book not Found")
            
# Function to remove a paricular student from student_data.pkl.
def remove_S():
    s_roll=input("Enter roll no.: ")
    with open("student_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.roll_no==s_roll:
                obj.remove(i)
                print("Student removed")
                i.display()
                with open("student_data.pkl",'wb') as f:
                    pickle.dump(obj,f)  
                break
        else:
            print("Student not Found")
            
# Function to remove a paricular faculty from faculty_data.pkl.            
def remove_F():
    eid=int(input("Enter Employee ID: "))
    with open("faculty_data.pkl",'rb') as f:
        obj=pickle.load(f)
        for i in obj:
            if i.fid==eid:
                obj.remove(i)
                print("Faculty removed")
                i.display()
                with open("faculty_data.pkl",'wb') as f:
                    pickle.dump(obj,f)  
                break
        else:
            print("Faculty not Found")