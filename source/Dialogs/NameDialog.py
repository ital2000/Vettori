# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nameDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlaneName(object):
    def setupUi(self, PlaneName):
        PlaneName.setObjectName("PlaneName")
        PlaneName.resize(286, 120)
        PlaneName.setMinimumSize(QtCore.QSize(286, 0))
        self.gridLayout = QtWidgets.QGridLayout(PlaneName)
        self.gridLayout.setObjectName("gridLayout")
        self.NameLine = QtWidgets.QLineEdit(PlaneName)
        self.NameLine.setObjectName("NameLine")
        self.gridLayout.addWidget(self.NameLine, 2, 1, 1, 1)
        self.TextSizeLine = QtWidgets.QSpinBox(PlaneName)
        self.TextSizeLine.setMinimum(1)
        self.TextSizeLine.setProperty("value", 16)
        self.TextSizeLine.setObjectName("TextSizeLine")
        self.gridLayout.addWidget(self.TextSizeLine, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(PlaneName)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(PlaneName)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.OkButton = QtWidgets.QPushButton(PlaneName)
        self.OkButton.setDefault(True)
        self.OkButton.setObjectName("OkButton")
        self.gridLayout.addWidget(self.OkButton, 3, 0, 1, 2)

        self.retranslateUi(PlaneName)
        QtCore.QMetaObject.connectSlotsByName(PlaneName)

    def retranslateUi(self, PlaneName):
        _translate = QtCore.QCoreApplication.translate
        PlaneName.setWindowTitle(_translate("PlaneName", "Plane Name"))
        self.NameLine.setText(_translate("PlaneName", "Name"))
        self.label.setText(_translate("PlaneName", "Text size"))
        self.label_2.setText(_translate("PlaneName", "Name"))
        self.OkButton.setText(_translate("PlaneName", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlaneName = QtWidgets.QDialog()
    ui = Ui_PlaneName()
    ui.setupUi(PlaneName)
    PlaneName.show()
    sys.exit(app.exec_())
