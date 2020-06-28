# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class SelectUI(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setFixedSize(650, 530)
        
        #exam file group
        self.tests = QGroupBox(Dialog)
        self.tests.setObjectName(u"tests")
        self.tests.setGeometry(QRect(20, 20, 293, 88))
        
        self.comboTest = QComboBox(self.tests)
        self.comboTest.setObjectName(u"comboTest")
        self.comboTest.setGeometry(QRect(20, 33, 150, 22))
        
        self.btnTest = QPushButton(self.tests)
        self.btnTest.setObjectName(u"btnTest")
        self.btnTest.setGeometry(QRect(180, 30, 93, 28))
        
        #re-test file group
        self.reTests = QGroupBox(Dialog)
        self.reTests.setObjectName(u"reTests")
        self.reTests.setGeometry(QRect(337, 20, 293, 88))
        
        self.comboRe = QComboBox(self.reTests)
        self.comboRe.setObjectName(u"comboRe")
        self.comboRe.setGeometry(QRect(20, 33, 150, 22))
        
        self.btnRe = QPushButton(self.reTests)
        self.btnRe.setObjectName(u"btnRe")
        self.btnRe.setGeometry(QRect(180, 30, 93, 28))
        
        #selected file(s) list
        self.fileList = QListWidget(Dialog)
        self.fileList.setObjectName(u"fileList")
        self.fileList.setGeometry(QRect(20, 120, 611, 341))
        self.fileList.setDragDropMode(QAbstractItemView.InternalMove)
        self.fileList.setDefaultDropAction(Qt.MoveAction)
        
        #setting button
        self.btnSetting = QPushButton(Dialog)
        self.btnSetting.setObjectName(u"btnSetting")
        self.btnSetting.setGeometry(QRect(30, 480, 93, 28))
        
        '''
        #start exam(selection type)
        self.btnSelStart = QPushButton(Dialog)
        self.btnSelStart.setObjectName(u"btnSelStart")
        self.btnSelStart.setGeometry(QRect(410, 480, 103, 28))
        '''
        
        #start button
        self.btnStart = QPushButton(Dialog)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(527, 480, 93, 28))
        
        #setting
        
        #group box for setting
        self.gbSetting = QGroupBox(Dialog)
        self.gbSetting.setObjectName(u"gbSetting")
        self.gbSetting.setGeometry(QRect(20, 520, 611, 181))
        
        #group box for question mod
        self.qusMod = QGroupBox(self.gbSetting)
        self.qusMod.setObjectName(u"qusMod")
        self.qusMod.setGeometry(QRect(10, 20, 196, 151))
        
        #widget for question mod
        self.glwMod = QWidget(self.qusMod)
        self.glwMod.setObjectName(u"glwMod")
        self.glwMod.setGeometry(QRect(13, 23, 170, 111))
        
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
        self.showAnswer.setGeometry(QRect(220, 20, 191, 71))
        
        #widget for show answer
        self.glwAns = QWidget(self.showAnswer)
        self.glwAns.setObjectName(u"glwAns")
        self.glwAns.setGeometry(QRect(13, 23, 170, 40))
        
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
        self.showPrefix.setGeometry(QRect(220, 100, 191, 71))
        
        self.glwPrefix = QWidget(self.showPrefix)
        self.glwPrefix.setObjectName(u"glwPrefix")
        self.glwPrefix.setGeometry(QRect(13, 23, 170, 40))
        
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
        self.shuffle.setGeometry(QRect(420, 20, 91, 71))
        
        self.spinShuffle = QSpinBox(self.shuffle)
        self.spinShuffle.setObjectName(u"spinShuffle")
        self.spinShuffle.setGeometry(QRect(20, 30, 42, 22))
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

