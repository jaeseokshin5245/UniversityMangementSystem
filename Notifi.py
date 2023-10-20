from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

# 외부 모듈
from subclass import Notifi_depart, Notifi_Uni

font = QFont(None, 12)

class NotifiWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NotifiWidget, self).__init__(parent)  
        grid = QGridLayout()
        grid.addWidget(self.Depart_notice(), 0, 0)
        grid.addWidget(self.Uni_notice(), 1, 0)
        self.setLayout(grid)

    def Depart_notice(self):
        
        self.groupbox = QGroupBox('학과 / 학사 공지')
        self.groupbox.setFixedSize(1240, 320)
        
        vbox = QVBoxLayout()
        noti = QTextEdit()
        noti.setFont(font)
        noti.setPlainText(Notifi_depart.notfi)
        noti.setReadOnly(True)
        vbox.addWidget(noti)
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)
        vbox.addWidget(Schedule)  
        
        self.groupbox.setLayout(vbox)
        return self.groupbox

    def Uni_notice(self):
        self.groupbox = QGroupBox('학교 공지사항')
        self.groupbox.setFixedSize(1240, 320)
        
        vbox = QVBoxLayout()
        uni_noti = QTextEdit()
        uni_noti.setPlainText(Notifi_Uni.late_uni_noti)
        uni_noti.setFont(font)
        uni_noti.setReadOnly(True)
        vbox.addWidget(uni_noti)
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)
        vbox.addWidget(Schedule)  

        self.groupbox.setLayout(vbox)
        return self.groupbox