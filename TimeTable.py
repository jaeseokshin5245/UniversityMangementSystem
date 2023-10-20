# 내장 모듈
from PyQt5 import QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *

# 외부 모듈
from subclass import Timetable_tt, Timetable_subdetail

class TimeTableWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TimeTableWidget, self).__init__(parent)
        
        grid = QGridLayout()
        grid.addWidget(Timetable_tt.timetable(self), 0, 0)
        grid.addWidget(Timetable_subdetail.subjectdetail(self), 0, 1)
        self.setLayout(grid)
