import random

students = list(range(1, 32))

remaining_students = students.copy()

while remaining_students:
    selected_student = random.choice(remaining_students)
    print(f"Изпитвайте ученика с номер: {selected_student}")
    remaining_students.remove(selected_student)

print("Всички ученици са изпитани!")

#Само така можах да го измисля
