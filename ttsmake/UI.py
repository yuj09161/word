# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *


class MakeUI(object):
    def setupUi(self, make, SCALE):
        #set size
        make.setFixedSize(640*SCALE, 480*SCALE)
        
        sizePolicy_FP = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy_FP.setHorizontalStretch(0)
        sizePolicy_FP.setVerticalStretch(0)
        
        sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy_FF.setHorizontalStretch(0)
        sizePolicy_FF.setVerticalStretch(0)
        
        #file select group box
        self.gbFile = QGroupBox(make)
        self.gbFile.setObjectName(u"fileSel")
        self.gbFile.setGeometry(QRect(15*SCALE, 20*SCALE, 491*SCALE, 71*SCALE))
        
        self.comboFile = QComboBox(self.gbFile)
        self.comboFile.setObjectName(u"comboSel")
        self.comboFile.setGeometry(QRect(20*SCALE, 27*SCALE, 341*SCALE, 22*SCALE))
        
        self.btnFile = QPushButton(self.gbFile)
        self.btnFile.setObjectName(u"btnSel")
        self.btnFile.setGeometry(QRect(380*SCALE, 25*SCALE, 93*SCALE, 28*SCALE))
        #end file select
        
        #buttons
        self.btnCheck = QPushButton(make)
        self.btnCheck.setObjectName(u"btnCheck")
        self.btnCheck.setGeometry(QRect(530*SCALE, 30*SCALE, 81*SCALE, 28*SCALE))
        
        self.btnStart = QPushButton(make)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(530*SCALE, 60*SCALE, 81*SCALE, 28*SCALE))
        #end buttons
        
        #main tabbed widget
        self.twMain = QTabWidget(make)
        self.twMain.setObjectName(u"twMain")
        self.twMain.setGeometry(QRect(15*SCALE, 101*SCALE, 610*SCALE, 291*SCALE))
        
        #file tab
        self.tFile = QWidget()
        self.tFile.setObjectName(u"tFile")
        self.twMain.addTab(self.tFile, "File")
        
        self.fileList = QListWidget(self.tFile)
        self.fileList.setObjectName(u"fileList")
        self.fileList.setGeometry(QRect(0*SCALE, 0*SCALE, 604*SCALE, 263*SCALE))
        self.fileList.setDragDropMode(QAbstractItemView.InternalMove)
        self.fileList.setDefaultDropAction(Qt.MoveAction)
        
        #manual tab
        self.tabManual = QWidget()
        self.tabManual.setObjectName(u"tabManual")
        self.twMain.addTab(self.tabManual, "")
        
        self.gbLang = QGroupBox(self.tabManual)
        self.gbLang.setObjectName(u"gbLang")
        self.gbLang.setGeometry(QRect(20*SCALE, 30*SCALE, 201*SCALE, 58*SCALE))
        
        #Language grid
        self.glLang = QGridLayout(self.gbLang)
        self.glLang.setObjectName(u"glLang")
        
        self.rbEng = QRadioButton(self.gbLang)
        self.rbEng.setObjectName(u"rbEng")
        self.glLang.addWidget(self.rbEng, 0, 0, 1, 1)

        self.rbKor = QRadioButton(self.gbLang)
        self.rbKor.setObjectName(u"rbKor")
        self.rbKor.setChecked(True)
        self.glLang.addWidget(self.rbKor, 0, 1, 1, 1)
        #end Language
        
        #Save Destination
        self.gbTo = QGroupBox(self.tabManual)
        self.gbTo.setObjectName(u"gbTo")
        self.gbTo.setGeometry(QRect(260*SCALE, 30*SCALE, 331*SCALE, 86*SCALE))
        self.glTo = QGridLayout(self.gbTo)
        self.glTo.setObjectName(u"glTo")

        self.rbHere = QRadioButton(self.gbTo)
        self.rbHere.setObjectName(u"rbHere")
        self.rbHere.setChecked(True)
        self.glTo.addWidget(self.rbHere, 0, 0, 1, 2)
        
        self.rbTts = QRadioButton(self.gbTo)
        self.rbTts.setObjectName(u"rbTts")
        self.rbTts.setEnabled(False)
        self.glTo.addWidget(self.rbTts, 0, 2, 1, 2)

        self.lbName = QLabel(self.gbTo)
        self.lbName.setObjectName(u"lbName")
        sizePolicy_FP.setHeightForWidth(self.lbName.sizePolicy().hasHeightForWidth())
        self.lbName.setSizePolicy(sizePolicy_FP)
        self.glTo.addWidget(self.lbName, 1, 0, 1, 1)

        self.lbNum = QLabel(self.gbTo)
        self.lbNum.setObjectName(u"lbNum")
        sizePolicy_FP.setHeightForWidth(self.lbNum.sizePolicy().hasHeightForWidth())
        self.lbNum.setSizePolicy(sizePolicy_FP)
        self.glTo.addWidget(self.lbNum, 1, 2, 1, 1)

        self.comboName = QComboBox(self.gbTo)
        self.comboName.setObjectName(u"comboName")
        self.comboName.setEnabled(False)
        self.glTo.addWidget(self.comboName, 1, 1, 1, 1)
        
        self.spNum = QSpinBox(self.gbTo)
        self.spNum.setObjectName(u"spinBox")
        sizePolicy_FF.setHeightForWidth(self.spNum.sizePolicy().hasHeightForWidth())
        self.spNum.setSizePolicy(sizePolicy_FF)
        self.glTo.addWidget(self.spNum, 1, 3, 1, 1)
        #end Save
        
        #input & make
        self.lbText = QLabel(self.tabManual)
        self.lbText.setObjectName(u"lbText")
        self.lbText.setGeometry(QRect(20*SCALE, 176*SCALE, 39*SCALE, 15*SCALE))
        
        self.lnToTts = QLineEdit(self.tabManual)
        self.lnToTts.setObjectName(u"lbToTts")
        self.lnToTts.setGeometry(QRect(70*SCALE, 172*SCALE, 411*SCALE, 24*SCALE))
        
        self.btnManual = QPushButton(self.tabManual)
        self.btnManual.setObjectName(u"btnMake")
        self.btnManual.setGeometry(QRect(500*SCALE, 170*SCALE, 93*SCALE, 28*SCALE))
        #end
        
        #end Manual Make
        
        #logger tab
        self.tLog = QWidget()
        self.tLog.setObjectName(u"tLog")
        self.twMain.addTab(self.tLog, "Log")
        
        self.pteLog = QPlainTextEdit(self.tLog)
        self.pteLog.setObjectName(u"pteLog")
        self.pteLog.setGeometry(QRect(0*SCALE, 0*SCALE, 604*SCALE, 263*SCALE))
        self.pteLog.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.pteLog.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pteLog.setReadOnly(True)
        #end tab
        
        #progress bar
        self.pgE = QProgressBar(make)
        self.pgE.setObjectName(u"pgE")
        self.pgE.setGeometry(QRect(70*SCALE, 400*SCALE, 541*SCALE, 23*SCALE))
        
        self.pgC = QProgressBar(make)
        self.pgC.setObjectName(u"pbC")
        self.pgC.setGeometry(QRect(70*SCALE, 440*SCALE, 541*SCALE, 23*SCALE))
        
        font_pg = QFont()
        font_pg.setPointSize(11)
        
        self.lbE = QLabel(make)
        self.lbE.setObjectName(u"lbE")
        self.lbE.setGeometry(QRect(20*SCALE, 403*SCALE, 42*SCALE, 18*SCALE))
        self.lbE.setFont(font_pg)
        
        self.lbC = QLabel(make)
        self.lbC.setObjectName(u"lbC")
        self.lbC.setGeometry(QRect(20*SCALE, 443*SCALE, 42*SCALE, 18*SCALE))
        self.lbC.setFont(font_pg)
        #end progress bar

        self.retranslateUi(make)

        QMetaObject.connectSlotsByName(make)
    # setupUi

    def retranslateUi(self, make):
        make.setWindowTitle(QCoreApplication.translate("make", u"TTS Maker", None))
        
        self.gbFile.setTitle(QCoreApplication.translate("make", u"File", None))
        self.btnFile.setText(QCoreApplication.translate("make", u"Add", None))
        
        self.btnCheck.setText(QCoreApplication.translate("make", u"Check", None))
        self.btnStart.setText(QCoreApplication.translate("make", u"Make", None))
        
        self.pgE.setFormat(QCoreApplication.translate("make", u"%v/%m", None))
        self.pgC.setFormat(QCoreApplication.translate("make", u"%v/%m", None))
        self.lbE.setText(QCoreApplication.translate("make", u"\uc804\uccb4:", None))
        self.lbC.setText(QCoreApplication.translate("make", u"\ud604\uc7ac:", None))
        
        self.gbLang.setTitle(QCoreApplication.translate("make", u"Language", None))
        self.rbEng.setText(QCoreApplication.translate("make", u"English", None))
        self.rbKor.setText(QCoreApplication.translate("make", u"Korean", None))
        self.lbText.setText(QCoreApplication.translate("make", u"Text: ", None))
        self.btnManual.setText(QCoreApplication.translate("make", u"Make", None))
        self.gbTo.setTitle(QCoreApplication.translate("make", u"To...", None))
        self.lbName.setText(QCoreApplication.translate("make", u"Name", None))
        self.lbNum.setText(QCoreApplication.translate("make", u"No.", None))
        self.rbTts.setText(QCoreApplication.translate("make", u"TTS Dir", None))
        self.rbHere.setText(QCoreApplication.translate("make", u"Current Dir", None))
        self.twMain.setTabText(1, QCoreApplication.translate("make", u"Manual", None))
    # retranslateUi

