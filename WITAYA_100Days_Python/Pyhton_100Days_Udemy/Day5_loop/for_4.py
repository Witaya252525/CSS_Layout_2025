


# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
print(student_scores)
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
total = 0
count = 0
for student in student_scores :
    total += student
    count += 1




    
print(f'the total height is = {total}')
print(f'the total count is  = { count}')
print(f'average is  = { total/count:0.2f}')




max = student_scores[0]
for sto in range (0, len(student_scores)):
    if student_scores[sto] > max :
        max = student_scores[sto]
        

    else:
        max = student_scores[0]
print(f' the max height is {max}')