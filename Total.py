# 파이썬 설치 모듈
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QVBoxLayout
# from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as Fc
# from matplotlib.figure import Figure

# 외부 모듈
from PyQt5 import QtWidgets
import pandas as pd

df = pd.read_excel("C:\\Users\\jaese\\Desktop\\huse\\subclass\\database.xlsx", sheet_name="Sheet1")
df_list = df.values.tolist()

sem_df = pd.read_excel("C:\\Users\\jaese\\Desktop\\huse\\subclass\\database.xlsx", sheet_name="sem_gpa")
sem_list = sem_df.values.tolist()

dset_seq = [1, 2, 5, 4, 3]

dataset = [[df_list[n][m] for m in dset_seq] for n in range(7)]

sem_dset =  [[sem_list[k][l] for l in range(4)] for k in range(9)]

dset_num  = len(dataset)

class TotalWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TotalWidget, self).__init__(parent)

        grid = QGridLayout()
        grid.addWidget(self.thisSemGPA(), 0, 0)
        grid.addWidget(self.thisSemGPAtotal(), 2, 0)
        grid.addWidget(self.Uni_point(), 1, 0)
        grid.addWidget(self.Sem_GPA(), 0, 1)
        # grid.addWidget(self.GPA_Transition(), 2, 1)
        grid.addWidget(self.Total_semester(), 1, 1)
        self.setLayout(grid)
    
    def thisSemGPA(self):
        thisSemGPAheader = ["과목명", "교수명", "수강 시간", "수업 분류", "학점"]
        
        pre_GPA = QTableWidget()
        pre_GPA.setRowCount(dset_num)
        pre_GPA.setColumnCount(5)
        pre_GPA.setHorizontalHeaderLabels(thisSemGPAheader)        
        pre_GPA.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for h in range(dset_num):
            for k in range(5):
                conut = QTableWidgetItem(str(dataset[h][k]))
                pre_GPA.setItem(h, k, conut)         

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(pre_GPA)
        vbox.addWidget(Schedule)

        groupbox = QGroupBox('이번 학기 과목별 학점')
        groupbox.setFixedSize(600, 280)
        groupbox.setLayout(vbox)

        return groupbox

    def thisSemGPAtotal(self):
        thisSemGPAtotalheader = ["전필 합계", "전선 합계", "교필 합계", 
                                "교선 합계", "학점", "전공평균", "학점 평균"]

        sub_type = ["전공필수","전공선택","교양필수","교양선택","P","NP"]

        JE = 0
        JS = 0
        GE = 0
        GS = 0
        JS_ = 0
        JE_ = 0

        To_numer = 0
        To_denom = 0
        
        pre_GPA = QTableWidget()
        pre_GPA.setRowCount(1)
        pre_GPA.setColumnCount(dset_num)
        pre_GPA.setHorizontalHeaderLabels(thisSemGPAtotalheader)        
        pre_GPA.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        
        for p in range(dset_num):
            if p == 0:
                for q in range(dset_num):
                    if dataset[q][3] == "전공필수":
                        JE += dataset[q][2]

                conut1 = QTableWidgetItem(str(JE))
                pre_GPA.setItem(1, p, conut1)

            if p == 1:
                for q in range(dset_num):
                    if dataset[q][3] == "전공선택":
                        JS += dataset[q][2]

                conut2 = QTableWidgetItem(str(JS))
                pre_GPA.setItem(1, p, conut2)
                
            if p == 2:
                for q in range(dset_num):
                    if dataset[q][3] == "교양필수":
                        GE += dataset[q][2]

                conut3 = QTableWidgetItem(str(GE))
                pre_GPA.setItem(1, p, conut3)
                
            if p == 3:
                for q in range(dset_num):
                    if dataset[q][3] == "교양선택":
                        GS += dataset[q][2] 

                conut4 = QTableWidgetItem(str(GS))
                pre_GPA.setItem(1, p, conut4)

            if p == 4:
                conut5 = QTableWidgetItem(str(JS+JE+GS+GE))
                pre_GPA.setItem(1, p, conut5)
                
            if p == 5:
                for q in range(dset_num):
                    if dataset[q][3] == "전공선택":
                        if dataset[q][4] == "P" or "NP":
                            pass

                        JS_ += dataset[q][2] * dataset[q][4]

                    elif dataset[q][3] == "전공필수":
                        if dataset[q][4] == "P" or "NP":
                            pass

                        JE_ += dataset[q][2] * dataset[q][4]

                count6 = QTableWidgetItem(str(round(((JS_ + JE_) / (JE + JS)), 2)))
                pre_GPA.setItem(1, p, count6)

            if p == 6:
                for q in range(dset_num):
                    if dataset[q][4] ==  "P" or "NP":
                            pass

                    To_denom += dataset[q][2]
                    To_numer += dataset[q][4] * dataset[q][2]
                        
                To_result = To_numer / To_denom
                conut7 = QTableWidgetItem(str(round(To_result, 2)))
                pre_GPA.setItem(1, p, conut7)              

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(pre_GPA)
        vbox.addWidget(Schedule)

        groupbox = QGroupBox('이번 학기 통계')
        groupbox.setFixedSize(600, 90)
        groupbox.setLayout(vbox)

        return groupbox

    def Uni_point(self):
        Uni_point_header = ["대분류", "중분류", "소분류", "인정 점수", "합계 점수"]
        
        pre_GPA = QTableWidget()
        pre_GPA.setRowCount(7)
        pre_GPA.setColumnCount(5)
        pre_GPA.setHorizontalHeaderLabels(Uni_point_header)        
        pre_GPA.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(7):
            for j in range(5):
                pre_GPA.setItem(i, j, QTableWidgetItem(''))

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(pre_GPA)
        vbox.addWidget(Schedule)

        groupbox = QGroupBox('우송지수')
        groupbox.setFixedSize(600, 150)
        groupbox.setLayout(vbox)

        return groupbox

    def Total_semester(self):
        hoz_header = ["필요 학점", "수강 학점", "잔여 학점", "학점 평균"]
        ver_header = ["전공", "교양", "전체"]

        total_gpa = 132
        mj_gpa = 83
        ge_gpa = 49
        com_mj = 12
        com_ge = 25
        
        total_sem = QTableWidget()
        total_sem.setRowCount(len(ver_header))
        total_sem.setColumnCount(len(hoz_header))
        total_sem.setVerticalHeaderLabels(ver_header)
        total_sem.setHorizontalHeaderLabels(hoz_header)
        total_sem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgetlist= [str(mj_gpa), str(ge_gpa), str(total_gpa), str(com_mj), str(com_ge), str(int(sem_list[8][1])), str(mj_gpa - com_mj), str(ge_gpa - com_ge), str(total_gpa - int(sem_list[8][1]))]

        for x in range(3):
            for y in range(3):
                if x == 0:
                    total_sem.setItem(y, x, QTableWidgetItem(widgetlist[y]))
                elif x == 1:
                    total_sem.setItem(y, x, QTableWidgetItem(widgetlist[y+3]))
                elif x == 2:
                    total_sem.setItem(y, x, QTableWidgetItem(widgetlist[y+6]))
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(total_sem)
        vbox.addWidget(Schedule)  

        groupbox = QGroupBox('학사 전체 학점')
        groupbox.setFixedSize(600, 150)
        groupbox.setLayout(vbox)

        return groupbox

    def Sem_GPA(self):

        hoz_header = ["수강 학점", "누적 수강 학점", "전공 평균", "학점 평균"]
        ver_header = ["1학년 1학기", "1학년 2학기", "2학년 1학기", "2학년 2학기", "3학년 1학기", "3학년 2학기", "4학년 1학기", "4학년 2학기", "기타학기"]

        total_sem = QTableWidget()
        total_sem.setRowCount(len(ver_header))
        total_sem.setColumnCount(len(hoz_header))
        total_sem.setVerticalHeaderLabels(ver_header)
        total_sem.setHorizontalHeaderLabels(hoz_header)
        total_sem.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for y in range(len(ver_header)):
            for u in range(len(hoz_header)):
                    rest_item = QTableWidgetItem(str(round(sem_dset[y][u], 2)))
                    total_sem.setItem(y, u, rest_item)
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(total_sem)
        vbox.addWidget(Schedule)

        groupbox = QGroupBox('학기별 학점')
        groupbox.setFixedSize(600, 280)
        groupbox.setLayout(vbox)
        return groupbox

    def GPA_Transition(self):
        sem_list = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "4-1", "4-2"]
        gpa_list = [4.13, 4.31, 4.25, 4.5, 4.11, 4.3, 4.21, 4.5]
        mj_list = [4.25, 4.07, 4.16, 4.5, 4, 3.95, 4.11, 4.5]

        canvas = Fc(Figure(figsize=(1,3)))

        self.ax = canvas.figure.subplots()
        self.ax.plot(sem_list, mj_list, color="#abb2b9", marker='o', linestyle='-',  label="Total")
        self.ax.plot(sem_list, gpa_list, color="#DD3737", marker='o', linestyle='-', label="Major")
        self.ax.legend()

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(canvas)
        vbox.addWidget(Schedule)

        groupbox = QGroupBox('학점 변화 추이')
        groupbox.setFixedSize(600, 200)
        groupbox.setLayout(vbox)

        return groupbox