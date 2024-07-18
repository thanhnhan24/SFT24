import sys
import psutil
import time
from threading import Thread
from typing import Iterable, Mapping
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 625)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.thumbnail = QLabel(self.centralwidget)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setGeometry(QRect(30, 30, 251, 81))
        self.thumbnail.setPixmap(QPixmap(u"bia.png"))
        self.thumbnail.setScaledContents(True)
        self.img_out_groupbox = QGroupBox(self.centralwidget)
        self.img_out_groupbox.setObjectName(u"img_out_groupbox")
        self.img_out_groupbox.setGeometry(QRect(30, 140, 651, 331))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.img_out_groupbox.setFont(font)
        self.img_out_1 = QLabel(self.img_out_groupbox)
        self.img_out_1.setObjectName(u"img_out_1")
        self.img_out_1.setGeometry(QRect(70, 60, 214, 160))
        self.img_out_1.setScaledContents(True)
        self.img_out_2 = QLabel(self.img_out_groupbox)
        self.img_out_2.setObjectName(u"img_out_2")
        self.img_out_2.setGeometry(QRect(370, 60, 214, 160))
        self.img_out_2.setScaledContents(True)
        self.label_4 = QLabel(self.img_out_groupbox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 250, 214, 16))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.img_out_groupbox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 250, 214, 16))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.hardware_status_groupbox = QGroupBox(self.centralwidget)
        self.hardware_status_groupbox.setObjectName(u"hardware_status_groupbox")
        self.hardware_status_groupbox.setGeometry(QRect(30, 490, 651, 81))
        self.hardware_status_groupbox.setFont(font)
        self.plainTextEdit_2 = QPlainTextEdit(self.hardware_status_groupbox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(430, 526, 111, 31))
        self.splitter_2 = QSplitter(self.hardware_status_groupbox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(380, 30, 201, 41))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.cpu_label = QLabel(self.splitter_2)
        self.cpu_label.setObjectName(u"cpu_label")
        self.splitter_2.addWidget(self.cpu_label)
        self.cpu_edit = QPlainTextEdit(self.splitter_2)
        self.cpu_edit.setObjectName(u"cpu_edit")
        self.cpu_edit.setReadOnly(True)
        self.splitter_2.addWidget(self.cpu_edit)
        self.splitter_3 = QSplitter(self.hardware_status_groupbox)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(20, 30, 341, 41))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.memory_label = QLabel(self.splitter_3)
        self.memory_label.setObjectName(u"memory_label")
        self.splitter_3.addWidget(self.memory_label)
        self.memory_edit = QPlainTextEdit(self.splitter_3)
        self.memory_edit.setObjectName(u"memory_edit")
        self.memory_edit.setReadOnly(True)
        self.splitter_3.addWidget(self.memory_edit)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(700, 120, 331, 451))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.control_panel_groupbox = QGroupBox(self.tab)
        self.control_panel_groupbox.setObjectName(u"control_panel_groupbox")
        self.control_panel_groupbox.setGeometry(QRect(10, 10, 311, 401))
        self.control_panel_groupbox.setFont(font)
        self.cam_1_button = QPushButton(self.control_panel_groupbox)
        self.cam_1_button.setObjectName(u"cam_1_button")
        self.cam_1_button.setGeometry(QRect(10, 30, 291, 41))
        self.cam_1_button.setCheckable(True)
        self.cam_1_button.setChecked(False)
        self.cam_2_button = QPushButton(self.control_panel_groupbox)
        self.cam_2_button.setObjectName(u"cam_2_button")
        self.cam_2_button.setGeometry(QRect(10, 80, 291, 41))
        self.cam_2_button.setCursor(QCursor(Qt.ArrowCursor))
        self.cam_2_button.setFocusPolicy(Qt.StrongFocus)
        self.cam_2_button.setCheckable(True)
        self.output_class_listview = QListView(self.control_panel_groupbox)
        self.output_class_listview.setObjectName(u"output_class_listview")
        self.output_class_listview.setGeometry(QRect(10, 160, 291, 71))
        self.output_console_listview = QListView(self.control_panel_groupbox)
        self.output_console_listview.setObjectName(u"output_console_listview")
        self.output_console_listview.setGeometry(QRect(10, 280, 291, 121))
        self.output_class_label = QLabel(self.control_panel_groupbox)
        self.output_class_label.setObjectName(u"output_class_label")
        self.output_class_label.setGeometry(QRect(10, 130, 141, 16))
        self.output_console_label = QLabel(self.control_panel_groupbox)
        self.output_console_label.setObjectName(u"output_console_label")
        self.output_console_label.setGeometry(QRect(10, 250, 171, 16))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(320, 30, 711, 81))
        self.splitter.setOrientation(Qt.Vertical)
        self.title = QLabel(self.splitter)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.splitter.addWidget(self.title)
        self.reference = QLabel(self.splitter)
        self.reference.setObjectName(u"reference")
        self.splitter.addWidget(self.reference)
        self.version = QLabel(self.splitter)
        self.version.setObjectName(u"version")
        self.splitter.addWidget(self.version)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.thumbnail.setText("")
        self.img_out_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"H\u00ccNH \u1ea2NH \u0110\u1ea6U RA", None))
        self.img_out_1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.img_out_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CAM 1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CAM 2", None))
        self.hardware_status_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"TH\u00d4NG S\u1ed0 PH\u1ea6N C\u1ee8NG", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.memory_label.setText(QCoreApplication.translate("MainWindow", u"MEMORY", None))
        self.control_panel_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"B\u1ea2NG \u0110I\u1ec0U KHI\u1ec2N", None))
        self.cam_1_button.setText(QCoreApplication.translate("MainWindow", u"CAM 1", None))
        self.cam_2_button.setText(QCoreApplication.translate("MainWindow", u"CAM 2", None))
        self.output_class_label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT CLASS", None))
        self.output_console_label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT CONSOLE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"GIAO DI\u1ec6N CH\u01af\u01a0NG TR\u00ccNH NH\u1eacN DI\u1ec6N KHU\u00d4N M\u1eb6T S\u1eec D\u1ee4NG YOLOv8", None))
        self.reference.setText(QCoreApplication.translate("MainWindow", u"SINH VI\u00caN: NGUY\u1ec4N THANH NH\u00c2N - 2286301149 - VI\u1ec6N K\u1ef8 THU\u1eacT HUTECH - KH\u00d3A 2022-2026", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"Phi\u00ean b\u1ea3n: 24.8.17.01", None))
    # retranslateUi


