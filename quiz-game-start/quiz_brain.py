class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number + 1}: {current_question.question} (True/False): ").lower()
            self.check_answer(user_answer, current_question.answer)
            self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Wrong!")
        print(f"Your current score is: {self.score}/{self.question_number +1}.")
