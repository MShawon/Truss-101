# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unitslFbzQx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(559, 375)
        MainWindow.setMinimumSize(QSize(559, 375))
        MainWindow.setMaximumSize(QSize(559, 375))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u" QComboBox {	\n"
"	font: 10pt \"MS Sans Serif\";\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 10)
        self.verticalSpacer_3 = QSpacerItem(20, 45, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        font1 = QFont()
        font1.setPointSize(9)
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.metricButton = QRadioButton(self.centralwidget)
        self.metricButton.setObjectName(u"metricButton")
        self.metricButton.setFont(font1)
        self.metricButton.setChecked(False)

        self.verticalLayout.addWidget(self.metricButton)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 5, -1, -1)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_metric = QWidget()
        self.page_metric.setObjectName(u"page_metric")
        self.verticalLayout_3 = QVBoxLayout(self.page_metric)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.page_metric)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2)

        self.layout_length_metric = QVBoxLayout()
        self.layout_length_metric.setObjectName(u"layout_length_metric")

        self.verticalLayout_3.addLayout(self.layout_length_metric)

        self.label_3 = QLabel(self.page_metric)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_3)

        self.layout_load_metric = QVBoxLayout()
        self.layout_load_metric.setObjectName(u"layout_load_metric")

        self.verticalLayout_3.addLayout(self.layout_load_metric)

        self.label_4 = QLabel(self.page_metric)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.layout_force_metric = QVBoxLayout()
        self.layout_force_metric.setObjectName(u"layout_force_metric")

        self.verticalLayout_3.addLayout(self.layout_force_metric)

        self.label_5 = QLabel(self.page_metric)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_5)

        self.layout_displacement_metric = QVBoxLayout()
        self.layout_displacement_metric.setObjectName(u"layout_displacement_metric")

        self.verticalLayout_3.addLayout(self.layout_displacement_metric)

        self.stackedWidget.addWidget(self.page_metric)
        self.page_imperial = QWidget()
        self.page_imperial.setObjectName(u"page_imperial")
        self.verticalLayout_4 = QVBoxLayout(self.page_imperial)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.page_imperial)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_6)

        self.layout_length_imperial = QVBoxLayout()
        self.layout_length_imperial.setObjectName(u"layout_length_imperial")

        self.verticalLayout_4.addLayout(self.layout_length_imperial)

        self.label_8 = QLabel(self.page_imperial)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_8)

        self.layout_load_imperial = QVBoxLayout()
        self.layout_load_imperial.setObjectName(u"layout_load_imperial")

        self.verticalLayout_4.addLayout(self.layout_load_imperial)

        self.label_9 = QLabel(self.page_imperial)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_9)

        self.layout_force_imperial = QVBoxLayout()
        self.layout_force_imperial.setObjectName(u"layout_force_imperial")

        self.verticalLayout_4.addLayout(self.layout_force_imperial)

        self.label_7 = QLabel(self.page_imperial)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_7)

        self.layout_displacement_imperial = QVBoxLayout()
        self.layout_displacement_imperial.setObjectName(u"layout_displacement_imperial")

        self.verticalLayout_4.addLayout(self.layout_displacement_imperial)

        self.stackedWidget.addWidget(self.page_imperial)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.buttonBox.accepted.connect(MainWindow.close)
        self.buttonBox.rejected.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Units", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Unit System :", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Imperial", None))
        self.metricButton.setText(QCoreApplication.translate("MainWindow", u"Metric", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Length :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Applied Loads:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Member Forces :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nodal Displacement : ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Length :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Applied Loads:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Member Forces :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nodal Displacement : ", None))
    # retranslateUi

