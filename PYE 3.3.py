score = input("Enter Score: ")
grade = float(score)
if grade > 1.0 or grade < 0.0:
    print("Error, the score should be in the range between 0.0 and 1.0")
if grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
else:
     print("F")