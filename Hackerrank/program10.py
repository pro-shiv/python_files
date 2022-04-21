n = int(input())
student_marks = {}
for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line)) 
        student_marks[name] = scores
        
print(student_marks)