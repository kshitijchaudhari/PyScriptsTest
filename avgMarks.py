if __name__ == '__main__':
    n = int(input("Enter the number of students "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter the student details ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks)
    query_name = input("Enter student name to query ")
    fl=[]
    fl= student_marks[query_name]
    print(fl)
    total=0.00
    for i in fl:
        total = i+total
    print(total)
    total= total/3
    print("%.2f" % total)