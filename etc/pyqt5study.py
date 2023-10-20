# # 간단한 창 만들기
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     w = QWidget()
#     w.resize(250, 250)
#     w.move(300, 300)
#     w.setWindowTitle("Example")
#     w.show()

#     sys.exit(app.exec_())

# # 버튼 및 툴팁 추가
# import sys
# from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
# from PyQt5.QtGui import QFont

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         QToolTip.setFont(QFont('SanSerif', 10))
#         self.setToolTip('This is Qwiget a wiget')
#         btn = QPushButton('Button', self)
#         btn.setToolTip("this is a QPushButton widget")
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)

#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('ToolTips')
#         self.show()

# if __name__== '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# # 스테이터스 바 만들기
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Status Bar
#         self.statusBar().showMessage("Nothing is happening")

#         # Push Button
#         btn= QPushButton("Button 01", self)
#         btn.setToolTip("this is a button 01 \nIt has no event handlers")
#         btn.setStatusTip("this is a button 01")
#         btn.move(0, 0)
        
#         # Window Title
#         self.setWindowTitle('Status Bar Example')
#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())

# # 메뉴 추가하기
# import sys, os
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
# from PyQt5.QtGui import QIcon

# dir = os.path.dirname(os.getcwd())

# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         exit= QAction(QIcon(dir+'/image/char.png'), '&Exit', self)
#         exit.setShortcut('Ctrl+e')
#         exit.setStatusTip('Exit Application')
#         exit.triggered.connect(QApplication.quit)

#         self.statusBar()

#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addAction(exit)

#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())

# # 하위 메뉴 추가
# import sys, os
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
# from PyQt5.QtGui import QIcon

# dir = os.path.dirname(os.getcwd())

# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         exit= QAction(QIcon(dir+'/image/char.png'), '&Exit', self)
#         exit.setShortcut('Ctrl+e')
#         exit.setStatusTip('Exit Application')
#         exit.triggered.connect(QApplication.quit)

#         open = QMenu('Open', self)
#         openSub = QAction(QIcon(dir+'/image/char.png'), '&Exit', self)
#         open.addAction(openSub)

#         self.statusBar()

#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&File')
#         fileMenu.addMenu(open)
#         fileMenu.addAction(exit)

#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())

# # 툴바 추가
# import os 
# import sys
# from PyQt5.QtWidgets import QApplication,QMainWindow, QAction, QMenu
# from PyQt5.QtGui import QIcon

# dir = os.path.dirname(os.getcwd())

# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         exit = QAction(QIcon(dir+'/image/char.png'), '&Exit', self)
#         exit.setShortcut('Ctrl+e')
#         exit.setStatusTip('Exit Application')
#         exit.setToolTip('Exit Application')
#         exit.triggered.connect(QApplication.quit)

#         self.statusBar()
                      
#         self.toolbar = self.addToolBar('Exit')
#         self.toolbar.addAction(exit)

#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())

# # 체크 박스
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.statusbar = self.statusBar()
#         self.statusbar.showMessage("this tis status bar")

#         check01 = QAction('Check 01', self, checkable=True)
#         check01.setStatusTip("statusbar visability")
#         check01.setChecked(True)
#         check01.triggered.connect(self.toggleMenu)

#         menubar = self.menuBar()
#         file = menubar.addMenu('File')
#         file.addAction(check01)
#         self.setGeometry(300, 300, 300, 300)
#         self.show()

#     def toggleMenu(self, state):
#         if state:
#             self.statusbar.show()
#         else:
#             self.statusbar.hide()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())

# # 마우스 오른쪽
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.show()

#     def contextMenuEvent(self,event):
#         cmenu = QMenu(self)
#         new = cmenu.addAction("New")
#         open = cmenu.addAction("Open")
#         quit = cmenu.addAction("Quit")
#         action = cmenu.exec_(self.mapToGlobal(event.pos()))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     ex.setGeometry(300, 300, 300, 300)
#     sys.exit(app.exec_())


# # 팝업 메뉴에 체크박스 추가
# import sys
# from PyQt5.QtWidgets import QApplication ,QMainWindow,  QAction, QMenu

