import sys
import os

from os import listdir
from os.path import isfile, join

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QPushButton,QVBoxLayout,QHBoxLayout,QMainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import QColor

import glob
import webbrowser

from time import gmtime, strftime
tarih = strftime("%Y-%m-%d %H:%M:%S", gmtime())

class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.yazi_alani_iki = QTextEdit()
        self.yazi_alani = QTextEdit()

        self.ac = QPushButton("Taramayı Başlat")
        self.recent = QPushButton("Recenti Aç")
        self.indir = QPushButton("İndirilenleri Aç")
        self.gecmis = QPushButton("Discord Adresine Git")
        
        self.yazi_alani.setStyleSheet("background-color: black;")
        self.yazi_alani.setTextColor(QColor(255,255,255))
        
        self.yazi_alani.setReadOnly(True)
        self.yazi_alani_iki.setReadOnly(True)

        h_box = QHBoxLayout()

        h_box.addWidget(self.ac)
        h_box.addWidget(self.recent)
        h_box.addWidget(self.indir)
        h_box.addWidget(self.gecmis)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        
        v_box.addWidget(self.yazi_alani_iki)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.ac.clicked.connect(self.dosya_ac)
        self.recent.clicked.connect(self.recent_ac)
        self.indir.clicked.connect(self.indir_ac)
        self.gecmis.clicked.connect(self.gecmis_ac)

    def gecmis_ac(self):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://discord.com/invite/amongustr")

    def recent_ac(self):
        path = r"C:\Users\user\Recent"
        path = os.path.realpath(path)
        os.startfile(path)

    def indir_ac(self):
        
        userpath = os.environ['USERPROFILE']

        path = userpath + "\Downloads"
        path = os.path.realpath(path)
        os.startfile(path)
        
    def dosya_ac(self):
        self.yazi_alani.setTextColor(QColor(255,255,255))
        self.yazi_alani.insertPlainText("Tarama başlatıldı. || Tarih: " + tarih + "\n")
        
        self.yazi_alani.insertPlainText("----------\n")
        
        dizin = glob.glob("C:\Windows\Prefetch\*.pf")
        yazi = "\n".join(dizin)
        self.yazi_alani_iki.insertPlainText(yazi) 

        kullanici = os.environ['USERPROFILE']

        tmpyol = kullanici + "\AppData\Local\Temp"

        tmpdizin = os.listdir(tmpyol)
        tmpyazi = "\n".join(tmpdizin)
        self.yazi_alani_iki.insertPlainText(tmpyazi) 
        
        pfdizin = os.listdir("C:\Program Files")
        pfyazi = "\n".join(pfdizin)
        self.yazi_alani_iki.insertPlainText(pfyazi)
        
        dtyol = kullanici + "\Desktop"

        dtdizin = os.listdir(dtyol)
        dtyazi = "\n".join(dtdizin)
        self.yazi_alani_iki.insertPlainText(dtyazi)

        dyol = kullanici + "\Downloads"

        ddizin = os.listdir(dyol)
        dyazi = "\n".join(ddizin)
        self.yazi_alani_iki.insertPlainText(dyazi)

        blacklist = ["cheat","CHEAT","Cheat","hack","Hack","HACK","hile","Hile","HİLE","hıle","Hıle","HILE"]
        
        tekrar = len(dizin)
        tmptekrar = len(tmpdizin)
        pftekrar = len(pfdizin)
        dttekrar = len(dtdizin)
        dtekrar = len(ddizin)
        blacktekrar = len(blacklist)
        
        if blacklist[0] in yazi or blacklist[1] in yazi or blacklist[2] in yazi or blacklist[3] in yazi or blacklist[4] in yazi or blacklist[5] in yazi or blacklist[6] in yazi or blacklist[7] in yazi or blacklist[8] in yazi or blacklist[9] in yazi or blacklist[10] in yazi or blacklist[11] in yazi:
            i = 0
            self.yazi_alani.insertPlainText("Birinci konumda bulunanlar:\n")            
            while i < tekrar:
                x = 0
                while x < blacktekrar:
                    if blacklist[x] in dizin[i]:
                        self.yazi_alani.insertPlainText(dizin[i] + "\n")
                    x += 1
                i += 1
                if i == tekrar:
                    self.yazi_alani.insertPlainText("----------\n")
        else:
            self.yazi_alani.insertPlainText("Birinci konumda herhangi bir şey bulunamadı.\n")
            self.yazi_alani.insertPlainText("----------\n")
            
        if blacklist[0] in tmpyazi or blacklist[1] in tmpyazi or blacklist[2] in tmpyazi or blacklist[3] in tmpyazi or blacklist[4] in tmpyazi or blacklist[5] in tmpyazi or blacklist[6] in tmpyazi or blacklist[7] in tmpyazi or blacklist[8] in tmpyazi or blacklist[9] in tmpyazi or blacklist[10] in tmpyazi or blacklist[11] in tmpyazi:
            i = 0
            self.yazi_alani.insertPlainText("İkinci konumda bulunanlar:\n")
            while i < tmptekrar:
                x = 0
                while x < blacktekrar:
                    if blacklist[x] in tmpdizin[i]:
                        self.yazi_alani.insertPlainText(tmpdizin[i] + "\n")
                    x += 1
                i += 1
                if i == tmptekrar:
                    self.yazi_alani.insertPlainText("----------\n")
        else:
            self.yazi_alani.insertPlainText("İkinci konumda herhangi bir şey bulunamadı.\n")
            self.yazi_alani.insertPlainText("----------\n")
            
        if blacklist[0] in pfyazi or blacklist[1] in pfyazi or blacklist[2] in pfyazi or blacklist[3] in pfyazi or blacklist[4] in pfyazi or blacklist[5] in pfyazi or blacklist[6] in pfyazi or blacklist[7] in pfyazi or blacklist[8] in pfyazi or blacklist[9] in pfyazi or blacklist[10] in pfyazi or blacklist[11] in pfyazi:
            i = 0
            self.yazi_alani.insertPlainText("Üçüncü konumda bulunanlar:\n")
            while i < pftekrar:
                x = 0
                while x < blacktekrar:
                    if blacklist[x] in pfdizin[i]:
                        self.yazi_alani.insertPlainText(pfdizin[i] + "\n")
                    x += 1
                i += 1
                if i == pftekrar:
                    self.yazi_alani.insertPlainText("----------\n")
        else:
            self.yazi_alani.insertPlainText("Üçüncü konumda herhangi bir şey bulunamadı.\n")
            self.yazi_alani.insertPlainText("----------\n")

        if blacklist[0] in dtyazi or blacklist[1] in dtyazi or blacklist[2] in dtyazi or blacklist[3] in dtyazi or blacklist[4] in dtyazi or blacklist[5] in dtyazi or blacklist[6] in dtyazi or blacklist[7] in dtyazi or blacklist[8] in dtyazi or blacklist[9] in dtyazi or blacklist[10] in dtyazi or blacklist[11] in dtyazi:
            i = 0
            self.yazi_alani.insertPlainText("Dördüncü konumda bulunanlar:\n")
            while i < dttekrar:
                x = 0
                while x < blacktekrar:
                    if blacklist[x] in dtdizin[i]:
                        self.yazi_alani.insertPlainText(dtdizin[i] + "\n")
                    x += 1
                i += 1
                if i == dttekrar:
                    self.yazi_alani.insertPlainText("----------\n")
        else:
            self.yazi_alani.insertPlainText("Dördüncü konumda herhangi bir şey bulunamadı.\n")
            self.yazi_alani.insertPlainText("----------\n")
            
        if blacklist[0] in dyazi or blacklist[1] in dyazi or blacklist[2] in dyazi or blacklist[3] in dyazi or blacklist[4] in dyazi or blacklist[5] in dyazi or blacklist[6] in dyazi or blacklist[7] in dyazi or blacklist[8] in dyazi or blacklist[9] in dyazi or blacklist[10] in dyazi or blacklist[11] in dyazi:
            i = 0
            self.yazi_alani.insertPlainText("Beşinci konumda bulunanlar:\n")
            while i < dtekrar:
                x = 0
                while x < blacktekrar:
                    if blacklist[x] in ddizin[i]:
                        self.yazi_alani.insertPlainText(ddizin[i] + "\n")
                    x += 1
                i += 1
                if i == dtekrar:
                     self.yazi_alani.insertPlainText("----------\n")                   
        else:
            self.yazi_alani.insertPlainText("Beşinci konumda herhangi bir şey bulunamadı.\n")
            self.yazi_alani.insertPlainText("----------\n")

        self.yazi_alani.insertPlainText("Tarama tamamlandı.\n")

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()


        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)

        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.menuleri_olustur()
    def menuleri_olustur(self):       

        self.setWindowTitle("discord.gg/amongustr")

        self.setGeometry(100, 100, 500, 500)

        self.show()

    def response(self,action):

        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()








app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())
