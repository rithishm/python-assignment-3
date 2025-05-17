if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Extract unique grades and sort them
    unique_grades = sorted(set(score for name, score in students))
    second_lowest = unique_grades[1]

    # Get names of students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest]
    second_lowest_students.sort()

    # Print each name on a new line
    for name in second_lowest_students:
        print(name)