class ConsoleMainWindow(QMainWindow):
    def __init__(self):
        super(ConsoleMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create an instance of HardwareWorker
        self.hardware_worker = HardwareWorker()

        # Connect signals from worker to update UI
        self.hardware_worker.memory_updated.connect(self.update_memory_info)
        self.hardware_worker.cpu_updated.connect(self.update_cpu_info)

        # Start the worker thread
        self.hardware_worker.start()

    def update_memory_info(self, total_memory, used_memory, memory_percentage):
        self.ui.memory_edit.setPlainText(f"Used: {used_memory:.2f} GB / {total_memory:.2f} GB")

    def update_cpu_info(self, cpu_percentage):
        self.ui.cpu_edit.setPlainText(f"{cpu_percentage}%")

class HardwareWorker(QThread):
    memory_updated = Signal(float, float, float)
    cpu_updated = Signal(float)

    def run(self):
        while True:
            total_memory, used_memory, memory_percentage = self.get_memory_info()
            cpu_percentage = self.get_cpu_info()

            # Emit signals to update UI
            self.memory_updated.emit(total_memory, used_memory, memory_percentage)
            self.cpu_updated.emit(cpu_percentage)

            # Sleep for a while
            self.msleep(1000)  # 1 second delay

    def get_memory_info(self):
        memory = psutil.virtual_memory()
        total_memory = memory.total / (1024 ** 3)  # Chuyển đổi từ byte sang GB
        used_memory = memory.used / (1024 ** 3)    # Chuyển đổi từ byte sang GB
        memory_percentage = memory.percent
        return total_memory, used_memory, memory_percentage

    def get_cpu_info(self):
        cpu_percentage = psutil.cpu_percent(interval=1)  # Đo trong 1 giây
        return cpu_percentage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = ConsoleMainWindow()
    mainwin.show()
    sys.exit(app.exec_())
