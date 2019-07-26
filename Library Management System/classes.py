class Student:
    def __init__(self,student_name,student_year,student_id,student_branch,roll_no):
        self.student_name=student_name
        self.student_year=student_year
        self.student_id=student_id
        self.student_branch=student_branch
        self.roll_no=roll_no
    def display(self):
        print(f"Name: {self.student_name},\nRoll no: {self.roll_no}\n**")
        
class Book_details:
    def __init__(self,b_name,quantity,isbn):
        self.b_name=b_name
        self.quantity=quantity
        self.isbn=isbn
    def display(self):
        print(f"Title: {self.b_name},\n Number of copies: {self.quantity},\n ISBN: {self.isbn}\n**")

class  Faculty:
    def __init__(self,fname,fid):
        self.fname=fname
        self.fid=fid
    def display(self):
        print(f"Faculty Name: {self.fname},\nFaculty ID: {self.fid}\n**")
        
issued_books=[]
issued_rolls=[]
issued_fbooks=[]
issued_fid=[]