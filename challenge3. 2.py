class student:
    
    def __init__(self,name,roll_number, cgpa):
        self. name=name
        self. roll_number=roll_number
        self. cgpe=cgp
        
        
    def sorted_student(student_list):
        sorted_student=sorted(studend_list, key=lambda student:student.cgpe,reverse=True)
        return sorted_student
        
        
        
    students=[
        student("hari","A123",7.8), 
        student("priya","A124",8.9), 
        student("kokila","A125",9.1), 
        student("Raja","A126",9.9)
    ]     
        
    sorted_students=sort_students(students)
       
       
       
    for student in sorted_students:
        print("name:{},roll number:{},cgpe:{}".fotmat(student.name,student.roll_number,student.cgpe)) 
    