# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailed.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_detailed(object):
    def setupUi(self, fgdc_detailed):
        fgdc_detailed.setObjectName("fgdc_detailed")
        fgdc_detailed.resize(1221, 794)
        self.horizontalLayout = QtWidgets.QHBoxLayout(fgdc_detailed)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(fgdc_detailed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fgdc_enttyp = QtWidgets.QGroupBox(self.frame)
        self.fgdc_enttyp.setObjectName("fgdc_enttyp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fgdc_enttyp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.fgdc_enttyp)
        self.label.setStyleSheet("font: italic 8pt;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btn_browse = QtWidgets.QPushButton(self.fgdc_enttyp)
        self.btn_browse.setObjectName("btn_browse")
        self.verticalLayout.addWidget(self.btn_browse)
        self.label_2 = QtWidgets.QLabel(self.fgdc_enttyp)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.fgdc_enttypl = QtWidgets.QLineEdit(self.fgdc_enttyp)
        self.fgdc_enttypl.setObjectName("fgdc_enttypl")
        self.verticalLayout.addWidget(self.fgdc_enttypl)
        self.label_3 = QtWidgets.QLabel(self.fgdc_enttyp)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.fgdc_enttypd = QtWidgets.QPlainTextEdit(self.fgdc_enttyp)
        self.fgdc_enttypd.setObjectName("fgdc_enttypd")
        self.verticalLayout.addWidget(self.fgdc_enttypd)
        self.label_4 = QtWidgets.QLabel(self.fgdc_enttyp)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.fgdc_enttypds = QtWidgets.QLineEdit(self.fgdc_enttyp)
        self.fgdc_enttypds.setObjectName("fgdc_enttypds")
        self.verticalLayout.addWidget(self.fgdc_enttypds)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.fgdc_enttyp)
        self.btn_remove = QtWidgets.QPushButton(self.frame)
        self.btn_remove.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 0, 0, 100), stop:1 rgba(147, 0, 0, 50));\n"
"")
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout_2.addWidget(self.btn_remove)
        self.horizontalLayout.addWidget(self.frame)
        self.attribute_frame = QtWidgets.QFrame(fgdc_detailed)
        self.attribute_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.attribute_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attribute_frame.setObjectName("attribute_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.attribute_frame)
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.attribute_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(15, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout.addWidget(self.attribute_frame)

        self.retranslateUi(fgdc_detailed)
        QtCore.QMetaObject.connectSlotsByName(fgdc_detailed)

    def retranslateUi(self, fgdc_detailed):
        _translate = QtCore.QCoreApplication.translate
        fgdc_detailed.setWindowTitle(_translate("fgdc_detailed", "Form"))
        self.fgdc_enttyp.setTitle(_translate("fgdc_detailed", "Dataset "))
        self.label.setText(_translate("fgdc_detailed", "If you have access to the dataset being documented in this metadata record browse to it by clicking the button below.\n"
"\n"
"This section will be autopopulated with appropriate content pulled from the data (column labels, min/max values, unique lists, etc.)."))
        self.btn_browse.setText(_translate("fgdc_detailed", "Browse to Dataset"))
        self.label_2.setText(_translate("fgdc_detailed", "Dataset Label"))
        self.label_3.setText(_translate("fgdc_detailed", "Dataset Description"))
        self.label_4.setText(_translate("fgdc_detailed", "Definition Sourse"))
        self.fgdc_enttypds.setText(_translate("fgdc_detailed", "Producer defined"))
        self.btn_remove.setText(_translate("fgdc_detailed", "Remove this Detailed"))
        self.label_5.setToolTip(_translate("fgdc_detailed", "Required"))
        self.label_5.setText(_translate("fgdc_detailed", "<html><head/><body><p><span style=\" font-style:italic; color:#55aaff;\">These represent the columns in your dataset.  Click below in each one and provide a definition for the column and a description for the column contents.</span></p></body></html>"))

