# 외부 모듈 불러오기
from PyQt5.QtWidgets import QTableWidget, QGroupBox, QAbstractItemView, QHeaderView, QTableWidgetItem, QVBoxLayout
import datetime 
import pandas as pd

# 로컬 데이터 불러오기
df = pd.read_excel(r"C:\Users\jaese\Desktop\huse\subclass\database.xlsx", sheet_name = "Sheet1")
df_list = df.values.tolist()

# 필요 리스트 생성
sub_seqen = [7, 1, 6, 2, 8, 9]

sample_sub = [[df_list[y][b] for b in sub_seqen] for y in range(7)]

time_trans= [[9, 1],[10, 2],[11, 3],[12, 4],[13, 5],
            [14, 6],[15, 7],[16, 8],[17, 9],[18, 10]]

dateDict = {0: 'Monday', 1:'Tueseday', 2:'Wedsnday', 3:'Thursday', 4:'Friday'}

datetime_date = datetime.datetime.today()
whatday = dateDict[datetime_date.weekday()]
dayofmonth = datetime_date.day

maintthozheader = ['오늘('+ str(dayofmonth)+')일']
mainttverheader = ["9시 - 10시","10시 - 11시","11시- 12시","12시 - 1시",
                    "1시- 2시","2시 - 3시","3시 - 4시","4시 - 5시","5시 - 6시"]
s_time_cor = 0
e_time_cor = 0

# 리스트 길이 상수
sub_num = len(sample_sub)
time_num = len(time_trans)

def Shinji(self):
    self.tableWidget = QTableWidget()
    self.tableWidget.setRowCount(len(mainttverheader))
    self.tableWidget.setColumnCount(len(maintthozheader))
    self.tableWidget.setHorizontalHeaderLabels(maintthozheader)
    self.tableWidget.setVerticalHeaderLabels(mainttverheader)
    self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    for h in range(sub_num):
        if whatday == sample_sub[h][0]:
            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]
        else:
            continue
        
        self.tableWidget.setSpan(s_time_cor-1, 0, e_time_cor-s_time_cor, 1)
        sample = QTableWidgetItem(sample_sub[h][1]+ '\n\n' + sample_sub[h][2] + '\n\n' + sample_sub[h][3] )
        self.tableWidget.setItem(s_time_cor-1, 0, sample)
        self.tableWidget.setColumnWidth(i, 100)

    vbox = QVBoxLayout()
    vbox.addWidget(self.tableWidget)

    groupbox = QGroupBox('시간표')
    groupbox.setFixedSize(300, 500)
    groupbox.setLayout(vbox)

    return groupbox