from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QGroupBox
from PyQt5.QtCore import Qt
import pandas as pd


wksch = pd.read_excel(r"C:\Users\jaese\Desktop\huse\subclass\database.xlsx", sheet_name = "week_sch")
wksch_list = wksch.values.tolist()

def tdaySch(self):

    text = QLabel(self)
    text.setText(wksch_list[0][0] + "\n" + wksch_list[0][1]+ "\n" + wksch_list[0][2]+ "\n" + wksch_list[0][3])
    text.setAlignment(Qt.AlignTop)
    text.move(0, 0)

    Schedule = QFrame()
    Schedule.setFrameShape(QFrame.NoFrame)

    vbox = QVBoxLayout()
    vbox.addWidget(Schedule)
    vbox.addWidget(text)

    groupbox = QGroupBox('주간 일정')
    groupbox.setFixedSize(1000, 200)
    groupbox.setLayout(vbox)

    return groupbox