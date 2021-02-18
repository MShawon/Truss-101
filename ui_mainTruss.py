# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainTrussEJGyIi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        if not WizardPage.objectName():
            WizardPage.setObjectName(u"WizardPage")
        WizardPage.resize(1099, 544)
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
        WizardPage.setPalette(palette)
        WizardPage.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(WizardPage)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(7)
        self.groupBox = QGroupBox(WizardPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 5, 0, 1, 1)

        self.pushbutton_displacement = QPushButton(self.groupBox)
        self.pushbutton_displacement.setObjectName(u"pushbutton_displacement")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushbutton_displacement.sizePolicy().hasHeightForWidth())
        self.pushbutton_displacement.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushbutton_displacement.setFont(font)
        self.pushbutton_displacement.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_displacement.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 152, 93);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 135, 55);\n"
"    border-style: inset;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/displacement.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_displacement.setIcon(icon)

        self.gridLayout_2.addWidget(self.pushbutton_displacement, 7, 0, 1, 1)

        self.pushbutton_supports = QPushButton(self.groupBox)
        self.pushbutton_supports.setObjectName(u"pushbutton_supports")
        sizePolicy.setHeightForWidth(self.pushbutton_supports.sizePolicy().hasHeightForWidth())
        self.pushbutton_supports.setSizePolicy(sizePolicy)
        self.pushbutton_supports.setFont(font)
        self.pushbutton_supports.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_supports.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(135, 177, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/support.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_supports.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushbutton_supports, 2, 0, 1, 1)

        self.pushbutton_properties = QPushButton(self.groupBox)
        self.pushbutton_properties.setObjectName(u"pushbutton_properties")
        sizePolicy.setHeightForWidth(self.pushbutton_properties.sizePolicy().hasHeightForWidth())
        self.pushbutton_properties.setSizePolicy(sizePolicy)
        self.pushbutton_properties.setFont(font)
        self.pushbutton_properties.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_properties.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(135, 177, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/property.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_properties.setIcon(icon2)

        self.gridLayout_2.addWidget(self.pushbutton_properties, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.pushbutton_influenceLine = QPushButton(self.groupBox)
        self.pushbutton_influenceLine.setObjectName(u"pushbutton_influenceLine")
        sizePolicy.setHeightForWidth(self.pushbutton_influenceLine.sizePolicy().hasHeightForWidth())
        self.pushbutton_influenceLine.setSizePolicy(sizePolicy)
        self.pushbutton_influenceLine.setFont(font)
        self.pushbutton_influenceLine.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_influenceLine.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 152, 93);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 135, 55);\n"
"    border-style: inset;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/moving.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_influenceLine.setIcon(icon3)

        self.gridLayout_2.addWidget(self.pushbutton_influenceLine, 9, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 10, 0, 1, 1)

        self.pushbutton_forces = QPushButton(self.groupBox)
        self.pushbutton_forces.setObjectName(u"pushbutton_forces")
        sizePolicy.setHeightForWidth(self.pushbutton_forces.sizePolicy().hasHeightForWidth())
        self.pushbutton_forces.setSizePolicy(sizePolicy)
        self.pushbutton_forces.setFont(font)
        self.pushbutton_forces.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_forces.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 152, 93);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 135, 55);\n"
