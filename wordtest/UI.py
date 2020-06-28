# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class SelectUI(object):
    def setupUi(self, Dialog, SCALE):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(650*SCALE, 530*SCALE)
        
        #exam file group
        self.tests = QGroupBox(Dialog)
        self.tests.setObjectName(u"tests")
        self.tests.setGeometry(QRect(20*SCALE, 20*SCALE, 293*SCALE, 88*SCALE))
        
        self.comboTest = QComboBox(self.tests)
        self.comboTest.setObjectName(u"comboTest")
        self.comboTest.setGeometry(QRect(20*SCALE, 33*SCALE, 150*SCALE, 22*SCALE))
        
        self.btnTest = QPushButton(self.tests)
        self.btnTest.setObjectName(u"btnTest")
        self.btnTest.setGeometry(QRect(180*SCALE, 30*SCALE, 93*SCALE, 28*SCALE))
        
        #re-test file group
        self.reTests = QGroupBox(Dialog)
        self.reTests.setObjectName(u"reTests")
        self.reTests.setGeometry(QRect(337*SCALE, 20*SCALE, 293*SCALE, 88*SCALE))
        
        self.comboRe = QComboBox(self.reTests)
        self.comboRe.setObjectName(u"comboRe")
        self.comboRe.setGeometry(QRect(20*SCALE, 33*SCALE, 150*SCALE, 22*SCALE))
        
        self.btnRe = QPushButton(self.reTests)
        self.btnRe.setObjectName(u"btnRe")
        self.btnRe.setGeometry(QRect(180*SCALE, 30*SCALE, 93*SCALE, 28*SCALE))
        
        #selected file(s) list
        self.fileList = QListWidget(Dialog)
        self.fileList.setObjectName(u"fileList")
        self.fileList.setGeometry(QRect(20*SCALE, 120*SCALE, 611*SCALE, 341*SCALE))
        self.fileList.setDragDropMode(QAbstractItemView.InternalMove)
        self.fileList.setDefaultDropAction(Qt.MoveAction)
        
        #setting button
        self.btnSetting = QPushButton(Dialog)
        self.btnSetting.setObjectName(u"btnSetting")
        self.btnSetting.setGeometry(QRect(30*SCALE, 480*SCALE, 93*SCALE, 28*SCALE))
        
        '''
        #start exam(selection type)
        self.btnSelStart = QPushButton(Dialog)
        self.btnSelStart.setObjectName(u"btnSelStart")
        self.btnSelStart.setGeometry(QRect(410*SCALE, 480*SCALE, 103*SCALE, 28*SCALE))
        '''
        
        #start button
        self.btnStart = QPushButton(Dialog)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(527*SCALE, 480*SCALE, 93*SCALE, 28*SCALE))
        
        #setting
        
        #group box for setting
        self.gbSetting = QGroupBox(Dialog)
        self.gbSetting.setObjectName(u"gbSetting")
        self.gbSetting.setGeometry(QRect(20*SCALE, 520*SCALE, 611*SCALE, 181*SCALE))
        
        #group box for question mod
        self.qusMod = QGroupBox(self.gbSetting)
        self.qusMod.setObjectName(u"qusMod")
        self.qusMod.setGeometry(QRect(10*SCALE, 20*SCALE, 196*SCALE, 151*SCALE))
        
        #widget for question mod
        self.glwMod = QWidget(self.qusMod)
        self.glwMod.setObjectName(u"glwMod")
        self.glwMod.setGeometry(QRect(13*SCALE, 23*SCALE, 170*SCALE, 111*SCALE))
        
        #grid for question mod
        self.gridQus = QGridLayout(self.glwMod)
        self.gridQus.setObjectName(u"gridQus")
        self.gridQus.setContentsMargins(10, 0, 10, 0)
        
        #english to korean check
        self.chkEtK = QCheckBox(self.glwMod)
        self.chkEtK.setObjectName(u"chkEtK")
        self.chkEtK.setChecked(True)
        self.gridQus.addWidget(self.chkEtK, 0, 1, 1, 1)
        
        #korean to english check
        self.chkKtE = QCheckBox(self.glwMod)
        self.chkKtE.setObjectName(u"chkKtE")
        self.chkKtE.setChecked(True)
        self.gridQus.addWidget(self.chkKtE, 1, 1, 1, 1)
        
        #group box for show answer
        self.showAnswer = QGroupBox(self.gbSetting)
        self.showAnswer.setObjectName(u"showAnswer")
        self.showAnswer.setGeometry(QRect(220*SCALE, 20*SCALE, 191*SCALE, 71*SCALE))
        
        #widget for show answer
        self.glwAns = QWidget(self.showAnswer)
        self.glwAns.setObjectName(u"glwAns")
        self.glwAns.setGeometry(QRect(13*SCALE, 23*SCALE, 170*SCALE, 40*SCALE))
        
        #grid for show answer
        self.gridOX = QGridLayout(self.glwAns)
        self.gridOX.setObjectName(u"gridOX")
        self.gridOX.setContentsMargins(10, 0, 10, 0)
        
        #radiobutton for answer show
        self.rbAnsY = QRadioButton(self.glwAns)
        self.rbAnsY.setObjectName(u"rbAnsY")
        self.rbAnsY.setChecked(True)
        self.gridOX.addWidget(self.rbAnsY, 0, 0, 1, 1)

        #radiobutton for answer hide
        self.rbAnsN = QRadioButton(self.glwAns)
        self.rbAnsN.setObjectName(u"rbAnsN")
        self.gridOX.addWidget(self.rbAnsN, 0, 2, 1, 1)
        
        #spacer
        self.spOX = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridOX.addItem(self.spOX, 0, 1, 1, 1)
        
        
        self.showPrefix = QGroupBox(self.gbSetting)
        self.showPrefix.setObjectName(u"showPrefix")
        self.showPrefix.setGeometry(QRect(220*SCALE, 100*SCALE, 191*SCALE, 71*SCALE))
        
        self.glwPrefix = QWidget(self.showPrefix)
        self.glwPrefix.setObjectName(u"glwPrefix")
        self.glwPrefix.setGeometry(QRect(13*SCALE, 23*SCALE, 170*SCALE, 40*SCALE))
        
        self.gridPrefix = QGridLayout(self.glwPrefix)
        self.gridPrefix.setObjectName(u"gridPrefix")
        self.gridPrefix.setContentsMargins(10, 0, 10, 0)
        
        self.rbPreY = QRadioButton(self.glwPrefix)
        self.rbPreY.setObjectName(u"rbPreY")
        self.rbPreY.setChecked(True)
        self.gridPrefix.addWidget(self.rbPreY, 0, 0, 1, 1)

        self.rbPreN = QRadioButton(self.glwPrefix)
        self.rbPreN.setObjectName(u"rbPreN")
        self.gridPrefix.addWidget(self.rbPreN, 0, 2, 1, 1)

        self.spPre = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridPrefix.addItem(self.spPre, 0, 1, 1, 1)

        self.shuffle = QGroupBox(self.gbSetting)
        self.shuffle.setObjectName(u"shuffle")
        self.shuffle.setGeometry(QRect(420*SCALE, 20*SCALE, 91*SCALE, 71*SCALE))
        
        self.spinShuffle = QSpinBox(self.shuffle)
        self.spinShuffle.setObjectName(u"spinShuffle")
        self.spinShuffle.setGeometry(QRect(20*SCALE, 30*SCALE, 42*SCALE, 22*SCALE))
        self.spinShuffle.setMaximum(99)
        self.spinShuffle.setValue(5)
        
        self.gbSetting.setVisible(False)
        
        #end setting

        #text setting
        self.retranslateUi(Dialog)

        #??(generated code)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"WordTest", None))
        self.tests.setTitle(QCoreApplication.translate("Dialog", u"Tests", None))
        self.btnTest.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.reTests.setTitle(QCoreApplication.translate("Dialog", u"Re-Tests", None))
        self.btnRe.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btnSetting.setText(QCoreApplication.translate("Dialog", u"Settings", None))
        #self.btnSelStart.setText(QCoreApplication.translate("Dialog", u"Selection Test", None))
        self.btnStart.setText(QCoreApplication.translate("Dialog", u"Start", None))
        
        self.gbSetting.setTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.qusMod.setTitle(QCoreApplication.translate("Dialog", u"Question Mode", None))
        self.chkEtK.setText(QCoreApplication.translate("Dialog", u"English to Korean", None))
        self.chkKtE.setText(QCoreApplication.translate("Dialog", u"Korean to English", None))
        self.showAnswer.setTitle(QCoreApplication.translate("Dialog", u"Show Right Answer?", None))
        self.rbAnsY.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.rbAnsN.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.showPrefix.setTitle(QCoreApplication.translate("Dialog", u"Show PreFix(s)?", None))
        self.rbPreY.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.rbPreN.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.shuffle.setTitle(QCoreApplication.translate("Dialog", u"Shuffle", None))
    # retranslateUi

