# -*- coding: utf-8 -*-

from PySide2.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import *


class MakeUI(object):
    def setupUi(self, make, SCALE):
        #set size
        make.setFixedSize(640*SCALE, 480*SCALE)
        
        self.centralwidget=QWidget(self)
        make.setCentralWidget(self.centralwidget)
        self.glMain=QGridLayout(self.centralwidget)
        self.glMain.setContentsMargins(20,20,20,20)
        
        sizePolicy_EF = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy_EF.setHorizontalStretch(0)
        sizePolicy_EF.setVerticalStretch(0)
        
        sizePolicy_FP = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy_FP.setHorizontalStretch(0)
        sizePolicy_FP.setVerticalStretch(0)
        
        sizePolicy_FF = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy_FF.setHorizontalStretch(0)
        sizePolicy_FF.setVerticalStretch(0)
        
        #file select group box
        self.gbFile = QGroupBox(self.centralwidget)
        self.gbFile.setObjectName(u"fileSel")
        self.glFile=QGridLayout(self.gbFile)
        self.glFile.setContentsMargins(10,2,10,2)
        
        self.comboFile = QComboBox(self.gbFile)
        self.comboFile.setObjectName(u"comboSel")
        sizePolicy_EF.setHeightForWidth(self.comboFile.sizePolicy().hasHeightForWidth())
        self.comboFile.setSizePolicy(sizePolicy_EF)
        self.glFile.addWidget(self.comboFile,0,0,1,1)
        
        self.btnAddAll = QPushButton(self.gbFile)
        self.btnAddAll.setObjectName(u"btnSel")
        self.glFile.addWidget(self.btnAddAll,0,1,1,1)
        
        self.btnAdd = QPushButton(self.gbFile)
        self.btnAdd.setObjectName(u"btnSel")
        self.glFile.addWidget(self.btnAdd,0,2,1,1)
        
        self.glMain.addWidget(self.gbFile,0,0,2,2)
        #end file select
        
        #buttons
        self.btnCheck = QPushButton(self.centralwidget)
        self.btnCheck.setObjectName(u"btnCheck")
        sizePolicy_FF.setHeightForWidth(self.btnCheck.sizePolicy().hasHeightForWidth())
        self.btnCheck.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.btnCheck,0,2,1,1)
        
        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        sizePolicy_FF.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy_FF)
        self.glMain.addWidget(self.btnStart,1,2,1,1)
        #end buttons
        
        #main tabbed widget
        self.twMain = QTabWidget(self.centralwidget)
        self.twMain.setObjectName(u"twMain")
        self.glMain.addWidget(self.twMain,2,0,1,3)
        
        ##file tab
        self.tFile = QWidget()
        self.tFile.setObjectName(u"tFile")
        self.glFile=QGridLayout(self.tFile)
        self.glFile.setContentsMargins(2,2,2,2)
        
        self.fileList = QListWidget(self.tFile)
        self.fileList.setObjectName(u"fileList")
        self.fileList.setDragDropMode(QAbstractItemView.InternalMove)
        self.fileList.setDefaultDropAction(Qt.MoveAction)
        self.glFile.addWidget(self.fileList,0,0,1,2)
        
        sp=QSpacerItem(80,20,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.glFile.addItem(sp,1,0,1,1)
        
        self.btnDelAll=QPushButton(self)
        self.glFile.addWidget(self.btnDelAll,1,1,1,1)
        
        self.twMain.addTab(self.tFile, "File")
        
        '''
        ##manual tab
        
        self.tManual = QWidget()
        self.tManual.setObjectName(u"tManual")
        
        self.gbLang = QGroupBox(self.tManual)
        self.gbLang.setObjectName(u"gbLang")
        self.glFile=QGridLayout(self.gbFile)
        self.glFile.setContentsMargins(2,2,2,2)
        self.gbLang
        
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
        self.gbTo = QGroupBox(self.tManual)
        self.gbTo.setObjectName(u"gbTo")
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
        
        self.gbTo
        #end Save
        
        #input & make
        self.lbText = QLabel(self.tManual)
        self.lbText.setObjectName(u"lbText")
        self.lbText
        
        self.lnToTts = QLineEdit(self.tManual)
        self.lnToTts.setObjectName(u"lbToTts")
        self.lnToTts
        
        self.btnManual = QPushButton(self.tManual)
        self.btnManual.setObjectName(u"btnMake")
        self.btnManual
        #end
        
        self.twMain.addTab(self.tManual, "")
        #end Manual Make
        '''
        
        ##master log tab
        self.pteLog = QPlainTextEdit(self.twMain)
        self.pteLog.setObjectName(u"pteLog")
        self.pteLog.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.pteLog.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pteLog.setReadOnly(True)
        self.twMain.addTab(self.pteLog, f"Log")
        
        #progress bar
        font_pg = QFont()
        font_pg.setPointSize(11)
        
        self.lbC = QLabel(self.centralwidget)
        self.lbC.setObjectName(u"lbC")
        sizePolicy_FF.setHeightForWidth(self.lbC.sizePolicy().hasHeightForWidth())
        self.lbC.setSizePolicy(sizePolicy_FF)
        self.lbC.setFont(font_pg)
        self.glMain.addWidget(self.lbC,4,0,1,1)
        
        self.pgC = QProgressBar(self.centralwidget)
        self.pgC.setObjectName(u"pbC")
        sizePolicy_EF.setHeightForWidth(self.pgC.sizePolicy().hasHeightForWidth())
        self.pgC.setSizePolicy(sizePolicy_EF)
        self.glMain.addWidget(self.pgC,4,1,1,2)
        #end progress bar

        self.retranslateUi(make)

        QMetaObject.connectSlotsByName(make)
    # setupUi

    def retranslateUi(self, make):
        make.setWindowTitle(QCoreApplication.translate("make", u"TTS Maker", None))
        
        self.gbFile.setTitle(QCoreApplication.translate("make", u"File", None))
        self.btnAddAll.setText(QCoreApplication.translate("make", u"Add All", None))
        self.btnAdd.setText(QCoreApplication.translate("make", u"Add", None))
        self.btnCheck.setText(QCoreApplication.translate("make", u"Check", None))
        self.btnStart.setText(QCoreApplication.translate("make", u"Make", None))
        
        self.btnDelAll.setText(QCoreApplication.translate("make", u"Delete All", None))
        
        self.lbC.setText(QCoreApplication.translate("make", u"\uc9c4\ud589\ub960:", None))
        self.pgC.setFormat(QCoreApplication.translate("make", u"%v/%m", None))
        
        '''
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
        '''
    # retranslateUi
    
    def makeTab(self,n):
        pteLog = QPlainTextEdit(self.twMain)
        pteLog.setObjectName(u"pteLog")
        pteLog.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        pteLog.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        pteLog.setReadOnly(True)
        
        self.twMain.addTab(pteLog, f"T{n}")
        
        return pteLog
