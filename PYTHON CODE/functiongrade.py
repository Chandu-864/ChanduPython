def grade(score):
    if score > 100:
        return "Your score is error"
    elif score >89 and score <101:
        return "Your garde is: A"
    elif score >79 and score<90:
         return "Your garde is: B"
    elif score >69 and score<80:
        return "Your garde is: C"
    elif score >59 and score<70:
        return "Your garde is: D"
    else:
        return "You failed in the exam"
score = int(input("Enter the score that you want to know the grade about: "))
Grade = grade(score)
print(Grade)