"    border-style: inset;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/stress.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_forces.setIcon(icon4)

        self.gridLayout_2.addWidget(self.pushbutton_forces, 8, 0, 1, 1)

        self.pushbutton_nodes = QPushButton(self.groupBox)
        self.pushbutton_nodes.setObjectName(u"pushbutton_nodes")
        sizePolicy.setHeightForWidth(self.pushbutton_nodes.sizePolicy().hasHeightForWidth())
        self.pushbutton_nodes.setSizePolicy(sizePolicy)
        self.pushbutton_nodes.setFont(font)
        self.pushbutton_nodes.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_nodes.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(135, 177, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/node.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_nodes.setIcon(icon5)
        self.pushbutton_nodes.setAutoDefault(False)
        self.pushbutton_nodes.setFlat(False)

        self.gridLayout_2.addWidget(self.pushbutton_nodes, 0, 0, 1, 1)

        self.pushbutton_members = QPushButton(self.groupBox)
        self.pushbutton_members.setObjectName(u"pushbutton_members")
        sizePolicy.setHeightForWidth(self.pushbutton_members.sizePolicy().hasHeightForWidth())
        self.pushbutton_members.setSizePolicy(sizePolicy)
        self.pushbutton_members.setFont(font)
        self.pushbutton_members.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_members.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(135, 177, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/member.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_members.setIcon(icon6)

        self.gridLayout_2.addWidget(self.pushbutton_members, 1, 0, 1, 1)

        self.pushbutton_report = QPushButton(self.groupBox)
        self.pushbutton_report.setObjectName(u"pushbutton_report")
        sizePolicy.setHeightForWidth(self.pushbutton_report.sizePolicy().hasHeightForWidth())
        self.pushbutton_report.setSizePolicy(sizePolicy)
        self.pushbutton_report.setFont(font)
        self.pushbutton_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_report.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(6, 207, 155);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(4, 163, 121);\n"
"    border-style: inset;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_report.setIcon(icon7)

        self.gridLayout_2.addWidget(self.pushbutton_report, 12, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 11, 0, 1, 1)

        self.pushbutton_loads = QPushButton(self.groupBox)
        self.pushbutton_loads.setObjectName(u"pushbutton_loads")
        sizePolicy.setHeightForWidth(self.pushbutton_loads.sizePolicy().hasHeightForWidth())
        self.pushbutton_loads.setSizePolicy(sizePolicy)
        self.pushbutton_loads.setFont(font)
        self.pushbutton_loads.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushbutton_loads.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(135, 177, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/load.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushbutton_loads.setIcon(icon8)

        self.gridLayout_2.addWidget(self.pushbutton_loads, 3, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 13, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(WizardPage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_geometry = QWidget()
        self.page_geometry.setObjectName(u"page_geometry")
        self.gridLayout_8 = QGridLayout(self.page_geometry)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stackedWidget_2 = QStackedWidget(self.page_geometry)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(330, 500))
        self.stackedWidget_2.setMaximumSize(QSize(350, 16777215))
        self.page_node = QWidget()
        self.page_node.setObjectName(u"page_node")
        self.gridLayout = QGridLayout(self.page_node)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 5, -1, -1)
        self.label_8 = QLabel(self.page_node)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 2, 0, 2, 1)

        self.line_4 = QFrame(self.page_node)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 1, 0, 1, 3)

        self.label_unit_node = QLabel(self.page_node)
        self.label_unit_node.setObjectName(u"label_unit_node")
        self.label_unit_node.setMinimumSize(QSize(291, 16))
        self.label_unit_node.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_unit_node.setFont(font2)

        self.gridLayout.addWidget(self.label_unit_node, 5, 0, 1, 3)

        self.tableWidget_nodes = QTableWidget(self.page_node)
        if (self.tableWidget_nodes.columnCount() < 2):
            self.tableWidget_nodes.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setBackground(QColor(85, 255, 127));
        self.tableWidget_nodes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setBackground(QColor(255, 85, 0));
        self.tableWidget_nodes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_nodes.rowCount() < 2):
            self.tableWidget_nodes.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_nodes.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_nodes.setVerticalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_nodes.setObjectName(u"tableWidget_nodes")
        self.tableWidget_nodes.setAlternatingRowColors(True)
        self.tableWidget_nodes.setTextElideMode(Qt.ElideRight)
        self.tableWidget_nodes.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget_nodes, 4, 0, 1, 3)

        self.update_nodes = QPushButton(self.page_node)
        self.update_nodes.setObjectName(u"update_nodes")
        self.update_nodes.setMinimumSize(QSize(23, 35))
        self.update_nodes.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_nodes.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.update_nodes, 2, 2, 2, 1)

        self.label_7 = QLabel(self.page_node)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_7.setFont(font3)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.spinBox_nodes = QSpinBox(self.page_node)
        self.spinBox_nodes.setObjectName(u"spinBox_nodes")
        self.spinBox_nodes.setMinimumSize(QSize(0, 30))
        self.spinBox_nodes.setMaximumSize(QSize(50, 16777215))
        self.spinBox_nodes.setMinimum(2)
        self.spinBox_nodes.setValue(2)

        self.gridLayout.addWidget(self.spinBox_nodes, 3, 1, 1, 1)

        self.stackedWidget_2.addWidget(self.page_node)
        self.page_member = QWidget()
        self.page_member.setObjectName(u"page_member")
        self.gridLayout_4 = QGridLayout(self.page_member)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 5, -1, -1)
        self.line_2 = QFrame(self.page_member)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 1, 0, 1, 3)

        self.label_3 = QLabel(self.page_member)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.spinBox_members = QSpinBox(self.page_member)
        self.spinBox_members.setObjectName(u"spinBox_members")
        self.spinBox_members.setMinimumSize(QSize(0, 30))
        self.spinBox_members.setMaximumSize(QSize(50, 16777215))
        self.spinBox_members.setMinimum(1)
        self.spinBox_members.setValue(1)

        self.gridLayout_4.addWidget(self.spinBox_members, 2, 1, 1, 1)

        self.label_4 = QLabel(self.page_member)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.update_members = QPushButton(self.page_member)
        self.update_members.setObjectName(u"update_members")
        self.update_members.setMinimumSize(QSize(23, 35))
        self.update_members.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_members.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.update_members, 2, 2, 1, 1)

        self.tableWidget_members = QTableWidget(self.page_member)
        if (self.tableWidget_members.columnCount() < 2):
            self.tableWidget_members.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setBackground(QColor(85, 255, 127));
        self.tableWidget_members.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(255, 85, 0));
        self.tableWidget_members.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        if (self.tableWidget_members.rowCount() < 1):
            self.tableWidget_members.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_members.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_members.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_members.setItem(0, 1, __qtablewidgetitem8)
        self.tableWidget_members.setObjectName(u"tableWidget_members")
        self.tableWidget_members.setAlternatingRowColors(True)
        self.tableWidget_members.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget_members, 3, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.page_member)
        self.page_supports = QWidget()
        self.page_supports.setObjectName(u"page_supports")
        self.gridLayout_5 = QGridLayout(self.page_supports)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 5, -1, -1)
        self.label_5 = QLabel(self.page_supports)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 3)

        self.line_3 = QFrame(self.page_supports)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 1, 0, 1, 3)

        self.label_6 = QLabel(self.page_supports)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinBox_supports = QSpinBox(self.page_supports)
        self.spinBox_supports.setObjectName(u"spinBox_supports")
        self.spinBox_supports.setMinimumSize(QSize(0, 30))
        self.spinBox_supports.setMaximumSize(QSize(50, 16777215))
        self.spinBox_supports.setMinimum(2)
        self.spinBox_supports.setValue(2)

        self.gridLayout_5.addWidget(self.spinBox_supports, 2, 1, 1, 1)

        self.update_supports = QPushButton(self.page_supports)
        self.update_supports.setObjectName(u"update_supports")
        self.update_supports.setMinimumSize(QSize(23, 35))
        self.update_supports.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_supports.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.gridLayout_5.addWidget(self.update_supports, 2, 2, 1, 1)

        self.tableWidget_supports = QTableWidget(self.page_supports)
        if (self.tableWidget_supports.columnCount() < 2):
            self.tableWidget_supports.setColumnCount(2)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setBackground(QColor(85, 255, 127));
        self.tableWidget_supports.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setBackground(QColor(255, 85, 0));
        self.tableWidget_supports.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        if (self.tableWidget_supports.rowCount() < 2):
            self.tableWidget_supports.setRowCount(2)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_supports.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_supports.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_supports.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_supports.setItem(1, 0, __qtablewidgetitem14)
        self.tableWidget_supports.setObjectName(u"tableWidget_supports")
        self.tableWidget_supports.setAlternatingRowColors(True)
        self.tableWidget_supports.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_5.addWidget(self.tableWidget_supports, 3, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.page_supports)
        self.page_loads = QWidget()
        self.page_loads.setObjectName(u"page_loads")
        self.gridLayout_3 = QGridLayout(self.page_loads)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 5, -1, -1)
        self.label_9 = QLabel(self.page_loads)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.line_5 = QFrame(self.page_loads)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 1, 0, 1, 3)

        self.label_10 = QLabel(self.page_loads)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.spinBox_loads = QSpinBox(self.page_loads)
        self.spinBox_loads.setObjectName(u"spinBox_loads")
        self.spinBox_loads.setMinimumSize(QSize(0, 30))
        self.spinBox_loads.setMaximumSize(QSize(50, 16777215))
        self.spinBox_loads.setMinimum(1)
        self.spinBox_loads.setValue(1)

        self.gridLayout_3.addWidget(self.spinBox_loads, 2, 1, 1, 1)

        self.update_loads = QPushButton(self.page_loads)
        self.update_loads.setObjectName(u"update_loads")
        self.update_loads.setMinimumSize(QSize(23, 35))
        self.update_loads.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_loads.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.update_loads, 2, 2, 1, 1)

        self.tableWidget_loads = QTableWidget(self.page_loads)
        if (self.tableWidget_loads.columnCount() < 3):
            self.tableWidget_loads.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setBackground(QColor(85, 255, 127));
        self.tableWidget_loads.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setBackground(QColor(255, 85, 0));
        self.tableWidget_loads.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setBackground(QColor(85, 170, 255));
        self.tableWidget_loads.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        if (self.tableWidget_loads.rowCount() < 1):
            self.tableWidget_loads.setRowCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_loads.setVerticalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_loads.setItem(0, 0, __qtablewidgetitem19)
        self.tableWidget_loads.setObjectName(u"tableWidget_loads")
        self.tableWidget_loads.setAlternatingRowColors(True)
        self.tableWidget_loads.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_loads.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_loads.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.tableWidget_loads, 3, 0, 1, 3)

        self.label_unit_load = QLabel(self.page_loads)
        self.label_unit_load.setObjectName(u"label_unit_load")
        self.label_unit_load.setMinimumSize(QSize(291, 16))
        self.label_unit_load.setMaximumSize(QSize(16777215, 40))
        self.label_unit_load.setFont(font2)

        self.gridLayout_3.addWidget(self.label_unit_load, 4, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.page_loads)
        self.page_properties = QWidget()
        self.page_properties.setObjectName(u"page_properties")
        self.gridLayout_6 = QGridLayout(self.page_properties)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 5, -1, -1)
        self.spinBox_property = QSpinBox(self.page_properties)
        self.spinBox_property.setObjectName(u"spinBox_property")
        self.spinBox_property.setMinimumSize(QSize(0, 30))
        self.spinBox_property.setMaximumSize(QSize(50, 16777215))
        self.spinBox_property.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_property.setMinimum(1)
        self.spinBox_property.setValue(1)

        self.gridLayout_6.addWidget(self.spinBox_property, 3, 1, 1, 1)

        self.label_12 = QLabel(self.page_properties)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_12, 3, 0, 1, 1)

        self.label = QLabel(self.page_properties)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_6.addWidget(self.label, 6, 0, 1, 3)

        self.line_6 = QFrame(self.page_properties)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line_6, 1, 0, 1, 3)

        self.tableWidget_property = QTableWidget(self.page_properties)
        if (self.tableWidget_property.columnCount() < 2):
            self.tableWidget_property.setColumnCount(2)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setBackground(QColor(85, 255, 127));
        self.tableWidget_property.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setBackground(QColor(255, 85, 0));
        self.tableWidget_property.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        if (self.tableWidget_property.rowCount() < 1):
            self.tableWidget_property.setRowCount(1)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_property.setVerticalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_property.setItem(0, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_property.setItem(0, 1, __qtablewidgetitem24)
        self.tableWidget_property.setObjectName(u"tableWidget_property")
        self.tableWidget_property.setInputMethodHints(Qt.ImhNone)
        self.tableWidget_property.setAlternatingRowColors(True)
        self.tableWidget_property.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_property.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_property.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_property, 4, 0, 1, 3)

        self.label_unit_property = QLabel(self.page_properties)
        self.label_unit_property.setObjectName(u"label_unit_property")
        self.label_unit_property.setMinimumSize(QSize(291, 16))
        self.label_unit_property.setMaximumSize(QSize(16777215, 40))
        self.label_unit_property.setFont(font2)

        self.gridLayout_6.addWidget(self.label_unit_property, 5, 0, 1, 3)

        self.update_property = QPushButton(self.page_properties)
        self.update_property.setObjectName(u"update_property")
        self.update_property.setMinimumSize(QSize(23, 35))
        self.update_property.setCursor(QCursor(Qt.PointingHandCursor))
        self.update_property.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.update_property, 3, 2, 1, 1)

        self.label_2 = QLabel(self.page_properties)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(9)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 3)

        self.label_11 = QLabel(self.page_properties)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 3)

        self.stackedWidget_2.addWidget(self.page_properties)

        self.gridLayout_8.addWidget(self.stackedWidget_2, 0, 0, 2, 1)

        self.label_23 = QLabel(self.page_geometry)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(300, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(10)
        self.label_23.setFont(font5)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_23, 0, 1, 1, 1)

        self.radioButtonDefault = QRadioButton(self.page_geometry)
        self.radioButtonDefault.setObjectName(u"radioButtonDefault")
        self.radioButtonDefault.setMaximumSize(QSize(100, 16777215))
        self.radioButtonDefault.setFont(font4)
        self.radioButtonDefault.setChecked(True)

        self.gridLayout_8.addWidget(self.radioButtonDefault, 0, 2, 1, 1)

        self.radioButtonBlack = QRadioButton(self.page_geometry)
        self.radioButtonBlack.setObjectName(u"radioButtonBlack")
        self.radioButtonBlack.setMaximumSize(QSize(100, 16777215))
        self.radioButtonBlack.setFont(font4)

        self.gridLayout_8.addWidget(self.radioButtonBlack, 0, 3, 1, 1)

        self.label_stabality = QLabel(self.page_geometry)
        self.label_stabality.setObjectName(u"label_stabality")
        self.label_stabality.setMinimumSize(QSize(100, 20))
        self.label_stabality.setMaximumSize(QSize(61625, 20))
        self.label_stabality.setFont(font3)
        self.label_stabality.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.label_stabality.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_stabality, 0, 4, 1, 1)

        self.graphLayout_geometry = QVBoxLayout()
        self.graphLayout_geometry.setSpacing(0)
        self.graphLayout_geometry.setObjectName(u"graphLayout_geometry")
        self.graphLayout_geometry.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_8.addLayout(self.graphLayout_geometry, 1, 1, 1, 4)

        self.stackedWidget.addWidget(self.page_geometry)
        self.page_displacement = QWidget()
        self.page_displacement.setObjectName(u"page_displacement")
        self.gridLayout_9 = QGridLayout(self.page_displacement)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_14 = QLabel(self.page_displacement)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 35))
        self.label_14.setFont(font3)

        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_16 = QLabel(self.page_displacement)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_16, 0, 1, 1, 1)

        self.pushButton_start = QPushButton(self.page_displacement)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(35, 0))
        self.pushButton_start.setMaximumSize(QSize(150, 35))
        self.pushButton_start.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(123, 193, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 162, 255);\n"
