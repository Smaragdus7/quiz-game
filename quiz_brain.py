class QuizBrain:
    def __init__(self, questions_list):
        self.score = 0
        self.question_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        length_list = len(self.questions_list)
        return self.question_number == length_list-1

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if self.user_answer.lower() == self.correct_answer.lower():
            print("You're right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"You're current score is {self.score}/{self.question_number}")
        print("\n")
