# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatosCliente.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegistroDatosPersonales(object):
    def setupUi(self, RegistroDatosPersonales):
        RegistroDatosPersonales.setObjectName("RegistroDatosPersonales")
        RegistroDatosPersonales.setWindowModality(QtCore.Qt.NonModal)
        RegistroDatosPersonales.resize(579, 522)
        RegistroDatosPersonales.setMinimumSize(QtCore.QSize(570, 379))
        RegistroDatosPersonales.setMaximumSize(QtCore.QSize(579, 600))
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(RegistroDatosPersonales)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(120, 210, 431, 145))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.edit_cliente = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edit_cliente.setObjectName("edit_cliente")
        self.verticalLayout_3.addWidget(self.edit_cliente)
        spacerItem = QtWidgets.QSpacerItem(40, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.edit_direccion = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edit_direccion.setObjectName("edit_direccion")
        self.verticalLayout_3.addWidget(self.edit_direccion)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_cedula = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edit_cedula.setObjectName("edit_cedula")
        self.horizontalLayout_4.addWidget(self.edit_cedula)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.edit_telefono = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.edit_telefono.setObjectName("edit_telefono")
        self.horizontalLayout_4.addWidget(self.edit_telefono)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(RegistroDatosPersonales)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 120, 521, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.text_numero_factura_datos = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.text_numero_factura_datos.setObjectName("text_numero_factura_datos")
        self.horizontalLayout_2.addWidget(self.text_numero_factura_datos)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.edit_fecha = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edit_fecha.setObjectName("edit_fecha")
        self.horizontalLayout_2.addWidget(self.edit_fecha)
        self.horizontalLayoutWidget = QtWidgets.QWidget(RegistroDatosPersonales)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 491, 84))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("recursos/logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6, QtCore.Qt.AlignHCenter)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(RegistroDatosPersonales)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(350, 460, 211, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.boton_Siguiente_Datos = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("recursos/siguiente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_Siguiente_Datos.setIcon(icon)
        self.boton_Siguiente_Datos.setIconSize(QtCore.QSize(25, 25))
        self.boton_Siguiente_Datos.setObjectName("boton_Siguiente_Datos")
        self.horizontalLayout_5.addWidget(self.boton_Siguiente_Datos)
        self.boton_Cancelar_Datos = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("recursos/cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_Cancelar_Datos.setIcon(icon1)
        self.boton_Cancelar_Datos.setIconSize(QtCore.QSize(25, 25))
        self.boton_Cancelar_Datos.setObjectName("boton_Cancelar_Datos")
        self.horizontalLayout_5.addWidget(self.boton_Cancelar_Datos)
        self.line_6 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_6.setGeometry(QtCore.QRect(10, 0, 551, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_7.setGeometry(QtCore.QRect(10, 100, 551, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_8.setGeometry(QtCore.QRect(10, 110, 551, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_9.setGeometry(QtCore.QRect(10, 150, 551, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_10.setGeometry(QtCore.QRect(10, 350, 551, 21))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_3 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 20, 241))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_4.setGeometry(QtCore.QRect(550, 120, 20, 241))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_5.setGeometry(QtCore.QRect(0, 10, 20, 101))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_11 = QtWidgets.QFrame(RegistroDatosPersonales)
        self.line_11.setGeometry(QtCore.QRect(550, 10, 20, 101))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_11 = QtWidgets.QLabel(RegistroDatosPersonales)
        self.label_11.setGeometry(QtCore.QRect(120, 380, 151, 131))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("recursos/registro copia.png"))
        self.label_11.setObjectName("label_11")
        self.text_numero_factura_datos_2 = QtWidgets.QLabel(RegistroDatosPersonales)
        self.text_numero_factura_datos_2.setGeometry(QtCore.QRect(30, 170, 301, 31))
        self.text_numero_factura_datos_2.setObjectName("text_numero_factura_datos_2")
        self.label_7 = QtWidgets.QLabel(RegistroDatosPersonales)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(RegistroDatosPersonales)
        self.label_8.setGeometry(QtCore.QRect(30, 260, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(RegistroDatosPersonales)
        self.label_9.setGeometry(QtCore.QRect(30, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(RegistroDatosPersonales)
        QtCore.QMetaObject.connectSlotsByName(RegistroDatosPersonales)

    def retranslateUi(self, RegistroDatosPersonales):
        _translate = QtCore.QCoreApplication.translate
        RegistroDatosPersonales.setWindowTitle(_translate("RegistroDatosPersonales", "Registro Datos Personales"))
        self.label_10.setText(_translate("RegistroDatosPersonales", "Teléfono/Celular"))
        self.label_3.setText(_translate("RegistroDatosPersonales", "Factura número:"))
        self.text_numero_factura_datos.setText(_translate("RegistroDatosPersonales", "0000001"))
        self.label_4.setText(_translate("RegistroDatosPersonales", "Fecha de emisión:"))
        self.edit_fecha.setToolTip(_translate("RegistroDatosPersonales", "Formato dd/mm/yy"))
        self.label_2.setText(_translate("RegistroDatosPersonales", "MODO MUEBLERÍA COMPAÑÍA LTDA"))
        self.label_5.setText(_translate("RegistroDatosPersonales", "Av. 12 de Abril y Av. Loja"))
        self.label_6.setText(_translate("RegistroDatosPersonales", "Cuenca - Ecuador"))
        self.label_12.setText(_translate("RegistroDatosPersonales", "Telf: 0991538711"))
        self.boton_Siguiente_Datos.setText(_translate("RegistroDatosPersonales", "Siguiente"))
        self.boton_Cancelar_Datos.setText(_translate("RegistroDatosPersonales", "Cancelar"))
        self.text_numero_factura_datos_2.setText(_translate("RegistroDatosPersonales", "Complete los campos de información para generar su factura.:"))
        self.label_7.setText(_translate("RegistroDatosPersonales", "Cliente:"))
        self.label_8.setText(_translate("RegistroDatosPersonales", "Dirección: "))
        self.label_9.setText(_translate("RegistroDatosPersonales", "Cédula/RUC: "))

