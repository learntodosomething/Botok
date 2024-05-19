import importlib
import pip

def check_and_install(package):
    try:
        importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
required_packages = [
    "PyQt5",
    "selenium",
    "pyautogui",
    "opencv-python",
    "beautifulsoup4",
    "numpy",
    "pillow",
    "requests",
    "keyboard",
    "matplotlib"
]

for package in required_packages:
    check_and_install(package)

print("Az összes szükséges csomag telepítve van.")



from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

sys.path.append("Values")
import Basics
import subprocess

from selenium import webdriver


# Bot 1 QThread
class BotThread1(QtCore.QThread):
    process_finished = QtCore.pyqtSignal()

    def run(self):
        python_file_path = "Bot_1/Bot_1.py"

        try:
            subprocess.run(["python", python_file_path])
        except subprocess.CalledProcessError as e:
            print(f"Hiba történt a fájl futtatása közben: {e}")

        self.process_finished.emit()

# Bot 2 QThread
class BotThread2(QtCore.QThread):
    process_finished = QtCore.pyqtSignal()

    def run(self):
        python_file_path = "Bot_2/Bot_2.py"

        try:
            subprocess.run(["python", python_file_path])
        except subprocess.CalledProcessError as e:
            print(f"Hiba történt a fájl futtatása közben: {e}")

        self.process_finished.emit()

# Bot 3 QThread
class BotThread3(QtCore.QThread):
    process_finished = QtCore.pyqtSignal()

    def run(self):
        python_file_path = "Bot_3/Bot_3.py"

        try:
            subprocess.run(["python", python_file_path])
        except subprocess.CalledProcessError as e:
            print(f"Hiba történt a fájl futtatása közben: {e}")

        self.process_finished.emit()

# Bot 4 QThread
class BotThread4(QtCore.QThread):
    process_finished = QtCore.pyqtSignal()

    def run(self):
        python_file_path = "Bot_4/Bot_4.py"

        try:
            subprocess.run(["python", python_file_path])
        except subprocess.CalledProcessError as e:
            print(f"Hiba történt a fájl futtatása közben: {e}")

        self.process_finished.emit()
  
class Worker(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    
    def run(self):
        try:
            # WebDriver inicializálása
            driver = webdriver.Firefox()
            # Az about:profiles oldal megnyitása
            driver.get("about:profiles")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Munka befejezése, jelzés küldése
            self.finished.emit()

            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_top)
        self.pushButton_6.setGeometry(QtCore.QRect(760, 10, 51, 23))
        self.pushButton_6.setStyleSheet("color: #FFF;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame_top)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 741, 25))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.textEdit.setStyleSheet("color: #FFF;")
        self.textEdit.setMarkdown("")
        self.textEdit.setPlaceholderText("C:\\Users\\user\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\btrbserg8285.default-release-000000000000000")
        self.textEdit.setObjectName("textEdit")
        self.Save = QtWidgets.QPushButton(self.frame_top)
        self.Save.setEnabled(True)
        self.Save.setGeometry(QtCore.QRect(820, 10, 61, 23))
        self.Save.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 125, 0);\n"
