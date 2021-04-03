class Quiz():
    title = ''
    __options = []              #list contains correct answers for the quiz
    attempted = False
    marks = 0
    def _init_(self,title,answer):
        self.title = title
        self.__options = answer
    def getans(self,attemptedAnswer):
        self.attempted = True
        ans = 0
        for (i,j) in zip(self.__options,attemptedAnswer):
            if i==j:
                ans+=1
        self.marks = ans
        return


class Course():
    courseCode = ''
    __quiz_ls = []              #list contains the quiz for the course

    def _init_(self,code,ls):
        self.courseCode = code
        self.__quiz_ls = ls
    def quizret(self,quizTitle):
        for quiz in self.__quiz_ls:
            if quizTitle == quiz.title:
                return quiz

    def getaverage(self):
        no_of_attempt = 0
        marks = 0
        for quiz in self.__quiz_ls:
            if quiz.attempted:
                no_of_attempt +=1
                marks += quiz.marks
        if no_of_attempt !=0:
            return int(marks/no_of_attempt)
        return 0
    def listUnattemptedQuiz(self):
        quiz_list = []
        for quiz in self.__quiz_ls:
            if not quiz.attempted:
                quiz_list.append(quiz.title)
        return quiz_list
class Student():
    entryNo = ''
    __course_ls = []

    def _init_(self,entryNo,course_ls):
        self.entryNo = entryNo
        self.__course_ls = course_ls

    def attempt(self,courseCode,quizTitle,attemptedAnswers):
        for course in self.__course_ls:
            if courseCode == course.courseCode:
                quiz = course.quizret(quizTitle)
                quiz.getans(attemptedAnswers)

    def getUnattemptedQuizzes(self):
        Unattempted_list = []
        for course in self.__course_ls:
            ls = course.listUnattemptedQuiz()
            for i in ls:
                Unattempted_list.append((course.courseCode,i))
        return Unattempted_list
    def getAverageScore(self,courseCode):
        for course in self.__course_ls:
            if courseCode == course.courseCode:
                return course.getaverage()



if __name__ == '__main__':
    col100q1 = Quiz('Quiz1',['a','b','b'])
    col100q2 = Quiz('Quiz2',['b','d','c'])
    col100 = Course('COL100',[col100q1,col100q2])

    mlt100q1 = Quiz('Quiz1',['a','b','d'])
    mlt100q2 = Quiz('Quiz2',['d','c','a'])
    mlt100 = Course('COL100',[mlt100q1,mlt100q2])

    s1 = Student('2019MSC2562',[col100,mlt100])
    s2 = Student('2017CS10377',[col100])

    s2.attempt('COL100', 'Quiz1',['a','b','c'])
    print(s2.getUnattemptedQuizzes())
    print(s2.getAverageScore('COL100'))

# start quiz
