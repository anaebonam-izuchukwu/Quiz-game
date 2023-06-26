class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.list = question_list

    def still_has_questions(self):
        # if self.question_number < len(self.list):
            # return True
        # else:
            # False
        #OR we can use
        return self.question_number < len(self.list)
        
    def next_question(self):
        current_question = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got the right answer")
        else:
            print("Wrong answer")
        
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    # def rating(self):
        # if self.score == 12:
            # print("Execellent Perfect score")
        # elif self.score < 12 >= 10:
            # print("Thats a fair score")
        # elif self.score == 0 :
            # print("No brains")
   
   
    

