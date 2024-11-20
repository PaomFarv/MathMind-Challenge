import random
import time

input("Press enter to begin.")
print("---------------------")

num_of_digits = input("How many digits you want in a number of the problems: ")
target_prob = input("How many problems you want to solve? ")

while True:
    if num_of_digits.isdigit() and target_prob.isdigit():
        num_of_digits = int(num_of_digits)
        target_prob = int(target_prob)
        break
    else:
        print("Invalid input,Please try again.")

def generate_numbers(num_of_digits):
     return int("".join(str(random.choice(range(10))) for _ in range(num_of_digits)))

operators = ['+','-','*']
marks = 0
start_time = time.time()

for num in range(target_prob):
    first_num = generate_numbers(num_of_digits)
    sec_num = generate_numbers(num_of_digits)
    operator_in_num = random.choice(operators)

    expression = f"{first_num} {operator_in_num} {sec_num}"
    answer = eval(expression)

    user_input = input(f"Problem #{num+1}: {expression} = ")

    try:
        user_input = int(user_input)       
        if user_input == answer:
            print("Correct!")
            marks += 1
    except ValueError:
        print("Invalid input,Please try again.")
end_time = time.time()
total_time = end_time - start_time
print(f"\nYou solved {marks} out of {target_prob} problems correctly.")
print(f"It took you {round(total_time,2)} seconds to finish.")
print("---------------------\n")