# class Example(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.statusbar = self.statusBar()
#         self.statusbar.showMessage("this is a status bar")
#         self.baronoff = QAction("Bar On /Off", self, checkable=True)
#         self.baronoff.setChecked(True)
#         self.baronoff.triggered.connect(self.toggleMenu)

#         self.show()

#     def contextMenuEvent(self, event):
#         cmenu = QMenu(self)
#         cmenu.addAction(self.baronoff)
#         action = cmenu.exec_(self.mapToGlobal(event.pos()))
#         self.statusbar.showMessage("this is a status bar.")

#     def toggleMenu(self, state):
#         if state:
#             self.statusbar.show()
#         else:
#             self.statusbar.hide()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# # 절대적 레이아웃 Absolute Layout

# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

# class MainFrame(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self. statusBar()

#         button1 = QPushButton("Button 1", self)
#         button1.move(0, 0)

#         button2 = QPushButton("Button2", self)
#         button2.move(200, 200)

#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainframe = MainFrame()
#     screen = app.primaryScreen()
#     size = screen.size()
#     mainframe.setGeometry(300, 300, 500, 300)
#     mainframe.setWindowTitle("Test")
#     sys.exit(app.exec_())


# # 박스 레이아웃 Box Layout

# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         ok_button = QPushButton("OK")
#         can_button = QPushButton("Cancel")

#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(ok_button)
#         hbox.addWidget(can_button)

#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)

#         self.setLayout(vbox)

#         self.show()

# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     ex= Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     ex.setGeometry(300, 300, 500, 300)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())

# # 박스 레이아웃 응용

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
# from PyQt5 import QtGui
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         ok_button = QPushButton("OK in hbox")
#         ok_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         can_button = QPushButton("Canclel in hbox")
#         can_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         hbox = QHBoxLayout()
        
#         vbox1 = QVBoxLayout()
#         vbox1.addWidget(ok_button)

#         vbox2 = QVBoxLayout()
#         vbox2.addWidget(can_button)

#         hbox.addLayout(vbox1)
#         hbox.addLayout(vbox2)

#         self.setLayout(hbox)
        
#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     ex.setGeometry(300, 300, 500, 300)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec())

# # 그리드 레이아웃 Grid layout

# from PyQt5.QtWidgets import (QGridLayout, QApplication, QWidget, QMainWindow, QAction, QPushButton, QHBoxLayout, QVBoxLayout)
# import sys

# class MainFrame(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         grid = QGridLayout()
#         self.setLayout(grid)

#         names = range(1, 11)
#         coords= [(i, j) for i in range(5) for j in range(2)]
#         for name, coord in zip(names, coords):
#             if name == '':
#                 continue
#             button = QPushButton(str(name))
#             grid.addWidget(button,*coord)
        
#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainframe = MainFrame()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w = 500
#     h = 300
#     mainframe.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     print(size.height())
#     print(size.width())
#     mainframe.setWindowTitle("test")
#     sys.exit(app.exec_())

# # 그리드와 박스 합쳐서 버튼 배치하기
# from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         grid = QGridLayout()
#         self.setLayout(grid)

#         names = range(1, 11)
#         coords = [(i, j) for i in range(5) for j in range(2)]
#         for name, coord in zip(names, coords):
#             if name=='':
#                 continue
#             button = QPushButton(str(name))
#             button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#             grid.addWidget(button, *coord)

#         hbox = QHBoxLayout()
#         for i in range(4):
#             i = QPushButton(str(i))
#             i.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#             hbox.addWidget(i)
#         grid.addLayout(hbox, 0, 2)

#         self.show()

# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     sys.exit(app.exec_())

# # 슬라이더와 그 값을 표시하는 패널 만들기
# from PyQt5.QtWidgets import QLCDNumber, QSlider, QApplication, QWidget, QVBoxLayout
# from PyQt5.QtCore import Qt
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)

#         vbox =QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)

#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)

#         self.show()

# if __name__== "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 800, 800
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle('Test Program')
#     sys.exit(app.exec_())

