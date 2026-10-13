# VTU 1st Sem Practice: Internal Assessment (IA) Calculator
print("=== PACE Mangalore: IA Marks Evaluator ===")

test1 = float(input("Enter marks for Test 1 (out of 20): "))
test2 = float(input("Enter marks for Test 2 (out of 20): "))
test3 = float(input("Enter marks for Test 3 (out of 20): "))
assignment = float(input("Enter Assignment marks (out of 10): "))

# VTU Logic: Consider the average of the BEST TWO test scores
test_scores = [test1, test2, test3]
test_scores.sort(reverse=True)  # Sorts highest to lowest
best_two_avg = (test_scores[0] + test_scores[1]) / 2

final_ia = best_two_avg + assignment
print("\n--- Final Results ---")
print(f"Average of Best Two Tests: {best_two_avg:.2f} / 20")
print(f"Total Internal Assessment Marks: {final_ia:.2f} / 30")

if final_ia >= 12:
    print("Status: ELIGIBLE for Semester End Examination (SEE) ✅")
else:
    print("Status: NOT ELIGIBLE (Attendance/CIE short) ❌")
