import functions as u
import matplotlib.pyplot as plt
import numpy as np
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    significance_level = 0.05
    difference_umbral = 0.01
    save_folder = None
    column = -1
    prueba = 'ad'
    criterio = 'aic'
    files, logs = [], []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 831, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QTableView(self.verticalLayoutWidget_2)
        self.tableView.setMinimumSize(QSize(0, 0))
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        spacerItem = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setIcon(self.style().standardIcon(
                                                          getattr(QStyle, 'SP_FileDialogInfoView')))
        self.pushButton_3.setMaximumSize(QSize(20, 16777215))
        self.pushButton_3.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem1 = QSpacerItem(150, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setMaximumSize(QSize(20, 16777215))
        self.pushButton_2.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileLinkIcon')))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setMaximumSize(QSize(20, 16777215))
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(self.style().standardIcon(
                                                         getattr(QStyle, 'SP_DialogDiscardButton')))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listView = QListView(self.verticalLayoutWidget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setMaximumSize(QSize(200, 16777215))
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.listView_2 = QListView(self.verticalLayoutWidget_2)
        self.listView_2.setMaximumSize(QSize(16777215, 180))
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout_3.addWidget(self.listView_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 858, 21))
        self.menubar.setObjectName("menubar")
        self.menuInicio = QMenu(self.menubar)
        self.menuInicio.setObjectName("menuInicio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfigurar = QAction(MainWindow)
        self.actionConfigurar.setObjectName("actionConfigurar")
        self.actionConfigurar.setIcon(self.style().standardIcon(
                                                        getattr(QStyle, 'SP_TitleBarNormalButton')))
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setIcon(self.style().standardIcon(
                                                          getattr(QStyle, 'SP_MessageBoxQuestion')))
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_DialogOkButton')))

        self.actionAdicionar_Fichero = QAction(MainWindow)
        self.actionAdicionar_Fichero.setIcon(self.style().standardIcon(
                                                                getattr(QStyle, 'SP_FileLinkIcon')))
        self.actionAdicionar_Fichero.setObjectName("actionAdicionar_Fichero")

        self.actionGenerar_datos = QAction(MainWindow)
        self.actionGenerar_datos.setIcon(self.style().standardIcon(
                                                           getattr(QStyle, 'SP_DialogApplyButton')))
        self.actionGenerar_datos.setObjectName("actionGenerar_datos")
        self.menuInicio.addAction(self.actionAdicionar_Fichero)
        self.menuInicio.addAction(self.actionGenerar_datos)
        self.menuInicio.addAction(self.actionConfigurar)
        self.menuInicio.addAction(self.actionAbout)
        self.menuInicio.addAction(self.actionSalir)
        self.menubar.addAction(self.menuInicio.menuAction())

        self.centralwidget.setLayout(self.verticalLayout_3)
        MainWindow.showMaximized()
        self.actionAbout.triggered.connect(self.functionAbout)
        self.actionSalir.triggered.connect(self.functionSalir)
        self.actionConfigurar.triggered.connect(self.functionConfigurar)
        self.actionAdicionar_Fichero.triggered.connect(self.functionAdicionar)
        self.pushButton_2.clicked.connect(self.functionAdicionar)
        self.pushButton_3.clicked.connect(self.functionDetails)
        self.pushButton.clicked.connect(self.functionEliminar)
        self.actionGenerar_datos.triggered.connect(self.functionGenerarDatos)
        self.listView.clicked.connect(self.onClickedRow)

        self.pushButton.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton.setToolTip('Eliminar fichero')
        self.pushButton_2.setToolTip('Adicionar ficheros')
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().hide()
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.filesModel = QStringListModel(self)
        self.logModel = QStringListModel(self)
        self.dataModel = QStandardItemModel(0, 0, self)

        # Right-click menu
        self.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listView.customContextMenuRequested.connect(self.myListWidgetContext)

        self.lbl = QLabel(self)
        self.movie = QMovie("img/loader.gif")
        self.lbl.setMovie(self.movie)
        self.verticalLayout_3.addWidget(self.lbl)
        self.movie.start()
        self.lbl.hide()

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def myListWidgetContext(self, position):
        popMenu = QMenu()
        add_action = QAction("Adicionar ficheros", self)
        add_action.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileLinkIcon')))
        popMenu.addAction(add_action)
        if self.listView.selectionModel() is not None and \
                len(self.listView.selectionModel().selectedRows()) > 0:
            info_action = QAction("Detalles", self)
            info_action.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileDialogInfoView')))
            popMenu.addAction(info_action)
            info_action.triggered.connect(self.functionDetails)

            graphic = QAction("Ver gráfica", self)
            graphic.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileDialogListView')))
            popMenu.addAction(graphic)
            graphic.triggered.connect(self.show_Grafica)

        add_action.triggered.connect(self.functionCargar)
        popMenu.exec_(self.listView.mapToGlobal(position))

    def show_Grafica(self, lbl):
        name = self.listView.selectionModel().selectedRows()[0].data()

        fdata = u.load_data(name)
        col_data, t, round = u.rows_to_columns(fdata['all'])
        data = np.array(col_data[0]).astype(np.float)
        self.lbl.show()
        plt.connect('draw_event', self.handleDialogShown)

        i, col, colors = 1, 0, ["red", "green", "blue", "yellow", "pink", "black", "orange",
                                "purple", "beige", "brown", "gray", "cyan", "magenta"]
        for points in col_data:
            plt.scatter(range(len(points)),
                        points,
                        color=colors[col],
                        label="Columna {0}".format(i))
            col = col + 1 if col < len(colors) - 1 else 0
            i += 1
        plt.gca().axes.yaxis.set_ticklabels([])
        plt.legend()
        plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Generador de datos artificiales (Statistical Density "
                                     "Oversampling)"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Detalles"))
        self.menuInicio.setTitle(_translate("MainWindow", "Menú"))
        self.actionConfigurar.setText(_translate("MainWindow", "Configurar"))
        self.actionAbout.setText(_translate("MainWindow", "Acerca de"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))

        self.actionAdicionar_Fichero.setText(_translate("MainWindow", "Adicionar ficheros"))
        self.actionGenerar_datos.setText(_translate("MainWindow", "Generar datos"))

    def functionAbout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Este sistema constituye un resultado del tema de investigación: '{0}' de los "
                    "autores:\n{1}".format("GENERACIÓN DE DATOS ARTIFICIALES EN PROBLEMAS "
                                           "DECLASIFICACIÓN CON CLASES "
                                           "NO BALANCEADAS",
                                           "- Ing. Yordan E. Estrada Rodriguez\n - Dr. Luis C "
                                           "Méndez "
                                           "González\n - Dr. Vicente García Jiménez"))
        msg.setWindowTitle("Acerca de")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def functionGenerarDatos(self):

        if self.save_folder is None:
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.DirectoryOnly)
            if dialog.exec_() == QDialog.Accepted:
                self.save_folder = dialog.selectedFiles()[0]
            else:
                return

        self.lbl.show()
        model = self.listView.model()

        for i in range(model.rowCount()):
            fdata = u.load_data(model.index(i).data())
            fixed_data, data_type, round_to = u.rows_to_columns(fdata[fdata['min']])
            generated_data = u.generateData(fixed_data, data_type, fdata, self.difference_umbral,
                                            self.prueba, self.criterio)
            result = u.save_data(self.save_folder +'/SDO_'+ os.path.basename(model.index(i).data()),
                                 generated_data,
                                 data_type,
                                 round_to,
                                 fdata['all'],
                                 fdata['min_col'])
        text = "Datos almacenados correctamente" if result else "Error al almacenar los datos"
        self.lbl.hide()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Información")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def functionSalir(self):
        quit()

    def functionCargar(self):
        self.openFileNameDialog()

    def handleDialogShown(self, x):
        self.lbl.hide()

    def functionDetails(self):
        self.lbl.show()
        name = self.listView.selectionModel().selectedRows()[0].data()
        DetailDialog.getDetail(name, self.lbl, self.prueba, self.criterio)

    def functionConfigurar(self):
        self.difference_umbral, self.significance_level, self.save_folder, self.column, \
        self.prueba, self.criterio,  ok = ConfigDialog.getConfig(
            self.significance_level, self.difference_umbral, self.save_folder, self.column,
            self.prueba, self.criterio)

    def functionAdicionar(self):
        self.openFileNameDialog()

    def functionEliminar(self):
        name = self.listView.selectionModel().selectedRows()[0].data()
        self.files.remove(name)
        self.filesModel.setStringList(self.files)
        self.listView.setModel(self.filesModel)
        if len(self.files) == 0:
            self.loadData()
            self.pushButton.setDisabled(True)
            self.pushButton_3.setDisabled(True)
        else:
            self.listView.setCurrentIndex(self.listView.model().index(len(self.files) - 1, 0))
            self.loadData(self.files[len(self.files) - 1])
        self.functionLog('Eliminado fichero: {}'.format(name))

    def functionLog(self, text):
        self.logs.append(text)
        self.logModel.setStringList(self.logs)
        self.listView_2.setModel(self.logModel)

    def onClickedRow(self, index=None):
        self.loadData(self.files[index.row()])
        self.listView.setToolTip(self.files[index.row()])
        self.pushButton.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.functionLog('Fichero seleccionado: {}'.format(self.files[index.row()]))

    def loadData(self, fileName=None):
        self.dataModel.clear()
        if fileName is not None:
            fdata = u.load_data(fileName, self.column)
            for row in fdata['all']:
                items = []
                for it in row:
                    items.append(QStandardItem(it))
                self.dataModel.appendRow(items)
            self.tableView.setModel(self.dataModel)

    def openFileNameDialog(self):
        txt_msg = ""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileNames = QFileDialog.getOpenFileNames(self, "Adicionar ficheros", "",
                                                 "Comma-Separated Files (*.csv)", options=options)[0]
        if len(fileNames) > 0:
            for j in fileNames:
                if j not in self.files:
                    self.files.append(j)
                    self.functionLog('Ficheros adicionados: {}'.format(j))
                else:
                    txt_msg += " - {0}\n".format(j)
        else:
            return

        if txt_msg != "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Los siguientes ficheros ya ha sido cargados:\n" + txt_msg)
            msg.setWindowTitle("Información")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        self.filesModel.setStringList(self.files)
        self.listView.setModel(self.filesModel)
        self.listView.setCurrentIndex(self.listView.model().index(len(self.files) - 1, 0))
        self.loadData(self.files[len(self.files) - 1])
        self.listView.setToolTip(self.files[-1])
        self.pushButton.setDisabled(False)
        self.pushButton_3.setDisabled(False)


