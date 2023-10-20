# import pandas as pd
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.text_edit = QPlainTextEdit(self)
#         self.text_edit.setPlainText("Line 1\nLine 2\nLine 3")
#         self.text_edit.textChanged.connect(self.save_to_excel)
#         self.text_edit.setFixedSize(500, 250)

#     def save_to_excel(self):
#         text = self.text_edit.toPlainText()
#         lines = text.split("\n")
#         df = pd.DataFrame(lines, columns=["Text"])
#         df.to_excel("text.xlsx", index=False)

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec_()
