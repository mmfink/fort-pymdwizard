# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_date.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_sngdate(object):
    def setupUi(self, fgdc_sngdate):
        fgdc_sngdate.setObjectName("fgdc_sngdate")
        fgdc_sngdate.resize(210, 47)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fgdc_sngdate)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_format = QtWidgets.QWidget(fgdc_sngdate)
        self.widget_format.setObjectName("widget_format")
        self.layout_format = QtWidgets.QHBoxLayout(self.widget_format)
        self.layout_format.setContentsMargins(0, 0, 6, 0)
        self.layout_format.setSpacing(0)
        self.layout_format.setObjectName("layout_format")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_format.addItem(spacerItem)
        self.lbl_format = QtWidgets.QLabel(self.widget_format)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_format.sizePolicy().hasHeightForWidth())
        self.lbl_format.setSizePolicy(sizePolicy)
        self.lbl_format.setStyleSheet("font: italic;")
        self.lbl_format.setObjectName("lbl_format")
        self.layout_format.addWidget(self.lbl_format)
        self.verticalLayout.addWidget(self.widget_format)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(fgdc_sngdate)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fgdc_caldate = QtWidgets.QLineEdit(fgdc_sngdate)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_caldate.sizePolicy().hasHeightForWidth())
        self.fgdc_caldate.setSizePolicy(sizePolicy)
        self.fgdc_caldate.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fgdc_caldate.setObjectName("fgdc_caldate")
        self.horizontalLayout.addWidget(self.fgdc_caldate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fgdc_sngdate)
        QtCore.QMetaObject.connectSlotsByName(fgdc_sngdate)

    def retranslateUi(self, fgdc_sngdate):
        _translate = QtCore.QCoreApplication.translate
        fgdc_sngdate.setWindowTitle(_translate("fgdc_sngdate", "Form"))
        self.lbl_format.setText(_translate("fgdc_sngdate", "YYYYMMDD"))
        self.label.setText(_translate("fgdc_sngdate", "Date"))

