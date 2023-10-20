import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the UI here

    def wtf(self):

        text_edit = QTextEdit()

        name = "John"

        text_edit.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
