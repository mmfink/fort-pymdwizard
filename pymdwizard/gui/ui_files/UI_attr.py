# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attr.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 771)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_attr = QtWidgets.QFrame(Form)
        self.fgdc_attr.setFrameShape(QtWidgets.QFrame.Panel)
        self.fgdc_attr.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fgdc_attr.setLineWidth(2)
        self.fgdc_attr.setMidLineWidth(2)
        self.fgdc_attr.setObjectName("fgdc_attr")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_attr)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.fgdc_attr)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.fgdc_attrlabl = QtWidgets.QLineEdit(self.fgdc_attr)
        self.fgdc_attrlabl.setStyleSheet("font: bold 12pt ;")
        self.fgdc_attrlabl.setObjectName("fgdc_attrlabl")
        self.verticalLayout.addWidget(self.fgdc_attrlabl)
        self.label = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fgdc_attrdef = QtWidgets.QTextBrowser(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_attrdef.sizePolicy().hasHeightForWidth())
        self.fgdc_attrdef.setSizePolicy(sizePolicy)
        self.fgdc_attrdef.setMaximumSize(QtCore.QSize(16777215, 50))
        self.fgdc_attrdef.setObjectName("fgdc_attrdef")
        self.verticalLayout.addWidget(self.fgdc_attrdef)
        self.label_3 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fgdc_attrdefs = QtWidgets.QLineEdit(self.fgdc_attr)
        self.fgdc_attrdefs.setObjectName("fgdc_attrdefs")
        self.verticalLayout.addWidget(self.fgdc_attrdefs)
        self.label_7 = QtWidgets.QLabel(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.fgdc_attrdomv = QtWidgets.QFrame(self.fgdc_attr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_attrdomv.sizePolicy().hasHeightForWidth())
        self.fgdc_attrdomv.setSizePolicy(sizePolicy)
        self.fgdc_attrdomv.setFrameShape(QtWidgets.QFrame.Box)
        self.fgdc_attrdomv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fgdc_attrdomv.setObjectName("fgdc_attrdomv")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.fgdc_attrdomv)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addWidget(self.fgdc_attrdomv)
        self.verticalLayout_2.addWidget(self.fgdc_attr)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Column Label"))
        self.label.setText(_translate("Form", "Column Definition"))
        self.label_3.setText(_translate("Form", "Definition Source"))
        self.fgdc_attrdefs.setText(_translate("Form", "Producer Defined"))
        self.label_7.setText(_translate("Form", "Column Contents Type"))
        self.comboBox.setItemText(0, _translate("Form", "Enumerated (Categorical Data)"))
        self.comboBox.setItemText(1, _translate("Form", "Range (Numeric data)"))
        self.comboBox.setItemText(2, _translate("Form", "Codeset (Commonly Used Categories)"))
        self.comboBox.setItemText(3, _translate("Form", "Unrepresentable (None of the above)"))
