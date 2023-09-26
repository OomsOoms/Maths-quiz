from app import QuestionList, User
from database import database_manager

class Quiz:

    def __init__(self, question_count):
        self.user = User()
        self.question_list = QuestionList(question_count)
        self.question_count = question_count

    def start_quiz(self):
        # Main game loop
        if self.user.name:
            for question in self.question_list.questions_list:
                if question.answer_question():
                    self.user.score += 1

            # Update the user's score in the database
            database_manager.update_score(self.user.score, self.user.name)
            # Get the user's total score from the database
            total_score = database_manager.select_total(self.user.name)
            
            print(f"\nYour final score: {self.user.score}/{self.question_count}\nYour all-time total score: {total_score}")

if __name__ == "__main__":
    game = Quiz(10)
    game.start_quiz()
