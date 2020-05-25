import pandas as pd
import random as rd

class Mg:
    def __init__(self,root):
        self.학번 = []
        self.이름 = []
        self.학과 = []
        self.학년 = []
        self.group_num=[]

        self.a_student = []
        self.students = pd.read_excel(root)

    def student_number(self): #사용법 ~.student_number()
        self.a,b = self.students.shape
        return self.a

    def shuffle_index(self,num,snum=1):  #사용법 ~.shuffle_index()
        for i in range(self.student_number()):
            self.a_student.append([self.students["학번"][i],
                                   self.students["이름"][i],
                                   self.students["학과"][i],
                                   self.students["학년"][i]])
        if snum == 1:#off
            rd.shuffle(self.a_student)
            for content in self.a_student:
                self.학번.append(content[0])
                self.이름.append(content[1])
                self.학과.append(content[2])
                self.학년.append(content[3])
        else:#on
            rd.shuffle(self.a_student)
            self.a_student.sort(key=lambda x : x[2])
            p=[]
            for content in self.a_student:
                self.학번.append(content[0])
                self.이름.append(content[1])
                self.학과.append(content[2])
                self.학년.append(content[3])
            

       

        return self.a_student

    def make_group(self,num,snum=1): #사용법 ~.make_group(숫자)
        self.shuffle_index(num,snum)
        for i in range(self.student_number()):
            if i%num == 0:
                self.group_num.append(str(int(i/num+1))+'조')
            else:
                self.group_num.append(' ')

        new_student={
            "조": self.group_num,
            "학번" : self.학번,
            "이름" : self.이름,
            "학과" : self.학과,
            "학년" : self.학년
        }
        ng = pd.DataFrame(new_student)
        ng.to_excel('조완성.xlsx')
#사용법
#       mg = Mg(파일경로)
#       mg.
