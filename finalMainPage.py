# ------------------------------------------------------------------------------
# Copyright (C) 2020-2021 Monirul Shawon
##
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
##
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------


import ctypes
import getpass
import logging
import os
import platform
import sys
import time

import requests
import urllib3
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from pyupdater.client import Client, FileDownloader
from pyupdater.utils.compat import url_quote

from client_config import ClientConfig
from mainTruss import MainPage
from supports import *
from ui_finalMainPage import Ui_MainWindow
from ui_units import Ui_MainWindow2

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

logger = logging.getLogger('Truss 101')

date = '<span style="color:#b19a66;">%m/%d/%Y</span> <span style="color:#56a187;">%I:%M:%S</span> %p'

my_system = platform.uname()
user = getpass.getuser()

log = logging.getLogger(__name__)

def monkey_response(self):
    """
    GitHub replaces space with dot(.) in filename
    pyupdater use url_quote to create file url
    hence this monkey patch replace space(%20) with dot(.)
    """
    data = None
    max_download_retries = self.max_download_retries
    for url in self.urls:
        # Create url for resource
        file_url = url + url_quote(self.filename)
        file_url = file_url.replace('%20', '.')
        print(file_url)
        log.debug("Url for request: %s", file_url)
        try:
            data = self.http_pool.urlopen(
                "GET", file_url, preload_content=False, retries=max_download_retries
            )
        except urllib3.exceptions.SSLError:
            log.debug("SSL cert not verified")
            continue
        except urllib3.exceptions.MaxRetryError:
            log.debug("MaxRetryError")
            continue
        except Exception as e:
            # Catch whatever else comes up and log it
            # to help fix other http related issues
            log.debug(str(e), exc_info=True)
        else:
            if data.status != 200:
                log.debug("Received a non-200 response %d", data.status)
                data = None
            else:
                break

    if data is not None:
        log.debug("Resource URL: %s", file_url)
    else:
        log.debug("Could not create resource URL.")
    return data


FileDownloader._create_response = monkey_response

class CustomFormatter(logging.Formatter):
    """
    Logging Formatter to add colors and count warning / errors
    """

    FORMATS = {
        logging.DEBUG: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#d4659d;">[ %(levelname)s ]</span>  %(message)s',
        logging.INFO: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#31aa6e;">[ %(levelname)s ]</span>  %(message)s',
        logging.WARNING: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#fd6152;">[ %(levelname)s ]</span>  %(message)s',
        logging.ERROR: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#ff0000;">[ %(levelname)s ]</span>  %(message)s',
        logging.CRITICAL: '[%(asctime)s] [ %(filename)s:%(lineno)d ] <span style="color:#ffff00;">[ %(levelname)s ]</span>  %(message)s'
    }


    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt,datefmt=date)
        return formatter.format(record)
    
class QTextEditLogger(logging.Handler):
    """
    Custom python logging handler to show log in
    a QPlainTextEdit
    """

    def __init__(self, parent):
        super().__init__()
        self.widget = QPlainTextEdit(parent)
        self.widget.setReadOnly(True)
        
        font = QFont("Monospace")
        font.setStyleHint(QFont.TypeWriter)
        self.widget.setFont(font)

        self.widget.appendPlainText('#######################################\n')
        self.widget.appendPlainText(f'System : {my_system.system}')
        self.widget.appendPlainText(f'Computer Name : {my_system.node}-{user}')
        self.widget.appendPlainText(f'Release : {my_system.release}')
        self.widget.appendPlainText(f'Version : {my_system.version}')
        self.widget.appendPlainText(f'Machine : {my_system.machine}')
        self.widget.appendPlainText(f'Processor : {my_system.processor}')
        self.widget.appendPlainText('\n#######################################\n')

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendHtml(msg)

class AnotherWindow(QWidget):
    """Show Python logging in debug window"""

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.logTextBox = QTextEditLogger(self)

        formatter = CustomFormatter()
        self.logTextBox.setFormatter(formatter)

        logger.addHandler(self.logTextBox)

        logger.setLevel(logging.DEBUG)

        layout.addWidget(self.logTextBox.widget)
        
        savebutton = QPushButton('Save logs in a file')
        layout.addWidget(savebutton)
        self.setLayout(layout)

        savebutton.clicked.connect(self.saveLog)

    def saveLog(self):
        logs = self.logTextBox.widget.toPlainText()
        document = os.path.expanduser('~/Documents') + '\debug'
        filename = QFileDialog.getSaveFileName(
                self, 'Save file', document, "Log files (*.log)")

        with open(filename[0],'w') as fh:
            fh.writelines(str(logs))