"}")
        self.Save.setObjectName("Save")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_1.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_1.setObjectName("btn_page_1")
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_2.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_2.setObjectName("btn_page_2")
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_3.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_3.setObjectName("btn_page_3")
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.btn_page_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_4.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_page_4.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.btn_page_4.setObjectName("btn_page_4")
        self.verticalLayout_4.addWidget(self.btn_page_4)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_pages)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.page_1)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setStyleSheet("font-size: 18px;  color: #FFF;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_7.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_7.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_7.setStyleSheet("color: #FFF;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_12.addWidget(self.pushButton_7)
        self.verticalLayout_5.addWidget(self.widget_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.widget_14 = QtWidgets.QWidget(self.widget_3)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_14)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_5.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_5.setStyleSheet("color: #FFF;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_13.addWidget(self.pushButton_5)
        self.verticalLayout_5.addWidget(self.widget_14)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.page_1)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet("color: #FFF;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_6.setStyleSheet("color: #FF0000;  font-size: 18px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.page_1)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFF;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_3.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_7 = QtWidgets.QWidget(self.page_2)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget_7)
        self.label_3.setStyleSheet("font-size: 18px;  color: #FFF;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.widget_16 = QtWidgets.QWidget(self.widget_7)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_16)
        self.pushButton_8.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_8.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_8.setStyleSheet("color: #FFF;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_14.addWidget(self.pushButton_8)
        self.verticalLayout_6.addWidget(self.widget_16)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.widget_15 = QtWidgets.QWidget(self.widget_7)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_15)
        self.pushButton_9.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_9.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_9.setStyleSheet("color: #FFF;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_15.addWidget(self.pushButton_9)
        self.verticalLayout_6.addWidget(self.widget_15)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.page_2)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget_6)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("color: #FF0000;  font-size: 18px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_2.setStyleSheet("color: #FFF;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #FFF;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_7.addWidget(self.widget_4)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_10 = QtWidgets.QWidget(self.page_3)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget_10)
        self.label_9.setStyleSheet("font-size: 18px;  color: #FFF;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.widget_17 = QtWidgets.QWidget(self.widget_10)
        self.widget_17.setObjectName("widget_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_17)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_17)
        self.pushButton_10.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_10.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_10.setStyleSheet("color: #FFF;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_17.addWidget(self.pushButton_10)
        self.verticalLayout_7.addWidget(self.widget_17)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.widget_18 = QtWidgets.QWidget(self.widget_10)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_18)
        self.pushButton_11.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_11.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_11.setStyleSheet("color: #FFF;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_16.addWidget(self.pushButton_11)
        self.verticalLayout_7.addWidget(self.widget_18)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem8)
        self.horizontalLayout_8.addWidget(self.widget_10)
        self.widget_9 = QtWidgets.QWidget(self.page_3)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.widget_9)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_8.setStyleSheet("color: #FF0000;  font-size: 18px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_9)
        self.pushButton_3.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_3.setStyleSheet("color: #FFF;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.page_3)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #FFF;")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.horizontalLayout_8.addWidget(self.widget_8)
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_13 = QtWidgets.QWidget(self.page)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.widget_13)
        self.label_12.setStyleSheet("font-size: 18px;  color: #FFF;")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.widget_20 = QtWidgets.QWidget(self.widget_13)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_20)
        self.pushButton_12.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_12.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_12.setStyleSheet("color: #FFF;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_19.addWidget(self.pushButton_12)
        self.verticalLayout_8.addWidget(self.widget_20)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem10)
        self.widget_19 = QtWidgets.QWidget(self.widget_13)
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_19)
        self.pushButton_13.setMinimumSize(QtCore.QSize(120, 70))
        self.pushButton_13.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_13.setStyleSheet("color: #FFF;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_18.addWidget(self.pushButton_13)
        self.verticalLayout_8.addWidget(self.widget_19)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_11.addWidget(self.widget_13)
        self.widget_12 = QtWidgets.QWidget(self.page)
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.widget_12)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_11.setStyleSheet("color: #FF0000;  font-size: 18px;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_12)
        self.pushButton_4.setMaximumSize(QtCore.QSize(120, 70))
        self.pushButton_4.setStyleSheet("color: #FFF;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.widget_12)
        self.widget_11 = QtWidgets.QWidget(self.page)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.widget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #FFF;")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_11.addWidget(self.widget_11)
        self.stackedWidget.addWidget(self.page)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        # Save 
        self.Save.setEnabled(False)
        self.textEdit.textChanged.connect(self.checkTextEdit)
        self.Save.clicked.connect(self.onSaveClicked)

        
        # Bot 1 RUN
        self.bot_thread_1 = BotThread1()
        self.bot_thread_1.process_finished.connect(self.bot_process_finished)
        self.pushButton.clicked.connect(self.start_bot_thread_1)

        # Bot 2 RUN
        self.bot_thread_2 = BotThread2()
        self.bot_thread_2.process_finished.connect(self.bot_process_finished_2)
        self.pushButton_2.clicked.connect(self.start_bot_thread_2)
        
        # Bot 3 RUN
        self.bot_thread_3 = BotThread3()
        self.bot_thread_3.process_finished.connect(self.bot_process_finished_3)
        self.pushButton_3.clicked.connect(self.start_bot_thread_3)

        # Bot 4 RUN
        self.bot_thread_4 = BotThread4()
        self.bot_thread_4.process_finished.connect(self.bot_process_finished_4)
        self.pushButton_4.clicked.connect(self.start_bot_thread_4)



        self.pushButton_7.clicked.connect(self.runPythonCode_1)
        self.pushButton_5.clicked.connect(self.runPythonCode_2)

        self.pushButton_8.clicked.connect(self.runPythonCode_3)
        self.pushButton_9.clicked.connect(self.runPythonCode_4)

        self.pushButton_10.clicked.connect(self.runPythonCode_5)
        self.pushButton_11.clicked.connect(self.runPythonCode_6)

        self.pushButton_12.clicked.connect(self.runPythonCode_7)
        self.pushButton_13.clicked.connect(self.runPythonCode_8)


        
        
        self.pushButton_6.clicked.connect(self.openWebdriverPage)
        ########################################################
        #                       FUNCTIONS
        ########################################################
        
        # Save
    def checkTextEdit(self):
        if self.textEdit.toPlainText().strip():  # Ha a szövegdoboz nem üres
            self.Save.setEnabled(True)
        else:
            self.Save.setEnabled(False)

    def onSaveClicked(self):
        text = self.textEdit.toPlainText()  # Az textEdit aktuális tartalmának lekérése
        print(text)
        print(Basics.my_variable)

        file_path = "Values/Basics.py"
        # Olvasd be a fájl tartalmát
        with open(file_path, "r") as file:
            lines = file.readlines()
        # Keresd meg a sorok között a my_variable értékét tartalmazó sort
        for i, line in enumerate(lines):
            if "my_variable" in line:
                # Ha megtaláltad a sort, cseréld ki az új értékre
                new_line = f'my_variable = r"{text}"\n'
                lines[i] = new_line
                break

        # Írd vissza a módosított sorokat a fájlba
        with open(file_path, "w") as file:
            file.writelines(lines)

        # Frissítsd a Basics.my_variable értékét
        Basics.my_variable = text




    # Bot 1 RUN
    def start_bot_thread_1(self):
        self.label_6.setText("Online")
        self.label_6.setStyleSheet("color: rgb(0, 255, 0); font-size: 18px;")
        self.pushButton.setEnabled(False)  # Disable button during bot execution
        self.bot_thread_1.start()

    def bot_process_finished(self):
        self.label_6.setText("Offline")
        self.label_6.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px;")
        self.pushButton.setEnabled(True)  # Re-enable button after bot execution
        print("Bot 1 process finished.")

    # Bot 2 RUN
    def start_bot_thread_2(self):
        self.label.setText("Online")
        self.label.setStyleSheet("color: rgb(0, 255, 0); font-size: 18px;")
        self.pushButton_2.setEnabled(False)  # Disable button during bot execution
        self.bot_thread_2.start()

    def bot_process_finished_2(self):
        self.label.setText("Offline")
        self.label.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px;")
        self.pushButton_2.setEnabled(True)  # Re-enable button after bot execution
        print("Bot 2 process finished.")


    # Bot 3 RUN
    def start_bot_thread_3(self):
        self.label_8.setText("Online")
        self.label_8.setStyleSheet("color: rgb(0, 255, 0); font-size: 18px;")
        self.pushButton.setEnabled(False)  # Disable button during bot execution
        self.bot_thread_3.start()

    def bot_process_finished_3(self):
        self.label_8.setText("Offline")
        self.label_8.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px;")
        self.pushButton.setEnabled(True)  # Re-enable button after bot execution
        print("Bot 1 process finished.")

    # Bot 4 RUN
    def start_bot_thread_4(self):
        self.label_11.setText("Online")
        self.label_11.setStyleSheet("color: rgb(0, 255, 0); font-size: 18px;")
        self.pushButton_4.setEnabled(False)  # Disable button during bot execution
        self.bot_thread_4.start()

    def bot_process_finished_4(self):
        self.label_11.setText("Offline")
        self.label_11.setStyleSheet("color: rgb(255, 0, 0); font-size: 18px;")
        self.pushButton_4.setEnabled(True)  # Re-enable button after bot execution
        print("Bot 2 process finished.")

    #ADAT KIOLVASÁS 1
    def runPythonCode_1(self):
        python_file_path = 'Bot_1/read_likedpost.py'

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')
    def runPythonCode_2(self):
        python_file_path = 'Bot_1/read_watch_time.py'  

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')

    #ADAT KIOLVASÁS 2
    def runPythonCode_3(self):
        python_file_path = 'Bot_2/read_likedpost.py'

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')
    def runPythonCode_4(self):
        python_file_path = 'Bot_2/read_watch_time.py'  

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')

    #ADAT KIOLVASÁS 3
    def runPythonCode_5(self):
        python_file_path = 'Bot_3/read_likedpost.py'

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')
    def runPythonCode_6(self):
        python_file_path = 'Bot_3/read_watch_time.py'  

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')

    #ADAT KIOLVASÁS 4
    def runPythonCode_7(self):
        python_file_path = 'Bot_4/read_likedpost.py'

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')
    def runPythonCode_8(self):
        python_file_path = 'Bot_4/read_watch_time.py'  

        try:
            subprocess.run(['python', python_file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f'Hiba történt a fájl futtatása közben: {e}')
        else:
            print('A Python kód sikeresen lefutott.')



            
    def openWebdriverPage(self):
        try:
            # WebDriver létrehozása
            driver = webdriver.Firefox()
            # Az about:profiles oldal megnyitása
            driver.get("about:profiles")
        except Exception as e:
            print(f"Error: {e}")
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application"))
        self.Btn_Toggle.setText(_translate("MainWindow", "Botok"))
        self.pushButton_6.setText(_translate("MainWindow", "Find it"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.btn_page_1.setText(_translate("MainWindow", "Bot 1"))
        self.btn_page_2.setText(_translate("MainWindow", "Bot 2"))
        self.btn_page_3.setText(_translate("MainWindow", "Bot 3"))
        self.btn_page_4.setText(_translate("MainWindow", "bot 4"))
        self.label_5.setText(_translate("MainWindow", "Bot 1\n"
"@booo81076"))
        self.pushButton_7.setText(_translate("MainWindow", "Like adatok"))
        self.pushButton_5.setText(_translate("MainWindow", "Nézettségi adatok"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_6.setText(_translate("MainWindow", "Offline"))
        self.label_4.setText(_translate("MainWindow", "Miután a bot bejelentkezett\n"
"Nyomj \"S\" betűt az induláshoz\n"
"A \"Q\" billentyűvel bármikor kiléphetsz\n"
"\n"
"A bot \"személyisége\":\n"
"Szereti az állatokat és jókedvű\n"
"\n"
"Kedvenc és keresett Tag-ek:\n"
"dog, cat, cute, puppy, kitten,\n"
"fluffy, adorable, love, funny,\n"
"playful, furry, sweet, charming,\n"
"amusing, delightful, charming,\n"
"precious, snuggly, endearing,\n"
"joyful, cheerful, mischievous,\n"
"whiskers, paws, purr, bark,\n"
"tail, snout, whimsical, bouncy"))
        self.label_3.setText(_translate("MainWindow", "Bot 2\n"
"@The_GuyWright_Official"))
        self.pushButton_8.setText(_translate("MainWindow", "Like adatok"))
        self.pushButton_9.setText(_translate("MainWindow", "Nézettségi adatok"))
        self.label.setText(_translate("MainWindow", "Offline"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Miután a bot bejelentkezett\n"
"Nyomj \"S\" betűt az indulushoz\n"
"A \"Q\" billentyűvel bármikor kiléphetsz\n"
"\n"
"A bot \"személyisége\":\n"
"Szereti az autókat, a sebességet és\n"
"nagyon motivált illetve törekvő\n"
"\n"
"Kedvenc és keresett Tag-ek:\n"
"car, motorcycle, truck, bike,\n"
"scooter, sedan, SUV, moped,\n"
"pickup, motorbike, jeep, roadster,\n"
"limousine, RV, quad bike, tractor,\n"
"dune buggy, hovercraft, kart, V8,\n"
"V6, turbo, supercharge, horsepower,\n"
"torque, cylinder, engine, gearbox,\n"
"drift, exhaust, chassis, suspension,\n"
"racing, speed, performance, luxury,\n"
"classic, muscle car, sportscar, off-road,\n"
"tuning, custom"))
        self.label_9.setText(_translate("MainWindow", "Bot 3\n"
"@coool._guy"))
        self.pushButton_10.setText(_translate("MainWindow", "Like adatok"))
        self.pushButton_11.setText(_translate("MainWindow", "Nézettségi adatok"))
        self.label_8.setText(_translate("MainWindow", "Offline"))
        self.pushButton_3.setText(_translate("MainWindow", "Start"))
        self.label_7.setText(_translate("MainWindow", "Miután a bot bejelentkezett\n"
"Nyomj \"S\" betűt az indulushoz\n"
"A \"Q\" billentyűvel bármikor kiléphetsz\n"
"\n"
"A bot \"személyisége\":\n"
"Szeret animéket nézni és játszani\n"
"\n"
"Kedvenc és keresett Tag-ek:\n"
"anime, manga, studio ghibli, shonen,\n"
"shojo, mecha, magical girl, fantasy,\n"
"adventure, slice of life, romance, comedy,\n"
"action, drama, supernatural, isekai,\n"
"superpowers, kawaii, cusplay, otaku,\n"
"fandom, character design, voice acting,\n"
"subbed, dubbed, opening song, ending song,\n"
"mascot,kawaii culture, gaming, conventions,\n"
"merchandise,Japanese, Ghibli movies,\n"
" mystical,enchanted, magical creatures,\n"
"legendary heroes, fairy tale, wonderland,\n"
"journey, imagination, dreams"))
        self.label_12.setText(_translate("MainWindow", "Bot 4\n"
"@goth.cat.girl"))
        self.pushButton_12.setText(_translate("MainWindow", "Like adatok"))
        self.pushButton_13.setText(_translate("MainWindow", "Nézettségi adatok"))
        self.label_11.setText(_translate("MainWindow", "Offline"))
        self.pushButton_4.setText(_translate("MainWindow", "Start"))
        self.label_10.setText(_translate("MainWindow", "Miután a bot bejelentkezett\n"
"Nyomj \"S\" betűt az induláshoz\n"
"A \"Q\" billentyűvel bármikor kiléphetsz\n"
"\n"
"A bot \"személyisége\":\n"
"Olyan mint egy serdülő kamasz\n"
"rossz a kedve és depresszív hangulatú\n"
"\n"
"Kedvenc és keresett Tag-ek:\n"
"sad, tears, upset, lonely, depressed,\n"
"heartbroken, gloomy, miserable, \n"
"melancholy, desperate, despair, sorrow, \n"
"disheartened,anguish, woeful, weep, pain,\n"
"hopeless, anxiety, unbearable, heartache,\n"
"desolation, overwhelmed, misery, \n"
"anguished, despondent, troubled, torment,\n"
"forlorn, doom"))


        # A gombnyomás eseménykezelőjének hozzáadása
        self.btn_page_1.clicked.connect(lambda: self.switch_page(0))  # 0. oldal (page_1)
        self.btn_page_2.clicked.connect(lambda: self.switch_page(1))  # 1. oldal (page_2)
        self.btn_page_3.clicked.connect(lambda: self.switch_page(2))  # 2. oldal (page_3)
        self.btn_page_4.clicked.connect(lambda: self.switch_page(3))  # 2. oldal (page_3)
    
    
    def switch_page(self, index):
        # A QStackedWidget-en belül váltás az adott indexre
        self.stackedWidget.setCurrentIndex(index)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
