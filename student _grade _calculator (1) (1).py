# 🎯 Project: Student Grade Calculator
# Internship Week Task

def calculate_grade(marks):
    """Function to calculate grade and message based on marks"""
    
    if 90 <= marks <= 100:
        return "A", "Excellent Work! 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good Job! You can improve more! 😊"
    elif 60 <= marks <= 69:
        return "D", "Keep Practicing! Don’t give up! 💪"
    else:
        return "F", "Don’t worry! Try harder next time! 📚"


# Day 2: Get student name
student_name = input("Enter student name: ")

# Day 4: Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input! Marks must be between 0 and 100.")
    
    except ValueError:
        print("❌ Please enter a valid number.")

# Day 3: Call grading function
grade, message = calculate_grade(marks)

# Day 5: Display final result
print("\n📊 RESULT FOR", student_name.upper() + ":")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)