from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class SelectTestUI(object):
    def setupUi(self, Dialog):
        Dialog.setFixedSize(640, 480)
        
        #main grid widget and layout
        self.glwMain = QWidget(Dialog)
        self.glwMain.setGeometry(QRect(0, 0, 641, 481))

        self.glMain = QGridLayout(self.glwMain)
        self.glMain.setContentsMargins(30, 30, 30, 30)
        
        #n/(num)
        self.lbPg = QLabel(self.glwMain)
        self.lbPg.setAlignment(Qt.AlignCenter)
        self.glMain.addWidget(self.lbPg, 0, 0, 1, 1)
        
        #remain time
        self.pgTime = QProgressBar(self.glwMain)
        self.glMain.addWidget(self.pgTime, 4, 0, 1, 1)
        
        #sizePolicy for question and answers
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        #font for question
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font.setPointSize(15)
        
        #question label
        self.lbQus = QLabel(self.glwMain)
        self.lbQus.setSizePolicy(sizePolicy)
        self.lbQus.setFont(font)
        self.lbQus.setAlignment(Qt.AlignCenter)
        sizePolicy.setHeightForWidth(self.lbQus.sizePolicy().hasHeightForWidth())
        self.glMain.addWidget(self.lbQus, 1, 0, 1, 1)
        
        #grid layout for answer buttons
        self.glAns = QGridLayout()
        
        #answer buttons
        self.btnAns1 = QPushButton(self.glwMain)
        sizePolicy.setHeightForWidth(self.btnAns1.sizePolicy().hasHeightForWidth())
        self.btnAns1.setSizePolicy(sizePolicy)
        self.glAns.addWidget(self.btnAns1, 0, 0, 1, 1)

        self.btnAns2 = QPushButton(self.glwMain)
        sizePolicy.setHeightForWidth(self.btnAns2.sizePolicy().hasHeightForWidth())
        self.btnAns2.setSizePolicy(sizePolicy)
        self.glAns.addWidget(self.btnAns2, 0, 1, 1, 1)

        self.btnAns3 = QPushButton(self.glwMain)
        sizePolicy.setHeightForWidth(self.btnAns3.sizePolicy().hasHeightForWidth())
        self.btnAns3.setSizePolicy(sizePolicy)
        self.glAns.addWidget(self.btnAns3, 1, 0, 1, 1)

        self.btnAns4 = QPushButton(self.glwMain)
        sizePolicy.setHeightForWidth(self.btnAns4.sizePolicy().hasHeightForWidth())
        self.btnAns4.setSizePolicy(sizePolicy)
        self.glAns.addWidget(self.btnAns4, 1, 1, 1, 1)
        #end answer buttons
        
        self.btnAns=(self.btnAns1,self.btnAns2,self.btnAns3,self.btnAns4)
        
        #stop/pause
        '''
        self.btnPause = QPushButton(Dialog)
        self.btnPause.setGeometry(QRect(20, 15, 55, 28))
        
        self.btnSkip = QPushButton(Dialog)
        self.btnSkip.setGeometry(QRect(570, 15, 50, 28))
        '''
        
        #add answer grid layout in main layout
        self.glMain.addLayout(self.glAns, 3, 0, 1, 1)

        #set text
        self.retranslateUi(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"WordTest", None))
        #self.pgTime.setFormat(QCoreApplication.translate("Dialog", u"%v/%m", None))
        self.pgTime.setFormat(QCoreApplication.translate("Dialog", u"???", None))
    # retranslateUi

