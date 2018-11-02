# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hcmgis_lec_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hcmgis_lec_form(object):
    def setupUi(self, hcmgis_lec_form):
        hcmgis_lec_form.setObjectName("hcmgis_lec_form")
        hcmgis_lec_form.setWindowModality(QtCore.Qt.ApplicationModal)
        hcmgis_lec_form.setEnabled(True)
        hcmgis_lec_form.resize(338, 148)
        hcmgis_lec_form.setMouseTracking(False)
        self.BtnOKCancel = QtWidgets.QDialogButtonBox(hcmgis_lec_form)
        self.BtnOKCancel.setGeometry(QtCore.QRect(175, 110, 156, 31))
        self.BtnOKCancel.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.BtnOKCancel.setObjectName("BtnOKCancel")
        self.LblInput = QtWidgets.QLabel(hcmgis_lec_form)
        self.LblInput.setGeometry(QtCore.QRect(10, 7, 321, 16))
        self.LblInput.setObjectName("LblInput")
        self.CboInput = QgsMapLayerComboBox(hcmgis_lec_form)
        self.CboInput.setGeometry(QtCore.QRect(10, 24, 321, 21))
        self.CboInput.setObjectName("CboInput")
        self.LblOutput_2 = QtWidgets.QLabel(hcmgis_lec_form)
        self.LblOutput_2.setGeometry(QtCore.QRect(10, 54, 321, 16))
        self.LblOutput_2.setObjectName("LblOutput_2")
        self.CboField = QgsFieldComboBox(hcmgis_lec_form)
        self.CboField.setGeometry(QtCore.QRect(10, 70, 321, 21))
        self.CboField.setObjectName("CboField")

        self.retranslateUi(hcmgis_lec_form)
        self.BtnOKCancel.accepted.connect(hcmgis_lec_form.accept)
        self.BtnOKCancel.rejected.connect(hcmgis_lec_form.reject)
        QtCore.QMetaObject.connectSlotsByName(hcmgis_lec_form)

    def retranslateUi(self, hcmgis_lec_form):
        _translate = QtCore.QCoreApplication.translate
        hcmgis_lec_form.setWindowTitle(_translate("hcmgis_lec_form", "Largest Empty Circle"))
        self.LblInput.setText(_translate("hcmgis_lec_form", "Input Point Layer"))
        self.LblOutput_2.setText(_translate("hcmgis_lec_form", "Unique field"))

from qgsfieldcombobox import QgsFieldComboBox
from qgsmaplayercombobox import QgsMapLayerComboBox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hcmgis_lec_form = QtWidgets.QDialog()
    ui = Ui_hcmgis_lec_form()
    ui.setupUi(hcmgis_lec_form)
    hcmgis_lec_form.show()
    sys.exit(app.exec_())

