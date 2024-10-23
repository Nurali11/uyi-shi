from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('font-size: 35px')
        self.rang_counter = 0
        self.setStyleSheet('background: rgb(255, 82, 82)') # color pickerdan oldim

        self.h_lay = QHBoxLayout()
        self.grid_lay = QGridLayout()
        self.v_main_lay = QVBoxLayout()

        self.lbl = QLabel("✖ gali")
        self.lbl.setStyleSheet('font-size: 25px')

        self.h_lay.addStretch()
        self.h_lay.addWidget(self.lbl)
        self.h_lay.addStretch()

        self.b1 = QPushButton('', clicked=lambda: self.Bosildi(self.b1))
        self.b2 = QPushButton('', clicked=lambda: self.Bosildi(self.b2))
        self.b3 = QPushButton('', clicked=lambda: self.Bosildi(self.b3))
        self.b4 = QPushButton('', clicked=lambda: self.Bosildi(self.b4))
        self.b5 = QPushButton('', clicked=lambda: self.Bosildi(self.b5))
        self.b6 = QPushButton('', clicked=lambda: self.Bosildi(self.b6))
        self.b7 = QPushButton('', clicked=lambda: self.Bosildi(self.b7))
        self.b8 = QPushButton('', clicked=lambda: self.Bosildi(self.b8))
        self.b9 = QPushButton('', clicked=lambda: self.Bosildi(self.b9))

        self.lst = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        self.noliklar = []
        self.xlar = []

        counter = 0
        for i in range(3):
            for j in range(3):
                self.lst[counter].setFixedSize(60, 50)
                self.grid_lay.addWidget(self.lst[counter], i, j)
                counter += 1

        self.v_main_lay.addLayout(self.h_lay)
        self.v_main_lay.addLayout(self.grid_lay)
        self.setLayout(self.v_main_lay)

    def Bosildi(self, btn):
        if btn.text() != "":
            return
        
        if self.rang_counter % 2 == 0:
            self.lbl.setText('O gali')
            btn.setText('✖')
            btn.setStyleSheet('font-size: 35px')
            self.setStyleSheet('background: lightgreen')
        else:
            self.lbl.setText('✖ gali')
            btn.setText('○')
            btn.setStyleSheet('font-size: 40px')
            self.setStyleSheet('background: rgb(255, 82, 82)')
        
        self.rang_counter += 1

        count = 0
        txt = ""
        for i in self.lst:
            if i.text() == '✖':
                if count not in self.xlar:
                    self.xlar.append(count)
                    txt = "Xlar"
            elif i.text() == '○':
                if count not in self.noliklar:
                    self.noliklar.append(count)
                    txt = "Noliklar"
            count += 1

        lst = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 4, 8],[2, 4, 6],[0, 3, 6],[1, 4, 7],[2, 5, 8]]

        for i in lst:
            a = i
            if txt == "Xlar":
                b = sorted(self.xlar)
            elif txt == "Noliklar":
                b = sorted(self.noliklar)
            c = [i for i in b if i in a]
            if a == c:
                self.msg = QMessageBox()
                self.msg.setText(f"{txt} yutdi!")
                self.msg.show()
                self.lbl.setText(f"{txt} yutdi!")
                self.Finish()  
                return 

    def Finish(self):
        for btn in self.lst:
            btn.setEnabled(False)

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
