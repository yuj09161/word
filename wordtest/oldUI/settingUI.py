from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class SettingUI(object):
    def setupUi(self, Dialog):
        Dialog.setFixedSize(420, 330)

        #set Exam Type
        self.examType = QGroupBox(Dialog)
        self.examType.setGeometry(QRect(10, 10, 291, 61))
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
        self.qusMod.setGeometry(QRect(10, 80, 191, 131))
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
        self.shuffle.setGeometry(QRect(320, 10, 91, 63))
        self.glShuffle = QGridLayout(self.shuffle)
        
        self.spinShuffle = QSpinBox(self.shuffle)
        self.spinShuffle.setMaximum(99)
        self.spinShuffle.setValue(10)
        self.glShuffle.addWidget(self.spinShuffle, 0, 0, 1, 1)
        #end Shuffle

        #seperator
        self.lnSep = QFrame(Dialog)
        self.lnSep.setGeometry(QRect(210, 80, 3, 131))
        self.lnSep.setFrameShape(QFrame.VLine)
        self.lnSep.setFrameShadow(QFrame.Sunken)
        #end seperator
        
        #bottom Buttons
        self.btnStart = QPushButton(Dialog)
        self.btnStart.setGeometry(QRect(320, 290, 93, 28))
        self.btnApply = QPushButton(Dialog)
        self.btnApply.setGeometry(QRect(220, 290, 93, 28))
        self.btnCancel = QPushButton(Dialog)
        self.btnCancel.setGeometry(QRect(10, 290, 93, 28))
        #end Buttons
        
        #Short Answer
        
        #Prefix Group group box
        self.showPrefix = QGroupBox(Dialog)
        self.showPrefix.setGeometry(QRect(220, 80, 191, 62))
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
        self.showAnswer.setGeometry(QRect(220, 150, 191, 62))
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
        self.timeout.setGeometry(QRect(220, 80, 191, 131))
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
        self.split.setGeometry(10, 220, 401, 61)
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

