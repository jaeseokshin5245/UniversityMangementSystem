from PyQt5.QtWidgets import QTextEdit, QLabel, QVBoxLayout, QFrame, QGroupBox
from PyQt5.QtCore import QFile, QIODevice, QTextStream, Qt
from PyQt5.QtGui import QFont
import datetime

def studyclub(self):
        font = QFont(None, 13)

        date = datetime.datetime.now()
        days_ahead = 0 - date.weekday()
        # 0 : 월요일 | 1 : 화요일 |2 : 수요일 |3 : 목요일 |4 : 금요일 |5 : 토요일 |6 : 일요일
        if days_ahead <= 0:
            days_ahead += 7

        lbl = QLabel('토익 스터디 | 매주 {}요일 오후 7시, 학교 앞 스타벅스 | 다음 모임까지 {}일 남음'.format("월", days_ahead), self)
        lbl.move(0, 0)

        txtedit = QTextEdit()
        txtedit.setText(self.s_string)
        txtedit.setFont(font)

        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(Schedule)
        vbox.addWidget(lbl)
        vbox.addWidget(txtedit)
        vbox.setAlignment(Qt.AlignTop)

        groupbox = QGroupBox('스터디')
        groupbox.setFixedSize(610, 320)
        groupbox.setLayout(vbox)
        
        text = txtedit.toPlainText()

        file = QFile("studyclub.txt")
        if file.open(QIODevice.WriteOnly | QIODevice.Text):
            stream =  QTextStream(file)
            stream << text
            stream.setCodec("UTF-8")
        file.close()

        return groupbox