class ConfigDialog(QDialog):
    def __init__(self, significance_level, umbral, save_f=None, col=-1, prueba='ad', criterio='aic',
                 parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.setWindowTitle('Configurar')
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.setFixedWidth(350)

        layout = QVBoxLayout(self)

        self.umbral_label = QLabel(self)
        self.umbral_label.setObjectName("label")
        self.umbral_label.setText('Umbral:')

        self.umbral = QDoubleSpinBox(self)
        self.umbral.setValue(umbral)

        # ==============Prueba a usar============================
        hboxt = QHBoxLayout()
        groupboxt = QGroupBox("Prueba a usar:", checkable=False)
        groupboxt.setLayout(hboxt)

        self.ad = QRadioButton("Ad")
        if prueba == 'ad': self.ad.setChecked(True)
        self.ad.setToolTip("Anderson-Darling")
        self.ks = QRadioButton("Ks")
        if prueba == 'ks': self.ks.setChecked(True)
        self.ks.setToolTip("Kolmogorov-Smirnov")
        self.cvm = QRadioButton("Cvm")
        if prueba == 'cvm': self.cvm.setChecked(True)
        self.cvm.setToolTip("Cramer-von-Mises")

        hboxt.addWidget(self.ad, alignment=Qt.AlignTop)
        hboxt.addWidget(self.ks, alignment=Qt.AlignTop)
        hboxt.addWidget(self.cvm, alignment=Qt.AlignTop)

        # ==============Criterio de selección =======================
        hboxc = QHBoxLayout()
        groupboxc = QGroupBox("Criterio de selección:", checkable=False)
        groupboxc.setLayout(hboxc)

        self.aic = QRadioButton("aic")
        if criterio == 'aic': self.aic.setChecked(True)
        self.aic.setToolTip("Criterio de Akaike")
        self.bic = QRadioButton("bic")
        if criterio == 'bic': self.bic.setChecked(True)
        self.bic.setToolTip("Criterio de Información Bayesiano")

        hboxc.addWidget(self.aic, alignment=Qt.AlignTop)
        hboxc.addWidget(self.bic, alignment=Qt.AlignTop)

        self.sl_label = QLabel(self)
        self.sl_label.setObjectName("label1")
        self.sl_label.setText('Nivel de significancia:')

        self.s_level = QDoubleSpinBox(self)
        self.s_level.setValue(significance_level)

        self.column_label = QLabel(self)
        self.column_label.setObjectName("label2")
        self.column_label.setText('Columna:')

        self.column = QSpinBox(self)
        self.column.setMaximum(10)
        self.column.setMinimum(-1)
        self.column.setValue(col)

        self.savef_label = QLabel(self)
        self.savef_label.setObjectName("label2")
        self.savef_label.setText('Almacenar resultados en:')

        self.holayout = QHBoxLayout(self)
        self.savef = QLineEdit(self)
        self.savef.setText(save_f)
        self.savef.setReadOnly(True)

        self.pButton = QPushButton(self)
        self.pButton.setText('...')
        self.pButton.setFixedWidth(20)
        self.pButton.clicked.connect(self.functionSaveFolder)

        self.holayout.addWidget(self.savef)
        self.holayout.addWidget(self.pButton)

        layout.addWidget(groupboxt)
        layout.addWidget(groupboxc)
        layout.addWidget(self.umbral_label)
        layout.addWidget(self.umbral)
        layout.addWidget(self.sl_label)
        layout.addWidget(self.s_level)
        layout.addWidget(self.column_label)
        layout.addWidget(self.column)
        layout.addWidget(self.savef_label)
        layout.addLayout(self.holayout)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def getPrueba(self):
        if self.cvm.isChecked(): return 'cvm'
        if self.ks.isChecked(): return 'ks'
        return 'ad'

    def getCriterio(self):
        if self.bic.isChecked(): return 'bic'
        return 'aic'

    def functionSaveFolder(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QDialog.Accepted:
            self.savef.setText(dialog.selectedFiles()[0])
            self.savef.setToolTip(dialog.selectedFiles()[0])

    def um(self):
        return self.umbral.value()

    def sl(self):
        return self.s_level.value()

    def sf(self):
        return self.savef.text()

    def col(self):
        return self.column.value()

    @staticmethod
    def getConfig(significance_level, umbral, savef, col, prueba, criterio, parent=None):
        dialog = ConfigDialog(significance_level, umbral, savef, col, prueba, criterio,  parent)
        result = dialog.exec_()
        um = dialog.um()
        sl = dialog.sl()
        sf = dialog.sf()
        col = dialog.col()
        test = dialog.getPrueba()
        crit = dialog.getCriterio()
        return um, sl, sf, col, test, crit,  result == QDialog.Accepted


class DetailDialog(QDialog):
    dialogShown = pyqtSignal()
    file = None
    difference_umbral = None
    prueba = None
    criterio = None

    def __init__(self, file=None, lbl=None, parent=None, prueba='ad', criterio='aic',
                 difference_umbral=0.01):
        super(DetailDialog, self).__init__(parent)
        self.file = file
        self.lbl_dialog = lbl
        self.difference_umbral = difference_umbral
        self.prueba = prueba
        self.criterio = criterio

        self.setWindowTitle('Detalles del fichero {}'.format(os.path.basename(file)))
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        self.resize(800, 450)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(self)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QTableView(self)
        self.tableView.setMaximumSize(QSize(16777215, 80))
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.listView = QListView(self)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        self.tableView.verticalHeader().hide()

        self.label.setText('Distribuciones por columnas de la clase minoritaria:')
        self.label_2.setText('Detalles:')

        self.dialogShown.connect(self.handleDialogShown)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.verticalLayout.addWidget(buttons)
        self.setLayout(self.verticalLayout)

    def handleDialogShown(self):
        self.process(self.file)
        self.lbl_dialog.hide()

    def showEvent(self, event):
        super(QDialog, self).showEvent(event)
        self.dialogShown.emit()

    def process(self, filename):
        fdata = u.load_data(filename)
        fixed_data, data_type, round = u.rows_to_columns(fdata[fdata['min']])
        selected_distribution = u.getDistributionInfo(fixed_data, data_type, self.difference_umbral,
                                                      self.prueba, self.criterio)

        distributionModel = QStandardItemModel(0, 0, self)
        listModel = QStringListModel(self)

        items = [QStandardItem(e['dist'][0]) for e in selected_distribution]
        distributionModel.appendRow(items)
        self.tableView.setModel(distributionModel)
        self.listView.setModel(listModel)

        lista = [
            'Fichero: {}'.format(filename),
            'Total de registros: {} '.format(len(fdata['a']) + len(fdata['b'])),
            'Total de columnas: {}'.format(len(fdata['a'][0])),
            'Prueba: {}'.format(self.prueba),
            'Criterio de selección: {}'.format(self.criterio),
            'Clase mayoritaria contiene {} elementos'.format(len(fdata[fdata['max']])),
            'Clase minoritaria contiene {} elementos'.format(len(fdata[fdata['min']])),
        ]
        listModel.setStringList(lista)

    @staticmethod
    def getDetail(file, lbl, prueba, criterio, parent=None):
        dialog = DetailDialog(file, lbl, parent, prueba, criterio)
        result = dialog.exec_()
        return result == QDialog.Accepted


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
