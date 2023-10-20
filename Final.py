# 내장 모듈
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget

# 외장 모듈
from Main import MainWidget
from TimeTable import TimeTableWidget
from Total import TotalWidget
from Cert import CertifiWidget
from Assign import AssignmentWidget
from Notifi import NotifiWidget
from Non import NonStudyWidget

# 필요 리스트 생성
name_list = ["메인 화면","시간표","과제","자격증","비교과","학사/학과 공지사항","학사 종합"]

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 30, 1280, 720)
        self.window = MainWindow(self)
        self.setCentralWidget(self.window)
        self.setWindowTitle("HUSE")

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        
        tab_list = [MainWidget(), TimeTableWidget(), AssignmentWidget(), CertifiWidget(), NonStudyWidget(), NotifiWidget(), TotalWidget()]
        # QApplication 이전에 Widget이 생성 될 수 없으므로 상단에 먼저 정의해 놓지 않고 메인 윈도우 코드 안에 선언

        tab_holder = QTabWidget()

        for t in range(len(name_list)):
            tab_holder.addTab(tab_list[t], name_list[t])

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(tab_holder)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())