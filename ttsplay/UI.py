# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class PlayUI(object):
    def setupUi(self, Dialog, SCALE):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(740*SCALE, 570*SCALE)
        
        ##top file set
        self.gbFile = QGroupBox(Dialog)
        self.gbFile.setObjectName(u"gbFile")
        self.gbFile.setGeometry(QRect(20*SCALE, 20*SCALE, 701*SCALE, 60*SCALE))
        
        self.lbFileName = QLabel(self.gbFile)
        self.lbFileName.setObjectName(u"lbFileName")
        self.lbFileName.setGeometry(QRect(20*SCALE, 20*SCALE, 68*SCALE, 21*SCALE))
        self.lbFileName.setAlignment(Qt.AlignCenter)
        
        self.comboName = QComboBox(self.gbFile)
        self.comboName.setObjectName(u"comboName")
        self.comboName.setGeometry(QRect(90*SCALE, 20*SCALE, 341*SCALE, 22*SCALE))
        
        self.lbRepeat = QLabel(self.gbFile)
        self.lbRepeat.setObjectName(u"lbRepeat")
        self.lbRepeat.setGeometry(QRect(440*SCALE, 20*SCALE, 56*SCALE, 21*SCALE))
        
        self.spinNum = QSpinBox(self.gbFile)
        self.spinNum.setObjectName(u"spinNum")
        self.spinNum.setGeometry(QRect(498*SCALE, 20*SCALE, 51*SCALE, 22*SCALE))
        self.spinNum.setMinimum(1)
        self.spinNum.setMaximum(99)
        
        self.btnSet = QPushButton(self.gbFile)
        self.btnSet.setObjectName(u"btnSet")
        self.btnSet.setGeometry(QRect(570*SCALE, 16*SCALE, 111*SCALE, 28*SCALE))
        ##end top file set
        
        ##main table view
        self.twWord = QTableWidget(Dialog)
        self.twWord.setColumnCount(2)
            
        __qtablewidgetitem = QTableWidgetItem()
        self.twWord.setHorizontalHeaderItem(0, __qtablewidgetitem)
        
        __qtablewidgetitem1 = QTableWidgetItem()
        self.twWord.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        
        self.twWord.setObjectName(u"twWord")
        self.twWord.setGeometry(QRect(20*SCALE, 90*SCALE, 700*SCALE, 411*SCALE))
        
        self.twWord.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.twWord.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.twWord.setGridStyle(Qt.SolidLine)
        self.twWord.setSortingEnabled(False)
        self.twWord.setEditTriggers(QAbstractItemView.NoEditTriggers)
        ##end main table view
        
        ##bottom
        self.pgBar = QProgressBar(Dialog)
        self.pgBar.setObjectName(u"pgBar")
        self.pgBar.setGeometry(QRect(30*SCALE, 522*SCALE, 541*SCALE, 23*SCALE))
        self.pgBar.setValue(0)
        
        self.btnStartStop = QPushButton(Dialog)
        self.btnStartStop.setObjectName(u"btnStartStop")
        self.btnStartStop.setGeometry(QRect(630*SCALE, 520*SCALE, 31*SCALE, 28*SCALE))
        
        self.btnPause = QPushButton(Dialog)
        self.btnPause.setObjectName(u"btnPause")
        self.btnPause.setGeometry(QRect(590*SCALE, 520*SCALE, 31*SCALE, 28*SCALE))
        
        self.btnMore = QPushButton(Dialog)
        self.btnMore.setObjectName(u"btnMore")
        self.btnMore.setGeometry(QRect(670*SCALE, 520*SCALE, 41*SCALE, 28*SCALE))
        ##end bottom
        
        ##tools panel
        
        #tools box
        self.gbTool = QGroupBox(Dialog)
        self.gbTool.setObjectName(u"gbTool")
        self.gbTool.setGeometry(QRect(740*SCALE, 10*SCALE, 111*SCALE, 541*SCALE))
        
        #make one file button
        self.btnMake = QPushButton(self.gbTool)
        self.btnMake.setObjectName(u"btnOne")
        self.btnMake.setGeometry(QRect(10*SCALE, 30*SCALE, 93*SCALE, 28*SCALE))
        
        #represh button
        self.btnRefresh = QPushButton(self.gbTool)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setGeometry(QRect(10*SCALE, 70*SCALE, 93*SCALE, 28*SCALE))
        
        #set reverse
        self.chkRev = QCheckBox(self.gbTool)
        self.chkRev.setObjectName(u"checkBox")
        self.chkRev.setGeometry(QRect(10*SCALE, 110*SCALE, 96*SCALE, 19*SCALE))
        
        ##end tools

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Play", None))
        ___qtablewidgetitem = self.twWord.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Eng", None));
        ___qtablewidgetitem1 = self.twWord.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Kor", None));
        self.gbFile.setTitle("")
        self.lbFileName.setText(QCoreApplication.translate("Dialog", u"FileName: ", None))
        self.lbRepeat.setText(QCoreApplication.translate("Dialog", u"Repeat: ", None))
        self.btnSet.setText(QCoreApplication.translate("Dialog", u"Set and Stop", None))
        self.btnPause.setText(QCoreApplication.translate("Dialog", u"\u2016", None))
        self.btnMore.setText(QCoreApplication.translate("Dialog", u">>", None))
        self.btnStartStop.setText(QCoreApplication.translate("Dialog", 'u"\u25b6"', None))
        self.gbTool.setTitle(QCoreApplication.translate("Dialog", u"Tools", None))
        self.btnMake.setText(QCoreApplication.translate("Dialog", u"Make File", None))
        self.btnRefresh.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.chkRev.setText(QCoreApplication.translate("Dialog", u"E\u2192K", None))
    # retranslateUi