class MainWindow(QMainWindow):
    """
    This is where everything started
    """
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.windowList = []
        self.nameList = []
        self.pathList = []
        self.count = 0
        self.metric_index = []
        self.imperial_index = [[0, 0, 0]]
        self.metricUnit = [[]]
        self.imperialUnit = [[[0, 0, 0]]]
        self.ui.closeEvent = self.closeEvent

        #Debug Window create
        self.debug = AnotherWindow()
        self.debug.resize(900,600)
        self.debug.setWindowTitle('Debug')
        icon = QIcon(":/newPrefix/logo@2x.png")
        self.debug.setWindowIcon(icon)        
        self.debug.setStyleSheet(u"background-color: rgb(58, 64, 76);\n"
                "color: rgb(204, 204, 204);\n"
                "font-size:9.5pt")


        "++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        self.APP_NAME = 'Truss 101'
        self.APP_VERSION = '1.1.1'
        self.APP_UPDATE_TIME = 'February 2021'
        "++++++++++++++++++++++++++++++++++++++++++++++++++++++"

        self.ui.statusbar.showMessage('Welcome to Truss 101')

        logger.info('Sys arguements : %s', str(sys.argv))
        file = os.path.basename(sys.argv[0])
        self.currentDirectory = sys.argv[0].replace(f'{file}', '')
        self.currentDirectory = self.currentDirectory.replace('\\', '/')
        logger.info('Current Directory : %s', self.currentDirectory)

        self.ui.pushButton_new.clicked.connect(self.new)
        self.ui.pushButton_open.clicked.connect(self.openfile)

        self.ui.photo_example.clicked.connect(self.example_1)
        self.ui.pushButton_example.clicked.connect(self.example_1)

        self.ui.photo_example_2.clicked.connect(self.example_2)
        self.ui.pushButton_example_2.clicked.connect(self.example_2)

        self.ui.photo_example_3.clicked.connect(self.example_3)
        self.ui.pushButton_example_3.clicked.connect(self.example_3)

        self.ui.photo_example_4.clicked.connect(self.example_4)
        self.ui.pushButton_example_4.clicked.connect(self.example_4)

        self.ui.photo_example_5.clicked.connect(self.example_5)
        self.ui.pushButton_example_5.clicked.connect(self.example_5)

        self.ui.photo_example_6.clicked.connect(self.example_6)
        self.ui.pushButton_example_6.clicked.connect(self.example_6)

        self.support_button = QPushButton('💝 Support Truss 101 With a Donation  ',self.ui.menubar)
        self.ui.menubar.setCornerWidget(self.support_button)
        self.support_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.support_button.setStyleSheet(
            "QPushButton:pressed { background-color: red }"
            "QPushButton:hover { background-color: rgb(121, 181, 255) }"
            )
        self.support_button.clicked.connect(self.openDonate)

        self.ui.pushButton_sendNote.clicked.connect(self.sayThanks)

        self.ui.actionUnits.triggered.connect(self.unit)
        self.ui.actionNew.triggered.connect(
            lambda: self.ui.tabWidget.setCurrentIndex(0))
        self.ui.actionClose.triggered.connect(self.showDialog)
        self.ui.actionQuit.triggered.connect(self.close)
        self.ui.actionOpen.triggered.connect(self.openfile)
        self.ui.actionSave.triggered.connect(self.savefile)
        self.ui.actionSave_as.triggered.connect(self.saveasfile)
        self.ui.actionHelp.triggered.connect(self.openHelp)
        self.ui.actionCheck_for_updates.triggered.connect(self.updateApp)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Author.triggered.connect(self.aboutAuthor)
        self.ui.actionView_License.triggered.connect(self.openLicense)
        self.ui.actionDebug.triggered.connect(self.debugWindow)

        self.ui.actionSave.setIcon(
            QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.ui.actionClose.setIcon(
            QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))

        self.ui.plainTextMessage.setPlainText('')
        self.ui.plainTextMessage.setPlaceholderText('Dear Monirul Shawon,\nThank you for ...')
        self.ui.plainTextName.setPlaceholderText(user)
        self.name = user

        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabBar().setTabButton(0, QTabBar.RightSide, None)
        self.ui.tabWidget.tabCloseRequested.connect(self.showDialog)
        self.ui.tabWidget.currentChanged.connect(self.unitWindowSet)
        self.ui.tabWidget.setStyleSheet("""
        QTabBar
        {
            font: 63 9pt "Segoe UI Semibold";
            color: black;
        }
        QTabBar::tab::selected {
            font: 63 9pt "Segoe UI Semibold";
            color: steelblue;
        }
        """)


        self.updateApp(oninit=True)

        if len(sys.argv) > 1:
            openwith = (sys.argv[1], "")
            self.openfile(demopath=openwith)
        else:
            pass
    
    def debugWindow(self):
        if self.debug.isVisible():
            self.debug.hide()
        else:
            self.debug.show()


    def openLicense(self):
        QDesktopServices.openUrl(
            "https://github.com/MShawon/Truss-101#license")

    def openDonate(self):
        QDesktopServices.openUrl(
            'https://paypal.me/mshawon1')

    def openHelp(self):
        QDesktopServices.openUrl(
            'https://github.com/MShawon/Truss-101#tutorial')

    def updateApp(self, oninit=False):
        """
        Update application from GitHub repository
        """

        self.oninit = oninit
        logger.info('Checking for updates...')
        self.ui.statusbar.showMessage('Checking for updates...')

        try:
            username = 'MShawon'
            repository = 'Truss-101'
            github_link = f'https://api.github.com/repos/{username}/{repository}/releases/latest'

            logger.info('GitHub api to parse latest version: %s', github_link)

            if self.oninit:
                timeout = 5
                ClientConfig.HTTP_TIMEOUT = 10
            else:
                timeout = 20
                ClientConfig.HTTP_TIMEOUT = 30

            x = requests.get(github_link, timeout=timeout)
            tag = x.json()['tag_name']
            body = x.json()['body']
            logger.info('Latest version : %s , Current Version : %s', tag, self.APP_VERSION)
            
            url = f'https://github.com/{username}/{repository}/releases/download/{tag}'

            # url = 'http://127.0.0.1:8000/'

            ClientConfig.UPDATE_URLS = [url]
            logger.info('Update download urls : %s', ClientConfig.UPDATE_URLS)

            def print_status_info(info):
                total = info.get(u'total')
                downloaded = info.get(u'downloaded')
                status = info.get(u'status')
                percentage = info.get(u'percent_complete')
                logger.info('Downloaded : %s , Total : %s , Status : %s , Pecentage : %s ', str(
                    downloaded), str(total), status, percentage)
                self.ui.statusbar.showMessage(f"{status} {percentage}%")
                if status == 'finished':
                    self.ui.statusbar.showMessage('Update finished')

            client = Client(ClientConfig())

            client.refresh()
            client.add_progress_hook(print_status_info)
            logger.info('Progress hooks %s', client.progress_hooks)

            self.app_update = client.update_check(
                self.APP_NAME, self.APP_VERSION)
            logger.info('App update : %s', self.app_update)

            if self.app_update is not None:
                self.ui.statusbar.showMessage(f'Update available!')
                body = body.splitlines()
                changelog = [line + "<br>" for line in body]
                changelog = "".join(changelog)

                msgBox = QMessageBox()
                msgBox.setWindowFlags(
                    Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setWindowTitle("Update Available!")
                msgBox.setText(
                    f"""<font color='steelblue' size='5'>{self.APP_NAME} version {self.APP_VERSION} needs to update to version {tag}</font>
                    <br><br><u>Changelog : </u><br>{changelog}
                    """)
                msgBox.setInformativeText(
                    "Do you want to download the update?")
                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msgBox.setDefaultButton(QMessageBox.Yes)
                ret = msgBox.exec_()

                if ret == QMessageBox.Yes:
                    logger.info('Version %s downloading...', tag)
                    self.app_update.download(background=True)

                    self.timer = QTimer()
                    self.timer.setInterval(40000)
                    self.timer.timeout.connect(self.extractUpdate)
                    self.timer.start()
                else:
                    logging.warning('App update ignored by user.')
                    pass

            else:
                if self.oninit:
                    logger.info('There are currently no updates available.')
                    self.ui.statusbar.showMessage('Welcome to Truss 101')
                    pass
                else:
                    logger.info('There are currently no updates available.')
                    self.ui.statusbar.showMessage(
                        'There are currently no updates available.')
                    msgBox = QMessageBox()
                    msgBox.setWindowFlags(
                        Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                    msgBox.setWindowTitle("Truss 101")
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText(
                        f"<font color='steelblue' size='5'>There are currently no updates available.</font>")
                    msgBox.exec_()

        except Exception as e:
            logging.critical(str(e))
            if self.oninit:
                self.ui.statusbar.showMessage('Welcome to Truss 101')
                pass
            else:
                self.ui.statusbar.showMessage(
                    'Check your internet connections and try again.')
                msgBox = QMessageBox()
                msgBox.setWindowFlags(
                    Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                msgBox.setWindowTitle("Truss 101")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText(
                    f"<font color='steelblue' size='5'>Something went wrong. Try again!</font>")
                msgBox.setInformativeText('Check your internet connections.')
                msgBox.exec_()

    def extractUpdate(self):
        if self.app_update.is_downloaded():
            msgBox = QMessageBox()
            msgBox.setWindowFlags(
                Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Update")
            msgBox.setText(
                f"<font color='steelblue' size='5'>Update downloaded successfully.</font>")
            msgBox.setInformativeText(
                "Do you want to update now and restart?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.button(QMessageBox.Yes).setText(
                'Update')
            msgBox.setDefaultButton(QMessageBox.Yes)
            ret = msgBox.exec_()
            if ret == QMessageBox.Yes:
                self.timer.stop()
                logger.info('New version downloaded. Extracting started...')
                self.app_update.extract_restart()
            else:
                logging.warning('New version downloaded. Extract ignored by user.')
                self.timer.stop()
                pass

    def about(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowFlags(
            Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.msgBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        icon = QIcon(f"{self.currentDirectory}/logo@4x.png")
        self.msgBox.setIconPixmap(icon.pixmap(96, 96))
        self.msgBox.setText(
            f"<font color='steelblue' size='4'>Version : {self.APP_VERSION} ({self.APP_UPDATE_TIME})</font>")

        self.msgBox.setInformativeText("""This application can solve statically determinate and indeterminate 2D truss structures using the Matrix Displacement Method.<br><br>
        Truss 101 has been developed for educational purposes only. Students or Educators are free to use this application.<br><br>
        GitHub : <a href="https://github.com/MShawon/Truss-101">https://github.com/MShawon/Truss-101</a><br><br>
        If you like my work, consider buying me a coffee ☕ <br>
        <a href="https://paypal.me/mshawon1">https://paypal.me/mshawon1</a><br>""")
        self.msgBox.setWindowTitle("About Truss 101")
        self.msgBox.exec_()

    def aboutAuthor(self):
        self.msgBox = QMessageBox()
        self.msgBox.setWindowFlags(
            Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
        self.msgBox.setText(
            f"""I'm currently a third year undergraduate student at Civil Engineering in Chittagong University of Engineering & Technology.""")
        self.msgBox.setInformativeText(
            "<font color='steelblue' size='3'><b>LinkedIn : </b></font><a href='https://www.linkedin.com/in/monirulislam107/'>Monirul Islam</a>")
        self.msgBox.setWindowTitle("About Author")
        self.msgBox.exec_()

    def unit(self):
        self.window_unit = QMainWindow(parent=self)
        self.ui2 = Ui_MainWindow2()
        self.ui2.setupUi(self.window_unit)
        self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial)
        self.window_unit.show()

        self.activateWindow()
        self.raise_()

        self.ui2.metricButton.clicked.connect(
            lambda: self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_metric))
        self.ui2.radioButton_2.clicked.connect(
            lambda: self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial))

        self.cb_length_m = QComboBox()
        self.cb_length_m.addItems(["m", "mm"])
        self.ui2.layout_length_metric.addWidget(self.cb_length_m)
        self.setLayout(self.ui2.layout_length_metric)

        self.cb_load_m = QComboBox()
        self.cb_load_m.addItems(["kN", "N", "kg"])
        self.ui2.layout_load_metric.addWidget(self.cb_load_m)
        self.setLayout(self.ui2.layout_length_metric)

        self.cb_force_m = QComboBox()
        self.cb_force_m.addItems(["kN", "N", "kg"])
        self.ui2.layout_force_metric.addWidget(self.cb_force_m)
        self.setLayout(self.ui2.layout_force_metric)

        self.cb_displacement_m = QComboBox()
        self.cb_displacement_m.addItem("mm")
        self.ui2.layout_displacement_metric.addWidget(self.cb_displacement_m)
        self.setLayout(self.ui2.layout_displacement_metric)
        self.cb_displacement_m.model().item(0).setEnabled(False)

        self.cb_length_i = QComboBox()
        self.cb_length_i.addItems(["ft", "in"])
        self.ui2.layout_length_imperial.addWidget(self.cb_length_i)
        self.setLayout(self.ui2.layout_length_imperial)

        self.cb_load_i = QComboBox()
        self.cb_load_i.addItems(["kip", "lb"])
        self.ui2.layout_load_imperial.addWidget(self.cb_load_i)
        self.setLayout(self.ui2.layout_length_imperial)

        self.cb_force_i = QComboBox()
        self.cb_force_i.addItems(["kip", "lb"])
        self.ui2.layout_force_imperial.addWidget(self.cb_force_i)
        self.setLayout(self.ui2.layout_force_imperial)

        self.cb_displacement_i = QComboBox()
        self.cb_displacement_i.addItem("in")
        self.ui2.layout_displacement_imperial.addWidget(self.cb_displacement_i)
        self.setLayout(self.ui2.layout_displacement_imperial)
        self.cb_displacement_i.model().item(0).setEnabled(False)
        try:
            if len(self.currentMetricIndex) > 0:
                self.ui2.metricButton.setChecked(True)
                self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_metric)
                self.cb_length_m.setCurrentIndex(self.currentMetricIndex[0][0])
                self.cb_load_m.setCurrentIndex(self.currentMetricIndex[0][1])
                self.cb_force_m.setCurrentIndex(self.currentMetricIndex[0][2])
            elif len(self.currentImperialIndex) > 0:
                self.ui2.radioButton_2.setChecked(True)
                self.ui2.stackedWidget.setCurrentWidget(self.ui2.page_imperial)
                self.cb_length_i.setCurrentIndex(
                    self.currentImperialIndex[0][0])
                self.cb_load_i.setCurrentIndex(self.currentImperialIndex[0][1])
                self.cb_force_i.setCurrentIndex(
                    self.currentImperialIndex[0][2])
        except:
            pass

        self.ui2.buttonBox.accepted.connect(self.updateCb)
        self.ui2.buttonBox.accepted.connect(self.unitPerPage)
        self.ui2.buttonBox.accepted.connect(self.unitWindowSet)
        self.ui2.buttonBox.accepted.connect(self.unitSendToPage)
        self.ui2.buttonBox.accepted.connect(self.unitSendForConverting)
        self.ui2.buttonBox.accepted.connect(self.tab_name_change)


    def updateCb(self):
        self.metric_index = []
        self.imperial_index = []
        if self.ui2.stackedWidget.currentIndex() == 0:
            self.metric_index.append([self.cb_length_m.currentIndex(
            ), self.cb_load_m.currentIndex(), self.cb_force_m.currentIndex()])
        else:
            self.imperial_index.append([self.cb_length_i.currentIndex(
            ), self.cb_load_i.currentIndex(), self.cb_force_i.currentIndex()])

    def closeEvent(self, event):
        index = self.ui.tabWidget.count()
        if index == 1:
            self.usedTime = (time.time() - start_time)/60
            logger.info('Total used time : %s minute', self.usedTime)
            event.accept()

        elif index == 2:
            self.returnValue = None
            self.showDialog(value=1)

            if self.returnValue == QMessageBox.Cancel:
                event.ignore()
            else:
                self.usedTime = (time.time() - start_time)/60
                logger.info('Total used time : %s minute', self.usedTime)
                event.accept()

        else:
            self.msgBox = QMessageBox()
            self.msgBox.setWindowFlags(
                Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
            self.msgBox.setIcon(QMessageBox.Warning)
            self.msgBox.setText(
                f"""<font color='steelblue' size='5'>Do you want to close all  {index-1} opened <br>projects?</font>""")
            self.msgBox.setInformativeText(
                "Your changes will be lost if you don't save them.")
            self.msgBox.setWindowTitle("Truss 101")
            self.msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.msgBox.button(QMessageBox.Yes).setIcon(
                QApplication.style().standardIcon(QStyle.SP_DialogApplyButton))
            self.msgBox.button(QMessageBox.No).setIcon(
                QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
            self.msgBox.setDefaultButton(QMessageBox.Yes)
            self.msgBox.setEscapeButton(QMessageBox.No)
            returnValue = self.msgBox.exec_()
            if returnValue == QMessageBox.Yes:
                self.usedTime = (time.time() - start_time)/60
                logger.info('Total used time : %s minute', self.usedTime)
                event.accept()

            else:
                event.ignore()

    def showDialog(self, value):
        if value:
            index = value
        else:
            index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.windowList[index-1].change > 0:
                self.msgBox = QMessageBox()
                self.msgBox.setWindowFlags(
                    Qt.Dialog | Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
                self.msgBox.setIcon(QMessageBox.Warning)
                self.msgBox.setText(
                    f"""<font color='steelblue' size='5'>Do you want to save the changes you<br>made to {self.ui.tabWidget.tabText(index)}?</font>""")
                self.msgBox.setInformativeText(
                    "Your changes will be lost if you don't save them.")
                self.msgBox.setWindowTitle("Truss 101")
                self.msgBox.setStandardButtons(
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
                self.msgBox.button(QMessageBox.Yes).setText("Save")
                self.msgBox.button(QMessageBox.Yes).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))

                self.msgBox.button(QMessageBox.No).setText("Don't Save")
                self.msgBox.button(QMessageBox.No).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
                self.msgBox.button(QMessageBox.Cancel).setIcon(
                    QApplication.style().standardIcon(QStyle.SP_DialogCancelButton))

                self.msgBox.setDefaultButton(QMessageBox.Yes)
                self.msgBox.setEscapeButton(QMessageBox.Cancel)
                self.returnValue = self.msgBox.exec_()
                if self.returnValue == QMessageBox.Yes:
                    self.savefile()
                    self.closeTab(index=index)
                elif self.returnValue == QMessageBox.No:
                    self.closeTab(index=index)
            else:
                self.closeTab(index=index)

    def closeTab(self, index=None):
        index = index
        self.windowList[index-1].closeEvent()
        self.ui.tabWidget.removeTab(index)
        self.windowList.pop(index-1)
        self.nameList.pop(index-1)
        self.pathList.pop(index-1)
        logger.info('Path List after CLOSING tab: %s', self.pathList)
        logger.info('Name List after CLOSING tab: %s', self.nameList)

        self.metricUnit.pop(index)
        self.imperialUnit.pop(index)

    def savefile(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            self.windowList[index-1].saveToFile()
            path = self.windowList[index-1].filename[0]
            if '/' in path:
                name = path.split('/')[-1][:-4]
            else:
                name = path.split('\\')[-1][:-4]

            self.pathList[index-1] = path
            self.nameList[index-1] = name
            logger.info('Path List after SAVING file: %s', self.pathList)
            logger.info('Name List after SAVING file: %s', self.nameList)
            self.tab_name_change()

    def saveasfile(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            self.windowList[index-1].saveToFile(saveas=True)

    def openfile(self, demopath=None, isdemo=None):
        demopath = demopath
        demo = isdemo
        #demopath= (f"{self.currentDirectory}Demo/Example 6.trs", "")
        self.window = MainPage(open=True, filename=demopath, demo=demo, logger=logger)
        path = self.window.filename[0]
        if '/' in path:
            name = path.split('/')[-1][:-4]
        else:
            name = path.split('\\')[-1][:-4]

        logger.info('Opened file : %s', name)
        index = self.ui.tabWidget.count()
        self.ui.tabWidget.insertTab(index, self.window, name)
        self.ui.tabWidget.setCurrentIndex(index)
        # self.ui.tabWidget.setTabIcon(index,QIcon('Artboard 1@4x-8.png'))
        # self.ui.tabWidget.setIconSize(QSize(24,24))
        self.ui.tabWidget.setTabToolTip(index, path)

        self.windowList.append(self.window)
        self.pathList.append(path)
        self.nameList.append(name)
        logger.info('Path List : %s', self.pathList)
        logger.info('Name List : %s', self.nameList)

        self.currentMetricIndex = self.window.currentMetricIndex
        self.currentImperialIndex = self.window.currentImperialIndex
        self.metricUnit.append(self.currentMetricIndex)
        self.imperialUnit.append(self.currentImperialIndex)

        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_nodes.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_members.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_supports.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_loads.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_property.cellChanged.connect(self.tab_name_change)
        self.ui.statusbar.showMessage(
            'Nodes are the points in (x,y) co-ordinate. Input (x,y) points in nodes table.')
        self.window.ui.pushbutton_nodes.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Nodes are the points in (x,y) co-ordinate. Input (x,y) points in nodes table.'))
        self.window.ui.pushbutton_members.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define members by connecting nodes. Don\'t forget to look at the graph while connecting nodes!'))
        self.window.ui.pushbutton_supports.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Three types of constraints are available. Select the appropriate one from the drop-down lists.'))
        self.window.ui.pushbutton_loads.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define nodal load and angle (degree) according to the node number.'))
        self.window.ui.pushbutton_properties.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define modulus of elasticity (E) and cross-sectional area (A) of the material.'))
        self.window.ui.pushbutton_displacement.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Use deflection magnifier to clearly see the displaced shape in blue.'))
        self.window.ui.pushbutton_forces.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Checkboxes in the top right can be used to modify graph details.'))
        self.window.ui.pushbutton_influenceLine.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Load path is plotted as a red line. Use Member box to navigate through members influence line.'))
        self.window.ui.pushbutton_report.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Once the pdf has been generated, it will be opened automatically.'))

    def new(self):
        self.count += 1
        self.window = MainPage(logger=logger)
        index = self.ui.tabWidget.count()
        name = f'Project Truss {self.count}'
        self.ui.tabWidget.insertTab(index, self.window, name)
        self.ui.tabWidget.setCurrentIndex(index)
        # self.ui.tabWidget.setTabIcon(index,QIcon('truss.png'))
        # self.ui.tabWidget.setIconSize(QSize(24,24))
        self.ui.tabWidget.setTabToolTip(index, name)

        self.windowList.append(self.window)
        self.pathList.append(name)
        self.nameList.append(name)
        logger.info('Path List : %s', self.pathList)
        logger.info('Name List : %s', self.nameList)

        self.metric_index = []
        self.imperial_index = [[0, 0, 0]]
        self.unitPerPage()
        self.unitSendToPage()

        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_nodes.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_members.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_supports.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_loads.cellChanged.connect(self.tab_name_change)
        self.windowList[self.ui.tabWidget.currentIndex(
        )-1].ui.tableWidget_property.cellChanged.connect(self.tab_name_change)
        self.ui.statusbar.showMessage(
            'Nodes are the points in (x,y) co-ordinate. Input (x,y) points in nodes table.')
        self.window.ui.pushbutton_nodes.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Nodes are the points in (x,y) co-ordinate. Input (x,y) points in nodes table.'))
        self.window.ui.pushbutton_members.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define members by connecting nodes. Don\'t forget to look at the graph while connecting nodes!'))
        self.window.ui.pushbutton_supports.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Three types of constraints are available. Select the appropriate one from the drop-down lists.'))
        self.window.ui.pushbutton_loads.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define nodal load and angle (degree) according to the node number.'))
        self.window.ui.pushbutton_properties.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Define modulus of elasticity (E) and cross-sectional area (A) of the material.'))
        self.window.ui.pushbutton_displacement.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Use deflection magnifier to clearly see the displaced shape in blue.'))
        self.window.ui.pushbutton_forces.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Checkboxes in the top right can be used to modify graph details.'))
        self.window.ui.pushbutton_influenceLine.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Load path is plotted as a red line. Use Member box to navigate through members influence line.'))
        self.window.ui.pushbutton_report.clicked.connect(lambda: self.ui.statusbar.showMessage(
            'Once the pdf has been generated, it will be opened automatically.'))

    def unitPerPage(self):
        index = self.ui.tabWidget.currentIndex()
        try:
            self.metricUnit[index] = self.metric_index
            self.imperialUnit[index] = self.imperial_index
        except:
            self.metricUnit.append(self.metric_index)
            self.imperialUnit.append(self.imperial_index)

    def unitWindowSet(self):
        index = self.ui.tabWidget.currentIndex()
        try:
            self.currentMetricIndex = self.metricUnit[index]
            self.currentImperialIndex = self.imperialUnit[index]
        except:
            self.currentMetricIndex = []
            self.currentImperialIndex = [[0, 0, 0]]
        if index == 0:
            self.ui.statusbar.showMessage('Welcome to Truss 101')

    def unitSendToPage(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.currentMetricIndex:
                self.windowList[index-1].change_unit_label(
                    unit=self.currentMetricIndex, type='metric')
            else:
                self.windowList[index-1].change_unit_label(
                    unit=self.currentImperialIndex, type='imperial')

    def unitSendForConverting(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.currentMetricIndex:
                self.windowList[index-1].unitConvert(type='metric')
            else:
                self.windowList[index-1].unitConvert(type='imperial')

    def tab_name_change(self):
        index = self.ui.tabWidget.currentIndex()
        if index > 0:
            if self.windowList[index-1].change > 0:
                self.ui.tabWidget.setTabText(index, self.nameList[index-1]+"*")
                self.ui.tabWidget.setTabToolTip(
                    index, f'{self.pathList[index-1]}')

            elif self.windowList[index-1].change == 0:
                self.ui.tabWidget.setTabText(index, self.nameList[index-1])
                self.ui.tabWidget.setTabToolTip(
                    index, f'{self.pathList[index-1]}')

    def sayThanks(self):
        webhook_id = 'your webhook id'
        webhook_token = 'your webhook token'
        webhook_url = f'https://discord.com/api/webhooks/{webhook_id}/{webhook_token}'

        if self.ui.plainTextMessage.toPlainText():
            messeage = self.ui.plainTextMessage.toPlainText()
        else:
            messeage = 'Dear Monirul Shawon, Thank you for...'      

        if self.ui.plainTextName.toPlainText():
            user = self.ui.plainTextName.toPlainText()
            note = {
                "content" : f'{messeage}',
                "username" : f'{user}'
            }
        else:
            note = {
                "content" : f'{messeage}',
                "username" : f'{self.name}'
            }

        try:
            requests.post(url=webhook_url, json=note, timeout=30)
            self.ui.plainTextMessage.setPlaceholderText('Thank you for sending the notes. Your notes have been sent successfully.')
            logger.info('Notes have been sent successfully')
        except:
            self.ui.plainTextMessage.setPlaceholderText('Oops! Something went wrong. Try again.')
            pass


    def example_1(self):
        example_path = (f"{self.currentDirectory}Demo/Example 1.trs", "")
        self.openfile(demopath=example_path, isdemo=True)

    def example_2(self):
        example_path = (f"{self.currentDirectory}Demo/Example 2.trs", "")
        self.openfile(demopath=example_path, isdemo=True)

    def example_3(self):
        example_path = (f"{self.currentDirectory}Demo/Example 3.trs", "")
        self.openfile(demopath=example_path, isdemo=True)

    def example_4(self):
        example_path = (f"{self.currentDirectory}Demo/Example 4.trs", "")
        self.openfile(demopath=example_path, isdemo=True)

    def example_5(self):
        example_path = (f"{self.currentDirectory}Demo/Example 5.trs", "")
        self.openfile(demopath=example_path, isdemo=True)

    def example_6(self):
        example_path = (f"{self.currentDirectory}Demo/Example 6.trs", "")
        self.openfile(demopath=example_path, isdemo=True)


if __name__ == "__main__":
    start_time = time.time()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    window = MainWindow()
    window.show()

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    logger.info('Screen size : %s', screensize)
    if screensize[0] == 1280:
        pass
    else:
        window.resize(screensize[0]*.9, screensize[1]*.9)
        x = screensize[0]*0.05
        window.move(x, 3)


    startUpTime = time.time() - start_time
    logger.info('Statup time : %.3f seconds' % startUpTime)
    sys.exit(app.exec_())
