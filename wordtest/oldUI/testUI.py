# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class TestUI(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(780, 600)
        
        #make result indicator
        #base
        self.gbResult = QGroupBox(Dialog)
        self.gbResult.setObjectName(u"gbResult")
        self.gbResult.setGeometry(QRect(20, 10, 741, 121))
        
        self.glwResult = QWidget(self.gbResult)
        self.glwResult.setObjectName(u"glwResult")
        self.glwResult.setGeometry(QRect(0, 20, 741, 81))
        
        self.gridRes = QGridLayout(self.glwResult)
        self.gridRes.setSpacing(10)
        self.gridRes.setObjectName(u"gridRes")
        self.gridRes.setContentsMargins(10, 10, 10, 10)
        #end base
        
        #make labels
        i=0
        for s in ('Total: ','English To Korean: ','Korean to English: '):
            tmp=QLabel(self.glwResult)
            tmp.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            tmp.setText(s)
            self.gridRes.addWidget(tmp,0,i,1,1)
            i+=1

        self.resT = QLabel(self.glwResult)
        self.resT.setObjectName(u"resT")
        self.resT.setLayoutDirection(Qt.LeftToRight)
        self.resT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridRes.addWidget(self.resT, 2, 0, 1, 1)

        self.resEtK = QLabel(self.glwResult)
        self.resEtK.setObjectName(u"resEtK")
        self.resEtK.setLayoutDirection(Qt.LeftToRight)
        self.resEtK.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridRes.addWidget(self.resEtK, 2, 1, 1, 1)
        
        self.resKtE = QLabel(self.glwResult)
        self.resKtE.setObjectName(u"resKtE")
        self.resKtE.setLayoutDirection(Qt.LeftToRight)
        self.resKtE.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridRes.addWidget(self.resKtE, 2, 2, 1, 1)
        #end labels
        #end result
        
        #make exam area
        self.scQus = QScrollArea(Dialog)
        self.scQus.setObjectName(u"scQus")
        self.scQus.setGeometry(QRect(20, 150, 741, 381))
        self.scQus.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scQus.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scQus.setWidgetResizable(True)
        
        self.boxQus = QWidget()
        self.boxQus.setObjectName(u"boxQus")
        self.boxQus.setGeometry(QRect(0, 0, 718, 379))

        self.gridMain = QGridLayout(self.boxQus)
        self.gridMain.setObjectName(u"gridMain")
        self.gridMain.setContentsMargins(10,10,10,10)

        i=0
        for s in ('No.','Question','Answer',None,'Correct Answer',None,'O/X'):
            if s:
                tmp=QLabel(self.boxQus)
                tmp.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                tmp.setText(s)
                self.gridMain.addWidget(tmp,0,i,1,1)
            i+=1
        #end exam area
        
        #end btn
        self.scQus.setWidget(self.boxQus)
        self.btnEnd = QPushButton(Dialog)
        self.btnEnd.setObjectName(u"btnEnd")
        self.btnEnd.setGeometry(QRect(670, 550, 93, 28))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"WordTest", None))
        self.gbResult.setTitle(QCoreApplication.translate("Dialog", u"Result", None))
        self.btnEnd.setText(QCoreApplication.translate("Dialog", u"Grading", None))