This is a forked and modified version of the USGS Metadata Wizard. Modifications to the original work are by Michelle M. Fink, Colorado Natural Heritage Program, Colorado State University [michelle.fink@colostate.edu]. Changes made are to facilitate my own, non-government related metadata needs. As such, this fork may not work for you or anyone else but me. My use of this code does not imply approval or endorsement by the USGS or any other government entity.  

The scripts in this repository are free software: you can redistribute and/or modify them under the terms of the [Creative Commons Attribution 4.0 International (CC BY 4.0) license](http://creativecommons.org/licenses/by/4.0/).  

The scripts are distributed in the hope that they will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.


Metadata Wizard
===========================================================================================

The MetadataWizard is a useful tool designed to facilitate FGDC  
metadata creation for spatial and non-spatial data sets.  It is a cross-platform desktop application
built using an open-source Python architecture.  

Complete user documentation available [here](https://doi-usgs.github.io/fort-pymdwizard).

![Alt text](docs/img/screenshot.png?raw=true "Screen shot")

It provides a user-friendly and efficient environment for metadata creation, 
editing, preview, and validation.  Built-in tools facilitate and automate the creation of high quality 
metadata records.


* Auto-population of challenging metadata sections such as the spatial reference, 
spatial organization, and entity and attributes, based on information contained in
the data (CSV, Excel, Shapefiles, etc.)<br>

 ![Alt text](./docs/img/EA_screenshot.png?raw=true "Screen shot") 

* Auto-population of contact information for USGS affiliates, 
taxonomic information from ITIS, or keywords from USGS controlled vocabularies.<br>

 ![Alt text](docs/img/keywords_screenshot.png?raw=true "Screen shot") 
* Built-in FGDC validator that highlights any missing or error elements directly on the GUI and in a printable report suitable for metadata review.<br>

 ![Alt text](docs/img/error_screenshot.png?raw=true "Screen shot") 

* Copy/Paste or Drag-and-Drop of entire sections, subsections, or individual content
between different records or other tools including XML-Notepad and text editors.
* Built-in help documentation that guides users through common and detailed questions about metadata.


This project is modeled off of the original [Metadata Wizard](https://github.com/dignizio-usgs/MDWizard_Source), which was designed as a toolbox in ArcMap and required an ESRI installation.

Recommended Citation:
----------------

Talbert, C.B., Ignizio, D.A., and Enns, K.D., 2017, Metadata Wizard (ver. 2.0.7, March 2022): U.S. Geological Survey software release, https://doi.org/10.5066/F7V9870D.

Authors:
----------------

Colin B. Talbert -- https://orcid.org/0000-0002-9505-1876<br>
Drew A. Ignizio -- https://orcid.org/0000-0001-8054-5139<br>
Kyle D. Enns -- https://orcid.org/0000-0001-7675-697X 

Acknowledgements:
----------------
The MetadataWizard was developed by the data management team at the USGS Fort Collins Science Center,<br>
with support from the USGS Science Analytics and Synthesis (SAS), 
and the USGS Council for Data integration (CDI).<br><br>
Ongoing support provided by the USGS Science Analytics and Synthesis (SAS)<br><br>

Disclaimer:
-----------

This software has been approved for release by the U.S. Geological Survey (USGS). 
Although the software has been subjected to rigorous review, the USGS reserves 
the right to update the software as needed pursuant to further analysis and 
review. No warranty, expressed or implied, is made by the USGS or the 
U.S. Government as to the functionality of the software and related material 
nor shall the fact of release constitute any such warranty. Furthermore, the 
software is released on condition that neither the USGS nor the U.S. Government 
shall be held liable for any damages resulting from its authorized 
or unauthorized use.

Contact:
-----------
ask-sdm@usgs.gov

