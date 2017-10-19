#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
License:            Creative Commons Attribution 4.0 International (CC BY 4.0)
                    http://creativecommons.org/licenses/by/4.0/

PURPOSE
------------------------------------------------------------------------------
Provide a pyqt widget for a Citation <citation> section


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
from copy import deepcopy
from lxml import etree

from PyQt5.QtWidgets import QMessageBox, QDialog
from PyQt5.QtCore import Qt

from pymdwizard.core import utils
from pymdwizard.core import xml_utils
from pymdwizard.core import datacite

from pymdwizard.gui.wiz_widget import WizardWidget
from pymdwizard.gui.ui_files import UI_citeinfo
from pymdwizard.gui.fgdc_date import FGDCDate
from pymdwizard.gui.repeating_element import RepeatingElement
from pymdwizard.gui.ui_files import UI_DOICiteinfoImporter

try:
    import habanero
    hananero_installed = True
except ImportError:
    hananero_installed = False

class Citeinfo(WizardWidget): #

    drag_label = "Citation information <citeinfo>"
    acceptable_tags = ['citation', 'citeinfo']

    def __init__(self, parent=None, include_lwork=True):
        self.include_lwork = include_lwork
        self.schema = 'bdp'
        WizardWidget.__init__(self, parent=parent)
        self.doi_lookup = None

    def build_ui(self, ):
        """
        Build and modify this widget's GUI

        Returns
        -------
        None
        """
        self.ui = UI_citeinfo.Ui_parent_form()
        self.ui.setupUi(self)

        if self.include_lwork:
            self.lworkcit_widget = Citeinfo(parent=self, include_lwork=False)
            self.lworkcit_widget.ui.lbl_dataset_title.setText('Larger Work Title')
            self.ui.lworkcite_widget.layout().addWidget(self.lworkcit_widget)
            self.lworkcit_widget.ui.fgdc_geoform.setEditText('publication')
        else:
            self.ui.fgdc_lworkcit.hide()
        self.include_lworkext_change(self.ui.radio_lworkyes.isChecked())

        self.ui.series_ext.hide()
        self.ui.pub_ext.hide()
        self.ui.pubdate_widget = FGDCDate(label='YYYYMMDD  ',
                                            show_format=False, required=True,
                                            fgdc_name='fgdc_pubdate')

        self.ui.pubdate_layout.addWidget(self.ui.pubdate_widget)


        self.onlink_list = RepeatingElement(add_text='Add online link',
                                            remove_text='Remove last',
                                            widget_kwargs={'label': 'Link',
                                                           'line_name':'fgdc_onlink'})
        self.onlink_list.add_another()
        self.ui.onlink_layout.addWidget(self.onlink_list)

        self.fgdc_origin = RepeatingElement(add_text='Add originator',
                                            remove_text='Remove last',
                                            widget_kwargs={'label': 'Originator',
                                                           'line_name':'fgdc_origin',
                                                           'required':True})
        self.fgdc_origin.add_another()
        self.ui.originator_layout.addWidget(self.fgdc_origin)

        self.setup_dragdrop(self)

        if not hananero_installed:
            self.ui.btn_import_doi.hide()

    def connect_events(self):
        """
        Connect the appropriate GUI components with the corresponding functions

        Returns
        -------
        None
        """
        self.ui.radio_lworkyes.toggled.connect(self.include_lworkext_change)
        self.ui.radio_seriesyes.toggled.connect(self.include_seriesext_change)
        self.ui.radio_pubinfoyes.toggled.connect(self.include_pubext_change)

        self.ui.btn_import_doi.clicked.connect(self.get_doi_citation)

    def get_doi_citation(self):
        if self.doi_lookup is None:
            self.doi_lookup = QDialog(parent=self)
            self.doi_lookup_ui = UI_DOICiteinfoImporter.Ui_ImportUsgsUser()
            self.doi_lookup_ui.setupUi(self.doi_lookup)
            self.doi_lookup_ui.btn_OK.clicked.connect(self.add_doi)
            self.doi_lookup_ui.btn_cancel.clicked.connect(self.cancel)
            utils.set_window_icon(self.doi_lookup)
        self.doi_lookup.show()

    def add_doi(self):
        doi = self.doi_lookup_ui.le_doi.text()
        try:
            citeinfo = datacite.get_doi_citation(doi)

            if citeinfo is None:
                msgbox = QMessageBox(self)
                utils.set_window_icon(msgbox)
                msgbox.setIcon(QMessageBox.Warning)
                msg = "'{}' Not Found on DataCite".format(doi)
                msg += '\nMake sure the DOI is valid and active.'
                msgbox.setText(msg)
                msgbox.setInformativeText("No matching citation found")
                msgbox.setWindowTitle("DOI Not Found")
                msgbox.setStandardButtons(QMessageBox.Ok)
                msgbox.exec_()
            else:
                self._from_xml(citeinfo.to_xml())
        except:
            msg = "We ran into a problem creating a citeinfo element from that DOI({})".format(doi)
            msg += "Check the DOI and/or manually create the citation for it"
            QMessageBox.warning(self, "Problem DOI", msg)
        self.cancel()

    def cancel(self):
        self.doi_lookup.deleteLater()
        self.doi_lookup = None

    def dragEnterEvent(self, e):
        """
        Only accept Dragged items that can be converted to an xml object with
        a root tag called in our list of acceptable_tags
        Parameters
        ----------
        e : qt event
        Returns
        -------
        """
        mime_data = e.mimeData()

        if e.mimeData().hasUrls():
            if 'doi' in e.mimeData().urls()[0].url().lower():
                e.accept()
        elif e.mimeData().hasFormat('text/plain'):
            if self.is_doi_str(mime_data.text()):
                e.accept()
            else:
                parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
                element = etree.fromstring(mime_data.text(), parser=parser)
                if element is not None and element.tag in self.acceptable_tags:
                    e.accept()
        else:
            e.ignore()

    def is_doi_str(self, string):
        return datacite.clean_doi(string).lower().strip().startswith('doi:')

    def dropEvent(self, e):
        """
        Updates the form with the contents of an xml node dropped onto it.
        Parameters
        ----------
        e : qt event
        Returns
        -------
        None
        """
        try:
            e.setDropAction(Qt.CopyAction)
            e.accept()
            mime_data = e.mimeData()
            if mime_data.hasUrls() or \
                    self.is_doi_str(mime_data.text()):
                if self.is_doi_str(mime_data.text()):
                    doi = mime_data.text()
                else:
                    doi = e.mimeData().urls()[0].url()
                try:
                    citeinfo = datacite.get_doi_citation(doi)
                    self._from_xml(citeinfo.to_xml())
                except:
                    msg = "We ran into a problem creating a citeinfo element from that DOI({})".format(doi)
                    msg += "Check the DOI and/or manually create the citation for it"
                    QMessageBox.warning(self, "Problem DOI", msg)
            else:
                element = xml_utils.string_to_node(mime_data.text())

                self._from_xml(element)
        except:
            e = sys.exc_info()[0]
            print('problem drop', e)


    def include_seriesext_change(self, b):
        """
        Extended citation to support series information of the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.series_ext.show()
        else:
            self.ui.series_ext.hide()

    def include_pubext_change(self, b):
        """
        Extended citation to support publication information of the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.pub_ext.show()
        else:
            self.ui.pub_ext.hide()

    def include_lworkext_change(self, b):
        """
        Extended citation to support a larger body of information for the record.

        Parameters
        ----------
        b: qt event

        Returns
        -------
        None
        """
        if b:
            self.ui.lworkcite_widget.show()
        else:
            self.ui.lworkcite_widget.hide()
                
    def _to_xml(self):
        """
        encapsulates the QLineEdit text in an element tag

        Returns
        -------
        citation element tag in xml tree
        """
        citeinfo = xml_utils.xml_node('citeinfo')

        for origin in self.fgdc_origin.get_widgets():
            xml_utils.xml_node('origin', text=origin.added_line.text(),
                               parent_node=citeinfo)

        pubdate = xml_utils.xml_node("pubdate",
                                     text=self.ui.pubdate_widget.get_date(),
                                     parent_node=citeinfo)
        title = xml_utils.xml_node("title", self.ui.fgdc_title.text(),
                                   parent_node=citeinfo)

        geoform = xml_utils.xml_node("geoform",
                                         self.ui.fgdc_geoform.currentText(),
                                         parent_node=citeinfo)

        if self.ui.radio_seriesyes.isChecked():
            serinfo = xml_utils.xml_node('serinfo', parent_node=citeinfo)
            sername = xml_utils.xml_node('sername',
                                         text=self.ui.fgdc_sername.text(),
                                         parent_node=serinfo)
            issue = xml_utils.xml_node('issue', text=self.ui.fgdc_issue.text(),
                                       parent_node=serinfo)

        if self.ui.radio_pubinfoyes.isChecked() and \
                (self.ui.fgdc_pubplace.text() != '' or
                 self.ui.fgdc_publish.text() != ''):
            pubinfo = xml_utils.xml_node('pubinfo', parent_node=citeinfo)
            pubplace = xml_utils.xml_node('pubplace', parent_node=pubinfo,
                                          text=self.ui.fgdc_pubplace.text())
            publish = xml_utils.xml_node('publish', parent_node=pubinfo,
                                         text=self.ui.fgdc_publish.text())

        if self.ui.fgdc_othercit.toPlainText():
            othercit = xml_utils.xml_node("othercit",
                                         self.ui.fgdc_othercit.toPlainText(),
                                         parent_node=citeinfo)

        for onlink in self.onlink_list.get_widgets():
            if onlink.added_line.text() != '':
                onlink_node = xml_utils.xml_node('onlink',
                                                 parent_node=citeinfo,
                                                 text=onlink.added_line.text())

        if self.include_lwork and self.ui.radio_lworkyes.isChecked():
            lworkcit = xml_utils.xml_node('lworkcit', parent_node=citeinfo)
            lwork = self.lworkcit_widget._to_xml()
            lworkcit.append(lwork)

        return citeinfo

    def _from_xml(self, citeinfo):
        """
        parses the xml code into the relevant citation elements

        Parameters
        ----------
        citation - the xml element status and its contents

        Returns
        -------
        None
        """
        self.original_xml = citeinfo
        self.clear_widget()
        try:
            if citeinfo.tag == "citation":
                citeinfo = citeinfo.xpath('citeinfo')[0]
            elif citeinfo.tag != 'citeinfo':
                print("The tag is not 'citation' or 'citeinfo'")
                return

            self.fgdc_origin.clear_widgets(add_another=False)
            originators = citeinfo.findall("origin")
            if originators :
                self.fgdc_origin.clear_widgets(add_another=False)
                for origin in citeinfo.findall('origin'):
                    origin_widget = self.fgdc_origin.add_another()
                    origin_widget.added_line.setText(origin.text)
            else:
                self.fgdc_origin.add_another()

            if citeinfo.findall('geoform'):
                self.ui.fgdc_geoform.setEditText(citeinfo.findall('geoform')[0].text)

            utils.populate_widget_element(self.ui.pubdate_widget.ui.fgdc_caldate,
                                          citeinfo, 'pubdate')
            utils.populate_widget_element(self.ui.fgdc_title, citeinfo, 'title')

            utils.populate_widget_element(self.ui.fgdc_othercit, citeinfo, 'othercit')

            self.onlink_list.clear_widgets()
            if citeinfo.findall("onlink"):
                for onlink in citeinfo.findall('onlink'):
                    onlink_widget = self.onlink_list.widgets[0]
                    onlink_widget.added_line.setText(onlink.text)

            if citeinfo.xpath('serinfo'):
                self.ui.radio_seriesyes.setChecked(True)
                utils.populate_widget(self, citeinfo.xpath('serinfo')[0])
            else:
                self.ui.radio_seriesyes.setChecked(False)

            pubinfo = citeinfo.xpath('pubinfo')
            if pubinfo:
                self.ui.radio_pubinfoyes.setChecked(True)
                utils.populate_widget_element(self.ui.fgdc_publish, pubinfo[0], 'publish')
                utils.populate_widget_element(self.ui.fgdc_pubplace, pubinfo[0], 'pubplace')
            else:
                self.ui.radio_pubinfoyes.setChecked(False)
                self.ui.radioButton_8.setChecked(True)

            if citeinfo.xpath('lworkcit'):
                try:
                    self.ui.radio_lworkyes.setChecked(True)
                    self.lworkcit_widget._from_xml(citeinfo.xpath('lworkcit/citeinfo')[0])
                except AttributeError:
                    msg = 'you pasted a citation element into the larger work citation area'
                    msg += '\n that contained a larger work citation'
                    msg += '\n Multiple nested larger work citations are not currently supported in the tool'
                    msg += '\n\n the larger work citation being pasted will be ignored'
                    QMessageBox.warning(self, "Dropped Content Warning", msg)

            else:
                self.ui.radio_lworkno.setChecked(True)

        except KeyError:
            pass


if __name__ == "__main__":
    utils.launch_widget(Citeinfo,
                        "Citation testing")

