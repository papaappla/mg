import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mg as nmg
class Start(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
#UI
    def initUI(self):
    #버튼
        btn_열기 = QPushButton('열기',self)
        btn_열기.resize(btn_열기.sizeHint())#sizeHint는 글씨 크깅에 맞춰서 버튼크기 조정
        btn_열기.move(450,30)
        btn_열기.clicked.connect(self.openFileNameDialog)


        btn_만들기 = QPushButton('만들기',self)
        btn_만들기.move(450,110)
        btn_만들기.clicked.connect(self.makeFile)

        btn_ONOFF = QPushButton('ON/OFF',self)
        btn_ONOFF.move(110,70)
        btn_ONOFF.clicked.connect(self.onOff)
        #btn_설명서 = QPushButton('?',self)
        #btn_설명서.setToolTip('설명서')
        #btn_설명서.move(450,150)

    #레이블
        lbl_학과고려 = QLabel('학과고려:',self)
        lbl_학과고려.move(50, 75)

        lbl_몇명 = QLabel('1조당 몇명인지 적어주세요',self)
        lbl_몇명.move(50,115)

        lbl_파일경로 = QLabel('파일경로:',self)
        lbl_파일경로.move(50,35)

        self.lbl_onoff = QLabel('off',self)
        self.lbl_onoff.move(200,75)

    #대화상자     
        self.몇명 = QLineEdit(self)#몇명인지 쓰기
        self.몇명.move(220,111)
        self.몇명.resize(200,20)
        self.몇명.setText('1')

        self.파일경로 = QLineEdit(self)
        self.파일경로.move(110,31)
        self.파일경로.resize(300,20)

    #창
        #self.setGeometry(2100,300,600,300)#시작 x,y 가로,세로
        self.resize(550,150)#가로세로
        self.setWindowTitle('조짜기 프로그램')
        self.show()
    
#기능
    #파일 열기
    def openFileNameDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"파일선택","",
                                                    "All Files (*);;Excel Files (.xlsx)")
        if fileName:
            self.파일경로.setText(fileName)
    #만들기
    def makeFile(self):
        self.ns = nmg.Mg(self.파일경로.text())
        num = int(self.몇명.text())
        if self.lbl_onoff == 'off':
            self.ns.make_group(num)
        else:
            self.ns.make_group(num,0)
    #on/off
    def onOff(self):
        if self.lbl_onoff.text() == 'off':
            self.lbl_onoff.setText('on')
            return 1
        else:
            self.lbl_onoff.setText('off')
            return 0

app = QApplication(sys.argv)
w = Start()
sys.exit(app.exec_())
