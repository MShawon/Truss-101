"""
GPL-3.0 License

Copyright (C) 2020-2021 Monirul Shawon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from ui_truss import Ui_WizardPage
from reportlab.platypus import (PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from io import BytesIO
import datetime
import os
import pickle
import re
import tempfile

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import \
    NavigationToolbar2QT as NavigationToolbar
from numpy.linalg import norm
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from supports import *

plt.style.use('seaborn-bright')



class NumberedCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []


    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()


    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)


    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            self.setFillColor('steelblue')
            self.drawString(
                inch, 9.2*inch, """{+}##############################{+}############################## {+}""")
            self.drawString(
                inch, 9.4*inch, """{+}--------------------------------------------------{+}---------------------------------------------------{+}""")
            self.drawString(inch, 9*inch, "{+}")
            self.drawString(7*inch, 9*inch, "{+}")
            self.drawString(inch, 8.8*inch, "{+}")
            self.drawString(7*inch, 8.8*inch, "{+}")
            self.drawString(inch, 8.6*inch, "{+}")
            self.drawString(7*inch, 8.6*inch, "{+}")
            self.drawString(inch, 8.4*inch, "{+}")
            self.drawString(7*inch, 8.4*inch, "{+}")
            self.drawString(inch, 8.2*inch, "{+}")
            self.drawString(7*inch, 8.2*inch, "{+}")
            self.drawString(inch, 8*inch, "{+}")
            self.drawString(7*inch, 8*inch, "{+}")
            self.drawString(inch, 7.8*inch, "{+}")
            self.drawString(7*inch, 7.8*inch, "{+}")
            self.drawString(
                inch, 7.6*inch, """{+}##############################{+}############################## {+}""")
            self.drawString(
                inch, 7.4*inch, """{+}--------------------------------------------------{+}---------------------------------------------------{+}""")
            self.setFillColor('black')
            self.setAuthor("Monirul Shawon")
            self.setTitle("Report")
            self.setSubject("Details report for Truss 101")
            self.setCreator("Truss 101")
        elif self._pageNumber == 2:
            im = ImageReader(buf_node)
            self.drawImage(im, inch*2.8, inch*4, width=5.1*inch, height=4*inch)
        elif self._pageNumber == member_page:
            im = ImageReader(buf_element)
            self.drawImage(im, inch*3.0, inch*6,
                           width=4.8*inch, height=3.7*inch)
        elif self._pageNumber == support_page:
            im = ImageReader(buf_support)
            self.drawImage(im, inch*3.4, inch*6.2,
                           width=4.5*inch, height=3.5*inch)

            # support
            data = [('Support', 'Node', 'Type')]
            for i, k in enumerate(support_report.keys()):
                node = re.findall(r'\d+', k)
                data.append((i+1, node[0], k.replace(node[0], '')))
            t = Table(data, hAlign='RIGHT', repeatRows=1)
            t.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('LINEBELOW', (0, 0), (2, 0), 2, colors.black),
            ]))
            t.wrapOn(self, 400, 100)
            t.drawOn(self, inch*4.5, inch*5)

        elif self._pageNumber == page_count - stress_page:
            im = ImageReader(buf_bar_force)
            self.drawImage(im, inch*0.1, inch*3.5, width=8*inch, height=6*inch)
            im = ImageReader(buf_reaction)
            self.drawImage(im, inch*1, inch*0.1, width=6*inch, height=4*inch)

        elif self._pageNumber == page_count - displacement_page:
            im = ImageReader(buf_displacement)
            self.drawImage(im, inch*3.8, inch*6,
                           width=4.5*inch, height=3.5*inch)
        self.setFont("Helvetica", 7)
        self.drawRightString(inch, 0.75 * inch,
                             "Page %d of %d" % (self._pageNumber, page_count))



class NavigationToolbar(NavigationToolbar):
    '''
    This is used to set customized navigation toolbar in graphs
    '''
    # toolitems = [t for t in NavigationToolbar.toolitems if
    #              t[0] in ('Home', 'Back', 'Forward', 'Pan', 'Zoom', 'Save')]

    NavigationToolbar.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        (None, None, None, None),
        ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
        ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
        ('Tight layout', 'Use tight layout if everything doesn\'t fit in graph',
         'subplots', 'configure_subplots'),
        (None, None, None, None),
        ('Save', 'Save the figure', 'filesave', 'save_figure'),
    )



class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter



