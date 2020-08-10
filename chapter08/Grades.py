class Grades(object):
    def __init__(self):
        """Create empty grades book"""
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    def getGrades(self, student):
        """RETURN A LIST OF GRADS FOR STUDENTS"""
        try: #return copy of list of student's grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
    def getStudents(self):
        """Return a sorted list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]  #return copy of list of students
    def gradeReport(course):
        """Assume course is of type Grades"""
        report = ''
        for s in course.getStudents():
            tot = 0.0
            numGrades = 0
            for g in course.getGrades(s):
                tot += g
                numGrades += 1
            try:
                average = tot/numGrades
                report = report + '\n' + str(s) +'\'s mean grade is ' + str(average)
            except ZeroDivisionError:
                report = report + '\n' + str(s) +' has no grades'
        return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1  = Grad('Billy Buckner')
g2  = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(ug3)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)

sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))
