
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print(student_marks)
    for name in student_marks:
        if name==query_name:
            values=student_marks[name]
            total=sum(values)
            avg=float(total/3)
            avgfinal=round(avg,3)

    print(avgfinal)
        
          
            



    