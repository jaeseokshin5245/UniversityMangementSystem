from PyQt5 import QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AssignmentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AssignmentWidget, self).__init__(parent)
        self.Assign_list()

    def Assign_list(self):
        self.lists = []
        self.listss = []

        self.buttonc = QPushButton('과제 항목 추가', self)
        self.buttonc.clicked.connect(self.con_button_click)
        self.buttonc.setFixedHeight(30)
        
        self.buttond = QPushButton('과제 항목 삭제(체크 항목만 삭제)', self)
        self.buttond.clicked.connect(self.don_button_click)
        self.buttond.setFixedHeight(30)
        
        self.buttons = QPushButton('과제 목록 및 내용 저장', self)
        self.buttons.clicked.connect(self.save_assign)
        self.buttons.setFixedHeight(30)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.buttonc)
        self.layout.addWidget(self.buttond)
        self.layout.addWidget(self.buttons)

    def con_button_click(self):
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)

        self.new_widget = QCheckBox('과제', self)

        self.layout.addWidget(self.new_widget) 
        self.layout.addWidget(self.te) 

        self.listss.append(self.te)  
        self.lists.append(self.new_widget)


    def don_button_click(self):
        for i in range(len(self.lists)-1, -1, -1):
            
            widgetdel = self.lists[i]
            self.widgetdels = self.listss[i]

            if widgetdel.isChecked():

                self.lists.remove(self.lists[i])
                self.layout.removeWidget(widgetdel)
                widgetdel.setParent(None)
                widgetdel.deleteLater()
                self.lists = self.lists

                self.listss.remove(self.listss[i])
                self.layout.removeWidget(self.widgetdels)
                self.widgetdels.setParent(None)
                self.widgetdels.deleteLater()
                self.listss = self.listss
            else:
                continue

    def save_assign(self):
        file = QFile("assignlist.txt")
        file.open(QIODevice.WriteOnly | QIODevice.Text)

        for i in range(len(self.listss)):
            text = self.listss[i].toPlainText()

            file = QFile("assignlist.txt")
            if file.open(QIODevice.Append | QIODevice.Text):

                stream = QTextStream(file)
                stream << text + '\n'
            file.close()
        QMessageBox.information(self,' ','내용이 저장되었습니다.')