# # ESC로 창 닫기
# from PyQt5.QtWidgets import QLCDNumber, QSlider, QGridLayout, QApplication, QWidget, QVBoxLayout
# from PyQt5.QtCore import Qt
# import sys
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         self.show()

#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()

# if __name__== "__main__":
#     app = QApplication(sys.argv)
#     ex= Example()
#     screen = app.primaryScreen()
#     size= screen.size()
#     w, h = 500, 500
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle('Test Program')
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import QLabel, QLCDNumber, QSlider, QGridLayout, QApplication, QWidget
# from PyQt5.QtCore import Qt
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()
#         x, y = 0, 0
#         self.text = "x: {0} y:{1}".format(x, y)
#         self.label = QLabel(self.text, self)
#         self.setMouseTracking(True)
#         grid.addWidget(self.label, 0,0, Qt.AlignTop)

#         self.setLayout(grid)

#         self.show()

#     def mouseMoveEvent(self, e):
#         x = e.x()
#         y = e.y()
#         text = "x: {0} y:{1}".format(x, y)
#         self.label.setText(text)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500 
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import QLabel, QLCDNumber, QSlider, QGridLayout, QApplication, QWidget
# from PyQt5.QtCore import Qt
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()
#         x, y = 0, 0
#         self.text = "x: {0} y:{1}".format(x, y)
#         self.lcd1 = QLCDNumber(self)
#         self.lcd2 = QLCDNumber(self)

#         grid.addWidget(self.lcd1, 0, 0)
#         grid.addWidget(self.lcd2, 1, 0)

#         self.setMouseTracking(True)
#         self.setLayout(grid)

#         self.show()

#     def mouseMoveEvent(self, e):
#         x = e.x()
#         y = e.y()
#         self.lcd1.display(x)
#         self.lcd2.display(y)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500 
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())

# 이벤트에서 Sender란

# from PyQt5.QtWidgets import QMainWindow, QPushButton, QGridLayout, QApplication, QWidget
# import sys

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
    
#     def initUI(self):

#         bt1 = QPushButton("Button 1", self)
#         bt2 = QPushButton("Button 2", self)


#         w1 = QWidget(self)
#         grid = QGridLayout()
#         grid.addWidget(bt1, 0, 0)
#         grid.addWidget(bt2, 0, 1)
#         w1.setLayout(grid)
#         self.setCentralWidget(w1)

#         bt1.clicked.connect(self.buttonClicked)
#         bt2.clicked.connect(self.buttonClicked)

#         self.statusBar()
#         self.show()

#     def buttonClicked(self):
#         sender = self.sender()
#         self.statusBar().showMessage("Sender is "+sender.text())
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500 
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())

# 마우스 클릭을 인식해서 프로그램이 종료되는 코드

# from PyQt5.QtWidgets import QMainWindow, QApplication
# from PyQt5.QtCore import QObject, pyqtSignal
# import sys

# class Communicate(QObject):
#     closeApp = pyqtSignal()

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)

#         self.show()

#     def mousePressEvent(self, e):
#         self.c.closeApp.emit()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500 
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())
          
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLCDNumber, QGridLayout, QWidget, QLabel
# from PyQt5.QtCore import Qt
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         grid = QGridLayout()
#         self.setLayout(grid)

#         # LCD Widgets
#         self.lcd1 = QLCDNumber()
#         self.lcd2 = QLCDNumber()
#         self.lb1 = QLabel("This is a label")

#         grid.addWidget(self.lcd1, 0, 0, Qt.AlignTop)
#         grid.addWidget(self.lcd2, 0, 1, Qt.AlignTop)
#         grid.addWidget(self.lb1, 0, 2, Qt.AlignTop)
#         self.setMouseTracking(True)
#         self.show()

#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Enter or Qt.Key_E:
#             self.lb1.setText(str(self.lcd1.value())+''+str(self.lcd2.value()))

#     def mouseMoveEvent(self, e):
#         x = e.x()
#         y = e.y()
#         self.lcd1.display(x)
#         self.lcd2.display(y)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = 500, 500 
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Test Program")
#     sys.exit(app.exec_())

