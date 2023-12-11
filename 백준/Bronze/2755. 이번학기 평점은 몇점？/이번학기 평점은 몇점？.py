#2755번 이번학기 평점은 몇점?

subject_count = int(input())
total_score = 0
total_grades = 0
num_score = 0

def new_round(n):
    n *= 100
    return (int(n)+1)/100 if (n - int(n)) >= 0.5 else int(n)/100

for i in range(subject_count):
    subject, grades, score = input().split()
    if(score == 'A+'):
        num_score = 4.3
    elif(score == 'A0'):
        num_score = 4.0
    elif(score == 'A-'):
        num_score = 3.7
    elif(score == 'B+'):
        num_score = 3.3
    elif(score == 'B0'):
        num_score = 3.0
    elif(score == 'B-'):
        num_score = 2.7
    elif(score == 'C+'):
        num_score = 2.3
    elif(score == 'C0'):
        num_score = 2.0
    elif(score == 'C-'):
        num_score = 1.7
    elif(score == 'D+'):
        num_score = 1.3
    elif(score == 'D0'):
        num_score = 1.0
    elif(score == 'D-'):
        num_score = 0.7
    else:
        num_score = 0.0
    total_score = total_score + int(grades) * num_score
    total_grades = total_grades + int(grades)
answer = new_round(total_score/total_grades)
print('{0:.2f}'.format(answer))
