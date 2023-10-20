# 내장 모듈
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout

# 외장 모듈
from subclass import main_timetable, main_monthlySch, main_todaySch, Notifi_depart, main_recentNotif

class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        Sj = main_timetable.Shinji(self)
        monthSch = main_monthlySch.mnthSch(self)
        todySch = main_todaySch.tdaySch(self)
        recentNoti = main_recentNotif.rcntNoti(self, Notifi_depart.notfi)
        
        grid = QGridLayout()
        grid.addWidget(monthSch, 0, 0)
        grid.addWidget(recentNoti, 1, 1)
        grid.addWidget(Sj, 0, 1)
        grid.addWidget(todySch, 1, 0)

        self.setLayout(grid)