"    border-style: inset;\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_start, 0, 2, 1, 1)

        self.pushButton_stop = QPushButton(self.page_displacement)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setMinimumSize(QSize(35, 0))
        self.pushButton_stop.setMaximumSize(QSize(149, 35))
        self.pushButton_stop.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 101, 111);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 49);\n"
"    border-style: inset;\n"
"}")

        self.gridLayout_9.addWidget(self.pushButton_stop, 0, 3, 1, 1)

        self.label_13 = QLabel(self.page_displacement)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.label_13, 0, 4, 1, 1)

        self.horizontalSlider = QSlider(self.page_displacement)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(150, 16777215))
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(10)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_9.addWidget(self.horizontalSlider, 0, 5, 1, 1)

        self.line_7 = QFrame(self.page_displacement)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_7, 1, 0, 1, 1)

        self.label_15 = QLabel(self.page_displacement)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font4)

        self.gridLayout_9.addWidget(self.label_15, 2, 0, 1, 1)

        self.tableWidget_displacement = QTableWidget(self.page_displacement)
        if (self.tableWidget_displacement.columnCount() < 3):
            self.tableWidget_displacement.setColumnCount(3)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setBackground(QColor(85, 255, 127));
        self.tableWidget_displacement.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setBackground(QColor(255, 85, 0));
        self.tableWidget_displacement.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setBackground(QColor(85, 170, 255));
        self.tableWidget_displacement.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        if (self.tableWidget_displacement.rowCount() < 1):
            self.tableWidget_displacement.setRowCount(1)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_displacement.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_displacement.setItem(0, 0, __qtablewidgetitem29)
        self.tableWidget_displacement.setObjectName(u"tableWidget_displacement")
        self.tableWidget_displacement.setMinimumSize(QSize(0, 0))
        self.tableWidget_displacement.setMaximumSize(QSize(350, 16777215))
        self.tableWidget_displacement.setAlternatingRowColors(True)
        self.tableWidget_displacement.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget_displacement.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_displacement.verticalHeader().setVisible(False)

        self.gridLayout_9.addWidget(self.tableWidget_displacement, 3, 0, 1, 1)

        self.label_unit_displacement = QLabel(self.page_displacement)
        self.label_unit_displacement.setObjectName(u"label_unit_displacement")
        self.label_unit_displacement.setMinimumSize(QSize(291, 16))
        self.label_unit_displacement.setMaximumSize(QSize(16777215, 40))
        self.label_unit_displacement.setFont(font2)

        self.gridLayout_9.addWidget(self.label_unit_displacement, 4, 0, 1, 1)

        self.graphLayout_displacement = QVBoxLayout()
        self.graphLayout_displacement.setSpacing(0)
        self.graphLayout_displacement.setObjectName(u"graphLayout_displacement")
        self.graphLayout_displacement.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_9.addLayout(self.graphLayout_displacement, 1, 1, 4, 5)

        self.stackedWidget.addWidget(self.page_displacement)
        self.page_forces = QWidget()
        self.page_forces.setObjectName(u"page_forces")
        self.gridLayout_10 = QGridLayout(self.page_forces)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tableWidget_result = QTableWidget(self.page_forces)
        if (self.tableWidget_result.columnCount() < 4):
            self.tableWidget_result.setColumnCount(4)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setBackground(QColor(238, 64, 53));
        self.tableWidget_result.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setBackground(QColor(243, 119, 54));
        self.tableWidget_result.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setBackground(QColor(253, 244, 152));
        self.tableWidget_result.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setBackground(QColor(123, 192, 67));
        self.tableWidget_result.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        if (self.tableWidget_result.rowCount() < 1):
            self.tableWidget_result.setRowCount(1)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_result.setVerticalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_result.setItem(0, 0, __qtablewidgetitem35)
        self.tableWidget_result.setObjectName(u"tableWidget_result")
        self.tableWidget_result.setMinimumSize(QSize(0, 0))
        self.tableWidget_result.setMaximumSize(QSize(350, 16777215))
        self.tableWidget_result.setAlternatingRowColors(True)
        self.tableWidget_result.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_result.verticalHeader().setVisible(False)

        self.gridLayout_10.addWidget(self.tableWidget_result, 3, 1, 1, 1)

        self.label_unit_stress = QLabel(self.page_forces)
        self.label_unit_stress.setObjectName(u"label_unit_stress")
        self.label_unit_stress.setMinimumSize(QSize(291, 20))
        self.label_unit_stress.setMaximumSize(QSize(16777215, 40))
        self.label_unit_stress.setFont(font2)

        self.gridLayout_10.addWidget(self.label_unit_stress, 4, 1, 1, 1)

        self.checkBox_loads = QCheckBox(self.page_forces)
        self.checkBox_loads.setObjectName(u"checkBox_loads")
        self.checkBox_loads.setMinimumSize(QSize(80, 0))
        self.checkBox_loads.setMaximumSize(QSize(100, 16777215))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        self.checkBox_loads.setFont(font6)
        self.checkBox_loads.setChecked(True)

        self.gridLayout_10.addWidget(self.checkBox_loads, 0, 5, 1, 1)

        self.checkBox_reactions = QCheckBox(self.page_forces)
        self.checkBox_reactions.setObjectName(u"checkBox_reactions")
        self.checkBox_reactions.setMinimumSize(QSize(80, 0))
        self.checkBox_reactions.setFont(font6)
        self.checkBox_reactions.setChecked(True)

        self.gridLayout_10.addWidget(self.checkBox_reactions, 0, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 0, 7, 1, 1)

        self.label_18 = QLabel(self.page_forces)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 35))
        self.label_18.setFont(font3)

        self.gridLayout_10.addWidget(self.label_18, 0, 1, 1, 1)

        self.label_17 = QLabel(self.page_forces)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)

        self.gridLayout_10.addWidget(self.label_17, 2, 1, 1, 1)

        self.checkBox_nodes = QCheckBox(self.page_forces)
        self.checkBox_nodes.setObjectName(u"checkBox_nodes")
        self.checkBox_nodes.setMinimumSize(QSize(80, 0))
        self.checkBox_nodes.setMaximumSize(QSize(100, 16777215))
        self.checkBox_nodes.setFont(font6)
        self.checkBox_nodes.setChecked(True)

        self.gridLayout_10.addWidget(self.checkBox_nodes, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.checkBox_members = QCheckBox(self.page_forces)
        self.checkBox_members.setObjectName(u"checkBox_members")
        self.checkBox_members.setMinimumSize(QSize(100, 0))
        self.checkBox_members.setMaximumSize(QSize(100, 16777215))
        self.checkBox_members.setFont(font6)
        self.checkBox_members.setChecked(True)

        self.gridLayout_10.addWidget(self.checkBox_members, 0, 4, 1, 1)

        self.line_8 = QFrame(self.page_forces)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_8, 1, 1, 1, 1)

        self.graphLayout_result = QVBoxLayout()
        self.graphLayout_result.setSpacing(0)
        self.graphLayout_result.setObjectName(u"graphLayout_result")
        self.graphLayout_result.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_10.addLayout(self.graphLayout_result, 2, 2, 3, 6)

        self.stackedWidget.addWidget(self.page_forces)
        self.page_influenceLine = QWidget()
        self.page_influenceLine.setObjectName(u"page_influenceLine")
        self.gridLayout_11 = QGridLayout(self.page_influenceLine)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_25 = QLabel(self.page_influenceLine)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 35))
        self.label_25.setFont(font3)

        self.gridLayout_11.addWidget(self.label_25, 0, 0, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_26 = QLabel(self.page_influenceLine)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(91, 20))
        self.label_26.setFont(font5)

        self.gridLayout_11.addWidget(self.label_26, 0, 2, 1, 1)

        self.comboBox_influence = QComboBox(self.page_influenceLine)
        self.comboBox_influence.setObjectName(u"comboBox_influence")
        self.comboBox_influence.setMaximumSize(QSize(73, 22))

        self.gridLayout_11.addWidget(self.comboBox_influence, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(273, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.line_10 = QFrame(self.page_influenceLine)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setMaximumSize(QSize(255, 21))
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_10, 2, 0, 1, 1)

        self.label_24 = QLabel(self.page_influenceLine)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)

        self.gridLayout_11.addWidget(self.label_24, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_27 = QLabel(self.page_influenceLine)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(69, 42))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(10)
        self.label_27.setFont(font7)

        self.horizontalLayout.addWidget(self.label_27)

        self.lineEdit_startingNode = QLineEdit(self.page_influenceLine)
        self.lineEdit_startingNode.setObjectName(u"lineEdit_startingNode")
        self.lineEdit_startingNode.setMaximumSize(QSize(50, 31))
        self.lineEdit_startingNode.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_startingNode)

        self.line = QFrame(self.page_influenceLine)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.label_28 = QLabel(self.page_influenceLine)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(69, 42))
        self.label_28.setFont(font7)

        self.horizontalLayout.addWidget(self.label_28)

        self.lineEdit_endingNode = QLineEdit(self.page_influenceLine)
        self.lineEdit_endingNode.setObjectName(u"lineEdit_endingNode")
        self.lineEdit_endingNode.setMaximumSize(QSize(50, 31))
        self.lineEdit_endingNode.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit_endingNode)


        self.gridLayout_11.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.pushButton_calculate = QPushButton(self.page_influenceLine)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setMinimumSize(QSize(35, 0))
        self.pushButton_calculate.setMaximumSize(QSize(121, 35))
        self.pushButton_calculate.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(255, 101, 111);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 1em;\n"
