def get_score(quiz_number):
    while True:
        try:
            score = float(input(f"Enter Quiz {quiz_number} score: "))

            if score < 0 or score > 100:
                print("Invalid score. Please enter a score from 0 to 100.")
            else:
                return score

        except ValueError:
            print("Invalid input. Please enter a numeric score.")


def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def display_result(name, average):
    print("\n===== STUDENT GRADE RESULT =====")
    print("Student Name:", name)
    print(f"Average Score: {average:.2f}")

    if average >= 75:
        print("Status: PASSED")
    else:
        print("Status: FAILED")


def main():
    print("===== STUDENT GRADE EVALUATION =====")

    while True:
        name = input("Enter student's name: ").strip()

        if name:
            break
        else:
            print("Name cannot be empty.")

    quiz1 = get_score(1)
    quiz2 = get_score(2)
    quiz3 = get_score(3)

    average = calculate_average(quiz1, quiz2, quiz3)

    display_result(name, average)


if __name__ == "__main__":
    main()