# 텍스트 입력 상자
# from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QInputDialog, QApplication
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()

#         self.btn = QPushButton('Dialog', self)
#         self.btn.clicked.connect(self.showDialog)

#         self.le = QLineEdit(self)
#         self.le.setReadOnly(True)

#         grid.addWidget(self.le, 0, 0)
#         grid.addWidget(self.btn, 0, 1)

#         self.setLayout(grid)

#         self.show()

#     def showDialog(self):
#         text, ok = QInputDialog.getText(self, 'Input Dialog', 'Please Input Text')
#         if ok:
#             self.le.setText(str(text))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = size.width()/4, size.height()/3
#     ex = Example()
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), int(w), int(h))
#     sys.exit(app.exec_())

# 창의 색을 바꾸는 대화상자 QColorDialog
# from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QColorDialog, QMainWindow, QFrame, QLabel
# from PyQt5.QtGui import QColor
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()

#         col =  QColor(0, 0, 0)

#         self.btn = QPushButton('Dialog', self)
#         grid.addWidget(self.btn, 0, 0)
#         self.btn.clicked.connect(self.showDialog)

#         self.frm = QFrame(self)
#         self.frm.setStyleSheet("QWidget { background-color: %s }"%col.name())

#         grid.addWidget(self.frm, 0, 1)

#         self.setLayout(grid)
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Color Dialog')
#         self.show()

#     def showDialog(self):
#         col = QColorDialog.getColor()
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget { background-color: %s }"%col.name())
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     screen = app.primaryScreen()
#     size = screen.size()
#     w = int(size.width()/4)
#     h = int(size.height()/3)
#     ex = Example()
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     sys.exit(app.exec_())

# from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QFontDialog, QApplication, QLabel
# from PyQt5.QtGui import QFontInfo
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()
#         self.setLayout(grid)
#         btn = QPushButton("Dialog", self)
#         btn.clicked.connect(self.showDialog)
#         grid.addWidget(btn, 0, 0)

#         self.lb = QLabel(self)
#         font = QFontInfo(self.lb.font())
#         self.lb.setText("This font is {}\n and size is : {}".format(font.family(), font.pointSize()))

#         grid.addWidget(self.lb)

#         self.show()

#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.lb.setFont(font)
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     screen = app.primaryScreen()
#     size = screen.size()
#     w = int(size.width()/4)
#     h = int(size.height()/3)
#     ex = Example()
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     sys.exit(app.exec_())

# 레이블 글자의 폰트와 크기를 바꾸는 QFontDialog
# from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QFontDialog, QApplication, QLabel
# from PyQt5.QtGui import QFontInfo
# import sys

# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         grid = QGridLayout()
#         self.setLayout(grid)

#         btn = QPushButton("Dialog", self)
#         btn.clicked.connect(self.showDialog)
#         grid.addWidget(btn, 0, 0)

#         self.lb = QLabel(self)
#         font = QFontInfo(self.lb.font())
#         self.lb.setText("This font is {}\n and size is : {}".format(font.family(), font.pointSize()))
#         grid.addWidget(self.lb)
#         self.show()

#     def showDialog(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             self.lb.setFont(font)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     screen = app.primaryScreen()
#     size = screen.size()
#     w = int(size.width()/4)
#     h = int(size.height()/3)
#     ex = Example()
#     ex.setGeometry(int(size.width()/2-w/2), int(size.width()/2-h/2), w, h)
#     sys.exit(app.exec_())

# 체크 박스와 토글 버튼
# from PyQt5.QtWidgets import QCheckBox, QPushButton, QMainWindow, QApplication, QFrame, QGridLayout,QSizePolicy, QVBoxLayout
# from PyQt5.QtGui import QColor
# import sys

# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Central Frame
#         self.cfrm = QFrame()
#         self.setCentralWidget(self.cfrm)
#         self.sfrm = QFrame()
#         self.col = QColor(0, 0, 0)
#         self.sfrm.setStyleSheet("Qframe{background-color : %s}"%self.col.name())
#         self.sfrm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # Toggle Button
#         self.btn1 = QPushButton("RED", self.cfrm)
#         self.btn1.setCheckable(True)
#         self.btn1.adjustSize()
#         self.btn1.clicked[bool].connect(self.changeColor)