"    padding: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 38, 49);\n"
"    border-style: inset;\n"
"}")

        self.gridLayout_11.addWidget(self.pushButton_calculate, 5, 0, 1, 1)

        self.tableWidget_influenceLine = QTableWidget(self.page_influenceLine)
        if (self.tableWidget_influenceLine.columnCount() < 2):
            self.tableWidget_influenceLine.setColumnCount(2)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setBackground(QColor(253, 244, 152));
        self.tableWidget_influenceLine.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setBackground(QColor(123, 192, 67));
        self.tableWidget_influenceLine.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        if (self.tableWidget_influenceLine.rowCount() < 1):
            self.tableWidget_influenceLine.setRowCount(1)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_influenceLine.setVerticalHeaderItem(0, __qtablewidgetitem38)
        self.tableWidget_influenceLine.setObjectName(u"tableWidget_influenceLine")
        self.tableWidget_influenceLine.setMinimumSize(QSize(0, 0))
        self.tableWidget_influenceLine.setMaximumSize(QSize(271, 16777215))
        self.tableWidget_influenceLine.setAlternatingRowColors(True)
        self.tableWidget_influenceLine.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_influenceLine.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_influenceLine.verticalHeader().setVisible(False)

        self.gridLayout_11.addWidget(self.tableWidget_influenceLine, 6, 0, 1, 1)

        self.label_unitLoad = QLabel(self.page_influenceLine)
        self.label_unitLoad.setObjectName(u"label_unitLoad")
        self.label_unitLoad.setMinimumSize(QSize(255, 20))
        self.label_unitLoad.setMaximumSize(QSize(255, 40))
        self.label_unitLoad.setFont(font2)

        self.gridLayout_11.addWidget(self.label_unitLoad, 7, 0, 1, 1)

        self.graphLayout_influenceLine = QVBoxLayout()
        self.graphLayout_influenceLine.setSpacing(0)
        self.graphLayout_influenceLine.setObjectName(u"graphLayout_influenceLine")
        self.graphLayout_influenceLine.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_11.addLayout(self.graphLayout_influenceLine, 1, 1, 7, 4)

        self.stackedWidget.addWidget(self.page_influenceLine)
        self.page_report = QWidget()
        self.page_report.setObjectName(u"page_report")
        self.page_report.setMaximumSize(QSize(165464, 16777215))
        self.gridLayout_12 = QGridLayout(self.page_report)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_21 = QLabel(self.page_report)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 0))
        self.label_21.setMaximumSize(QSize(150, 31))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.label_21.setFont(font8)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_21)

        self.projectName = QPlainTextEdit(self.page_report)
        self.projectName.setObjectName(u"projectName")
        self.projectName.setMinimumSize(QSize(300, 0))
        self.projectName.setMaximumSize(QSize(630, 35))
        font9 = QFont()
        font9.setFamily(u"SansSerif")
        font9.setPointSize(10)
        self.projectName.setFont(font9)

        self.horizontalLayout_2.addWidget(self.projectName)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_22 = QLabel(self.page_report)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 0))
        self.label_22.setMaximumSize(QSize(150, 31))
        self.label_22.setFont(font8)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.userName = QPlainTextEdit(self.page_report)
        self.userName.setObjectName(u"userName")
        self.userName.setMinimumSize(QSize(100, 0))
        self.userName.setMaximumSize(QSize(630, 35))
        self.userName.setFont(font9)

        self.horizontalLayout_3.addWidget(self.userName)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.pushbutton_generate = QPushButton(self.page_report)
        self.pushbutton_generate.setObjectName(u"pushbutton_generate")
        self.pushbutton_generate.setMinimumSize(QSize(174, 0))
        self.pushbutton_generate.setMaximumSize(QSize(20, 40))
        self.pushbutton_generate.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(58, 192, 37);\n"
