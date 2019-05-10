from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 299)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_start = QtWidgets.QPushButton(self.centralwidget)
        self.pb_start.setObjectName("pb_start")
        self.horizontalLayout.addWidget(self.pb_start)
        self.pb_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pb_pause.setObjectName("pb_pause")
        self.horizontalLayout.addWidget(self.pb_pause)
        self.pb_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pb_stop.setObjectName("pb_stop")
        self.horizontalLayout.addWidget(self.pb_stop)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.count = 0
        self.lcdNumber.setDigitCount(8)

        self.pb_start.clicked.connect(self.start)
        self.pb_pause.clicked.connect(self.pause)
        self.pb_stop.clicked.connect(self.stop)

        self.pb_pause.setEnabled(False)
        self.pb_stop.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_start.setText(_translate("MainWindow", "Start"))
        self.pb_pause.setText(_translate("MainWindow", "Pause"))
        self.pb_stop.setText(_translate("MainWindow", "Stop"))

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)

    def show_time(self):
        self.count += 1
        # self.lcdNumber.display(self.count)
        self.hms = str(self.count//3600) + ":" + str(int((self.count%3600)/60)) + ":" + str(self.count%60)
        self.lcdNumber.display(self.hms)
        self.pb_start.setEnabled(False)
        self.pb_pause.setEnabled(True)
        self.pb_stop.setEnabled(True)

    def pause(self):
        self.timer.stop()
        self.pb_pause.setEnabled(False)
        self.pb_start.setEnabled(True)

    def stop(self):
        self.listWidget.addItem(
            "{0} hour {1} min {2} sec".format(str(self.count // 3600), str(int((self.count % 3600) / 60)),
                                              str(self.count % 60)))
        
        self.timer.stop()
        self.count = 0
        self.lcdNumber.display(self.count)
        self.pb_stop.setEnabled(False)
        self.pb_start.setEnabled(True)
        self.pb_pause.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


