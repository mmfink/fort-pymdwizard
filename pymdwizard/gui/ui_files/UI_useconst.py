# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'useconst.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 130)
        Form.setMinimumSize(QtCore.QSize(0, 130))
        Form.setMaximumSize(QtCore.QSize(16777215, 165))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(3, 3, 3, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("font: italic;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fgdc_useconst = GrowingTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_useconst.sizePolicy().hasHeightForWidth())
        self.fgdc_useconst.setSizePolicy(sizePolicy)
        self.fgdc_useconst.setMinimumSize(QtCore.QSize(0, 45))
        self.fgdc_useconst.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fgdc_useconst.setObjectName("fgdc_useconst")
        self.verticalLayout.addWidget(self.fgdc_useconst)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Data Use Constraints"))
        self.label.setText(_translate("Form", "Describe any restrictions or legal prerequisites for USING the dataset.  Use Constraints may include restrictions applied to assure the protection of privacy or intellectual property, and any special restrictions or limitations on using the dataset."))
        self.fgdc_useconst.setPlainText(_translate("Form", "None.  Users are advised to read the dataset\'s metadata thoroughly to understand appropriate use and data limitations."))

from growingtextedit import GrowingTextEdit