"	color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 165, 32);\n"
"    border-style: inset;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pushbutton_generate)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_12.addLayout(self.verticalLayout_2, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.label_19 = QLabel(self.page_report)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(850, 100))
        self.label_19.setMaximumSize(QSize(16777215, 100))
        self.label_19.setFont(font4)

        self.gridLayout_12.addWidget(self.label_19, 2, 0, 1, 2)

        self.label_20 = QLabel(self.page_report)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 35))
        self.label_20.setMaximumSize(QSize(16777215, 35))
        self.label_20.setFont(font3)

        self.gridLayout_12.addWidget(self.label_20, 0, 0, 1, 1)

        self.line_9 = QFrame(self.page_report)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_12.addWidget(self.line_9, 1, 0, 1, 2)

        self.widget = QWidget(self.page_report)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(320, 300))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setSizeIncrement(QSize(0, 0))
        self.widget.setStyleSheet(u"\n"
"border-image: url(:/newPrefix/Example/Screenshot 2020-11-19 021116.png)  0 0 0 0 stretch stretch;")

        self.gridLayout_12.addWidget(self.widget, 3, 1, 3, 1)

        self.stackedWidget.addWidget(self.page_report)

        self.gridLayout_7.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.retranslateUi(WizardPage)

        self.pushbutton_nodes.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WizardPage)
    # setupUi

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(QCoreApplication.translate("WizardPage", u"WizardPage", None))
        self.groupBox.setTitle("")
        self.pushbutton_displacement.setText(QCoreApplication.translate("WizardPage", u"\n"
" Displacements\n"
"", None))
        self.pushbutton_supports.setText(QCoreApplication.translate("WizardPage", u"\n"
" Supports\n"
"", None))
        self.pushbutton_properties.setText(QCoreApplication.translate("WizardPage", u"\n"
" Properties\n"
"", None))
        self.pushbutton_influenceLine.setText(QCoreApplication.translate("WizardPage", u"\n"
" Influence Line\n"
"", None))
        self.pushbutton_forces.setText(QCoreApplication.translate("WizardPage", u"\n"
" Forces\n"
"", None))
        self.pushbutton_nodes.setText(QCoreApplication.translate("WizardPage", u"\n"
" Nodes\n"
"", None))
        self.pushbutton_members.setText(QCoreApplication.translate("WizardPage", u"\n"
" Members\n"
"", None))
        self.pushbutton_report.setText(QCoreApplication.translate("WizardPage", u"\n"
" Report\n"
"", None))
        self.pushbutton_loads.setText(QCoreApplication.translate("WizardPage", u"\n"
" Loads\n"
"", None))
        self.label_8.setText(QCoreApplication.translate("WizardPage", u"Nodes : ", None))
        self.label_unit_node.setText(QCoreApplication.translate("WizardPage", u"* Unit of x and y : foot (ft)", None))
        ___qtablewidgetitem = self.tableWidget_nodes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WizardPage", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget_nodes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WizardPage", u"Y", None));
        ___qtablewidgetitem2 = self.tableWidget_nodes.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WizardPage", u"1", None));
        ___qtablewidgetitem3 = self.tableWidget_nodes.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WizardPage", u"2", None));
        self.update_nodes.setText(QCoreApplication.translate("WizardPage", u"Update", None))
        self.label_7.setText(QCoreApplication.translate("WizardPage", u"Truss Nodes", None))
        self.label_3.setText(QCoreApplication.translate("WizardPage", u"Truss Members", None))
        self.label_4.setText(QCoreApplication.translate("WizardPage", u"Members : ", None))
        self.update_members.setText(QCoreApplication.translate("WizardPage", u"Update", None))
        ___qtablewidgetitem4 = self.tableWidget_members.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WizardPage", u"From \n"
