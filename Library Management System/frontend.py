from methods import *
import getpass
import sys

def main():
    done=False
    while done==False:
        print(""" ======LIBRARY MANAGEMENT SYSTEM=======
                  1. ADMIN
                  2. FACULTY
                  3. STUDENT
                  4. Exit
                  """)
        ch=int(input("Enter choice: "))
        if ch==1:
            print("Enter Password:")
            p = getpass.getpass()
            if p == '123':
                print('Welcome User\n')
                choice=int(input("""Select any one: 
1. Add Student
2. Display all Students
3. Add Faculty
4. Display all Faculties
5. Add Book
6. Show all Books
7. Remove Student
8. Remove Faculty
9. Search Student 
10. Search Faculty
11. Search Book
12. Issue Book Student
13. Issue Book Faculty
14. Return Book Student
15. Return Book Faculty
16. Display Student Records
17. Display Faculty Records
18. EXIT
**************************
**************************
"""))
                if choice==1:
                    addStudent()
                elif choice==2:
                    showStudents()
                elif choice==3:
                    addFaculty()
                elif choice==4:
                    showFaculties()
                elif choice==5:
                    addBook()
                elif choice==6:
                    showBook()
                elif choice==7:
                    remove_S()
                elif choice==8:
                    remove_F()
                elif choice==9:
                    search_S()
                elif choice==10:
                    search_F()
                elif choice==11:
                    search_B()
                elif choice==12:
                    Book_issue_S(issued_books,issued_rolls)
                elif choice==13:
                    Book_issue_F(issued_fbooks,issued_fid)
                elif choice==14:
                    return_book_S(issued_books,issued_rolls)
                elif choice==15:
                    return_book_F(issued_fbooks,issued_fid)
                elif choice==16:
                    display_records_S(issued_books,issued_rolls)
                elif choice==17:
                    display_records_F(issued_fbooks,issued_fid)
                else:
                    sys.exit(0)
            else: 
                print('Invalid Password. Try Again!')
            
        elif ch==2:
            choice=int(input("""Select any one:
                                    1. Display Records
                                    2. Show Available Books
                                    3. Search Book
                                    4. EXIT
                                    """))
            if choice==1:
                display_records_F(issued_fbooks,issued_fid)
            elif choice==2:
                showBook()
            elif choice==3:
                search_B()
            else:
                sys.exit(0)
        
        elif ch==3:
            choice=int(input("""Select any one: 
                                    1. Display Records
                                    2. Show Available Books
                                    3. Search Book 
                                    4. EXIT
                                    """))
            if choice==1:
                display_records_S(issued_books,issued_rolls)
            elif choice==2:
                showBook()
            elif choice==3:
                search_B()
            else:
                sys.exit(0) 

        else:
            sys.exit(0)
main()