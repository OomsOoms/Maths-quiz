import random

class QuestionList:
    def __init__(self, question_count):
        # Generate a list of Question objects
        self.questions_list = {Question(f"{question_number}/{question_count}") for question_number in range(1, question_count + 1)}

class Question():
    def __init__(self, question_number):
        # Generate two random operands
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)

        # Randomly select an operation
        operator = random.choice(['+', '-', '*', '/'])

        # Formulate the question
        self.question = f"{question_number}: What is {operand1} {operator} {operand2}?"

        # Caculate the answer
        self.answer = eval(f"{operand1} {operator} {operand2}")

    def answer_question(self):
        # Check the inputted answer, convert to float as so all answers are the same, ValueError if invalid
        try:
            user_input = float(input(f"\n{self.question}\nYour answer: "))
            # Return boolean to determin if score is added
            if user_input == float(self.answer):
                print("\033[92mCorrect!\033[0m")
                return True
            else:
                print(f"\033[91mIncorrect! Answer: {self.answer}\033[0m")
                return False
            
        except ValueError:
            print("Invalid answer")