#         self.btn2 = QPushButton("GREEN", self.cfrm)
#         self.btn2.setCheckable(True)
#         self.btn2.adjustSize()
#         self.btn2.clicked[bool].connect(self.changeColor)

#         self.btn3 = QPushButton("BLUE", self.cfrm)
#         self.btn3.setCheckable(True)
#         self.btn3.adjustSize()
#         self.btn3.clicked[bool].connect(self.changeColor)

#         # Checkbox
#         self.tg1 = QCheckBox("ON/OFF", self.cfrm)
#         self.tg1.adjustSize()
#         self.tg1.setChecked(False)
#         self.tg1.toggled[bool].connect(self.onoffframe)

#         # Layout
#         grid = QGridLayout()
#         self.cfrm.setLayout(grid)
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addWidget(self.btn1)
#         vbox.addWidget(self.btn2)
#         vbox.addWidget(self.btn3)
#         vbox.addWidget(self.tg1)
#         grid.addLayout(vbox, 0, 0)
#         grid.addWidget(self.sfrm, 0, 1)

#         # Show the Window
#         self.show()

#     def onoffframe(self, e):
#         if e:
#             self.sfrm.hide()
#         else:
#             self.sfrm.show()

#     def changeColor(self, e):
#         # Get the name of sender (in this case, it;s the name of button)
#         color = self.sender()

#         if e:
#             val= 255
#         else:
#             val = 0

#         # chage the color of the sub-frame widget
#         if color.text() == 'RED':
#             self.col.setRed(val)

#         elif color.text() == 'GREEN':
#             self.col.setGreen(val)

#         elif color.text() == 'BLUE':
#             self.col.setBlue(val)

#         self.sfrm.setStyleSheet("QFrame{background-color : %s}"%self.col.name())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     screen = app.primaryScreen()
#     size = screen.size()
#     w, h = int(size.width()/3), int(size.height()/3)
#     ex.setGeometry(int(size.width()/2-w/2), int(size.height()/2-h/2), w, h)
#     ex.setWindowTitle("Drill")
#     sys.exit(app.exec_())

# 스크롤바(슬라이더) / 로딩창(진행표시줄)
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar, QSlider, QGridLayout, QFrame, QLabel
# from PyQt5.QtCore import QTimer, Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):

#         # Center Widget Set
#         cfrm = QFrame(self)
#         self.setCentralWidget(cfrm)
#         grid = QGridLayout()
#         cfrm.setLayout(grid)

#         # 슬라이더

#         self.sld = QSlider(Qt.Horizontal, cfrm)
#         self.sld.adjustSize()
#         self.sld.setTickPosition(1)
#         self.sld.setMaximum(10)
#         self.sld.setMinimum(1)
#         self.sld.valueChanged[int].connect(self.label_out)
#         grid.addWidget(self.sld, 1, 0, 1, 2)

#         # 레이블
#         self.lb = QLabel("Velocity :", cfrm)
#         self.lb.adjustSize()
#         grid.addWidget(self.lb, 0, 0, 1, 1)

#         # 로딩창
#         self.pbar = QProgressBar(cfrm)
#         self.pbar.adjustSize()
#         self.pbar.text()
#         grid.addWidget(self.pbar, 2, 0, 1, 2)
#         self.timer = QTimer()
#         self.step = 0

#         # 시작 버튼
#         self.btn = QPushButton("시작", cfrm)
#         grid.addWidget(self.btn, 3, 0, 1, 1)
#         self.btn.clicked.connect(self.timer_active)

#         self.show()

#     def label_out(self, e):
#         # 이 메소드는 레이블 텍스트를 조절
#         if e:
#             self.lb.setText("Velocity : "+str(self.sld.value()))

