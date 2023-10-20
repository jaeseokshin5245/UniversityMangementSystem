from PyQt5.QtWidgets import (QTableWidget, QHeaderView, QTableWidgetItem,
QFrame, QGroupBox,  QVBoxLayout)


def Project_total():
        month = ["1월","2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"]
        field = ["기획", "그래픽 및 사운드", "개발"]    

        total_plan = QTableWidget()
        total_plan.setColumnCount(len(month))
        total_plan.setHorizontalHeaderLabels(month)
        total_plan.setRowCount(len(field))
        total_plan.setVerticalHeaderLabels(field)
        total_plan.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for n in range(len(field)):
            for m in range(len(month)):
                total_plan.setItem(n, m, QTableWidgetItem(''))
        
        Schedule = QFrame()
        Schedule.setFrameShape(QFrame.NoFrame)

        vbox = QVBoxLayout()
        vbox.addWidget(total_plan)
        vbox.addWidget(Schedule)  

        groupbox = QGroupBox('프로젝트 일정')
        groupbox.setFixedSize(610, 320)
        groupbox.setLayout(vbox)

        return groupbox