class MainPage(QWizardPage):
    def __init__(self, open=None, filename=None, demo=None, logger=None):
        super(MainPage, self).__init__()
        self.ui = Ui_WizardPage()
        self.ui.setupUi(self)
        self.open = open
        self.filename = filename
        self.demo = demo
        self.logger = logger
        self.save = 0
        self.change = 0
        self.savedemo = None

        if self.demo:
            self.savedemo = True
            if '/' in self.filename[0]:
                self.name = self.filename[0].split("/")[-1]
            else:
                self.name = self.filename[0].split("\\")[-1]

        'Unit conversion'
        self.current_metric_index = []
        self.current_imperial_index = [[0, 0, 0]]

        self.unit_node = 1
        self.displacement_unit = 12
        self.reverse_unit = 1
        self.displacement_factor = 0.1
        self.force_unit = 1
        self.bar_force_unit = 1
        self.stress_unit = 1000
        self.force_unit_name = 'k'
        self.unit_report = [
            'ft', 'kip (k)', 'kip (k)', 'ksi', 'in<super size=6>2</super>', 'in']

        'Modified close event to close all matplotlib graph'
        self.ui.closeEvent = self.closeEvent

        'Graph widget 1'
        self.graph_widget = QWidget()
        self.graph_widget.figure1 = plt.figure()
        self.graph_widget.canvas1 = FigureCanvas(self.graph_widget.figure1)
        self.graph_widget.toolbar1 = NavigationToolbar(
            self.graph_widget.canvas1, self.graph_widget)
        self.ui.graphLayout_geometry.addWidget(self.graph_widget.toolbar1)
        self.ui.graphLayout_geometry.addWidget(self.graph_widget.canvas1)
        ax = self.graph_widget.figure1.add_subplot(111)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.grid(True)

        'Graph widget 2'
        self.graph_widget2 = QWidget()
        self.graph_widget2.figure2 = plt.figure()
        self.graph_widget2.canvas2 = FigureCanvas(self.graph_widget2.figure2)
        self.graph_widget2.toolbar2 = NavigationToolbar(
            self.graph_widget2.canvas2, self.graph_widget2)
        self.ui.graphLayout_displacement.addWidget(self.graph_widget2.toolbar2)
        self.ui.graphLayout_displacement.addWidget(self.graph_widget2.canvas2)
        ax2 = self.graph_widget2.figure2.add_subplot(111)
        ax2.axis('off')

        'Graph widget 3'
        self.graph_widget3 = QWidget()
        self.graph_widget3.figure3 = plt.figure()
        self.graph_widget3.canvas3 = FigureCanvas(self.graph_widget3.figure3)
        self.graph_widget3.toolbar3 = NavigationToolbar(
            self.graph_widget3.canvas3, self.graph_widget3)
        self.ui.graphLayout_result.addWidget(self.graph_widget3.toolbar3)
        self.ui.graphLayout_result.addWidget(self.graph_widget3.canvas3)
        ax3 = self.graph_widget3.figure3.add_subplot(111)
        ax3.axis('off')

        'Graph widget 4'
        self.graph_widget4 = QWidget()
        self.graph_widget4.figure4 = plt.figure()
        self.graph_widget4.canvas4 = FigureCanvas(self.graph_widget4.figure4)
        self.graph_widget4.toolbar4 = NavigationToolbar(
            self.graph_widget4.canvas4, self.graph_widget4)
        self.ui.graphLayout_influenceLine.addWidget(
            self.graph_widget4.toolbar4)
        self.ui.graphLayout_influenceLine.addWidget(self.graph_widget4.canvas4)
        ax4 = self.graph_widget4.figure4.add_subplot(211)
        self.ax5 = self.graph_widget4.figure4.add_subplot(212)

        '''
        page changing by clicking pushButton and connecting them to stackedWidget
        '''
        self.ui.pushbutton_nodes.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_geometry))
        self.ui.pushbutton_nodes.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_node))

        self.ui.pushbutton_members.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_geometry))
        self.ui.pushbutton_members.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_member))

        self.ui.pushbutton_supports.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_geometry))
        self.ui.pushbutton_supports.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_supports))

        self.ui.pushbutton_loads.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_geometry))
        self.ui.pushbutton_loads.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_loads))

        self.ui.pushbutton_properties.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_geometry))
        self.ui.pushbutton_properties.clicked.connect(
            lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_properties))

        self.ui.pushbutton_displacement.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_displacement))

        self.ui.pushbutton_forces.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_forces))

        'This is special for influence line development'
        self.ui.pushbutton_influenceLine.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_influenceLine))

        self.ui.pushbutton_report.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_report))

        self.ui.lineEdit_startingNode.textChanged[str].connect(self.movingload)
        self.ui.lineEdit_endingNode.textChanged[str].connect(self.movingload)

        '''
        connecting desired functions by clicking pushButtons
        '''
        self.ui.pushbutton_nodes.clicked.connect(self.node)
        self.ui.pushbutton_members.clicked.connect(self.member)
        self.ui.pushbutton_supports.clicked.connect(self.support)
        self.ui.pushbutton_loads.clicked.connect(self.force)
        self.ui.pushbutton_properties.clicked.connect(self.assign_property)

        self.ui.pushbutton_displacement.clicked.connect(self.node)
        self.ui.pushbutton_displacement.clicked.connect(self.displacement)

        self.ui.pushbutton_forces.clicked.connect(self.node)
        self.ui.pushbutton_forces.clicked.connect(self.displacement)

        self.ui.pushbutton_influenceLine.clicked.connect(self.influence_table)
        self.ui.pushButton_calculate.clicked.connect(self.influence_line)

        'Supports combo add in support table'
        for i in range(2):
            supports_cb = QComboBox()
            supports_cb.addItems(
                ['pinned', 'horizontal roller', 'vertical roller'])
            self.ui.tableWidget_supports.setCellWidget(i, 1, supports_cb)
            supports_cb.currentIndexChanged.connect(self.support)

        if self.open:
            self.open_from_file()

        '''table update'''
        self.ui.update_loads.clicked.connect(
            lambda: self.ui.tableWidget_loads.setRowCount(self.ui.spinBox_loads.value()))

        self.ui.update_members.clicked.connect(self.member_table)

        self.ui.update_supports.clicked.connect(self.support_table)

        self.ui.update_property.clicked.connect(self.property_table)

        self.ui.update_nodes.clicked.connect(self.node)
        self.ui.tableWidget_nodes.cellChanged.connect(self.node)
        self.ui.tableWidget_nodes.cellChanged.connect(self.update_change)

        self.ui.update_members.clicked.connect(self.member)
        self.ui.tableWidget_members.cellChanged.connect(self.member)
        self.ui.tableWidget_members.cellChanged.connect(self.update_change)

        self.ui.update_supports.clicked.connect(self.support)
        self.ui.tableWidget_supports.cellChanged.connect(self.support)
        self.ui.tableWidget_supports.cellChanged.connect(
            self.update_change)

        self.ui.update_loads.clicked.connect(self.force)
        self.ui.tableWidget_loads.cellChanged.connect(self.force)
        self.ui.tableWidget_loads.cellChanged.connect(self.update_change)

        self.ui.update_property.clicked.connect(self.assign_property)
        self.ui.tableWidget_property.cellChanged.connect(self.assign_property)
        self.ui.pushbutton_properties.clicked.connect(self.assign_property)
        self.ui.tableWidget_property.cellChanged.connect(
            self.update_change)

        'Member colour change in graph'
        self.ui.radioButtonDefault.toggled.connect(self.graph)
        self.ui.radioButtonBlack.toggled.connect(self.graph)

        'Animation'
        self.ui.pushButton_start.clicked.connect(self.animation)
        self.ui.pushButton_stop.clicked.connect(self.stop_animation)
        self.ui.horizontalSlider.valueChanged.connect(self.displacement_graph)

        'Force, stress radio button'
        self.ui.radioButton_force.toggled.connect(self.force_or_stress)

        'Nodes,loads,reactions and members checkbox in stress graph'
        self.ui.checkBox_nodes.stateChanged.connect(self.stress_graph)
        self.ui.checkBox_members.stateChanged.connect(self.stress_graph)
        self.ui.checkBox_forces.stateChanged.connect(self.stress_graph)
        self.ui.checkBox_loads.stateChanged.connect(self.stress_graph)
        self.ui.checkBox_reactions.stateChanged.connect(self.stress_graph)

        'Report generate'
        self.ui.pushbutton_generate.clicked.connect(self.generate_report)
        self.ui.projectName.setPlaceholderText('Project Truss')
        self.ui.userName.setPlaceholderText('Anonymous')

        'Table no edit triggers and setColumnWidth'
        self.ui.tableWidget_loads.setColumnWidth(1, 100)

        self.ui.tableWidget_displacement.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        self.ui.tableWidget_result.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_result.setColumnWidth(0, 60)
        self.ui.tableWidget_result.setColumnWidth(1, 60)
        self.ui.tableWidget_result.setColumnWidth(2, 100)

        self.ui.tableWidget_influenceLine.setEditTriggers(
            QAbstractItemView.NoEditTriggers)

        'To allow only int in influence line starting and ending node'
        self.onlyInt = QIntValidator()
        self.ui.lineEdit_startingNode.setValidator(self.onlyInt)
        self.ui.lineEdit_endingNode.setValidator(self.onlyInt)

        '''
        Align Delegate
        Set table item alignment in center
        '''
        delegate = AlignDelegate(self.ui.tableWidget_nodes)
        self.ui.tableWidget_nodes.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_members)
        self.ui.tableWidget_members.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_supports)
        self.ui.tableWidget_supports.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_loads)
        self.ui.tableWidget_loads.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_property)
        self.ui.tableWidget_property.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_displacement)
        self.ui.tableWidget_displacement.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_result)
        self.ui.tableWidget_result.setItemDelegate(delegate)
        delegate = AlignDelegate(self.ui.tableWidget_influenceLine)
        self.ui.tableWidget_influenceLine.setItemDelegate(delegate)

        self.ui.comboBox_influence.currentIndexChanged.connect(
            self.influence_table)

    '''
    opening from a file
    '''

    def open_from_file(self):
        currentdirectory = os.path.expanduser('~/Documents')
        if not self.filename:
            self.filename = QFileDialog.getOpenFileName(
                self, 'Open file', currentdirectory, "Truss101 files (*.trs)")
        with open(self.filename[0], 'rb') as outfile:
            try:
                self.current_metric_index = pickle.load(outfile)
                self.current_imperial_index = pickle.load(outfile)
                self.ndofs = pickle.load(outfile)
                self.X = pickle.load(outfile)
                self.Y = pickle.load(outfile)
                self.X_withoutunit = pickle.load(outfile)
                self.Y_withoutunit = pickle.load(outfile)
                self.node_values = pickle.load(outfile)
                self.degrees_of_freedom = pickle.load(outfile)
                self.member_values = pickle.load(outfile)
                self.elements = pickle.load(outfile)
                self.plot_final = pickle.load(outfile)
                self.plot_displacement_final = pickle.load(outfile)
                self.restrained_dofs = pickle.load(outfile)
                self.support_node = pickle.load(outfile)
                self.support_graph = pickle.load(outfile)
                self.support_displacement_graph = pickle.load(outfile)
                self.support_force = pickle.load(outfile)
                self.forces = pickle.load(outfile)
                self.force_graph = pickle.load(outfile)
                self.properties = pickle.load(outfile)
                self.properties_list = pickle.load(outfile)

                self.max_X = max(self.X)
                self.max_Y = max(self.Y)
                self.min_X = min(self.X)
                self.min_Y = min(self.Y)
                self.max_XY = max(self.max_X, self.max_Y)
                self.min_XY = min(self.max_X, self.max_Y)

            except:
                self.max_X = max(self.X)
                self.max_Y = max(self.Y)
                self.min_X = min(self.X)
                self.min_Y = min(self.Y)
                self.max_XY = max(self.max_X, self.max_Y)
                self.min_XY = min(self.max_X, self.max_Y)

                self.graph()
                pass

            # node
        try:
            self.ui.tableWidget_nodes.setRowCount(len(self.X_withoutunit))
            self.ui.spinBox_nodes.setValue(len(self.X_withoutunit))

            for i, (j, k) in enumerate(zip(self.X_withoutunit, self.Y_withoutunit)):
                self.ui.tableWidget_nodes.setItem(
                    i, 0, QTableWidgetItem(str(j)))
                self.ui.tableWidget_nodes.setItem(
                    i, 1, QTableWidgetItem(str(k)))
            # member
            self.ui.tableWidget_members.setRowCount(len(self.elements))
            self.ui.spinBox_members.setValue(len(self.elements))
            if len(self.properties_list) > 1:
                self.ui.spinBox_property.setValue(len(self.properties_list))
                self.ui.tableWidget_members.setColumnCount(3)
                self.ui.tableWidget_members.setHorizontalHeaderLabels(
                    ['From\nNode', 'To\nNode', 'property'])
                self.ui.tableWidget_members.setColumnWidth(0, 80)
                self.ui.tableWidget_members.setColumnWidth(1, 80)
                for k, v in self.elements.items():
                    property_cb = QComboBox()
                    item = [str(i) for i in range(
                        1, self.ui.spinBox_property.value()+1)]
                    property_cb.addItems(item)
                    property_cb.setCurrentText(str(self.properties[k][1]))
                    self.ui.tableWidget_members.setCellWidget(
                        k-1, 2, property_cb)
                    self.ui.tableWidget_members.setItem(
                        k-1, 0, QTableWidgetItem(str(v[0])))
                    self.ui.tableWidget_members.setItem(
                        k-1, 1, QTableWidgetItem(str(v[1])))
            else:
                for k, v in self.elements.items():
                    self.ui.tableWidget_members.setItem(
                        k-1, 0, QTableWidgetItem(str(v[0])))
                    self.ui.tableWidget_members.setItem(
                        k-1, 1, QTableWidgetItem(str(v[1])))

            # supports
            self.ui.tableWidget_supports.setRowCount(len(self.support_node))
            self.ui.spinBox_supports.setValue(len(self.support_node))
            for i, j in enumerate(self.support_graph.keys()):
                supports_cb = QComboBox()
                supports_cb.addItems(
                    ['pinned', 'horizontal roller', 'vertical roller'])
                node = re.findall(r'\d+', j)
                string = j.replace(node[0], '')
                supports_cb.setCurrentText(string)
                self.ui.tableWidget_supports.setItem(
                    i, 0, QTableWidgetItem(node[0]))
                self.ui.tableWidget_supports.setCellWidget(i, 1, supports_cb)
                supports_cb.currentIndexChanged.connect(self.support)

            # loads
            self.ui.tableWidget_loads.setRowCount(len(self.force_graph))
            self.ui.spinBox_loads.setValue(len(self.force_graph))
            for k, v in self.force_graph.items():
                self.ui.tableWidget_loads.setItem(
                    k, 0, QTableWidgetItem(str(v[-2])))
                self.ui.tableWidget_loads.setItem(
                    k, 1, QTableWidgetItem(str(v[3])))
                self.ui.tableWidget_loads.setItem(
                    k, 2, QTableWidgetItem(str(v[2])))
            # property
            self.ui.tableWidget_property.setRowCount(len(self.properties_list))
            self.ui.spinBox_property.setValue(len(self.properties_list))
            for k, v in self.properties_list.items():
                self.ui.tableWidget_property.setItem(
                    k-1, 0, QTableWidgetItem(str(v[0])))
                self.ui.tableWidget_property.setItem(
                    k-1, 1, QTableWidgetItem(str(v[1])))

        except:
            pass
        if self.current_imperial_index:
            self.change_unit_label(
                unit=self.current_imperial_index, type='imperial')
            self.unit_convert(type='imperial')
        elif self.current_metric_index:
            self.change_unit_label(unit=self.current_metric_index, type='metric')
            self.unit_convert(type='metric')
        self.change = 0
        self.save += 1

    '''
    save into a file
    '''

    def save_to_file(self, saveas=None):
        self.saveas = saveas
        currentdirectory = os.path.expanduser('~/Documents')

        if self.save == 0:
            self.filename = QFileDialog.getSaveFileName(
                self, 'Save file', currentdirectory, "Truss101 files (*.trs)")
        elif self.saveas:
            self.filename = QFileDialog.getSaveFileName(
                self, 'Save file', currentdirectory, "Truss101 files (*.trs)")
        elif self.savedemo:
            self.filename = QFileDialog.getSaveFileName(
                self, 'Save file', currentdirectory, "Truss101 files (*.trs)")

        with open(self.filename[0], 'wb') as outfile:
            self.change = 0
            self.save += 1
            try:
                pickle.dump(self.current_metric_index, outfile)
                pickle.dump(self.current_imperial_index, outfile)
                pickle.dump(self.ndofs, outfile)
                pickle.dump(self.X, outfile)
                pickle.dump(self.Y, outfile)
                pickle.dump(self.X_withoutunit, outfile)
                pickle.dump(self.Y_withoutunit, outfile)
                pickle.dump(self.node_values, outfile)
                pickle.dump(self.degrees_of_freedom, outfile)
                pickle.dump(self.member_values, outfile)
                pickle.dump(self.elements, outfile)
                pickle.dump(self.plot_final, outfile)
                pickle.dump(self.plot_displacement_final, outfile)
                pickle.dump(self.restrained_dofs, outfile)
                pickle.dump(self.support_node, outfile)
                pickle.dump(self.support_graph, outfile)
                pickle.dump(self.support_displacement_graph, outfile)
                pickle.dump(self.support_force, outfile)
                pickle.dump(self.forces, outfile)
                pickle.dump(self.force_graph, outfile)
                pickle.dump(self.properties, outfile)
                pickle.dump(self.properties_list, outfile)
            except:
                pass

    '''
    add comboBox in table
    '''

    def member_table(self):
        previous = self.ui.tableWidget_members.rowCount()
        self.ui.tableWidget_members.setRowCount(
            self.ui.spinBox_members.value())

        if self.ui.spinBox_property.value() > 1:
            self.ui.tableWidget_members.setColumnCount(3)
            self.ui.tableWidget_members.setHorizontalHeaderLabels(
                ['From\nNode', 'To\nNode', 'property'])

            total = self.ui.spinBox_property.value()+1
            for row in range(self.ui.spinBox_members.value()-previous):
                property_cb = QComboBox()
                item = [str(i) for i in range(1, total)]
                property_cb.addItems(item)
                self.ui.tableWidget_members.setCellWidget(
                    row+previous, 2, property_cb)
                property_cb.currentIndexChanged.connect(self.assign_property)

            self.ui.tableWidget_members.setColumnWidth(0, 80)
            self.ui.tableWidget_members.setColumnWidth(1, 80)


    def support_table(self):
        previous = self.ui.tableWidget_supports.rowCount()
        self.ui.tableWidget_supports.setRowCount(
            self.ui.spinBox_supports.value())
        for row in range(self.ui.spinBox_supports.value()-previous):
            supports_cb = QComboBox()
            supports_cb.addItems(
                ['pinned', 'horizontal roller', 'vertical roller'])
            self.ui.tableWidget_supports.setItem(
                row+previous, 0, QTableWidgetItem('1'))
            self.ui.tableWidget_supports.setCellWidget(
                row+previous, 1, supports_cb)
            supports_cb.currentIndexChanged.connect(self.support)


    def property_table(self):

        self.ui.tableWidget_property.setRowCount(
            self.ui.spinBox_property.value())
        if self.ui.spinBox_property.value() > 1:
            self.ui.tableWidget_members.setColumnCount(3)
            self.ui.tableWidget_members.setHorizontalHeaderLabels(
                ['From\nNode', 'To\nNode', 'property'])
            self.ui.tableWidget_members.setColumnWidth(0, 80)
            self.ui.tableWidget_members.setColumnWidth(1, 80)

            for row in range(self.ui.spinBox_members.value()):
                property_cb = QComboBox()
                item = [str(i) for i in range(
                    1, self.ui.spinBox_property.value()+1)]
                property_cb.addItems(item)

                self.ui.tableWidget_members.setCellWidget(row, 2, property_cb)
                property_cb.currentIndexChanged.connect(self.assign_property)

        elif self.ui.spinBox_property.value() == 1:
            self.ui.tableWidget_members.setColumnCount(2)
            self.ui.tableWidget_members.setHorizontalHeaderLabels(
                ['From\nNode', 'To\nNode'])
            self.ui.tableWidget_members.setColumnWidth(0, 150)
            self.ui.tableWidget_members.setColumnWidth(1, 150)

    '''
    constructing lists and dictionary to collect data from tables and then calculating.
    '''

    def node(self):
        self.ui.tableWidget_nodes.setRowCount(self.ui.spinBox_nodes.value())
        self.X = []
        self.Y = []
        self.X_withoutunit = []
        self.Y_withoutunit = []
        self.node_values = {}
        self.degrees_of_freedom = {}
        for row in range(1, self.ui.spinBox_nodes.value()+1):
            try:
                x = float(self.ui.tableWidget_nodes.item(row-1, 0).text())
                y = float(self.ui.tableWidget_nodes.item(row-1, 1).text())
                self.X.append(x*self.unit_node)
                self.Y.append(y*self.unit_node)
                self.X_withoutunit.append(x)
                self.Y_withoutunit.append(y)
                self.node_values[row] = x*self.unit_node, y*self.unit_node
                self.degrees_of_freedom[row] = 2*row-1, 2*row
            except:
                continue
        self.ndofs = 2*len(self.node_values)
        self.logger.debug('Number of degrees of freedom : %s', self.ndofs)
        self.logger.debug('Degrees of freedom : %s', self.degrees_of_freedom)
        self.logger.debug('Node values : %s', self.node_values)

        try:
            self.max_X = max(self.X)
            self.max_Y = max(self.Y)
            self.min_X = min(self.X)
            self.min_Y = min(self.Y)
            self.max_XY = max(self.max_X, self.max_Y)
            self.min_XY = min(self.max_X, self.max_Y)

        except:
            pass

        self.member()


    def member(self):
        self.ui.tableWidget_members.setRowCount(
            self.ui.spinBox_members.value())
        self.member_values = {}
        self.elements = {}
        From_node = []
        To_node = []

        plot_x1 = []
        plot_x2 = []
        plot_y1 = []
        plot_y2 = []
        self.plot_final = {}
        self.plot_displacement_final = {}
        for row in range(self.ui.spinBox_members.value()):
            try:
                node1 = int(self.ui.tableWidget_members.item(row, 0).text())
                node2 = int(self.ui.tableWidget_members.item(row, 1).text())

                for k, v in self.node_values.items():
                    if node1 == k:
                        From_node = v
                        plot_x1 = v[0]
                        plot_y1 = v[1]
                    elif node2 == k:
                        To_node = v
                        plot_x2 = v[0]
                        plot_y2 = v[1]
                    self.plot_final[row+1] = (plot_x1,
                                              plot_x2), (plot_y1, plot_y2)
                    self.plot_displacement_final[row+1] = (plot_x1*self.reverse_unit, plot_x2 *
                                                           self.reverse_unit), (plot_y1*self.reverse_unit, plot_y2*self.reverse_unit)
                    self.member_values[row+1] = From_node, To_node
                self.elements[row+1] = node1, node2
            except:
                continue

        self.logger.debug('Member values : %s', self.member_values)
        self.logger.debug('Elements : %s', self.elements)
        self.logger.debug('Member plot data : %s', self.plot_final)
        self.logger.debug('Member displacement data : %s',
                          self.plot_displacement_final)

        self.support()


    def support(self):
        self.ui.tableWidget_supports.setRowCount(
            self.ui.spinBox_supports.value())
        self.restrained_dofs = []
        self.support_node = []
        self.support_graph = {}
        self.support_displacement_graph = {}
        self.support_force = {}
        global support_report
        for row in range(self.ui.spinBox_supports.value()):
            try:
                node = int(self.ui.tableWidget_supports.item(row, 0).text())
                support_type = self.ui.tableWidget_supports.cellWidget(
                    row, 1).currentIndex()

                self.support_node.append(node)
                p = self.node_values[node][0]
                q = self.node_values[node][1]
                # Pinned Support
                if support_type == 0:
                    self.restrained_dofs.append(2*node-1)
                    self.restrained_dofs.append(2*node)
                    self.support_force[2*node-1] = 0
                    self.support_force[2*node] = 0
                    if q > 0:
                        if p == 0:
                            self.support_graph[f'pinned{node}'] = [p, q], 270
                            self.support_displacement_graph[f'pinned{node}'] = [
                                p*self.reverse_unit, q*self.reverse_unit], 270
                        elif p == self.max_X:
                            self.support_graph[f'pinned{node}'] = [p, q], 90
                            self.support_displacement_graph[f'pinned{node}'] = [
                                p*self.reverse_unit, q*self.reverse_unit], 90
                        elif q == self.max_Y:
                            self.support_graph[f'pinned{node}'] = [p, q], 180
                            self.support_displacement_graph[f'pinned{node}'] = [
                                p*self.reverse_unit, q*self.reverse_unit], 180
                        else:
                            self.support_graph[f'pinned{node}'] = [p, q], 0
                            self.support_displacement_graph[f'pinned{node}'] = [
                                p*self.reverse_unit, q*self.reverse_unit], 0
                    else:
                        self.support_graph[f'pinned{node}'] = [p, q], 0
                        self.support_displacement_graph[f'pinned{node}'] = [
                            p*self.reverse_unit, q*self.reverse_unit], 0
                # Horizontal ROller Support
                elif support_type == 1:
                    self.restrained_dofs.append(2*node)
                    self.support_force[2*node] = 0
                    # Bottom
                    if q == self.max_Y:
                        self.support_graph[f'horizontal roller{node}'] = [
                            p, q], 180
                        self.support_displacement_graph[f'horizontal roller{node}'] = [
                            p*self.reverse_unit, q*self.reverse_unit], 180
                    # Top
                    else:
                        self.support_graph[f'horizontal roller{node}'] = [
                            p, q], 0
                        self.support_displacement_graph[f'horizontal roller{node}'] = [
                            p*self.reverse_unit, q*self.reverse_unit], 0
                # Vertical Roller support
                elif support_type == 2:
                    self.restrained_dofs.append(2*node-1)
                    self.support_force[2*node-1] = 0
                    # Left
                    if p < self.max_X/2:
                        self.support_graph[f'vertical roller{node}'] = [
                            p, q], 270
                        self.support_displacement_graph[f'vertical roller{node}'] = [
                            p*self.reverse_unit, q*self.reverse_unit], 270
                    # Right
                    else:
                        self.support_graph[f'vertical roller{node}'] = [
                            p, q], 90
                        self.support_displacement_graph[f'vertical roller{node}'] = [
                            p*self.reverse_unit, q*self.reverse_unit], 90
            except:
                continue

        self.restrained_dofs.sort()
        self.logger.debug('Restrained dofs sorted: %s', self.restrained_dofs)
        self.logger.debug('Support Node : %s', self.support_node)
        self.logger.debug('Support graph : %s', self.support_graph)
        self.logger.debug('Support displacement graph : %s',
                          self.support_displacement_graph)
        self.logger.debug('Support force : %s', self.support_force)

        support_report = self.support_graph
        self.force()


    def force(self):
        self.forces = {}
        self.force_graph = {}
        for i in range(1, self.ui.spinBox_nodes.value()+1):
            self.forces[i] = 0, 0

        for row in range(self.ui.spinBox_loads.value()):
            try:
                node = int(self.ui.tableWidget_loads.item(row, 0).text())
                magnitude = float(
                    self.ui.tableWidget_loads.item(row, 1).text())
                angle = float(self.ui.tableWidget_loads.item(row, 2).text())

                force_x = np.around((np.cos(np.radians(
                    angle)))*magnitude*self.force_unit, decimals=10) + self.forces[node][0]
                force_y = np.around((np.sin(np.radians(
                    angle)))*magnitude*self.force_unit, decimals=10) + self.forces[node][1]
                self.forces[node] = force_x, force_y

                if node in self.support_node:
                    self.support_force[node*2-1] = force_x
                    self.support_force[node*2] = force_y

                p = self.node_values[node][0]
                q = self.node_values[node][1]
                positive_angle = angle % 360
                if positive_angle >= 0 and positive_angle < 60:
                    self.force_graph[row] = p, q, angle, magnitude, node, f'right'
                elif positive_angle >= 60 and positive_angle < 120:
                    self.force_graph[row] = p, q, angle, magnitude, node, f'center'
                elif positive_angle >= 120 and positive_angle < 240:
                    self.force_graph[row] = p, q, angle, magnitude, node, f'left'
                elif positive_angle >= 240 and positive_angle < 300:
                    self.force_graph[row] = p, q, angle, magnitude, node, f'center'
                else:
                    self.force_graph[row] = p, q, angle, magnitude, node, f'right'
            except:
                continue

        self.logger.debug('Forces : %s', self.forces)
        self.logger.debug('Force graph : %s', self.force_graph)

        self.assign_property()


    def assign_property(self):
        self.properties_list = {}
        self.properties = {}
        properties_number = int(self.ui.spinBox_property.value())
        member = int(self.ui.spinBox_members.value())
        if properties_number == 1:
            stiffness = float(self.ui.tableWidget_property.item(0, 0).text())
            area = float(self.ui.tableWidget_property.item(0, 1).text())
            self.properties_list[1] = stiffness, area
            for i in range(1, member+1):
                self.properties[i] = (stiffness, area), 1
        else:
            for i in range(1, properties_number+1):
                try:
                    stiffness = float(
                        self.ui.tableWidget_property.item(i-1, 0).text())
                    area = float(
                        self.ui.tableWidget_property.item(i-1, 1).text())
                    self.properties_list[i] = stiffness, area
                except:
                    continue

            for row in range(member):
                try:
                    number = int(self.ui.tableWidget_members.cellWidget(
                        row, 2).currentText())
                    self.properties[row +
                                    1] = self.properties_list[number], number
                except:
                    continue

        self.logger.debug('Unique properties : %s', self.properties_list)
        self.logger.debug('Member assigned properties : %s', self.properties)

        self.calculation()
        self.graph()


    def change_unit_label(self, unit=None, type=None):
        self.unit = unit
        self.type = type
        self.current_metric_index = []
        self.current_imperial_index = []
        if self.type == 'metric':
            self.current_metric_index = self.unit
            self.unit_report = [
                'm', 'kilo newton (kN)', 'kilo newton (kN)', 'GPa', 'mm<super size=6>2</super>', 'mm']

            self.ui.label_unit_property.setText(
                '* Unit of E : Giga Pascal (GPa)')
            self.ui.label.setText(
                '* Unit of Area (A) : milimeter squared (mm^2)')
            self.ui.label_unit_displacement.setText(
                '* Unit of displacement : milimeter (mm)')

            if self.current_metric_index[0][0] == 0:
                self.ui.label_unit_node.setText(
                    '* Unit of x and y : meter (m)')
            if self.current_metric_index[0][0] == 1:
                self.unit_report[0] = 'mm'
                self.ui.label_unit_node.setText(
                    '* Unit of x and y : milimeter (mm)')
            if self.current_metric_index[0][1] == 0:
                self.ui.label_unit_load.setText(
                    '* Unit of load : kilo Newton (kN)')
                self.ui.label_unitLoad.setText(
                    '* Unit Load : 1 kilo Newton (kN)')
            if self.current_metric_index[0][1] == 1:
                self.unit_report[1] = 'Newton (N)'
                self.ui.label_unit_load.setText('* Unit of load : Newton (N)')
                self.ui.label_unitLoad.setText('* Unit Load : 1 Newton (N)')
            if self.current_metric_index[0][1] == 2:
                self.unit_report[1] = 'kilogram (kg)'
                self.ui.label_unit_load.setText(
                    '* Unit of load : kilogram (kg)')
                self.ui.label_unitLoad.setText('* Unit Load : 1 kilogram (kg)')
            if self.current_metric_index[0][2] == 0:
                self.ui.label_unit_stress.setText(
                    '* Unit of force : kilo Newton (kN)')
                self.ui.tableWidget_influenceLine.setHorizontalHeaderLabels(
                    ['Load\nPosition', 'Force\n(kN)'])
            if self.current_metric_index[0][2] == 1:
                self.unit_report[2] = 'Newton (N)'
                self.ui.label_unit_stress.setText(
                    '* Unit of force :  Newton (N)')
                self.ui.tableWidget_influenceLine.setHorizontalHeaderLabels(
                    ['Load\nPosition', 'Force\n(N)'])
            if self.current_metric_index[0][2] == 2:
                self.unit_report[2] = 'kilogram (kg)'
                self.ui.label_unit_stress.setText(
                    '* Unit of force : kilogram (kg)')
                self.ui.tableWidget_influenceLine.setHorizontalHeaderLabels(
                    ['Load\nPosition', 'Force\n(kg)'])

        else:
            self.current_imperial_index = self.unit
            self.unit_report = [
                'ft', 'kip (k)', 'kip (k)', 'ksi', 'in<super size=6>2</super>', 'in']

            self.ui.label_unit_property.setText(
                '* Unit of E : kip per inch squared (ksi)')
            self.ui.label.setText('* Unit of Area (A) : inch squared (in^2)')
            self.ui.label_unit_displacement.setText(
                '* Unit of displacement : inch (in)')

            if self.current_imperial_index[0][0] == 0:
                self.ui.label_unit_node.setText(
                    '* Unit of x and y : foot (ft)')
            if self.current_imperial_index[0][0] == 1:
                self.unit_report[0] = 'in'
                self.ui.label_unit_node.setText(
                    '* Unit of x and y : inch (in)')
            if self.current_imperial_index[0][1] == 0:
                self.ui.label_unit_load.setText('* Unit of load : kip (k)')
                self.ui.label_unitLoad.setText('* Unit Load : 1  kip (k)')
            if self.current_imperial_index[0][1] == 1:
                self.unit_report[1] = 'pound (lb)'
                self.ui.label_unit_load.setText('* Unit of load : pound (lb)')
                self.ui.label_unitLoad.setText('* Unit Load : 1 pound (lb)')
            if self.current_imperial_index[0][2] == 0:
                self.ui.label_unit_stress.setText('* Unit of force : kip (k)')
                self.ui.tableWidget_influenceLine.setHorizontalHeaderLabels(
                    ['Load\nPosition', 'Force\n(kip)'])
            if self.current_imperial_index[0][2] == 1:
                self.unit_report[2] = 'pound (lb)'
                self.ui.label_unit_stress.setText(
                    '* Unit of force : pound (lb)')
                self.ui.tableWidget_influenceLine.setHorizontalHeaderLabels(
                    ['Load\nPosition', 'Force\n(lb)'])

        self.old_label_unit_stress = self.ui.label_unit_stress.text()


    def unit_convert(self, type=None):
        self.change += 1

        self.type = type
        if self.type == 'metric':
            self.logger.debug('Metric unit : %s', self.current_metric_index)

            # Length
            if self.current_metric_index[0][0] == 0:
                self.unit_node = 1
                self.displacement_unit = 1000
                self.reverse_unit = 1
                self.displacement_factor = 0.01
                # Load
                if self.current_metric_index[0][1] == 0:
                    self.force_unit = 1
                    self.force_unit_name = 'kN'
                elif self.current_metric_index[0][1] == 1:
                    self.force_unit = 0.001
                    self.force_unit_name = 'N'
                elif self.current_metric_index[0][1] == 2:
                    self.force_unit = 0.00980665
                    self.force_unit_name = 'kg'

                # Force
                if self.current_metric_index[0][2] == 0:
                    self.bar_force_unit = 1/1000  # (1/1000)/1
                    self.stress_unit = 1000
                elif self.current_metric_index[0][2] == 1:
                    self.bar_force_unit = 1  # (1/1000)/0.001
                    self.stress_unit = 1
                elif self.current_metric_index[0][2] == 2:
                    self.bar_force_unit = (1/1000)/0.00980665
                    self.stress_unit = 9.80665

                self.node()
                self.displacement()
                self.influence_line()

            elif self.current_metric_index[0][0] == 1:
                self.unit_node = 0.001
                self.displacement_unit = 1
                self.reverse_unit = 1000
                self.displacement_factor = 0.01
                # Load
                if self.current_metric_index[0][1] == 0:
                    self.force_unit = 1000
                    self.force_unit_name = 'kN'
                elif self.current_metric_index[0][1] == 1:
                    self.force_unit = 1
                    self.force_unit_name = 'N'
                elif self.current_metric_index[0][1] == 2:
                    self.force_unit = 9.80665
                    self.force_unit_name = 'kg'

                # Force
                if self.current_metric_index[0][2] == 0:
                    self.bar_force_unit = 1/1000  # (1/1000)/1
                    self.stress_unit = 1000
                elif self.current_metric_index[0][2] == 1:
                    self.bar_force_unit = 1  # (1/1000)/0.001
                    self.stress_unit = 1
                elif self.current_metric_index[0][2] == 2:
                    self.bar_force_unit = (1/1000)/0.00980665
                    self.stress_unit = 9.80665

                self.node()
                self.displacement()
                self.influence_line()

        else:
            self.logger.debug('Imperial unit : %s', self.current_imperial_index)

            # Length
            if self.current_imperial_index[0][0] == 0:
                self.unit_node = 1
                self.displacement_unit = 12
                self.reverse_unit = 1
                self.displacement_factor = 0.1
                # Load
                if self.current_imperial_index[0][1] == 0:
                    self.force_unit = 1
                    self.force_unit_name = 'k'
                elif self.current_imperial_index[0][1] == 1:
                    self.force_unit = 0.001
                    self.force_unit_name = 'lb'

                # Force
                if self.current_imperial_index[0][2] == 0:
                    self.bar_force_unit = 1/12
                    self.stress_unit = 1000
                elif self.current_imperial_index[0][2] == 1:
                    self.bar_force_unit = (1/12)*1000
                    self.stress_unit = 1

                self.node()
                self.displacement()
                self.influence_line()

            elif self.current_imperial_index[0][0] == 1:
                self.unit_node = 1/12
                self.displacement_unit = 1
                self.reverse_unit = 12
                self.displacement_factor = 0.1
                # Load
                if self.current_imperial_index[0][1] == 0:
                    self.force_unit = 12
                    self.force_unit_name = 'k'
                elif self.current_imperial_index[0][1] == 1:
                    self.force_unit = 0.012
                    self.force_unit_name = 'lb'

                # Force
                if self.current_imperial_index[0][2] == 0:
                    self.bar_force_unit = 1/12
                    self.stress_unit = 1000
                elif self.current_imperial_index[0][2] == 1:
                    self.bar_force_unit = (1/12)*1000
                    self.stress_unit = 1

                self.node()
                self.displacement()
                self.influence_line()

        self.force_or_stress()


    def calculation(self):
        if len(self.elements)+len(self.restrained_dofs) < self.ndofs:
            self.logger.debug("Unstable structure : [bar : %s + reaction : %s less than 2*no of joints : %s]", len(
                self.elements), len(self.restrained_dofs), self.ndofs)
            self.ui.label_stabality.setText('Unstable')
            self.ui.label_stabality.setStyleSheet("color: rgb(255,0,0);")
        else:
            try:
                self.x_axis = np.array([1, 0])
                self.y_axis = np.array([0, 1])

                self.K = np.zeros([self.ndofs, self.ndofs])

                self.details = np.array([['Member', 'From\nNode', 'To\nNode', 'From\nPoint\n(x)', 'From\nPoint\n(y)',
                                          'To\nPoint\n(x)', 'To\nPoint\n(y)', 'Sine', 'Cosine', 'Length', 'E (ksi)', 'Area']])
                self.report_k = {}
                for key, v in self.member_values.items():
                    fromPoint = np.array(v[0])
                    toPoint = np.array(v[1])
                    elementVector = toPoint-fromPoint

                    fromNode = self.elements[key][0]
                    toNode = self.elements[key][1]

                    dof = []
                    dof.extend(self.degrees_of_freedom[fromNode])
                    dof.extend(self.degrees_of_freedom[toNode])
                    dofs = np.array(dof)

                    cosine = np.dot(elementVector, self.x_axis) / \
                        norm(elementVector)
                    sine = np.dot(elementVector, self.y_axis) / \
                        norm(elementVector)
                    length = norm(elementVector)

                    self.details_initial = np.array([[key, fromNode, toNode, f'{v[0][0]:.2f}', f'{v[0][1]:.2f}', f'{v[1][0]:.2f}',
                                                      f'{v[1][1]:.2f}', f'{sine:.2f}', f'{cosine:.2f}', f'{length:.2f}', self.properties[key][0][0], self.properties[key][0][1]]], dtype=object)
                    self.details = np.append(
                        self.details, self.details_initial, axis=0)

                    E = self.properties[key][0][0]
                    A = self.properties[key][0][1]
                    Ck = (E*A)/length

                    tau = np.array(
                        [[cosine, sine, 0, 0], [0, 0, cosine, sine]], dtype=float)
                    k = np.array([[1, -1], [-1, 1]])
                    k_r = tau.T.dot(k).dot(tau)

                    serial = [dofs.tolist()]
                    for i, j in enumerate(np.around(k_r*Ck, 3).tolist()):
                        j.append(serial[0][i])
                        serial.append(j)

                    self.report_k[key] = serial

                    B = np.zeros((4, self.ndofs))
                    index = dofs-1
                    for i in range(4):
                        B[i, index[i]] = 1.0

                    K_rG = B.T.dot(k_r).dot(B)

                    self.K = self.K + (Ck * K_rG)

                self.F = []
                for f in self.forces.values():
                    self.F.extend(f)
                self.F = np.array(self.F)
                # Final purpose
                self.remove_indices = np.array(self.restrained_dofs)-1

                self.K_final = np.delete(self.K, self.remove_indices, axis=0)
                self.K_final = np.delete(
                    self.K_final, self.remove_indices, axis=1)
                self.logger.debug('Global stiffness matrix : %s',self.K_final)


                self.F_final = np.delete(self.F, self.remove_indices)
                self.logger.debug("Force calculated : %s", self.F_final)


                # Deflectiion global
                self.D_global = np.linalg.inv(self.K_final).dot(self.F_final)
                self.logger.debug('Global deflection : %s',self.D_global)

                self.ui.label_stabality.setText('Stable')
                self.ui.label_stabality.setStyleSheet(
                    "color: rgb(255, 85, 0);")
            except:
                self.logger.debug("Unstable structure")
                self.ui.label_stabality.setText('Unstable')
                self.ui.label_stabality.setStyleSheet("color: rgb(255,0,0);")
                pass


    def displacement(self):
        if self.ui.label_stabality.text() == 'Stable':
            self.ui.label_15.setText("The horizontal (x) and vertical (y) displacements \n"
                                     "are shown below.")
            self.ui.label_15.setFont(QFont('Segoe UI Semibold', 9))
            self.ui.pushButton_start.setVisible(True)
            self.ui.pushButton_stop.setVisible(True)
            self.ui.horizontalSlider.setVisible(True)
            self.ui.label_17.setText("Member tension(T) and compression(C) are shown \n"
                                     "in the graph as well as support reactions. The \n"
                                     "brightness of colors shows their relative strength.")
            self.ui.label_17.setFont(QFont('Segoe UI Semibold', 9))
            self.ui.checkBox_nodes.setVisible(True)
            self.ui.checkBox_members.setVisible(True)
            self.ui.checkBox_forces.setVisible(True)
            self.ui.checkBox_loads.setVisible(True)
            self.ui.checkBox_reactions.setVisible(True)

            self.dofs_list = []
            for i in self.degrees_of_freedom.values():
                self.dofs_list.extend(i)

            self.reaction_indices = []
            for i in self.dofs_list:
                if i not in self.restrained_dofs:
                    # this is the correct one removing restrained dofs
                    self.reaction_indices.append(i)
            self.reaction_indices = np.array(
                self.reaction_indices)-1     # -1 for indexing purposes
            self.logger.debug('Reaction indices : %s', self.reaction_indices)

            self.D_big = np.zeros((self.ndofs))
            for i, j in enumerate(self.reaction_indices):
                self.D_big[j] = self.D_global[i]

            self.D_big = np.around(self.D_big*self.displacement_unit, 4)
            self.logger.debug('Deflection with zeros : %s', self.D_big)
            
            self.ui.tableWidget_displacement.setRowCount(len(self.node_values))

            for i in range(1, len(self.node_values)+1):
                self.ui.tableWidget_displacement.setItem(
                    i-1, 0, QTableWidgetItem(str(i)))
                self.ui.tableWidget_displacement.setItem(
                    i-1, 1, QTableWidgetItem(str(self.D_big[2*i-2])))
                self.ui.tableWidget_displacement.setItem(
                    i-1, 2, QTableWidgetItem(str(self.D_big[2*i-1])))

            abs_D = list(map(lambda x: abs(x), self.D_big))
            max_displacement = max(abs_D)
            if max_displacement > 0:
                self.factored_D = [i/max_displacement for i in self.D_big]
            else:
                self.factored_D = [0 for _ in range(self.ndofs)]

            self.logger.debug('Factored deflection : %s', self.factored_D)

            self.displacement_graph()
            self.reaction_calculation()

        else:
            self.ui.label_15.setText(
                "<font color='orange' size='10'>The truss is unstable, it <br>cannot be analyzed.</font>")
            self.ui.tableWidget_displacement.setRowCount(0)
            self.ui.pushButton_start.setVisible(False)
            self.ui.pushButton_stop.setVisible(False)
            self.ui.horizontalSlider.setVisible(False)
            self.ui.label_17.setText(
                "<font color='orange' size='10'>The truss is unstable, it <br>cannot be analyzed.</font>")
            self.ui.tableWidget_result.setRowCount(0)
            self.ui.checkBox_nodes.setVisible(False)
            self.ui.checkBox_members.setVisible(False)
            self.ui.checkBox_forces.setVisible(False)
            self.ui.checkBox_loads.setVisible(False)
            self.ui.checkBox_reactions.setVisible(False)


    def animation(self):
        self.count = 1
        self.done = 0
        self.max_count = 0
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.animation_mechanism)
        self.timer.start()


    def stop_animation(self):
        self.timer.stop()


    def animation_mechanism(self):
        self.done += 1
        if self.max_count < 51:
            self.count += 1
            self.max_count = self.count
            self.ui.horizontalSlider.setValue(self.count)

        elif self.max_count == 51:
            self.count -= 1
            self.min_count = self.count
            self.ui.horizontalSlider.setValue(self.count)
            if self.min_count == 0:
                self.max_count = 0

        if self.done == 200:
            self.timer.stop()
        else:
            self.ui.stackedWidget.currentChanged.connect(
                lambda: self.timer.stop())


    def reaction_calculation(self):
        self.K_reaction = np.delete(self.K, self.reaction_indices, axis=0)
        self.F_reaction = np.delete(self.F, self.reaction_indices)
        self.D_reaction = np.zeros((self.ndofs))

        for i, j in enumerate(self.reaction_indices):
            self.D_reaction[j] = self.D_global[i]

        self.R_global = np.dot(self.K_reaction, self.D_reaction)
        self.R_global = np.around(self.R_global/self.force_unit, 2)

        self.sort_support_force = []
        if len(self.support_force) > 0:
            for i in sorted(self.support_force):
                if i in self.restrained_dofs:
                    self.sort_support_force.append(self.support_force[i])
            self.sort_support_force = np.array(
                self.sort_support_force)/self.force_unit

            self.R_global = np.around(self.R_global-self.sort_support_force, 2)

        self.logger.debug('Reaction global : %s', self.R_global)

        self.R_graph = {}
        for i, j in enumerate(self.restrained_dofs):
            if j % 2 == 0:
                self.R_graph[i] = self.node_values[j /
                                                   2], 90, self.R_global[i], f'center'
            else:
                self.R_graph[i] = self.node_values[(
                    j+1)/2], 0, self.R_global[i], f'left'

        self.logger.debug('Reaction graph : %s',self.R_graph)

        D_r = np.zeros(4)
        self.bar_force = []
        for k, v in self.member_values.items():
            fromPoint = np.array(v[0])
            toPoint = np.array(v[1])
            elementVector = toPoint-fromPoint

            fromNode = self.elements[k][0]
            toNode = self.elements[k][1]

            dof = []
            dof.extend(self.degrees_of_freedom[fromNode])
            dof.extend(self.degrees_of_freedom[toNode])
            self.dofs = np.array(dof)

            cosine = np.dot(elementVector, self.x_axis)/norm(elementVector)
            sine = np.dot(elementVector, self.y_axis)/norm(elementVector)
            length = norm(elementVector)

            E = self.properties[k][0][0]
            A = self.properties[k][0][1]
            Ck = (E*A)/length

            tau = np.array([-cosine, -sine, cosine, sine], dtype=float)

            D_r[0] = self.D_big[fromNode*2-2]
            D_r[1] = self.D_big[fromNode*2-1]
            D_r[2] = self.D_big[toNode*2-2]
            D_r[3] = self.D_big[toNode*2-1]

            sigma = np.round((Ck*np.dot(tau, D_r))*self.bar_force_unit, 4)
            self.bar_force.append(sigma)

        self.logger.debug('bar_force : %s', self.bar_force)

        self.bar_stress = []
        for key,value in self.properties.items():
            force = self.bar_force[key-1]
            area = value[0][1]
            stress  = round(((force/area) * self.stress_unit), 4)
            self.bar_stress.append(stress)

        self.logger.debug('Stress : %s', self.bar_stress)

        self.stress_table = []
        for i, j in enumerate(self.bar_force):
            if j > 0:
                self.stress_table.append(
                    (i+1, f"{self.elements[i+1][0]}-{self.elements[i+1][1]}", abs(j), 'tension'))
            elif j < 0:
                self.stress_table.append(
                    (i+1, f"{self.elements[i+1][0]}-{self.elements[i+1][1]}", abs(j), 'compression'))
            else:
                self.stress_table.append(
                    (i+1, f"{self.elements[i+1][0]}-{self.elements[i+1][1]}", 0, 'zero'))

        self.ui.tableWidget_result.setRowCount(len(self.member_values))

        for i, v in enumerate(self.stress_table):
            self.ui.tableWidget_result.setItem(
                i, 0, QTableWidgetItem(str(v[0])))
            self.ui.tableWidget_result.setItem(i, 1, QTableWidgetItem(v[1]))

            item1 = QTableWidgetItem(f"{v[2]}")
            item2 = QTableWidgetItem(v[3])
            if v[3] == 'tension':
                item1.setTextColor(QColor(10, 54, 157))
                item2.setTextColor(QColor(10, 54, 157))
            elif v[3] == 'compression':
                item1.setTextColor(QColor(255, 36, 0))
                item2.setTextColor(QColor(255, 36, 0))
            self.ui.tableWidget_result.setItem(i, 2, item1)
            self.ui.tableWidget_result.setItem(i, 3, item2)

        factoring = sorted([abs(i) for i in self.bar_force])
        self.logger.debug('Factoring : %s', factoring)

        alpha = []
        if max(factoring) > 0:
            for i in np.linspace(0.3, 1, len(factoring)):
                alpha.append(i)
            self.factored_bar_force = {key: value for (
                key, value) in zip(factoring, alpha)}
        else:
            self.factored_bar_force = {key: 0 for key in factoring}

        self.logger.debug('Factored bar_force : %s', self.factored_bar_force)

        self.stress_graph()


    def force_or_stress(self):
        try:
            if self.ui.radioButton_stress.isChecked():
                self.ui.tableWidget_result.setHorizontalHeaderLabels(
                        ['Member', 'Node', 'Stress', 'Direction'])

                if self.type == 'metric':
                    self.ui.label_unit_stress.setText(
                        '* Unit of stress : Megapascal (MPa)')
                else:
                    self.ui.label_unit_stress.setText(
                        '* Unit of stress : Pound per square inch (psi)')
                showme = self.bar_stress
            
            else:
                self.ui.tableWidget_result.setHorizontalHeaderLabels(
                    ['Member', 'Node', 'Force', 'Direction'])
                        
                self.ui.label_unit_stress.setText(self.old_label_unit_stress)
                showme = self.bar_force

            for i, j in enumerate(showme):
                value = QTableWidgetItem(str(abs(j)))
                if j > 0 :
                    value.setTextColor(QColor(10, 54, 157))
                elif j < 0 :
                    value.setTextColor(QColor(255, 36, 0))
                self.ui.tableWidget_result.setItem(i, 2, value)

            self.stress_graph()

        except:
            pass


    def graph(self):
        try:
            self.graph_widget.figure1.clear()
            ax = self.graph_widget.figure1.add_subplot(111)
            self.graph_widget.figure1.tight_layout()

            if self.ui.stackedWidget_2.currentIndex() == 0:
                ax.grid(True)
                ax.spines['right'].set_visible(False)
                ax.spines['top'].set_visible(False)
                if self.max_X > self.max_Y:
                    ax.margins(0.25, 0.5)
                else:
                    ax.margins(0.5, 0.25)
            else:
                if self.max_X > self.max_Y:
                    ax.margins(0.15, 0.35)
                else:
                    ax.margins(0.35, 0.15)
                ax.grid(False)
                ax.axis('off')

            # node plot
            ax.scatter(self.X, self.Y, c='whitesmoke',
                       s=200, edgecolors='k', zorder=9)
            for i, _ in enumerate(self.X):
                ax.annotate(
                    i+1, (self.X[i], self.Y[i]), zorder=10, ha='center', va='center', size='8')
            self.graph_widget.canvas1.draw()

            # member plot
            if self.ui.radioButtonDefault.isChecked():
                for v in self.plot_final.values():
                    ax.plot(v[0], v[1], linewidth=2)
            else:
                for v in self.plot_final.values():
                    ax.plot(v[0], v[1], linewidth=2, c='k')
            self.graph_widget.canvas1.draw()

            # support draw
            for k, v in self.support_graph.items():
                if 'pinned' in k:
                    pinned_support = pinnedSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax.plot(v[0][0], v[0][1], marker=pinned_support, color='k',
                            markerfacecolor='lightsteelblue', markersize=50)
                elif 'roller' in k:
                    roller_support = rollerSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax.plot(v[0][0], v[0][1], marker=roller_support, color='k',
                            markerfacecolor='lightsteelblue', markersize=55)
            self.graph_widget.canvas1.draw()

            # Force draw
            for v in self.force_graph.values():
                arrow = ownArrow()
                arrow = arrow.transformed(
                    matplotlib.transforms.Affine2D().rotate_deg(v[2]))
                ax.plot(v[0], v[1], marker=arrow, color='r',
                        markersize=60, markeredgewidth=1)

                ax.annotate(f'{v[3]} {self.force_unit_name}',
                            xy=(v[0], v[1]), xycoords='data',
                            xytext=(
                                32*np.cos(np.radians(v[2]-180)), 35*np.sin(np.radians(v[2]-180))),
                            textcoords='offset points',
                            ha=v[-1], va='center', zorder=20, color='r')
            self.graph_widget.canvas1.draw()

        except:
            pass


    def displacement_graph(self):
        self.scale = self.ui.horizontalSlider.value()*self.displacement_factor

        self.X_displacement = [self.X_withoutunit[int(
            i/2)]+j*self.scale for i, j in enumerate(self.factored_D) if i % 2 == 0]
        self.Y_displacement = [self.Y_withoutunit[int(
            i/2)]+j*self.scale for i, j in enumerate(self.factored_D) if i % 2 != 0]

        self.node_displacement = {}
        for i, j in self.elements.items():
            self.node_displacement[i] = (self.X_displacement[j[0]-1], self.X_displacement[j[1]-1]
                                         ), (self.Y_displacement[j[0]-1], self.Y_displacement[j[1]-1])

        self.force_displacement = {}
        for k, v in self.force_graph.items():
            s = v[-2]
            self.force_displacement[k] = self.X_displacement[s -
                                                             1], self.Y_displacement[s-1], v[2], v[3], s, v[-1]

        try:
            self.graph_widget2.figure2.clear()

            ax2 = self.graph_widget2.figure2.add_subplot(111)
            self.graph_widget2.figure2.tight_layout()

            if max(self.X_withoutunit) > max(self.Y_withoutunit):
                ax2.margins(0.15, 0.35)
            else:
                ax2.margins(0.35, 0.15)

            ax2.axis('off')

            # node plot
            ax2.scatter(self.X_withoutunit, self.Y_withoutunit,
                        c='whitesmoke', s=200, edgecolors='yellow', zorder=9)
            for i, _ in enumerate(self.X_withoutunit):
                ax2.annotate(i+1, (self.X_withoutunit[i], self.Y_withoutunit[i]),
                             zorder=10, ha='center', va='center', c='y', size='8')

            ax2.scatter(self.X_displacement, self.Y_displacement,
                        c='whitesmoke', s=200, edgecolors='k', zorder=30)
            for i, _ in enumerate(self.X_displacement):
                ax2.annotate(
                    i+1, (self.X_displacement[i], self.Y_displacement[i]), zorder=30, ha='center', va='center', size='8')

            # member plot
            for v in self.plot_displacement_final.values():
                ax2.plot(v[0], v[1], color='gray', alpha=0.5)
            for v in self.node_displacement.values():
                ax2.plot(v[0], v[1], color='turquoise', zorder=15, linewidth=2)

            # support draw
            for k, v in self.support_displacement_graph.items():
                if 'pinned' in k:
                    pinned_support = pinnedSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax2.plot(v[0][0], v[0][1], marker=pinned_support, color='k',
                             markerfacecolor='lightsteelblue', markersize=50)
                elif 'roller' in k:
                    roller_support = rollerSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax2.plot(v[0][0], v[0][1], marker=roller_support, color='k',
                             markerfacecolor='lightsteelblue', markersize=55)

            # Force draw
            for v in self.force_displacement.values():
                arrow = ownArrow()
                arrow = arrow.transformed(
                    matplotlib.transforms.Affine2D().rotate_deg(v[2]))
                ax2.plot(v[0], v[1], marker=arrow, color='r',
                         markersize=60, markeredgewidth=1, zorder=19)

                ax2.annotate(f'{v[3]} {self.force_unit_name}',
                             xy=(v[0], v[1]), xycoords='data',
                             xytext=(
                                 32*np.cos(np.radians(v[2]-180)), 35*np.sin(np.radians(v[2]-180))),
                             textcoords='offset points',
                             ha=v[-1], va='center', zorder=20, color='r')

            self.graph_widget2.canvas2.draw()

        except:
            pass


    def stress_graph(self):
        try:
            self.graph_widget3.figure3.clear()
            ax3 = self.graph_widget3.figure3.add_subplot(111)
            self.graph_widget3.figure3.tight_layout()

            if self.max_X > self.max_Y:
                ax3.margins(0.15, 0.35)
            else:
                ax3.margins(0.35, 0.15)

            ax3.axis('off')

            if self.ui.checkBox_nodes.isChecked():
                # node plot
                ax3.scatter(self.X, self.Y, c='whitesmoke',
                            s=200, edgecolors='k', zorder=9)
                for i, _ in enumerate(self.X):
                    ax3.annotate(
                        i+1, (self.X[i], self.Y[i]), zorder=10, ha='center', va='center', size='8')
                self.graph_widget3.canvas3.draw()
            else:
                for k, v in self.support_graph.items():
                    ax3.scatter(v[0][0], v[0][1], c='whitesmoke',
                                s=200, edgecolors='k', zorder=9)
                    ax3.annotate(k[-1:], (v[0][0], v[0][1]),
                                 zorder=10, ha='center', va='center', size='8')
                self.graph_widget3.canvas3.draw()

            if self.ui.checkBox_members.isChecked():
                # member plot
                for k, v in self.plot_final.items():
                    bar_force_value = self.bar_force[k-1]
                    if bar_force_value < 0:
                        ax3.plot(v[0], v[1], color='crimson', alpha=self.factored_bar_force[abs(
                            bar_force_value)], linewidth=2)
                    elif bar_force_value > 0:
                        ax3.plot(v[0], v[1], color='dodgerblue', alpha=self.factored_bar_force[abs(
                            bar_force_value)], linewidth=2)
                    else:
                        ax3.plot(v[0], v[1], color='k', alpha=0.5, linewidth=2)

                    if self.ui.checkBox_forces.isChecked():
                        if self.ui.radioButton_stress.isChecked():
                            ax3.annotate(abs(self.bar_stress[k-1]), (np.mean(v[0]), np.mean(
                                v[1])), zorder=50, ha='center', va='center', size='10')
                        else:
                            ax3.annotate(abs(bar_force_value), (np.mean(v[0]), np.mean(
                                v[1])), zorder=50, ha='center', va='center', size='10')

                    else:
                        ax3.annotate(k, (np.mean(v[0]), np.mean(
                            v[1])), zorder=50, ha='center', va='center', size='10')
                            
                self.graph_widget3.canvas3.draw()

            # support draw
            for k, v in self.support_graph.items():
                if 'pinned' in k:
                    pinned_support = pinnedSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax3.plot(v[0][0], v[0][1], marker=pinned_support, color='k',
                             markerfacecolor='lightsteelblue', markersize=50)
                elif 'roller' in k:
                    roller_support = rollerSupport().transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax3.plot(v[0][0], v[0][1], marker=roller_support, color='k',
                             markerfacecolor='lightsteelblue', markersize=55)
            self.graph_widget3.canvas3.draw()

            if self.ui.checkBox_loads.isChecked():
                # Force draw
                for v in self.force_graph.values():
                    arrow = ownArrow()
                    arrow = arrow.transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[2]))
                    ax3.plot(v[0], v[1], marker=arrow, color='r',
                             markersize=60, markeredgewidth=1)

                    ax3.annotate(f'{v[3]} {self.force_unit_name}',
                                 xy=(v[0], v[1]), xycoords='data',
                                 xytext=(
                                     32*np.cos(np.radians(v[2]-180)), 35*np.sin(np.radians(v[2]-180))),
                                 textcoords='offset points',
                                 ha=v[-1], va='center', zorder=20, color='r')
                self.graph_widget3.canvas3.draw()

            if self.ui.checkBox_reactions.isChecked():
                # Reaction draw
                for v in self.R_graph.values():
                    arrow = reactionArrow()
                    arrow = arrow.transformed(
                        matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                    ax3.plot(v[0][0], v[0][1], marker=arrow,
                             color='green',  markersize=60, markeredgewidth=1.0)

                    ax3.annotate(f'{v[2]} {self.force_unit_name}',
                                 xy=(v[0][0], v[0][1]), xycoords='data',
                                 xytext=(
                                     32*np.cos(np.radians(v[1])), 35*np.sin(np.radians(v[1]))),
                                 textcoords='offset points',
                                 ha=v[-1], va='center', zorder=30, color='green', size=10)
                self.graph_widget3.canvas3.draw()

        except:
            pass


    def report_graph(self):
        fig, ax_r = plt.subplots()
        fig.tight_layout()
        if self.max_X > self.max_Y:
            ax_r.margins(0.15, 0.35)
        else:
            ax_r.margins(0.35, 0.15)

        global buf_node
        buf_node = BytesIO()
        ax_r.grid(True)
        ax_r.spines['right'].set_visible(False)
        ax_r.spines['top'].set_visible(False)
        # node plot
        ax_r.scatter(self.X, self.Y, c='whitesmoke',
                     s=200, edgecolors='k', zorder=9)
        for i, _ in enumerate(self.X):
            ax_r.annotate(i+1, (self.X[i], self.Y[i]),
                          zorder=10, ha='center', va='center', size='8')

        fig.savefig(buf_node, format="png", bbox_inches='tight', dpi=300)
        buf_node.seek(0)
        self.graph_widget.canvas1.draw()

        global buf_element
        buf_element = BytesIO()
        ax_r.grid(False)
        ax_r.axis('off')
        # member plot
        for k, v in self.plot_final.items():
            ax_r.plot(v[0], v[1], linewidth=2)

        fig.savefig(buf_element, format="png", bbox_inches='tight', dpi=300)
        buf_element.seek(0)

        global buf_support
        buf_support = BytesIO()
        # support draw
        for k, v in self.support_graph.items():
            if 'pinned' in k:
                pinned_support = pinnedSupport().transformed(
                    matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                ax_r.plot(v[0][0], v[0][1], marker=pinned_support, color='k',
                          markerfacecolor='lightsteelblue', markersize=50)
            elif 'roller' in k:
                roller_support = rollerSupport().transformed(
                    matplotlib.transforms.Affine2D().rotate_deg(v[1]))
                ax_r.plot(v[0][0], v[0][1], marker=roller_support, color='k',
                          markerfacecolor='lightsteelblue', markersize=55)

        # Force draw
        for v in self.force_graph.values():
            arrow = ownArrow()
            arrow = arrow.transformed(
                matplotlib.transforms.Affine2D().rotate_deg(v[2]))
            ax_r.plot(v[0], v[1], marker=arrow, color='r',
                      markersize=60, markeredgewidth=1)

            ax_r.annotate(f'{v[3]} {self.force_unit_name}',
                          xy=(v[0], v[1]), xycoords='data',
                          xytext=(32*np.cos(np.radians(v[2]-180)),
                                  35*np.sin(np.radians(v[2]-180))),
                          textcoords='offset points',
                          ha=v[-1], va='center', zorder=20, color='r')

        fig.savefig(buf_support, format="png", bbox_inches='tight', dpi=300)
        buf_support.seek(0)


    def update_change(self):
        self.change += 1


    def generate_report(self):
        global member_page
        global support_page
        global stress_page
        global displacement_page
        
        total_node = len(self.node_values)
        total_member = len(self.member_values)
        
        if total_node < 27:
            member_page = 3
        else:
            member_page = int((total_node - 27) / 37) + 4

        if total_member < 33:
            support_page = member_page + 1
        else:
            support_page = int((total_member - 33) / 37) + member_page + 2

        if total_node < 34:
            displacement_page = 0
        else:
            displacement_page = int((total_node - 33) / 37) + 1

        stress_page = int(total_member / 37) + displacement_page + 2

        self.report = True
        if not self.demo:
            self.save_to_file()
        else:
            self.savedemo = None
            self.filename = list(self.filename)
            self.filename[0] = f'{tempfile.gettempdir()}'+f'\\{self.name}'
            self.filename = tuple(self.filename)
            self.save_to_file()
            self.savedemo = True

        self.report_graph()
        date = datetime.datetime.now().strftime("%A, %B %d, %Y at %I:%M %p %Z")
        self.logger.debug('Date : %s', date)
        
        banner_1 = """
        ..########..########....##..........##....######......######..<br/>
        ........##........##..........##..##..........##..##........##..##........##<br/>
        ........##........##..........##..##..........##..##..............##............<br/>
        ........##........########....##..........##....######......######..<br/>
        ........##........##......##......##..........##.......
        .......##..............##<br/>
        ........##........##........##....##..........##..##........##..##........##<br/>
        ........##........##..........##....#######......######......######..
        """
        banner_2 = """
        ........##..........#####............##..........<br/>
        ....####........##......##......####..........<br/>
        ........##......##..........##........##..........<br/>
        ........##......##..........##........##..........<br/>
        ........##......##..........##........##..........<br/>
        ........##........##......##..........##..........<br/>
        ....######......#####........######......<br/>
        """

        if self.ui.projectName.toPlainText():
            project = self.ui.projectName.toPlainText()
        else:
            project = 'Project Truss'
        if self.ui.userName.toPlainText():
            username = self.ui.userName.toPlainText()
        else:
            username = 'Anonymous'

        self.pdfname = self.filename[0].replace('trs', 'pdf')


        self.logger.debug('Saved Filename : %s', self.filename[0])
        self.logger.debug('Pdfname : %s', self.pdfname)

        styles = getSampleStyleSheet()

        doc = SimpleDocTemplate(self.pdfname)

        #self.graph_widget4.figure4.savefig(f'{self.pdfname}.svg',bbox_inches='tight', format='svg', dpi=3000)

        story = []
        story.append(
            Paragraph("<font size='25'>Truss Analysis Report</font>", styles['Title']))
        story.append(Spacer(1, 105))
        story.append(Paragraph(
            f"<para alignment=center size=12 color='steelblue'><strong>Project Name :</strong> {project}</para>"))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            f"<para alignment=center size=12 color='steelblue'><strong>User Name :</strong> {username}</para>"))
        story.append(Spacer(1, 3))
        story.append(Paragraph(
            f"<para alignment=center size=12 color='steelblue'><strong>Created at :</strong> {date}</para>"))
        story.append(Spacer(1, 100))
        story.append(Paragraph(
            "<font size='20'><b>This report was generated by using </b>-----</font>"))
        story.append(Spacer(1, 30))
        story.append(Paragraph(f"""<para color='green' alignment=center>
        {banner_1}
        </para>"""))
        story.append(Spacer(1, 10))
        story.append(Paragraph(f"""<para color='green' alignment=center>
        {banner_2}
        </para>"""))
        story.append(Spacer(1, 100))
        story.append(Paragraph("""N.B: This application has been developed for educational purposes only. 
        Students or Educators are free to use this application."""))
        story.append(PageBreak())

        # Page 2 units
        story.append(Paragraph(f"""<font size='20' color='steelblue'> Units : US Customary System of Units</font><br/><br/>
        <b>Length:</b> {self.unit_report[0]}<br/>
        <b>Applied Load:</b> {self.unit_report[1]}<br/>
        <b>Memnber Forces:</b> {self.unit_report[2]}<br/>
        <b>Modulus of Elasticity (E):</b> {self.unit_report[3]}<br/>
        <b>Cross-sectional Area (A):</b> {self.unit_report[4]}<br/>
        <b>Displacement :</b> {self.unit_report[-1]}<br/><br/><br/>
        <font size='20' color='steelblue'>Truss Geometry : Nodes </font><br/><br/>
        Nodes are the points in (x,y) co-ordinate.<br/><br/><br/>
        """))
        # node
        data = [('Node', "X", "Y")]
        for i, j in enumerate(self.X):
            data.append((i+1, f'{j:.2f}', f'{self.Y[i]:.2f}'))
        t = Table(data, hAlign='LEFT', repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (2, 0), 2, colors.black),
        ]))
        story.append(t)
        story.append(PageBreak())

        # page 3 member
        story.append(Paragraph(
            """<font size='20' color='steelblue'>Truss Members </font><br/><br/>
            Below is the diagram showing how members are connected.<br/><br/><br/>
            """))
        t = Table(self.details[:, 0:3].tolist(), hAlign='LEFT', repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (2, 0), 2, colors.black),
        ]))
        story.append(t)
        story.append(PageBreak())

        # Page 4 Loads and supports
        story.append(Paragraph("""<font size='20' color='steelblue'>Truss Loads and Supports </font><br/><br/>
                Loads direction,magnitude,value as well as Supports are shown below with diagram and table.<br/><br/><br/>"""))
        # load
        data = [('Node', 'Magnitude\n(K)', 'angle\n(degree)')]
        for v in self.force_graph.values():
            data.append((v[-2], v[3], v[2]))
        t = Table(data, hAlign='LEFT', repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (2, 0), 2, colors.black),
        ]))

        story.append(t)
        story.append(PageBreak())

        # Page 5 details
        story.append(Paragraph(
            """<font size='20' color='steelblue'>Before doing matrices </font><br/><br/><br/>"""))
        t = Table(self.details.tolist(), repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (12, 0), 2, colors.black),
            ('LINEABOVE', (0, 0), (12, 0), 2, colors.black),
            ('BACKGROUND', (0, 0), (12, 0), colors.lightblue),
            # ('NOSPLIT',(0,0),(-1,-1)),
        ]))
        story.append(t)
        story.append(PageBreak())

        # Page 6 Member stiffness
        story.append(Paragraph("""<font size='20' color='steelblue'>Member Stiffness Matrices</font><br/><br/>
            This stiffness matrix is for an element.  
            The element attaches to two nodes and each of these nodes has two degrees of freedom.  
            The rows and columns of the stiffness matrix correlate to those degrees of freedom.
        """))
        story.append(Spacer(1, 30))
        member_matrices = [["k = EA / L", Paragraph('<para alignment=center size=15>c<super size=8>2</super></para>'), 'cs', Paragraph('<para alignment=center size=15>-c<super size=8>2</super></para>'), '-cs'],
                           ["", 'cs', Paragraph('<para alignment=center size=15> s<super size=8>2</super></para>'), '-cs', Paragraph(
                               '<para alignment=center size=15>-s<super size=8>2</super></para>')],
                           ["", Paragraph('<para alignment=center size=15>-c<super size=8>2</super></para>'), '-cs', Paragraph(
                               '<para alignment=center size=15>c<super size=8>2</super></para>'), 'cs'],
                           ["", '-cs', Paragraph('<para alignment=center size=15>-s<super size=8>2</super></para>'),
                            'cs', Paragraph('<para alignment=center size=15> s<super size=8>2</super></para>')],
                           ]
        t = Table(member_matrices, 4*[0.9*inch], 4*[0.3*inch])
        t.setStyle(TableStyle([
            ("SIZE", (0, 0), (-1, -1), 15),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 0), (0, 3), 'RIGHT'),
            ('SPAN', (0, 0), (0, 3)),
            ('LINEBEFORE', (1, 0), (1, 3), 2, colors.black),
            ('LINEAFTER', (-1, 0), (-1, 3), 2, colors.black)
        ]))
        story.append(t)
        story.append(Spacer(1, 30))
        for k, v in self.report_k.items():
            t = Table(v, 5*[1*inch], 5*[0.3*inch], hAlign='RIGHT')
            t.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 1), (-2, -1), 0.25, colors.black),
                ('ALIGN', (-1, 0), (-1, -1), 'LEFT')
            ]))
            story.append(Paragraph(
                f"<font size='15' color='steelblue'><u> Member {k} :</u></font><br/><br/>"))
            story.append(t)
            story.append(Spacer(1, 32))
        if len(self.elements) not in [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43.47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99]:
            story.append(PageBreak())

        # page 7 Stiffness matrix(unconstrained)
        story.append(Paragraph(f"""<font size='20' color='steelblue'>System or Global Stiffness Matrix (unconstrained)</font><br/><br/>
            We add the degree of freedom for each member stiffness matrix into the same degree of freedom in the structural matrix.  
            The resulting structural stiffness matrix is shown below.
            (To fit on a page the matrix may split into 8 columns and row into several pages)
        """))
        story.append(Spacer(1, 30))
        data = {}
        for i in range(1, self.ndofs, 8):
            d = [[j for j in range(i, i+8) if j < self.ndofs+1]]
            for k, v in enumerate(np.around(self.K[:, [j for j in range(i-1, i+7) if j < self.ndofs]], 2).tolist()):
                v.append(k+1)
                d.append(v)
            data[i] = d

        for value in data.values():
            t = Table(value, repeatRows=1)
            t.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 1), (-2, -1), 0.25, colors.black),
                ('ALIGN', (-1, 0), (-1, -1), 'LEFT'),
            ]))
            story.append(t)
            story.append(PageBreak())

        # Page 8 stiffness matrix (constrained)
        story.append(Paragraph(f"""<font size='20' color='steelblue'>System or Global Stiffness Matrix (constrained)</font><br/><br/>
            We have boundary conditions at supports.  Our assumption is that these joints will not move in the constrained direction.  
            We remove these from our matrix.  The constrained displacements are dof <br/>{self.restrained_dofs}.<br/>
            The resulting matrix is:
            (To fit on a page the matrix may split into 8 columns and row into several pages)<br/><br/>
        """))
        story.append(Spacer(1, 20))
        data = {}
        for i in range(1, len(self.reaction_indices), 8):
            d = [(self.reaction_indices[i-1:i+7]+1).tolist()]
            constrained = np.around(self.K[:, [j for j in range(
                i-1, i+7) if j < len(self.reaction_indices)]], 2).tolist()
            for k, v in enumerate(constrained):
                if k+1 not in self.restrained_dofs:
                    v.append(k+1)
                    d.append(v)
            data[i] = d

        for value in data.values():
            t = Table(value, repeatRows=1)
            t.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 1), (-2, -1), 0.25, colors.black),
                ('ALIGN', (-1, 0), (-1, -1), 'LEFT'),
            ]))
            story.append(t)
            story.append(PageBreak())

        # Page 9 Force_final
        story.append(Paragraph(f"""<font size='20' color='steelblue'>Force Matrix</font><br/><br/> 
            The constrained displacements are dof {self.restrained_dofs}.
            Like System stiffness matrix we remove these from our force matrix.
            The resulting matrix is:<br/><br/><br/><br/>
        """))
        data = list(zip(self.F_final, self.reaction_indices+1))
        t = Table(data)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (0, -1), 0.5, colors.black),
        ]))
        story.append(t)
        story.append(PageBreak())

        global buf_bar_force
        buf_bar_force = BytesIO()
        self.ui.checkBox_nodes.setChecked(False)
        self.ui.checkBox_forces.setChecked(False)
        self.ui.checkBox_loads.setChecked(False)
        self.ui.checkBox_reactions.setChecked(False)
        self.graph_widget3.figure3.savefig(buf_bar_force, format='png', bbox_inches='tight', dpi=300)
        buf_bar_force.seek(0)

        global buf_reaction
        buf_reaction = BytesIO()
        self.ui.checkBox_members.setChecked(False)
        self.ui.checkBox_reactions.setChecked(True)
        self.graph_widget3.figure3.savefig(buf_reaction, format='png', dpi=300)
        buf_reaction.seek(0)

        self.ui.checkBox_nodes.setChecked(True)
        self.ui.checkBox_members.setChecked(True)
        self.ui.checkBox_forces.setChecked(True)
        self.ui.checkBox_loads.setChecked(True)
        self.ui.checkBox_reactions.setChecked(True)

        # Page 10 Member Force
        story.append(Paragraph("""<font size='20' color='steelblue'>Member Forces and Support Reactions</font><br/>
            <br/>&sigma; = E/L {-c&nbsp; -s &nbsp;c &nbsp;s} q  <br/>We use this equation to compute the member Force of 
            each element.Support reactions are shown in the diagram.<br/><br/><br/>
        """))
        story.append(PageBreak())

        data = [('Member', 'Node', 'Force', 'Stress', 'Direction')]
        for i, j in enumerate(self.bar_force):
            if j > 0:
                data.append(
                    (i+1, f"{self.elements[i+1][0]}-{self.elements[i+1][1]}", j, self.bar_stress[i], 'tension'))
            else:
                data.append(
                    (i+1, f"{self.elements[i+1][0]}-{self.elements[i+1][1]}", j, self.bar_stress[i], 'compression'))
        t = Table(data, hAlign='LEFT', repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (4, 0), 2, colors.black),
            #('NOSPLIT',(0, 0), (-1, -1))
        ]))

        story.append(t)
        story.append(PageBreak())

        # Page 11 nodal displacement1
        story.append(Paragraph("""<font size='20' color='steelblue'>Nodal Displacements</font><br/><br/>
        The horizontal(x) and vertical(y) displacements are shown below.<br/><br/><br/>"""))
        data = [('Node', 'x\ndisplacement', 'y\ndisplacement')]
        for i in range(1, int(self.ndofs/2)+1):
            data.append(
                (i, f'{self.D_big[2*i-2]:.3f}', f'{self.D_big[2*i-1]:.3f}'))
        t = Table(data, hAlign='LEFT', repeatRows=1)
        t.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('LINEBELOW', (0, 0), (2, 0), 2, colors.black),
        ]))
        story.append(t)

        global buf_displacement
        buf_displacement = BytesIO()
        self.ui.horizontalSlider.setValue(30)
        self.graph_widget2.figure2.savefig(
            buf_displacement, format='png', bbox_inches='tight', dpi=300)
        buf_displacement.seek(0)

        doc.build(story, canvasmaker=NumberedCanvas)

        os.startfile(self.pdfname)


    """
    Influence line
    """

    def movingload(self):
        """
        THis will create moving node dictionary from load starting and ending position
        """
        try:
            self.load_path = []
            self.moving_node = {}
            self.moving_position = []

            starting_node = int(self.ui.lineEdit_startingNode.text())
            ending_node = int(self.ui.lineEdit_endingNode.text())

            self.starting_value = self.node_values[starting_node]
            self.ending_value = self.node_values[ending_node]
            self.starting_X = self.starting_value[0]
            self.starting_Y = self.starting_value[1]
            self.ending_X = self.ending_value[0]
            self.ending_Y = self.ending_value[1]

            self.load_path = [[self.starting_X, self.ending_X], [
                self.starting_Y, self.ending_Y]]

            self.movingload_graph()

            slope_required = (self.ending_Y - self.starting_Y) / \
                (self.ending_X - self.starting_X)

            self.logger.debug('Moving load starting node : %s', self.starting_value)
            self.logger.debug('Moving node ending node : %s', self.ending_value)
            self.logger.debug('Slope required : %s', slope_required)


            if self.starting_X < self.ending_X:
                sorted_node = dict(
                    sorted(self.node_values.items(), key=lambda item: item[1][0]))
                sorted_node_revised = {key: value for key, value in sorted_node.items(
                ) if value[0] >= self.starting_X and value[0] <= self.ending_X}

            else:
                sorted_node = dict(
                    sorted(self.node_values.items(), key=lambda item: item[1][0], reverse=True))
                sorted_node_revised = {key: value for key, value in sorted_node.items(
                ) if value[0] <= self.starting_X and value[0] >= self.ending_X}

            self.logger.debug('Sorted node revised : %s', sorted_node_revised)

            for key, value in sorted_node_revised.items():
                if key == starting_node:
                    self.moving_node[key] = value
                else:
                    try:
                        if ((value[1] - self.starting_Y) / (value[0] - self.starting_X)) == slope_required:
                            self.moving_node[key] = value
                    except:
                        continue

            self.logger.debug('Moving node : %s', self.moving_node)
            
            self.moving_position = [key for key in self.moving_node.keys()]
            self.logger.debug('Moving position : %s', self.moving_position)

        except KeyError:
            self.movingload_graph()

        except:
            pass

    def influence_line(self):
        """
        influence line for every member will be calculated and
        will collect them in force_influence dictionary.
        """
        try:
            self.ui.tableWidget_influenceLine.setRowCount(0)
            self.influence_list = []
            self.force_influence = {i: []
                                    for i in range(1, len(self.member_values)+1)}

            for node in self.moving_node.keys():
                self.F_unit = np.zeros(self.ndofs)
                self.F_unit[2*node-1] = -1*self.force_unit
                self.F_unit = np.delete(
                    self.F_unit, self.remove_indices, axis=0)

                # Deflection unit load
                self.D_unit = np.linalg.inv(self.K_final).dot(self.F_unit)
                self.D_big_unit = np.zeros((self.ndofs))

                for i, j in enumerate(self.reaction_indices):
                    self.D_big_unit[j] = self.D_unit[i]
                self.D_big_unit = np.around(
                    self.D_big_unit*self.displacement_unit, 4)

                D_r = np.zeros(4)
                self.influence = []
                for k, v in self.member_values.items():
                    fromPoint = np.array(v[0])
                    toPoint = np.array(v[1])
                    elementVector = toPoint-fromPoint

                    fromNode = self.elements[k][0]
                    toNode = self.elements[k][1]

                    dof = []
                    dof.extend(self.degrees_of_freedom[fromNode])
                    dof.extend(self.degrees_of_freedom[toNode])
                    self.dofs = np.array(dof)

                    cosine = np.dot(elementVector, self.x_axis) / \
                        norm(elementVector)
                    sine = np.dot(elementVector, self.y_axis) / \
                        norm(elementVector)
                    length = norm(elementVector)

                    E = self.properties[k][0][0]
                    A = self.properties[k][0][1]
                    Ck = (E*A)/length

                    tau = np.array([-cosine, -sine, cosine, sine], dtype=float)

                    D_r[0] = self.D_big_unit[fromNode*2-2]
                    D_r[1] = self.D_big_unit[fromNode*2-1]
                    D_r[2] = self.D_big_unit[toNode*2-2]
                    D_r[3] = self.D_big_unit[toNode*2-1]

                    sigma = np.round((Ck*np.dot(tau, D_r))*self.bar_force_unit, 4)

                    self.influence.append(sigma)

                self.influence_list.append(self.influence)

            for i in self.influence_list:
                for j in range(len(self.member_values)):
                    self.force_influence[j+1].append(i[j])
                    
            self.logger.debug('Force influence : %s', self.force_influence)

            self.ui.comboBox_influence.clear()
            item = [str(key) for key in self.member_values.keys()]
            self.ui.comboBox_influence.addItems(item)

        except:
            pass


    def influence_table(self):
        """
        for member selected from combobox influence line will be 
        shown in table
        """
        try:
            self.ui.tableWidget_influenceLine.setRowCount(
                len(self.moving_node))
            currentIndex = int(self.ui.comboBox_influence.currentText())

            for key, value in self.force_influence.items():
                if key == currentIndex:
                    for index, (position, result) in enumerate(zip(self.moving_position, value)):
                        self.ui.tableWidget_influenceLine.setItem(
                            index, 0, QTableWidgetItem(str(position)))
                        self.ui.tableWidget_influenceLine.setItem(
                            index, 1, QTableWidgetItem(str(result)))

            self.influence_graph(member=currentIndex)
        except:
            self.movingload_graph()
            pass


    def movingload_graph(self):
        """
        complete truss structures and load path shown in graph
        """
        try:
            self.graph_widget4.figure4.clear()
            ax4 = self.graph_widget4.figure4.add_subplot(211)
            self.ax5 = self.graph_widget4.figure4.add_subplot(212)

            ax4.axis('off')
            self.ax5.axis('off')

            # node plot
            ax4.scatter(self.X, self.Y, c='whitesmoke',
                        s=200, edgecolors='k', zorder=9)
            for i, _ in enumerate(self.X):
                ax4.annotate(
                    i+1, (self.X[i], self.Y[i]), zorder=10, ha='center', va='center', size='8')
            # creating space to adjust with influence line
            ax4.scatter(self.max_X*1.05, 0, s=0)
            self.graph_widget4.canvas4.draw()

            # member plot
            for k, v in self.plot_final.items():
                ax4.plot(v[0], v[1], linewidth=1.2, c='k')

                ax4.annotate(k, (np.mean(v[0]), np.mean(
                    v[1])), zorder=50, ha='center', va='center', size='10', c='red')
            self.graph_widget4.canvas4.draw()

            # moving load path
            ax4.plot(self.load_path[0], self.load_path[1],
                     zorder=10, linewidth=2, c='red')
            self.graph_widget4.canvas4.draw()

            self.graph_widget4.figure4.tight_layout()

        except:
            pass


    def influence_graph(self, member):
        """
        influence line graph
        """
        self.movingload_graph()
        try:
            x_scatter = []
            force_scatter = []
            moving_load_x = [x[0] for x in self.moving_node.values()]
            influence_line = self.force_influence[member]

            for i, j in enumerate(influence_line):
                if j != 0:
                    x_scatter.append(moving_load_x[i])
                    force_scatter.append(j)

            """
            Handling spaces to adjust with truss even if moving load doesn't start 
            from (0,0) co-ordinates
            """
            self.ax5.scatter([self.min_X, self.max_X*1.05], [0, 0], s=0)
            self.graph_widget4.canvas4.draw()

            '''
            scatter and force annotation (y-axis)
            '''
            self.ax5.scatter(x_scatter, force_scatter, s=10, c='k', zorder=5)

            for i, j in enumerate(force_scatter):
                if j < 0:
                    self.ax5.annotate(f'{j:.2f}', xy=(x_scatter[i], force_scatter[i]*1.08),
                                      ha='center', va='top', zorder=10)
                else:
                    self.ax5.annotate(f'{j:.2f}', xy=(x_scatter[i], force_scatter[i]*1.08),
                                      ha='center', va='bottom', zorder=10)
            self.graph_widget4.canvas4.draw()

            '''
            scatter and unit load position annotation (x-axis)
            '''
            self.ax5.scatter(
                moving_load_x, [0]*len(moving_load_x), marker="|", c='k')
            for i, j in enumerate(moving_load_x):
                self.ax5.annotate(f'{j:g}', xy=(j, -0.025),
                                  ha='center', va='top', zorder=10)
            self.graph_widget4.canvas4.draw()

            '''
            Influence line
            '''
            self.ax5.plot(moving_load_x, influence_line, linewidth=2)
            self.ax5.fill_between(
                moving_load_x, influence_line, alpha=0.20, color='b')
            self.graph_widget4.canvas4.draw()

            '''
            Horizontal line (x)
            '''
            self.ax5.plot(
                [moving_load_x[0], moving_load_x[-1]*1.05], [0, 0], c='k')
            self.ax5.annotate('x', xy=(moving_load_x[-1]*1.05, 0),
                              xycoords='data',
                              ha='left', va='center',
                              zorder=10, size='12')
            self.graph_widget4.canvas4.draw()

            '''
            Vertical line (F)
            '''
            max_force = (max(max(influence_line), -min(influence_line)))*1.2
            self.ax5.plot([self.starting_X, self.starting_X],
                          [-max_force, max_force], c='k')
            self.ax5.annotate('F', xy=(self.starting_X, max_force),
                              xycoords='data',
                              ha='center', va='bottom',
                              zorder=10, size='12')
            self.graph_widget4.canvas4.draw()

        except:
            pass


    def closeEvent(self):
        try:
            if self.demo and self.report:
                os.remove(self.filename[0])
                os.remove(self.pdfname)
        except:
            pass
        # figs = list(map(plt.figure, plt.get_fignums()))
        # print(figs)
        # print(f'Total figures remaining : {len(figs)}')

        plt.close('all')


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')

#     #window = MainPage(open=True, filename=(filepath,""))
#     window = MainPage(open=True)
#     window.show()

#     sys.exit(app.exec_())
