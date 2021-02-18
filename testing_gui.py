# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 274)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.modeSelector = QtWidgets.QComboBox(self.formLayoutWidget)
        self.modeSelector.setObjectName("modeSelector")
        self.modeSelector.addItem("")
        self.modeSelector.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.modeSelector)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.count = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.count.setObjectName("count")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.count)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.wait_time = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.wait_time.setObjectName("wait_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wait_time)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.timeout = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.timeout.setObjectName("timeout")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timeout)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(370, 10, 20, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 10, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 0, 371, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(10, 150, 371, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(190, 30, 181, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.unlock = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.unlock.setObjectName("unlock")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.unlock)
        self.lock = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.lock.setObjectName("lock")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lock)
        self.sync = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.sync.setObjectName("sync")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sync)
        self.theft = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.theft.setObjectName("theft")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.theft)
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(230, 100, 93, 21))
        self.exit.setObjectName("exit")
        self.operation_status = QtWidgets.QLabel(Dialog)
        self.operation_status.setGeometry(QtCore.QRect(10, 170, 361, 51))
        self.operation_status.setObjectName("operation_status")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.modeSelector.setItemText(0, _translate("Dialog", "BLE"))
        self.modeSelector.setItemText(1, _translate("Dialog", "KEY"))
        self.label.setText(_translate("Dialog", "Operation Mode"))
        self.label_2.setText(_translate("Dialog", "Count"))
        self.label_3.setText(_translate("Dialog", "Response Timeout"))
        self.label_4.setText(_translate("Dialog", "Ride Time"))
        self.unlock.setText(_translate("Dialog", "Unlock"))
        self.lock.setText(_translate("Dialog", "Lock"))
        self.sync.setText(_translate("Dialog", "Sync Trigger"))
        self.theft.setText(_translate("Dialog", "Theft Trigger"))
        self.exit.setText(_translate("Dialog", "GIT PUSH & EXIT"))
        self.operation_status.setText(_translate("Dialog", "Status"))