"Node", None));
        ___qtablewidgetitem5 = self.tableWidget_members.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WizardPage", u"To \n"
"Node", None));
        ___qtablewidgetitem6 = self.tableWidget_members.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WizardPage", u"1", None));

        __sortingEnabled = self.tableWidget_members.isSortingEnabled()
        self.tableWidget_members.setSortingEnabled(False)
        self.tableWidget_members.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("WizardPage", u"Truss Supports", None))
        self.label_6.setText(QCoreApplication.translate("WizardPage", u"Supports : ", None))
        self.update_supports.setText(QCoreApplication.translate("WizardPage", u"Update", None))
        ___qtablewidgetitem7 = self.tableWidget_supports.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WizardPage", u"Node", None));
        ___qtablewidgetitem8 = self.tableWidget_supports.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WizardPage", u"Type", None));
        ___qtablewidgetitem9 = self.tableWidget_supports.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WizardPage", u"1", None));
        ___qtablewidgetitem10 = self.tableWidget_supports.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WizardPage", u"2", None));

        __sortingEnabled1 = self.tableWidget_supports.isSortingEnabled()
        self.tableWidget_supports.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.tableWidget_supports.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WizardPage", u"1", None));
        ___qtablewidgetitem12 = self.tableWidget_supports.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WizardPage", u"2", None));
        self.tableWidget_supports.setSortingEnabled(__sortingEnabled1)

        self.label_9.setText(QCoreApplication.translate("WizardPage", u"Truss Loads", None))
        self.label_10.setText(QCoreApplication.translate("WizardPage", u"Loads : ", None))
        self.update_loads.setText(QCoreApplication.translate("WizardPage", u"Update", None))
        ___qtablewidgetitem13 = self.tableWidget_loads.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WizardPage", u"Node", None));
        ___qtablewidgetitem14 = self.tableWidget_loads.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WizardPage", u"Magnitude", None));
        ___qtablewidgetitem15 = self.tableWidget_loads.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WizardPage", u"Angle", None));
        ___qtablewidgetitem16 = self.tableWidget_loads.verticalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WizardPage", u"1", None));

        __sortingEnabled2 = self.tableWidget_loads.isSortingEnabled()
        self.tableWidget_loads.setSortingEnabled(False)
        self.tableWidget_loads.setSortingEnabled(__sortingEnabled2)

        self.label_unit_load.setText(QCoreApplication.translate("WizardPage", u"* Unit of load : kip (k)", None))
        self.label_12.setText(QCoreApplication.translate("WizardPage", u"Properties : ", None))
        self.label.setText(QCoreApplication.translate("WizardPage", u"* Unit of Area (A) : inch squared (in^2)", None))
        ___qtablewidgetitem17 = self.tableWidget_property.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WizardPage", u"Modulus of  \n"
