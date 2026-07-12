def student_scaling():
    students_list = {
        "John" : [90, 90, 100, 85, 85, 80],
        "Jane" : [80, 70, 80, 90, 70, 85],
        "Jim" : [100, 60, 80, 30, 50, 90],
        "Jeff" : [90, 50, 70, 10, 80, 75],
        "Jerry": [100, 100, 100, 95, 75]
    }

    for name, grades in students_list.items():
        average_grade = sum(grades) / len(grades)

        print(name, "average:", average_grade)
    
        if average_grade >= 90:
            print(students_list[name])
            print("Great!")

        elif average_grade >= 80:
            print("Good!")

        elif average_grade >= 70:
            print("Mediocre...")

        else:
            print("Not good, this student needs to study harder.")

student_scaling()