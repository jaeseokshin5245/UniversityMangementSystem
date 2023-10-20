from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

# 외부 모듈
from subclass import cert_offSch as coS
from subclass import cert_toeic as te

class CertifiWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CertifiWidget, self).__init__(parent)
        grid = QGridLayout()
        # grid.addWidget(self.officialCertSch(), 0, 0)
        # grid.addWidget(self.TOEICSch(), 1, 0)
        grid.addWidget(self.preparing_cert(), 0, 1)
        grid.addWidget(self.completed_cert(), 1, 1)
        self.setLayout(grid)

    def officialCertSch(self):
        testSchdulehozheader = ["필기원서접수\n시작일", "필기원서접수\n종료일",
                             "필기시험일","필기합격\n발표일","응시자격\n서류제출 시작일",
                             "응시자격\n서류제출종료일","면접원서접수\n시작일","면접원서접수\n종료일",
                             "면접시작일","면접종료일","합격자발표일"]

        testSchduleverheader = ["기사/산업기사\n(2023년도 제1회)","기사/산업기사\n(2023년도 제2회)",
                                "기사/산업기사\n(2023년도 제3회)", "기사/산업기사\n(2023년도 제4회)"]
        
        offiSch = QTableWidget()
        offiSch.setColumnCount(len(testSchdulehozheader))
        offiSch.setRowCount(len(testSchduleverheader))
        offiSch.setHorizontalHeaderLabels(testSchdulehozheader)
        offiSch.setVerticalHeaderLabels(testSchduleverheader)
        offiSch.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for a in range(len(testSchduleverheader)):
            for b in range(1, len(testSchdulehozheader)+1):
                cert = QTableWidgetItem(str(coS.cert_list[a][b]))
                offiSch.setItem(a, b, cert)
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(Schedule)  
        vbox.addWidget(offiSch)

        groupbox = QGroupBox('2023년 기사/산업기사 일정')
        groupbox.setFixedSize(600, 320)
        groupbox.setLayout(vbox)

        return groupbox

    def TOEICSch(self):

        toeicSchHeader = ["회차", "시험 일시", "성적발표 일시", "정기 접수", "특별 접수"]

        offiSch = QTableWidget()
        offiSch.setColumnCount(len(toeicSchHeader))
        offiSch.setRowCount(26)
        offiSch.setHorizontalHeaderLabels(toeicSchHeader)
        offiSch.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        offiSch.resizeRowsToContents()

        for a in range(26):
            for b in range(len(toeicSchHeader)):
                cert = QTableWidgetItem(te.final_toeic[a][b])
                offiSch.setItem(a, b, cert)

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(Schedule)  
        vbox.addWidget(offiSch)

        groupbox = QGroupBox('2023년 토익 시험 일정')
        groupbox.setFixedSize(600, 320)
        groupbox.setLayout(vbox)

        return groupbox

    def preparing_cert(self):

        pre_cert_list= ["과목명", "필기 시험일", "필기 원서 \n 접수 기간", "실기 시험일", "실기 원서 \n 접수 기간", "최종합격 발표일"]

        offiSch = QTableWidget()
        offiSch.setColumnCount(len(pre_cert_list))
        offiSch.setRowCount(5)
        offiSch.setHorizontalHeaderLabels(pre_cert_list)
        offiSch.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        offiSch.resizeRowsToContents()
        for a in range(5):
            for b in range(len(pre_cert_list)):
                cert = QTableWidgetItem(' ')

                offiSch.setItem(a, b, cert)
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(Schedule)  
        vbox.addWidget(offiSch)

        groupbox = QGroupBox('취득 준비 자격증')
        groupbox.setFixedSize(600, 320)
        groupbox.setLayout(vbox)

        return groupbox

    def completed_cert(self):

        pre_cert_list= ["과목명", "취득 자격증 종류", "취득일", "취득만료일", "취득 연장 기한", "취득 연장 방법"]

        offiSch = QTableWidget()
        offiSch.setColumnCount(len(pre_cert_list))
        offiSch.setRowCount(10)
        offiSch.setHorizontalHeaderLabels(pre_cert_list)
        offiSch.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for a in range(10):
            for b in range(len(pre_cert_list)):
                cert = QTableWidgetItem(' ')

                offiSch.setItem(a, b, cert)
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(Schedule)  
        vbox.addWidget(offiSch)

        groupbox = QGroupBox('취득한 자격증')
        groupbox.setFixedSize(600, 320)
        groupbox.setLayout(vbox)

        return groupbox