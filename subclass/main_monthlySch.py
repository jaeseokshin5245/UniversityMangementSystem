from PyQt5.QtWidgets import QCalendarWidget, QVBoxLayout, QGroupBox, QFrame, QLabel


def mnthSch(self):
        cal = QCalendarWidget(self)

        vbox = QVBoxLayout()
        vbox.addWidget(cal)

        groupbox = QGroupBox('월간 일정')
        groupbox.setFixedSize(1000, 500)
        groupbox.setLayout(vbox)

        return groupbox
