# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Citation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1017, 568)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.fgdc_citeinfo = QtWidgets.QGroupBox(Form)
        self.fgdc_citeinfo.setGeometry(QtCore.QRect(9, 9, 1001, 200))
        self.fgdc_citeinfo.setMinimumSize(QtCore.QSize(0, 200))
        self.fgdc_citeinfo.setObjectName("fgdc_citeinfo")
        self.fgdc_title = QtWidgets.QLineEdit(self.fgdc_citeinfo)
        self.fgdc_title.setGeometry(QtCore.QRect(20, 70, 901, 20))
        self.fgdc_title.setObjectName("fgdc_title")
        self.label = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 731, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 361, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_5.setGeometry(QtCore.QRect(410, 90, 181, 16))
        self.label_5.setObjectName("label_5")
        self.fgdc_origin = QtWidgets.QLineEdit(self.fgdc_citeinfo)
        self.fgdc_origin.setGeometry(QtCore.QRect(20, 130, 361, 20))
        self.fgdc_origin.setObjectName("fgdc_origin")
        self.fgdc_pubdate = QtWidgets.QLineEdit(self.fgdc_citeinfo)
        self.fgdc_pubdate.setGeometry(QtCore.QRect(410, 130, 211, 20))
        self.fgdc_pubdate.setObjectName("fgdc_pubdate")
        self.label_9 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_9.setGeometry(QtCore.QRect(690, 90, 161, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.fgdc_citeinfo)
        self.lineEdit.setGeometry(QtCore.QRect(690, 130, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_10 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_10.setGeometry(QtCore.QRect(690, 110, 301, 16))
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_6.setGeometry(QtCore.QRect(410, 110, 281, 16))
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_15.setGeometry(QtCore.QRect(450, 160, 451, 21))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_16.setGeometry(QtCore.QRect(20, 160, 361, 16))
        self.label_16.setObjectName("label_16")
        self.groupBox_2 = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 160, 101, 21))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 0, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.fgdc_citeinfo)
        self.groupBox_3.setGeometry(QtCore.QRect(820, 160, 101, 21))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(60, 0, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.label_17 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_17.setGeometry(QtCore.QRect(20, 180, 411, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.fgdc_citeinfo)
        self.label_18.setGeometry(QtCore.QRect(450, 180, 431, 16))
        self.label_18.setObjectName("label_18")
        self.fgdc_title.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.fgdc_origin.raise_()
        self.fgdc_pubdate.raise_()
        self.label_9.raise_()
        self.lineEdit.raise_()
        self.label_10.raise_()
        self.label_6.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.lworkcit = QtWidgets.QGroupBox(Form)
        self.lworkcit.setGeometry(QtCore.QRect(10, 360, 1001, 191))
        self.lworkcit.setObjectName("lworkcit")
        self.label_11 = QtWidgets.QLabel(self.lworkcit)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 171, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.lworkcit)
        self.label_12.setGeometry(QtCore.QRect(500, 10, 221, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.lworkcit)
        self.label_13.setGeometry(QtCore.QRect(190, 100, 191, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.lworkcit)
        self.label_14.setGeometry(QtCore.QRect(10, 100, 191, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 60, 461, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox = QtWidgets.QComboBox(self.lworkcit)
        self.comboBox.setGeometry(QtCore.QRect(10, 130, 141, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_7.setGeometry(QtCore.QRect(190, 130, 141, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_23 = QtWidgets.QLabel(self.lworkcit)
        self.label_23.setGeometry(QtCore.QRect(380, 100, 81, 16))
        self.label_23.setObjectName("label_23")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_8.setGeometry(QtCore.QRect(374, 130, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.listWidget = QtWidgets.QListWidget(self.lworkcit)
        self.listWidget.setGeometry(QtCore.QRect(500, 30, 161, 61))
        self.listWidget.setObjectName("listWidget")
        self.label_24 = QtWidgets.QLabel(self.lworkcit)
        self.label_24.setGeometry(QtCore.QRect(720, 30, 131, 16))
        self.label_24.setObjectName("label_24")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_9.setGeometry(QtCore.QRect(720, 50, 231, 21))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_25 = QtWidgets.QLabel(self.lworkcit)
        self.label_25.setGeometry(QtCore.QRect(720, 70, 131, 16))
        self.label_25.setObjectName("label_25")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_10.setGeometry(QtCore.QRect(720, 90, 231, 21))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_26 = QtWidgets.QLabel(self.lworkcit)
        self.label_26.setGeometry(QtCore.QRect(720, 120, 131, 16))
        self.label_26.setObjectName("label_26")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_11.setGeometry(QtCore.QRect(720, 140, 231, 21))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_27 = QtWidgets.QLabel(self.lworkcit)
        self.label_27.setGeometry(QtCore.QRect(500, 140, 211, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_12.setGeometry(QtCore.QRect(500, 160, 211, 21))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_28 = QtWidgets.QLabel(self.lworkcit)
        self.label_28.setGeometry(QtCore.QRect(500, 100, 181, 16))
        self.label_28.setObjectName("label_28")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.lworkcit)
        self.lineEdit_13.setGeometry(QtCore.QRect(500, 120, 211, 21))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(400, 340, 451, 21))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 361, 16))
        self.label_7.setObjectName("label_7")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(280, 340, 101, 21))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 0, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 451, 101))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(210, 20, 231, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 50, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 50, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(460, 210, 551, 101))
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 50, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(220, 20, 231, 16))
        self.label_22.setObjectName("label_22")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 50, 201, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fgdc_citeinfo.setTitle(_translate("Form", "Citation"))
        self.label.setText(_translate("Form", "Data Set Title"))
        self.label_2.setText(_translate("Form", "A good title includes \'What\', \'Where\', and \'When\'.  (Example: Point Locations of Wind Turbines in Colorado, Derived from 2010 NAIP Imagery"))
        self.label_3.setText(_translate("Form", "Data Set Author / Originator"))
        self.label_4.setText(_translate("Form", "Who created the data set? List the organization and/or person(s)"))
        self.label_5.setText(_translate("Form", "Publication Date (YYYYMMDD)"))
        self.label_9.setText(_translate("Form", "Online Link for the Data Set"))
        self.label_10.setText(_translate("Form", "Is there a link to the data or agency that produced it?"))
        self.label_6.setText(_translate("Form", "When was the data set published or finalized?"))
        self.label_15.setText(_translate("Form", "Can you provide more publication information about this data set?"))
        self.label_16.setText(_translate("Form", "Is this data set part of a series?"))
        self.radioButton_3.setText(_translate("Form", "Yes"))
        self.radioButton_4.setText(_translate("Form", "No"))
        self.radioButton_5.setText(_translate("Form", "Yes"))
        self.radioButton_6.setText(_translate("Form", "No"))
        self.label_17.setText(_translate("Form", "Is it a release with an assigned issue number (e.g. USGS Data Series)"))
        self.label_18.setText(_translate("Form", "More details are always helpful for finding and properly referencing data."))
        self.lworkcit.setTitle(_translate("Form", "Larger Work"))
        self.label_11.setText(_translate("Form", "Title of Larger Work"))
        self.label_12.setText(_translate("Form", "Author / Originator of Larger Work"))
        self.label_13.setText(_translate("Form", "Publication Date (YYYYMMDD)"))
        self.label_14.setText(_translate("Form", "Larger Work Format"))
        self.comboBox.setItemText(0, _translate("Form", "Publication (Book)"))
        self.comboBox.setItemText(1, _translate("Form", "Publication (Journal)"))
        self.comboBox.setItemText(2, _translate("Form", "Publication (Other)"))
        self.comboBox.setItemText(3, _translate("Form", "Ongoing Project"))
        self.comboBox.setItemText(4, _translate("Form", "Website"))
        self.comboBox.setItemText(5, _translate("Form", "GIS Data Project/Collection"))
        self.comboBox.setItemText(6, _translate("Form", "GIS Data Service"))
        self.comboBox.setItemText(7, _translate("Form", "Other"))
        self.label_23.setText(_translate("Form", "Edition"))
        self.label_24.setText(_translate("Form", "Publisher"))
        self.label_25.setText(_translate("Form", "Publication Place"))
        self.label_26.setText(_translate("Form", "Online Link"))
        self.label_27.setText(_translate("Form", "Issue Name / Number within Series"))
        self.label_28.setText(_translate("Form", "Series of Journal Name"))
        self.label_8.setText(_translate("Form", "If the citation of a larger project is relevant, you may optionally cite it here."))
        self.label_7.setText(_translate("Form", "Is this data set associated with a larger work?"))
        self.radioButton.setText(_translate("Form", "Yes"))
        self.radioButton_2.setText(_translate("Form", "No"))
        self.label_19.setText(_translate("Form", "Series Name"))
        self.label_20.setText(_translate("Form", "Issue Name / Number within Series"))
        self.label_21.setText(_translate("Form", "Publication Place"))
        self.label_22.setText(_translate("Form", "Publisher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

