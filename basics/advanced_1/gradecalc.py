ranks = ('F','','D0','D+','C0','C+','B0','B+','A0','A+')
scoresum = 0
gradesum = 0

for _ in range(20):
    subject, score, grade = input().split()
    score = float(score)
    if grade == 'P':
        continue
    else:
        grade = 0.5 * ranks.index(grade)
    scoresum += score
    gradesum += score * grade

print(gradesum/scoresum)