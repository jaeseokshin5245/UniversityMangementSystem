# 내장 모듈
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget

# 외장 모듈
from Assign import AssignmentWidget

# 필요 리스트 생성
name_list = ["메인 화면","시간표","과제","비교과","학사 종합"]

WIDTH = 1920
LENGTH = 1080

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(int(WIDTH * 0.25),int(LENGTH * 0.25) , 1280, 720)
        self.window = MainWindow(self)
        self.setCentralWidget(self.window)
        self.setWindowTitle("HUSE")

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        # QApplication 이전에 Widget이 생성 될 수 없으므로 상단에 먼저 정의해 놓지 않고 메인 윈도우 코드 안에 선언

        tab_holder = QTabWidget()
        tab_holder.addTab(AssignmentWidget(), "과제")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(tab_holder)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())