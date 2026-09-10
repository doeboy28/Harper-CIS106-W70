last_name = input("Enter your last name: ")
midterm = float(input("Enter midterm exam score: "))
final_exam = float(input("Enter final exam score: "))

total_exam_points = (midterm * 0.40) + (final_exam * 0.60)

print(f"{last_name}'s total exam points: {total_exam_points:.2f}")
