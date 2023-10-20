from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QGroupBox
import pandas as pd

df = pd.read_excel(r"C:\Users\jaese\Desktop\huse\subclass\database.xlsx", sheet_name = "pro_plan")

pl_list = df.values.tolist()

proj_list = [[pl_list[h][g] for g in range(2)] for h in range(10)]

def Project_unit(self):

        def Activated(text):
            for wht in range(10):
                if text == proj_list[wht][0]:
                    self.proj_con.setText(proj_list[wht][1])
                    self.proj_con.adjustSize()

        combx = QComboBox(self)
        for cmbxitem in range(10):
            combx.addItem(proj_list[cmbxitem][0])
        combx.activated[str].connect(Activated)

        self.proj_con = QLabel('', self)
        self.proj_con.move(0, 0)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.proj_con)
        vbox.addWidget(combx)

        groupbox = QGroupBox('프로젝트 단위 및 할 일')
        groupbox.setFixedSize(610, 320)
        groupbox.setLayout(vbox)

        return groupbox