class SettingUI(object):
    def setupUi(self, Dialog, SCALE):
        Dialog.setFixedSize(420*SCALE, 330*SCALE)

        #set Exam Type
        self.examType = QGroupBox(Dialog)
        self.examType.setGeometry(QRect(10*SCALE, 10*SCALE, 291*SCALE, 61*SCALE))
        self.glType = QGridLayout(self.examType)
        
        self.rbTypeW = QRadioButton(self.examType)
        self.rbTypeW.setChecked(True)
        self.glType.addWidget(self.rbTypeW, 1, 0, 1, 1)

        self.spType = QSpacerItem(68, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.glType.addItem(self.spType, 1, 1, 1, 1)

        self.rbTypeC = QRadioButton(self.examType)
        self.glType.addWidget(self.rbTypeC, 1, 2, 1, 1)
        #end Type
        
        #Question Mode group box
        self.qusMod = QGroupBox(Dialog)
        self.qusMod.setGeometry(QRect(10*SCALE, 80*SCALE, 191*SCALE, 131*SCALE))
        self.glMod = QGridLayout(self.qusMod)
        
        self.chkEtK = QCheckBox(self.qusMod)
        self.chkEtK.setChecked(True)
        self.glMod.addWidget(self.chkEtK, 0, 0, 1, 1)

        self.chkKtE = QCheckBox(self.qusMod)
        self.chkKtE.setChecked(True)
        self.glMod.addWidget(self.chkKtE, 1, 0, 1, 1)
        #end Question Mode

        #set Shuffle Num
        self.shuffle = QGroupBox(Dialog)
        self.shuffle.setGeometry(QRect(320*SCALE, 10*SCALE, 91*SCALE, 63*SCALE))
        self.glShuffle = QGridLayout(self.shuffle)
        
        self.spinShuffle = QSpinBox(self.shuffle)
        self.spinShuffle.setMaximum(99)
        self.spinShuffle.setValue(10)
        self.glShuffle.addWidget(self.spinShuffle, 0, 0, 1, 1)
        #end Shuffle

        #seperator
        self.lnSep = QFrame(Dialog)
        self.lnSep.setGeometry(QRect(210*SCALE, 80*SCALE, 3*SCALE, 131*SCALE))
        self.lnSep.setFrameShape(QFrame.VLine)
        self.lnSep.setFrameShadow(QFrame.Sunken)
        #end seperator
        
        #bottom Buttons
        self.btnStart = QPushButton(Dialog)
        self.btnStart.setGeometry(QRect(320*SCALE, 290*SCALE, 93*SCALE, 28*SCALE))
        self.btnApply = QPushButton(Dialog)
        self.btnApply.setGeometry(QRect(220*SCALE, 290*SCALE, 93*SCALE, 28*SCALE))
        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setGeometry(QRect(10*SCALE, 290*SCALE, 93*SCALE, 28*SCALE))
        #end Buttons
        
        #Short Answer
        
        #Prefix Group group box
        self.showPrefix = QGroupBox(Dialog)
        self.showPrefix.setGeometry(QRect(220*SCALE, 80*SCALE, 191*SCALE, 62*SCALE))
        self.glPrefix = QGridLayout(self.showPrefix)

        self.rbPreY = QRadioButton(self.showPrefix)
        self.rbPreY.setChecked(True)
        self.glPrefix.addWidget(self.rbPreY, 0, 0, 1, 1)
        
        self.spPre = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.glPrefix.addItem(self.spPre, 0, 1, 1, 1)

        self.rbPreN = QRadioButton(self.showPrefix)
        self.glPrefix.addWidget(self.rbPreN, 0, 2, 1, 1)
        #end Prefix
        
        #Set Show Answer
        self.showAnswer = QGroupBox(Dialog)
        self.showAnswer.setGeometry(QRect(220*SCALE, 150*SCALE, 191*SCALE, 62*SCALE))
        self.glShowAnswer = QGridLayout(self.showAnswer)
        
        self.rbAnsY = QRadioButton(self.showAnswer)
        self.rbAnsY.setChecked(True)
        self.glShowAnswer.addWidget(self.rbAnsY, 0, 0, 1, 1)

        self.spOX = QSpacerItem(54, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.glShowAnswer.addItem(self.spOX, 0, 1, 1, 1)

        self.rbAnsN = QRadioButton(self.showAnswer)
        self.glShowAnswer.addWidget(self.rbAnsN, 0, 2, 1, 1)
        #end ShowAnswer
        
        self.showPrefix.hide()
        self.showAnswer.hide()
        #end Short Answer
        
        #Selection
        
        #Timeout
        self.timeout = QGroupBox(Dialog)
        self.timeout.setGeometry(QRect(220*SCALE, 80*SCALE, 191*SCALE, 131*SCALE))
        self.glTimeout = QGridLayout(self.timeout)
        self.chkTimeout = QCheckBox(self.timeout)
        self.chkTimeout.setChecked(True)

        self.glTimeout.addWidget(self.chkTimeout, 0, 0, 1, 2)

        self.lbShow = QLabel(self.timeout)
        self.glTimeout.addWidget(self.lbShow, 1, 0, 1, 1)

        self.spinShow = QDoubleSpinBox(self.timeout)
        self.spinShow.setDecimals(1)
        self.glTimeout.addWidget(self.spinShow, 2, 0, 1, 1)

        self.spinSel = QDoubleSpinBox(self.timeout)
        self.spinSel.setDecimals(1)
        self.glTimeout.addWidget(self.spinSel, 2, 1, 1, 1)

        self.lbSelect = QLabel(self.timeout)
        self.glTimeout.addWidget(self.lbSelect, 1, 1, 1, 1)
        
        self.timeout.hide()
        #end Timeout
        
        #end Selection
        
        #Split setting
        self.split = QGroupBox(Dialog)
        self.split.setGeometry(QRect(10*SCALE, 220*SCALE, 401*SCALE, 61*SCALE))
        self.glsplit = QGridLayout(self.split)
        
        self.chkSplit = QCheckBox(self.split)
        self.chkSplit.setChecked(False)
        self.glsplit.addWidget(self.chkSplit, 0, 0, 1, 1)
        
        self.splitWrap=QWidget(Dialog)
        self.glsplit.addWidget(self.splitWrap,1,0,1,1)
        self.glWrap=QGridLayout(self.splitWrap)

        self.lbSize = QLabel(self.splitWrap)
        self.glWrap.addWidget(self.lbSize, 0, 0, 1, 1)
        
        self.spinSize = QSpinBox(self.splitWrap)
        self.glWrap.addWidget(self.spinSize, 0, 1, 1, 1)
        
        self.lbNo = QLabel(self.splitWrap)
        self.glWrap.addWidget(self.lbNo, 0, 2, 1, 1)
        
        self.spinNo = QSpinBox(self.splitWrap)
        self.glWrap.addWidget(self.spinNo, 0, 3, 1, 1)
        
        self.lbStart = QLabel(self.splitWrap)
        self.glWrap.addWidget(self.lbStart, 1, 0, 1, 1)

        self.spinStart = QSpinBox(self.splitWrap)
        self.glWrap.addWidget(self.spinStart, 1, 1, 1, 1)

        self.lbEnd = QLabel(self.splitWrap)
        self.glWrap.addWidget(self.lbEnd, 1, 2, 1, 1)

        self.spinEnd = QSpinBox(self.splitWrap)
        self.glWrap.addWidget(self.spinEnd, 1, 3, 1, 1)
        
        self.splitWrap.hide()
        #end Split
        
        
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings - WordTest", None))
        
        self.examType.setTitle(QCoreApplication.translate("Dialog", u"Exan Type?", None))
        self.rbTypeW.setText(QCoreApplication.translate("Dialog", u"Short-Anwer", None))
        self.rbTypeC.setText(QCoreApplication.translate("Dialog", u"Choice", None))
        
        self.qusMod.setTitle(QCoreApplication.translate("Dialog", u"Question Mode", None))
        self.chkEtK.setText(QCoreApplication.translate("Dialog", u"English to Korean", None))
        self.chkKtE.setText(QCoreApplication.translate("Dialog", u"Korean to English", None))
        
        self.shuffle.setTitle(QCoreApplication.translate("Dialog", u"Shuffle", None))
        
        self.btnStart.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.btnApply.setText(QCoreApplication.translate("Dialog", u"Apply", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        
        self.showPrefix.setTitle(QCoreApplication.translate("Dialog", u"Show PreFix(s)?", None))
        self.rbPreY.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.rbPreN.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.showAnswer.setTitle(QCoreApplication.translate("Dialog", u"Show Right Answer?", None))
        self.rbAnsY.setText(QCoreApplication.translate("Dialog", u"Yes", None))
        self.rbAnsN.setText(QCoreApplication.translate("Dialog", u"No", None))
        
        self.timeout.setTitle(QCoreApplication.translate("Dialog", u"Timeout", None))
        self.chkTimeout.setText(QCoreApplication.translate("Dialog", u"Enabled", None))
        self.lbShow.setText(QCoreApplication.translate("Dialog", u"Show", None))
        self.lbSelect.setText(QCoreApplication.translate("Dialog", u"Select", None))
        
        self.split.setTitle(QCoreApplication.translate("Dialog", u"Split", None))
        self.lbSize.setText(QCoreApplication.translate("Dialog", u"Size", None))
        self.lbNo.setText(QCoreApplication.translate("Dialog", u"No.", None))
        self.lbStart.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.lbEnd.setText(QCoreApplication.translate("Dialog", u"End", None))
        
        self.chkSplit.setText(QCoreApplication.translate("Dialog", u"Disabled", None))
    # retranslateUi

class TestUI(object):
    def setupUi(self, Dialog, SCALE):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(780*SCALE, 600*SCALE)
        
        #make result indicator
        #base
        self.gbResult = QGroupBox(Dialog)
        self.gbResult.setObjectName(u"gbResult")
        self.gbResult.setGeometry(QRect(20*SCALE, 10*SCALE, 741*SCALE, 121*SCALE))
        
        self.glwResult = QWidget(self.gbResult)
        self.glwResult.setObjectName(u"glwResult")
        self.glwResult.setGeometry(QRect(0*SCALE, 20*SCALE, 741*SCALE, 81*SCALE))
        
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
        self.scQus.setGeometry(QRect(20*SCALE, 150*SCALE, 741*SCALE, 381*SCALE))
        self.scQus.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scQus.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scQus.setWidgetResizable(True)
        
        self.boxQus = QWidget()
        self.boxQus.setObjectName(u"boxQus")
        self.boxQus.setGeometry(QRect(0*SCALE, 0*SCALE, 718*SCALE, 379*SCALE))

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
        self.btnEnd.setGeometry(QRect(670*SCALE, 550*SCALE, 93*SCALE, 28*SCALE))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"WordTest", None))
        self.gbResult.setTitle(QCoreApplication.translate("Dialog", u"Result", None))
        self.btnEnd.setText(QCoreApplication.translate("Dialog", u"Grading", None))


class SelectTestUI(object):
    def setupUi(self, Dialog, SCALE):
        Dialog.setFixedSize(640*SCALE, 480*SCALE)
        
        #main grid widget and layout
        self.glwMain = QWidget(Dialog)
        self.glwMain.setGeometry(QRect(0*SCALE, 0*SCALE, 641*SCALE, 481*SCALE))

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
        self.btnPause.setGeometry(QRect(20*SCALE, 15*SCALE, 55*SCALE, 28*SCALE))
        
        self.btnSkip = QPushButton(Dialog)
        self.btnSkip.setGeometry(QRect(570*SCALE, 15*SCALE, 50*SCALE, 28*SCALE))
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