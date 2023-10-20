# 외부 모듈 불러오기
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QAbstractItemView, QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QColor
import pandas as pd

# 로컬 데이터 불러오기
route = r"C:\Users\jaese\Desktop\huse\subclass\database.xlsx"

df = pd.read_excel(route, sheet_name= "Sheet1")

df_list = df.values.tolist()

# 필요 리스트 생성
sub_seq = [7, 1, 6, 2, 8, 9]

sample_sub = [[df_list[m][u] for u in sub_seq] for m in range(7)]

weekdaylist = ['월', '화', '수', '목', '금']

daytimelist= ["9시 - 10시","10시 - 11시","11시- 12시","12시 - 1시",
            "1시- 2시","2시 - 3시","3시 - 4시","4시 - 5시","5시 - 6시"]

wkday_trans = [{"Monday" : 0}, {"Tueseday" : 1}, {"Wedsday":  2}, {"Thursday":3}, {"Friday":  4}]

sht_wkday = ["Mon", "Tue", "Wed", "Thu", "Fri"]

time_trans= [[9, 1],[10, 2],[11, 3],[12, 4],[13, 5],
            [14, 6],[15, 7],[16, 8],[17, 9],[18, 10]]

tt_color = [[255, 207, 210],
            [241, 192, 232], 
            [207, 186, 240],
            [163, 196, 243], 
            [144, 219, 244], 
            [152, 245, 225],
            [185, 251, 192]]

# 리스트 길이 상수화
sub_num = len(sample_sub)
daytimelen = len(daytimelist)
weekdaylen = len(weekdaylist)
time_num = len(time_trans)

# 시간표 주 함수
def timetable(self):

    self.tableWidget = QTableWidget()
    self.tableWidget.setRowCount(daytimelen)
    self.tableWidget.setColumnCount(weekdaylen)
    self.tableWidget.setHorizontalHeaderLabels(weekdaylist)
    self.tableWidget.setVerticalHeaderLabels(daytimelist)
    self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    for i in range(daytimelen):
        for j in range(weekdaylen):
            self.tableWidget.setItem(i, j, QTableWidgetItem(''))   
            self.tableWidget.setColumnWidth(j, 100)

    for h in range(sub_num):
        if sht_wkday[0] in sample_sub[h][0]:
            day_cor = wkday_trans[0]["Monday"]

            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]
            

        elif sht_wkday[1] in sample_sub[h][0]:
            day_cor = wkday_trans[1]["Tueseday"]

            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]

        elif sht_wkday[2] in sample_sub[h][0]:
            day_cor = wkday_trans[2]["Wedsday"]

            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]

        elif sht_wkday[3] in sample_sub[h][0]:
            day_cor = wkday_trans[3]["Thursday"]

            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]

        elif sht_wkday[4] in sample_sub[h][0]:
            day_cor = wkday_trans[4]["Friday"]

            for i in range(time_num):
                if sample_sub[h][4] == time_trans[i][0]:
                    s_time_cor = time_trans[i][1]
                
                if sample_sub[h][5] == time_trans[i][0]:
                    e_time_cor = time_trans[i][1]
        
        self.tableWidget.setSpan(s_time_cor-1, day_cor, e_time_cor-s_time_cor, 1)
        sample = QTableWidgetItem(sample_sub[h][1] + '\n\n' + sample_sub[h][2] + '\n\n'+ sample_sub[h][3])
        self.tableWidget.setItem(s_time_cor-1, day_cor, sample)
        self.tableWidget.item(s_time_cor-1, day_cor).setBackground(QColor(tt_color[h][0],tt_color[h][1],tt_color[h][2]))

    vbox = QVBoxLayout()
    vbox.addWidget(self.tableWidget)

    groupbox = QGroupBox('시간표')
    groupbox.setFixedSize(700, 650)
    groupbox.setLayout(vbox)

    return groupbox
