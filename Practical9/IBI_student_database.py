#Create a class
class students:
    #Init method
    def __init__(self,name,major,score_portfolio,score_project,score_exam):
        self.name = name
        self.major = major
        self.score_portfolio = score_portfolio
        self.score_project = score_project
        self.score_exam = score_exam
    #Method in the class to print all the information of a student
    def information(self):
        print(self.name,self.major,self.score_portfolio,self.score_project,self.score_exam)

#Example
stu1 = students('John','BMI',90,80,90)
stu1.information()
#Or use: students.information(stu1)