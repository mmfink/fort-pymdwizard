#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Contact Info <cntinfo> widget


SCRIPT DEPENDENCIES
------------------------------------------------------------------------------
    None


U.S. GEOLOGICAL SURVEY DISCLAIMER
------------------------------------------------------------------------------
Any use of trade, product or firm names is for descriptive purposes only and
does not imply endorsement by the U.S. Geological Survey.

Although this information product, for the most part, is in the public domain,
it also contains copyrighted material as noted in the text. Permission to
reproduce copyrighted items for other than personal use must be secured from
the copyright owner.

Although these data have been processed successfully on a computer system at
the U.S. Geological Survey, no warranty, expressed or implied is made
regarding the display or utility of the data on any other system, or for
general or scientific purposes, nor shall the act of distribution constitute
any such warranty. The U.S. Geological Survey shall not be held liable for
improper or incorrect use of the data described and/or contained herein.

Although this program has been used by the U.S. Geological Survey (USGS), no
warranty, expressed or implied, is made by the USGS or the U.S. Government as
to the accuracy and functioning of the program and related program material
nor shall the fact of distribution constitute any such warranty, and no
responsibility is assumed by the USGS in connection therewith.
------------------------------------------------------------------------------
"""

import sys

from lxml import etree

from PyQt5.QtGui import QPainter, QFont, QPalette, QBrush, QColor, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
from PyQt5.QtWidgets import QWidget, QLineEdit, QSizePolicy, QComboBox, QTableView, QRadioButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QStyleOptionHeader, QHeaderView, QStyle
from PyQt5.QtCore import QAbstractItemModel, QModelIndex, QSize, QRect, QPoint

from pymdwizard.core import utils
from pymdwizard.core import xml_utils

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_ContactInfo
from pymdwizard.gui.ui_files import UI_USGSContactImporter

class ContactInfo(WizardWidget):
    xpath_root = "cntinfo"
    drag_label = "Contact Information <cntinfo>"

    # This dictionary provides a mechanism for crosswalking between
    # gui elements (pyqt widgets) and the xml document
    xpath_lookup = {'cntper': 'cntperp/cntper',
                    'cntorg': 'cntperp/cntorg',
                    'cntpos': 'cntpos',
                    'address': 'cntaddr/address',
                    'address2': 'cntaddr/address[2]',
                    'address3': 'cntaddr/address[3]',
                    'city': 'cntaddr/city',
                    'state': 'cntaddr/state',
                    'postal': 'cntaddr/postal',
                    'state': 'cntaddr/state',
                    'country': 'cntaddr/country',
                    'addrtype': 'cntaddr/addrtype',
                    'cntvoice': 'cntvoice',
                    'cntfax': 'cntfax',
                    'cntemail': 'cntemail'}

    ui_class = UI_ContactInfo.Ui_USGSContactInfoWidget

    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.btn_import_contact.clicked.connect(self.find_usgs_contact)
        self.ui.rbtn_perp.toggled.connect(self.switch_primary)

    def find_usgs_contact(self):
        self.usgs_contact = QDialog(self)
        self.usgs_contact_ui = UI_USGSContactImporter.Ui_ImportUsgsUser()
        self.usgs_contact_ui.setupUi(self.usgs_contact)
        self.usgs_contact_ui.btn_OK.clicked.connect(self.add_contact)
        self.usgs_contact_ui.btn_cancel.clicked.connect(self.cancel)

        self.usgs_contact.show()

    def add_contact(self):
        username = self.usgs_contact_ui.le_usgs_ad_name.text()
        # strip off the @usgs.gov if they entered one
        username = username.split("@")[0]

        cntperp = utils.get_usgs_contact_info(username,
                                              as_dictionary=False)
        if cntperp.getchildren()[0].getchildren()[0].text.strip():
            self._from_xml(cntperp)
            self.usgs_contact.deleteLater()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("'{}' Not Found".format(username))
            msg.setInformativeText("The Metadata Wizard was unable to locate the provided user name in the USGS directory")
            msg.setWindowTitle("Name Not Found")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.exec_()

    def cancel(self):
        self.usgs_contact.deleteLater()

    def switch_primary(self):
        """
        Switches form to reflect either organization or person primary

        Returns
        -------
        None
        """
        if self.ui.rbtn_perp.isChecked():
            self.ui.left_vertical_layout.insertWidget(0, self.ui.lbl_cntper)
            self.ui.required_horizontal_layout.insertWidget(0, self.ui.cntper)
            self.ui.left_vertical_layout.insertWidget(2, self.ui.lbl_cntorg)
            self.ui.optional_horizontal_layout.insertWidget(0, self.ui.cntorg)
        else:
            self.ui.left_vertical_layout.insertWidget(0, self.ui.lbl_cntorg)
            self.ui.required_horizontal_layout.insertWidget(0, self.ui.cntorg)
            self.ui.left_vertical_layout.insertWidget(2, self.ui.lbl_cntper)
            self.ui.optional_horizontal_layout.insertWidget(0, self.ui.cntper)

    def dragEnterEvent(self, e):
        """

        Parameters
        ----------
        e : qt event

        Returns
        -------

        """
        print("cinfo drag enter")
        mime_data = e.mimeData()
        if e.mimeData().hasFormat('text/plain'):
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            element = etree.fromstring(mime_data.text(), parser=parser)
            if element.tag == 'ptcontac' or element.tag == 'cntinfo':
                e.accept()
        else:
            e.ignore()

    def _to_xml(self):

        cntinfo = etree.Element("cntinfo")

        cntper = etree.Element("cntper")
        cntper.text = self.findChild(QLineEdit, "cntper").text()
        cntorg = etree.Element("cntorg")
        cntorg.text = self.findChild(QLineEdit, "cntorg").text()

        rbtn_perp = self.findChild(QRadioButton, 'rbtn_perp')
        if rbtn_perp.isChecked():
            cntperp = etree.Element("cntperp")
            cntperp.append(cntper)
            cntperp.append(cntorg)
            cntinfo.append(cntperp)
        else:
            cntorgp = etree.Element("cntorgp")
            cntorgp.append(cntorg)
            cntorgp.append(cntper)
            cntinfo.append(cntorgp)

        cntpos = etree.Element("cntpos")
        cntpos.text = self.findChild(QLineEdit, "cntpos").text()
        cntinfo.append(cntpos)

        cntaddr = etree.Element("cntaddr")
        addrtype = etree.Element("addrtype")
        addrtype.text = self.findChild(QComboBox, "addrtype").currentText()
        cntaddr.append(addrtype)

        for label in ['address', 'address2', 'address3', 'city', 'state',
                      'postal', 'country']:
            widget = self.findChild(QLineEdit, label)
            try:
                node = etree.Element(label)
                node.text = widget.text()
                cntaddr.append(node)
            except:
                pass

        cntinfo.append(cntaddr)

        for label in ['cntvoice', 'cntfax', 'cntemail']:
            widget = self.findChild(QLineEdit, label)
            try:
                node = etree.Element(label)
                node.text = widget.text()
                cntinfo.append(node)
            except:
                pass

        return cntinfo

    def _from_xml(self, contact_information):
        contact_dict = xml_utils.node_to_dict(contact_information)
        utils.populate_widget(self, contact_dict)

        addrtype_widget = self.findChild(QComboBox, 'addrtype')


        if 'cntinfo' in contact_dict:
            contact_dict = contact_dict['cntinfo']

        try:
            addrtype = contact_dict['cntaddr']['addrtype']
            addrtype_widget.setEditText(addrtype)
        except KeyError:
            pass

        try:
            if 'cntorgp' in contact_dict:
                rbtn_orgp = self.findChild(QRadioButton, 'rbtn_orgp')
                rbtn_orgp.setChecked(True)
            elif 'cntperp' in contact_dict:
                rbtn_perp = self.findChild(QRadioButton, 'rbtn_perp')
                rbtn_perp.setChecked(True)
        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(ContactInfo)