#     def time(self):
#         # 이세소드는 타이머 신호를 받아와서 프로그래스바를 조절
#         if self.step*self.sld.value() < 100:
#             self.step += 1 
#         else:
#             self.timer.stop()
#             self.btn.setDisabled(False)
#             self.sld.setDisabled(False)

#         self.pbar.setValue(self.step*self.sld.value())

#     def timer_active(self):
#         # 이 메소드는 매 mil-seconds 마다 타이버 신호를 발산
#         if self.step*self.sld.value() >= 100:
#             self.step = 0
#             self.pbar.setValue(0)

#         else:
#             print("Start")
#             self.timer.timeout.connect(self.time)
#             # mil-seconds
#             self.timer.start(1000)
#             self.btn.setDisabled(True)
#             self.sld.setDisabled(True)

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     mw = MainWindow()
#     sys.exit(app.exec_())

# QCalenderWidger

# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
# from PyQt5.QtCore import QDate
# import sys

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         cal = QCalendarWidget(self)
#         cal.setGridVisible(True)
#         cal.clicked[QDate].connect(self.showDate)
    
#         self.lbl = QLabel(self)
#         date = cal.selectedDate()
#         self.lbl.setText(date.toString())

#         vbox = QVBoxLayout()
#         vbox.addWidget(cal)
#         vbox.addWidget(self.lbl)

#         self.setLayout(vbox)

#         self.setWindowTitle('QCalendarWidget')
#         self.setGeometry(300, 300, 400, 300)
#         self.show()

#     def showDate(self, date):
#         self.lbl.setText(date.toString())
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)
# from PyQt5.QtCore import Qt

# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         lcd = QLCDNumber(self)
#         dial = QDial(self)
#         btn1 = QPushButton("Big", self)
#         btn2 = QPushButton("Small", self)

#         hbox = QHBoxLayout()
#         hbox.addWidget(btn1)
#         hbox.addWidget(btn2)

#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(dial)
#         vbox.addLayout(hbox)
#         vbox.addLayout(vbox)
#         self.setLayout(vbox)

#         dial.valueChanged.connect(lcd.display)
#         btn1.clicked.connect(self.resizeBig)
#         btn2.clicked.connect(self.resizeSmall)

#         self.setWindowTitle("Signal and Slot")
#         self.setGeometry(200, 200, 200, 200)
#         self.show()

#     def keyPressEvent(self, e) -> None:
#         if e.key() == Qt.Key_Escape:
#             self.close()
#         elif e.key() == Qt.Key_F:
#             self.showFullScreen()
#         elif e.key() == Qt.Key_N:
#             self.showNormal()

#     def resizeBig(self):
#         self.resize(400, 500)

#     def resizeSmall(self):
#         self.resize(200, 250)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     ex.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication , QWidget

# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('Reimplementing event handler')
#         self.setGeometry(300, 300, 300, 200)
#         self.show()

#     def keyPressEvent(self, e) -> None:
#         if e.key() == Qt.Key_Escape:
#             self.close()
#         elif e.key() == Qt.Key_F:
#             self.showFullScreen()
#         elif e.key() == Qt.Key_N:
#             self.showNormal()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp
#     ex.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# class MyApp(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         x = 0
#         y = 0

#         self.text =  'x: {0}, y: {1}'.format(x, y)
#         self.label = QLabel(self.text, self)
#         self.label.move(20, 20)

#         self.setMouseTracking(True)

#         self.setWindowTitle("Reimplemeting event handler")
#         self.setGeometry(300, 300, 300, 200)
#         self.show()

#     def mouseMoveEvent(self, e):
#         x = e.x()
#         y = e.y()

#         text = 'x: {0}, y: {1}'.format(x, y)
#         self.label.setText(text)
#         self.label.adjustSize()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtCore import pyqtSignal, QObject
# from PyQt5.QtWidgets import QApplication, QMainWindow

# class Communicate(QObject):

#     closeApp = pyqtSignal()

# class MyApp(QMainWindow):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)

#         self.setWindowTitle('Emitting Signal')
#         self.setGeometry(300, 300, 300, 200) 
#         self.show()

#     def mousePressEvent(self, e):
#         self.c.closeApp.emit()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QcomboBox')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())