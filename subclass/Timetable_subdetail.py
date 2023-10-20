# 외부 모듈 불러오기
from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout ,QGroupBox
from PyQt5.QtGui import QFont
import pandas as pd

# 로컬 데이터 불러오기
route = r"C:\Users\jaese\Desktop\huse\subclass\database.xlsx"

df = pd.read_excel(route, sheet_name= "Sheet1")

df_list = df.values.tolist()

# 필요 리스트 생성
data_sequence  = [1, 2, 6, 5, 7, 4, 8, 9, 10, 11, 12]
data = [[df_list[n][i] for i in data_sequence] for n in range(7)]

# 주 함수
def subjectdetail(self):
        # 부 함수
        def onActivated(text):
                for sp in range(7):
                        if text == data[sp][0]:
                                self.lbl.setText(sptext(*data[sp]))
                                self.lbl.adjustSize()

        def sptext(sub_nm, pro_nm, cls_rm, gpa, whdy, mgbl,stime, etime, mid, fin, ratio):
                output = ("과목명: {}".format(sub_nm)+
                        "\n\n교수명: {}".format(pro_nm)+
                        "\n\n강의실: {}".format(cls_rm)+
                        "\n\n학점: {}".format(gpa)+
                        "\n\n과목 종류: {}".format(mgbl)+
                        "\n\n수업 시간: {} {}시 부터 - {}시 까지".format(whdy, stime, etime)+
                        "\n\n중간 평가 방식: {}".format(mid)+
                        "\n\n기말평가 방식: {}".format(fin)+
                        "\n\n학점 비율: \n\n {}\n\n\n\n".format(ratio))
                return output

        font = QFont(None, 12)

        cb = QComboBox(self)
        cb.setFont(font)
        for cbitem in range(7):
                cb.addItem(df_list[cbitem][1])
        cb.activated[str].connect(onActivated)

        self.lbl = QLabel('', self)
        self.lbl.move(0, 0)
        self.lbl.setFont(font)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.lbl)
        vbox.addWidget(cb)

        groupbox = QGroupBox('과목 세부')
        groupbox.setFixedSize(500, 650)
        groupbox.setLayout(vbox)

        return groupbox