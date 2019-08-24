# -*- coding: utf-8 -*-
"""
/***********************************************************************************************************************
 LandslidesSurvey

 This QGIS plugin allows to retrieve all the data inserted through the smartphone application LandslidesSurvey
 (https://github.com/epessina/LandslidesSurvey). The data can be filtered using a vector layer and downloaded both in
 JSON format and as a Shapefile.
 The plugin is compatible with QGIS 3.x.x and does not require any additional dependency.

 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
 -----------------------------------------------------------------------------------------------------------------------
        begin                : 2019-08-20
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Edoardo Pessina
        email                : edoardo2.pessina@mail.polimi.it
 **********************************************************************************************************************/

/****************************************************************
 *    This program is free software; you can redistribute it    *
 *    and/or modify it under the terms of the GNU GPLv3         *
 *    License https://choosealicense.com/licenses/gpl-3.0/#)    *
 ***************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'landslides_survey_dialog_base.ui'))


class LandslidesSurveyDialog(QtWidgets.QDialog, FORM_CLASS):
    """ The dialogue of the plugin. """

    def __init__(self, parent = None):
        """ Constructor. """

        super(LandslidesSurveyDialog, self).__init__(parent)

        self.setupUi(self)
