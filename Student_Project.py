class Student:
    def __init__(self, rn, n, m):
        self.rn = rn
        self.name = n
        self.marks = m

    def __str__(self):
        return f" RN: { self.rn }, NAME: { self.name }, MARKS: { self.marks }"

stud_list = [] 

def compare_students_rn(student):
    return student.rn
def compare_students_name(student):
    return student.name
def compare_students_marks(student):
    return student.marks

while True:

    ch = int(input("\nEnter Choice: \n1.Add Student \t2.Show Students \n3. Update Student \t4. Delete Student \n5. Exit"))

    match ch:
        case 1:
            print('\n1. ADD STUDENT')
            rn = int(input('Enter Roll No.: '))
            name = input('Enter Name: ')
            marks = float(input('Enter Marks: '))
            s = Student(rn, name, marks)
            stud_list.append(s)
            print('\nSTUDENT ADDED')

        case 2:
            print('\n2. SHOW STUDENTS')

            #while True:
            chs = int(input("\nEnter Choice to Show Students: \n1. Show Students Roll Numberwise \n2. Show Students Namewise \n3.Show Students Markswise\n"))
            match chs:
                case 1:
                    sorted_students = sorted(stud_list, key=compare_students_rn)
                    for stud in sorted_students:
                        print(stud)
                case 2:
                    sorted_students = sorted(stud_list, key=compare_students_name)
                    for stud in sorted_students:
                        print(stud)
                case 3:
                    sorted_students = sorted(stud_list, key=compare_students_marks, reverse=True)
                    for stud in sorted_students:
                        print(stud)
                case _:
                    print('INVALID CHOICE')
             
        case 3:
            print('\n3. UPDATE SUDENT')

            rn = int(input("Enter roll number to update: "))
            found = False

            for stud in stud_list:
                if stud.rn == rn:
                    found = True
                    n = input('Enter Name to update: ')
                    m = float(input('Enter Marks to updated: '))
                    stud.name = n
                    stud.marks = m
                    print('Student Updated')
                    break

            if not found:
                print('No student found with roll number', rn)

        case 4:
            print('\n4. DELETE SUDENT')

            rn = int(input("Enter roll number to delete"))
            found = False
            
            for stud in stud_list:
                if stud.rn == rn:
                    found = True
                    StudentToBeRemoved = stud
                    break
            if found:
                stud_list.remove(StudentToBeRemoved)
                print(StudentToBeRemoved, "Removed")
                
            else:
                print('No student found')
           
        case 5:
            print('\n5. EXITED')
            break

        case _:
            print('INVALID CHOICE')
