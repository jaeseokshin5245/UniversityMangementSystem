from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import QFile, QTextStream

from subclass.Non_proplan import Project_total
from subclass.Non_procon import Project_unit
from subclass.Non_entclub import entclub
from subclass.Non_studyclub import studyclub

dateDict = {0: 'Monday', 1:'Tueseday', 2:'Wedsnday', 3:'Thursday', 4:'Friday'}

class NonStudyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NonStudyWidget, self).__init__(parent)

        s_file  = QFile("studyclub.txt")
        s_file.open(QFile.ReadOnly | QFile.Text)

        s_stream = QTextStream(s_file)
        s_stream.setCodec("UTF-8")

        self.s_string = s_stream.readAll()
        s_file.close()

        e_file  = QFile("entclub.txt")
        e_file.open(QFile.ReadOnly | QFile.Text)

        e_stream = QTextStream(e_file)
        e_stream.setCodec("UTF-8")

        self.e_string = e_stream.readAll()
        e_file.close()

        grid = QGridLayout()
        grid.addWidget(Project_total(), 0, 0)
        grid.addWidget(Project_unit(self), 1, 0)
        grid.addWidget(studyclub(self), 0, 1)
        grid.addWidget(entclub(self), 1, 1)
        self.setLayout(grid)