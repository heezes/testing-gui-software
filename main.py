import testing_gui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import time
import os
import mqtt_app


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = testing_gui.Ui_Dialog()
    ui.setupUi(MainWindow)
    mqtt = mqtt_app.mqtt_application(ui)
    ui.unlock.clicked.connect(lambda: mqtt.unlockPressed())
    ui.lock.clicked.connect(lambda: mqtt.lockPressed())
    ui.sync.clicked.connect(lambda: mqtt.syncPressed())
    ui.theft.clicked.connect(lambda: mqtt.theftPressed())
    ui.exit.clicked.connect(lambda: mqtt.exitPressed())
    MainWindow.show()
    sys.exit(app.exec_())