"Elasticity \n"
"(E)", None));
        ___qtablewidgetitem18 = self.tableWidget_property.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WizardPage", u"Area \n"
"(A)", None));
        ___qtablewidgetitem19 = self.tableWidget_property.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WizardPage", u"1", None));

        __sortingEnabled3 = self.tableWidget_property.isSortingEnabled()
        self.tableWidget_property.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget_property.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WizardPage", u"29000", None));
        ___qtablewidgetitem21 = self.tableWidget_property.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WizardPage", u"1.00", None));
        self.tableWidget_property.setSortingEnabled(__sortingEnabled3)

        self.label_unit_property.setText(QCoreApplication.translate("WizardPage", u"* Unit of E : kip per inch squared (ksi)", None))
        self.update_property.setText(QCoreApplication.translate("WizardPage", u"Update", None))
        self.label_2.setText(QCoreApplication.translate("WizardPage", u"If the number of properties is greater than 1 \n"
"use members page to specify the properties \n"
"for each truss member. In case you don't \n"
"know the property leave it to the default one.", None))
        self.label_11.setText(QCoreApplication.translate("WizardPage", u"Truss Properties", None))
        self.label_23.setText(QCoreApplication.translate("WizardPage", u"Member colour : ", None))
        self.radioButtonDefault.setText(QCoreApplication.translate("WizardPage", u"Default", None))
        self.radioButtonBlack.setText(QCoreApplication.translate("WizardPage", u"Black", None))
        self.label_stabality.setText(QCoreApplication.translate("WizardPage", u"Unstable", None))
        self.label_14.setText(QCoreApplication.translate("WizardPage", u"Nodal Displacement", None))
        self.label_16.setText(QCoreApplication.translate("WizardPage", u"Animation : ", None))
        self.pushButton_start.setText(QCoreApplication.translate("WizardPage", u"Start", None))
        self.pushButton_stop.setText(QCoreApplication.translate("WizardPage", u"Stop", None))
        self.label_13.setText(QCoreApplication.translate("WizardPage", u"Magnifier : ", None))
        self.label_15.setText(QCoreApplication.translate("WizardPage", u"The horizontal (x) and vertical (y) displacements \n"
"are shown below.", None))
        ___qtablewidgetitem22 = self.tableWidget_displacement.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("WizardPage", u"Node\n"
"Number", None));
        ___qtablewidgetitem23 = self.tableWidget_displacement.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("WizardPage", u"X\n"
"Displacement", None));
        ___qtablewidgetitem24 = self.tableWidget_displacement.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("WizardPage", u"Y\n"
"Displacement", None));
        ___qtablewidgetitem25 = self.tableWidget_displacement.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("WizardPage", u"1", None));

        __sortingEnabled4 = self.tableWidget_displacement.isSortingEnabled()
        self.tableWidget_displacement.setSortingEnabled(False)
        self.tableWidget_displacement.setSortingEnabled(__sortingEnabled4)

        self.label_unit_displacement.setText(QCoreApplication.translate("WizardPage", u"* Unit of displacement : inch (in)", None))
        ___qtablewidgetitem26 = self.tableWidget_result.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("WizardPage", u"Member", None));
        ___qtablewidgetitem27 = self.tableWidget_result.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("WizardPage", u"Node", None));
        ___qtablewidgetitem28 = self.tableWidget_result.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("WizardPage", u"Force", None));
        ___qtablewidgetitem29 = self.tableWidget_result.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("WizardPage", u"Direction", None));
        ___qtablewidgetitem30 = self.tableWidget_result.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("WizardPage", u"1", None));

        __sortingEnabled5 = self.tableWidget_result.isSortingEnabled()
        self.tableWidget_result.setSortingEnabled(False)
        self.tableWidget_result.setSortingEnabled(__sortingEnabled5)

        self.label_unit_stress.setText(QCoreApplication.translate("WizardPage", u"* Unit of force: kip (k)", None))
        self.checkBox_loads.setText(QCoreApplication.translate("WizardPage", u"Loads", None))
        self.checkBox_reactions.setText(QCoreApplication.translate("WizardPage", u"Reactions", None))
        self.label_18.setText(QCoreApplication.translate("WizardPage", u"Member Forces and Support Reactions", None))
        self.label_17.setText(QCoreApplication.translate("WizardPage", u"Member tension(T) and compression(C) are shown \n"
"in the graph as well as support reactions. The \n"
"brightness of colors shows their relative strength.", None))
        self.checkBox_nodes.setText(QCoreApplication.translate("WizardPage", u"Nodes", None))
        self.checkBox_members.setText(QCoreApplication.translate("WizardPage", u"Members", None))
        self.label_25.setText(QCoreApplication.translate("WizardPage", u"Influence Line for a Unit Load", None))
        self.label_26.setText(QCoreApplication.translate("WizardPage", u"Member : ", None))
        self.label_24.setText(QCoreApplication.translate("WizardPage", u"Moving load only in a straight line is \n"
"currently supported.", None))
        self.label_27.setText(QCoreApplication.translate("WizardPage", u"Starting \n"
"Node", None))
        self.label_28.setText(QCoreApplication.translate("WizardPage", u"Ending \n"
"Node", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("WizardPage", u"Calculate", None))
        ___qtablewidgetitem31 = self.tableWidget_influenceLine.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("WizardPage", u"Position", None));
        ___qtablewidgetitem32 = self.tableWidget_influenceLine.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("WizardPage", u"Force", None));
        ___qtablewidgetitem33 = self.tableWidget_influenceLine.verticalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("WizardPage", u"1", None));
        self.label_unitLoad.setText(QCoreApplication.translate("WizardPage", u"* Unit Load: 1 kip (k)", None))
        self.label_21.setText(QCoreApplication.translate("WizardPage", u"Project Name : ", None))
        self.label_22.setText(QCoreApplication.translate("WizardPage", u"User Name : ", None))
        self.pushbutton_generate.setText(QCoreApplication.translate("WizardPage", u"\n"
"Generate\n"
"", None))
        self.label_19.setText(QCoreApplication.translate("WizardPage", u"A report can be generated containing input and output data as well as Stiffness Matrices which were used to solve this truss. \n"
"Enter project's name and user name to be displayed on the very first page of the report. Generated pdf will be placed in the\n"
"current project's directory. Make sure to  save your project before attempting to generate a report. Depending on the size of \n"
"the project it will take a minute or two to generate a report.", None))
        self.label_20.setText(QCoreApplication.translate("WizardPage", u"Report (PDF)", None))
    # retranslateUi

