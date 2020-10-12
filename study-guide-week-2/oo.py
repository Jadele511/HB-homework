# Create your classes here
class Student():

    def __init__(self, first, last, address):
        self.first = first
        self.last = last
        self.address = address


class Question():

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        print(self.question)
        user_ans = input()
        return True if user_ans == self.correct_answer else False


class Exam():

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return (score / len(self.questions)) * 100


class StudentExam():

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam

    def take_test(self):
        self.score = self.exam.administer()
        print(self.score)


class Quiz(Exam):
    pass


class StudentQuiz(StudentExam):

    def take_test(self):
        print(1) if self.exam.administer() > 50 else print(0)


def example():
    exam = Exam('midterm')
    q1 = Question('q1', 'a1')
    q2 = Question('q2', 'a2')
    q3 = Question('q3', 'a3')
    exam.add_question(q1)
    exam.add_question(q2)
    exam.add_question(q3)
    stu = Student('anne', 'lee', '3')
    stu_exam = StudentExam(stu, exam)
    stu_exam.take_test()


def example_quiz():
    quiz = Quiz('midterm')
    q1 = Question('q1', 'a1')
    q2 = Question('q2', 'a2')
    q3 = Question('q3', 'a3')
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    stu = Student('anne', 'lee', '3')
    stu_exam = StudentQuiz(stu, quiz)
    stu_exam.take_test()
