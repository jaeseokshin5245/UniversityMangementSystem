from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTextEdit

def rcntNoti(self, ex_source):
    noti = QTextEdit()
    noti.setPlainText(ex_source)
    noti.setReadOnly(True)

    vbox = QVBoxLayout()
    vbox.addWidget(noti)

    groupbox = QGroupBox('최근 학사 공지')
    groupbox.setFixedSize(300, 200)
    groupbox.setLayout(vbox)

    return groupbox