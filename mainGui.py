# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(988, 706)
        mainWindow.setStyleSheet("*:disabled {\n"
"    background-color:rgb(30, 30, 30);    \n"
"    color: rgb(127, 127, 127);\n"
"}\n"
"*{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"QLabel:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox{\n"
"    border: 1px solid rgb(70, 70, 70);\n"
"    margin-top: 1em;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QGroupBox:disabled {\n"
"    background-color: rgb(90, 90, 90);\n"
"}\n"
"QGroupBox::title {\n"
"    background-color: rgb(90, 90, 90);\n"
"        top: -0.8em;\n"
"        left: 1em;\n"
"}\n"
"QMenu::item{\n"
"    background-color: rgb(90, 90, 90);\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    color: cyan;\n"
"}\n"
"QMenu::item:selected {\n"
"    color: cyan;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.word_1 = QtWidgets.QHBoxLayout()
        self.word_1.setObjectName("word_1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_1.addItem(spacerItem)
        self.label_0_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_0_0.setFont(font)
        self.label_0_0.setObjectName("label_0_0")
        self.word_1.addWidget(self.label_0_0)
        self.label_0_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_0_1.setFont(font)
        self.label_0_1.setObjectName("label_0_1")
        self.word_1.addWidget(self.label_0_1)
        self.label_0_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_0_2.setFont(font)
        self.label_0_2.setObjectName("label_0_2")
        self.word_1.addWidget(self.label_0_2)
        self.label_0_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_0_3.setFont(font)
        self.label_0_3.setObjectName("label_0_3")
        self.word_1.addWidget(self.label_0_3)
        self.label_0_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_0_4.setFont(font)
        self.label_0_4.setObjectName("label_0_4")
        self.word_1.addWidget(self.label_0_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_1.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.word_1)
        self.word_2 = QtWidgets.QHBoxLayout()
        self.word_2.setObjectName("word_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_2.addItem(spacerItem2)
        self.label_1_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_1_0.setFont(font)
        self.label_1_0.setObjectName("label_1_0")
        self.word_2.addWidget(self.label_1_0)
        self.label_1_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_1_1.setFont(font)
        self.label_1_1.setObjectName("label_1_1")
        self.word_2.addWidget(self.label_1_1)
        self.label_1_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_1_2.setFont(font)
        self.label_1_2.setObjectName("label_1_2")
        self.word_2.addWidget(self.label_1_2)
        self.label_1_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_1_3.setFont(font)
        self.label_1_3.setObjectName("label_1_3")
        self.word_2.addWidget(self.label_1_3)
        self.label_1_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_1_4.setFont(font)
        self.label_1_4.setObjectName("label_1_4")
        self.word_2.addWidget(self.label_1_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.word_2)
        self.word_3 = QtWidgets.QHBoxLayout()
        self.word_3.setObjectName("word_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_3.addItem(spacerItem4)
        self.label_2_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_2_0.setFont(font)
        self.label_2_0.setObjectName("label_2_0")
        self.word_3.addWidget(self.label_2_0)
        self.label_2_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_2_1.setFont(font)
        self.label_2_1.setObjectName("label_2_1")
        self.word_3.addWidget(self.label_2_1)
        self.label_2_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_2_2.setFont(font)
        self.label_2_2.setObjectName("label_2_2")
        self.word_3.addWidget(self.label_2_2)
        self.label_2_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_2_3.setFont(font)
        self.label_2_3.setObjectName("label_2_3")
        self.word_3.addWidget(self.label_2_3)
        self.label_2_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_2_4.setFont(font)
        self.label_2_4.setObjectName("label_2_4")
        self.word_3.addWidget(self.label_2_4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.word_3)
        self.word_4 = QtWidgets.QHBoxLayout()
        self.word_4.setObjectName("word_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_4.addItem(spacerItem6)
        self.label_3_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_3_0.setFont(font)
        self.label_3_0.setObjectName("label_3_0")
        self.word_4.addWidget(self.label_3_0)
        self.label_3_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_3_1.setFont(font)
        self.label_3_1.setObjectName("label_3_1")
        self.word_4.addWidget(self.label_3_1)
        self.label_3_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_3_2.setFont(font)
        self.label_3_2.setObjectName("label_3_2")
        self.word_4.addWidget(self.label_3_2)
        self.label_3_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_3_3.setFont(font)
        self.label_3_3.setObjectName("label_3_3")
        self.word_4.addWidget(self.label_3_3)
        self.label_3_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_3_4.setFont(font)
        self.label_3_4.setObjectName("label_3_4")
        self.word_4.addWidget(self.label_3_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_4.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.word_4)
        self.word_5 = QtWidgets.QHBoxLayout()
        self.word_5.setObjectName("word_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_5.addItem(spacerItem8)
        self.label_4_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_4_0.setFont(font)
        self.label_4_0.setObjectName("label_4_0")
        self.word_5.addWidget(self.label_4_0)
        self.label_4_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_4_1.setFont(font)
        self.label_4_1.setObjectName("label_4_1")
        self.word_5.addWidget(self.label_4_1)
        self.label_4_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_4_2.setFont(font)
        self.label_4_2.setObjectName("label_4_2")
        self.word_5.addWidget(self.label_4_2)
        self.label_4_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_4_3.setFont(font)
        self.label_4_3.setObjectName("label_4_3")
        self.word_5.addWidget(self.label_4_3)
        self.label_4_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_4_4.setFont(font)
        self.label_4_4.setObjectName("label_4_4")
        self.word_5.addWidget(self.label_4_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.word_5.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.word_5)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.wod_6 = QtWidgets.QHBoxLayout()
        self.wod_6.setObjectName("wod_6")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wod_6.addItem(spacerItem11)
        self.label_5_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_5_0.setFont(font)
        self.label_5_0.setObjectName("label_5_0")
        self.wod_6.addWidget(self.label_5_0)
        self.label_5_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_5_1.setFont(font)
        self.label_5_1.setObjectName("label_5_1")
        self.wod_6.addWidget(self.label_5_1)
        self.label_5_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_5_2.setFont(font)
        self.label_5_2.setObjectName("label_5_2")
        self.wod_6.addWidget(self.label_5_2)
        self.label_5_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_5_3.setFont(font)
        self.label_5_3.setObjectName("label_5_3")
        self.wod_6.addWidget(self.label_5_3)
        self.label_5_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label_5_4.setFont(font)
        self.label_5_4.setObjectName("label_5_4")
        self.wod_6.addWidget(self.label_5_4)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.wod_6.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.wod_6)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem17)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Q = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Q.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Q.setFont(font)
        self.pushButton_Q.setObjectName("pushButton_Q")
        self.horizontalLayout_2.addWidget(self.pushButton_Q)
        self.pushButton_W = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_W.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_W.setFont(font)
        self.pushButton_W.setObjectName("pushButton_W")
        self.horizontalLayout_2.addWidget(self.pushButton_W)
        self.pushButton_E = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_E.setFont(font)
        self.pushButton_E.setObjectName("pushButton_E")
        self.horizontalLayout_2.addWidget(self.pushButton_E)
        self.pushButton_R = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_R.setFont(font)
        self.pushButton_R.setObjectName("pushButton_R")
        self.horizontalLayout_2.addWidget(self.pushButton_R)
        self.pushButton_T = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_T.setFont(font)
        self.pushButton_T.setObjectName("pushButton_T")
        self.horizontalLayout_2.addWidget(self.pushButton_T)
        self.pushButton_Y = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Y.setFont(font)
        self.pushButton_Y.setObjectName("pushButton_Y")
        self.horizontalLayout_2.addWidget(self.pushButton_Y)
        self.pushButton_U = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_U.setFont(font)
        self.pushButton_U.setObjectName("pushButton_U")
        self.horizontalLayout_2.addWidget(self.pushButton_U)
        self.pushButton_I = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_I.setFont(font)
        self.pushButton_I.setObjectName("pushButton_I")
        self.horizontalLayout_2.addWidget(self.pushButton_I)
        self.pushButton_O = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_O.setFont(font)
        self.pushButton_O.setObjectName("pushButton_O")
        self.horizontalLayout_2.addWidget(self.pushButton_O)
        self.pushButton_P = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_P.setFont(font)
        self.pushButton_P.setObjectName("pushButton_P")
        self.horizontalLayout_2.addWidget(self.pushButton_P)
        self.pushButton_GG = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_GG.setFont(font)
        self.pushButton_GG.setObjectName("pushButton_GG")
        self.horizontalLayout_2.addWidget(self.pushButton_GG)
        self.pushButton_UU = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_UU.setFont(font)
        self.pushButton_UU.setObjectName("pushButton_UU")
        self.horizontalLayout_2.addWidget(self.pushButton_UU)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem18)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)
        self.pushButton_A = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_A.setFont(font)
        self.pushButton_A.setObjectName("pushButton_A")
        self.horizontalLayout_3.addWidget(self.pushButton_A)
        self.pushButton_S = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_S.setFont(font)
        self.pushButton_S.setObjectName("pushButton_S")
        self.horizontalLayout_3.addWidget(self.pushButton_S)
        self.pushButton_D = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_D.setFont(font)
        self.pushButton_D.setObjectName("pushButton_D")
        self.horizontalLayout_3.addWidget(self.pushButton_D)
        self.pushButton_F = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_F.setFont(font)
        self.pushButton_F.setObjectName("pushButton_F")
        self.horizontalLayout_3.addWidget(self.pushButton_F)
        self.pushButton_G = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_G.setFont(font)
        self.pushButton_G.setObjectName("pushButton_G")
        self.horizontalLayout_3.addWidget(self.pushButton_G)
        self.pushButton_H = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_H.setFont(font)
        self.pushButton_H.setObjectName("pushButton_H")
        self.horizontalLayout_3.addWidget(self.pushButton_H)
        self.pushButton_J = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_J.setFont(font)
        self.pushButton_J.setObjectName("pushButton_J")
        self.horizontalLayout_3.addWidget(self.pushButton_J)
        self.pushButton_K = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_K.setFont(font)
        self.pushButton_K.setObjectName("pushButton_K")
        self.horizontalLayout_3.addWidget(self.pushButton_K)
        self.pushButton_L = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_L.setFont(font)
        self.pushButton_L.setObjectName("pushButton_L")
        self.horizontalLayout_3.addWidget(self.pushButton_L)
        self.pushButton_SS = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_SS.setFont(font)
        self.pushButton_SS.setObjectName("pushButton_SS")
        self.horizontalLayout_3.addWidget(self.pushButton_SS)
        self.pushButton_II = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_II.setFont(font)
        self.pushButton_II.setObjectName("pushButton_II")
        self.horizontalLayout_3.addWidget(self.pushButton_II)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem23)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem24)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem25)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_6.addWidget(self.pushButton_24)
        self.pushButton_Z = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Z.setFont(font)
        self.pushButton_Z.setObjectName("pushButton_Z")
        self.horizontalLayout_6.addWidget(self.pushButton_Z)
        self.pushButton_X = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_X.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_X.setFont(font)
        self.pushButton_X.setObjectName("pushButton_X")
        self.horizontalLayout_6.addWidget(self.pushButton_X)
        self.pushButton_C = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setObjectName("pushButton_C")
        self.horizontalLayout_6.addWidget(self.pushButton_C)
        self.pushButton_V = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_V.setFont(font)
        self.pushButton_V.setObjectName("pushButton_V")
        self.horizontalLayout_6.addWidget(self.pushButton_V)
        self.pushButton_B = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_B.setFont(font)
        self.pushButton_B.setObjectName("pushButton_B")
        self.horizontalLayout_6.addWidget(self.pushButton_B)
        self.pushButton_N = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_N.setFont(font)
        self.pushButton_N.setObjectName("pushButton_N")
        self.horizontalLayout_6.addWidget(self.pushButton_N)
        self.pushButton_M = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_M.setFont(font)
        self.pushButton_M.setObjectName("pushButton_M")
        self.horizontalLayout_6.addWidget(self.pushButton_M)
        self.pushButton_OO = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_OO.setFont(font)
        self.pushButton_OO.setObjectName("pushButton_OO")
        self.horizontalLayout_6.addWidget(self.pushButton_OO)
        self.pushButton_CC = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_CC.setFont(font)
        self.pushButton_CC.setObjectName("pushButton_CC")
        self.horizontalLayout_6.addWidget(self.pushButton_CC)
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setObjectName("pushButton_58")
        self.horizontalLayout_6.addWidget(self.pushButton_58)
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setObjectName("pushButton_59")
        self.horizontalLayout_6.addWidget(self.pushButton_59)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem26)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(mainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSee_online_help = QtWidgets.QAction(mainWindow)
        self.actionSee_online_help.setObjectName("actionSee_online_help")
        self.actionSee_offline_help = QtWidgets.QAction(mainWindow)
        self.actionSee_offline_help.setObjectName("actionSee_offline_help")

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Sonsuz Wordle Türkçe"))
        self.label_0_0.setText(_translate("mainWindow", "_"))
        self.label_0_1.setText(_translate("mainWindow", "_"))
        self.label_0_2.setText(_translate("mainWindow", "_"))
        self.label_0_3.setText(_translate("mainWindow", "_"))
        self.label_0_4.setText(_translate("mainWindow", "_"))
        self.label_1_0.setText(_translate("mainWindow", "_"))
        self.label_1_1.setText(_translate("mainWindow", "_"))
        self.label_1_2.setText(_translate("mainWindow", "_"))
        self.label_1_3.setText(_translate("mainWindow", "_"))
        self.label_1_4.setText(_translate("mainWindow", "_"))
        self.label_2_0.setText(_translate("mainWindow", "_"))
        self.label_2_1.setText(_translate("mainWindow", "_"))
        self.label_2_2.setText(_translate("mainWindow", "_"))
        self.label_2_3.setText(_translate("mainWindow", "_"))
        self.label_2_4.setText(_translate("mainWindow", "_"))
        self.label_3_0.setText(_translate("mainWindow", "_"))
        self.label_3_1.setText(_translate("mainWindow", "_"))
        self.label_3_2.setText(_translate("mainWindow", "_"))
        self.label_3_3.setText(_translate("mainWindow", "_"))
        self.label_3_4.setText(_translate("mainWindow", "_"))
        self.label_4_0.setText(_translate("mainWindow", "_"))
        self.label_4_1.setText(_translate("mainWindow", "_"))
        self.label_4_2.setText(_translate("mainWindow", "_"))
        self.label_4_3.setText(_translate("mainWindow", "_"))
        self.label_4_4.setText(_translate("mainWindow", "_"))
        self.label_5_0.setText(_translate("mainWindow", "_"))
        self.label_5_1.setText(_translate("mainWindow", "_"))
        self.label_5_2.setText(_translate("mainWindow", "_"))
        self.label_5_3.setText(_translate("mainWindow", "_"))
        self.label_5_4.setText(_translate("mainWindow", "_"))
        self.pushButton_Q.setText(_translate("mainWindow", "Q"))
        self.pushButton_W.setText(_translate("mainWindow", "W"))
        self.pushButton_E.setText(_translate("mainWindow", "E"))
        self.pushButton_R.setText(_translate("mainWindow", "R"))
        self.pushButton_T.setText(_translate("mainWindow", "T"))
        self.pushButton_Y.setText(_translate("mainWindow", "Y"))
        self.pushButton_U.setText(_translate("mainWindow", "U"))
        self.pushButton_I.setText(_translate("mainWindow", "I"))
        self.pushButton_O.setText(_translate("mainWindow", "O"))
        self.pushButton_P.setText(_translate("mainWindow", "P"))
        self.pushButton_GG.setText(_translate("mainWindow", "Ğ"))
        self.pushButton_UU.setText(_translate("mainWindow", "Ü"))
        self.pushButton_A.setText(_translate("mainWindow", "A"))
        self.pushButton_S.setText(_translate("mainWindow", "S"))
        self.pushButton_D.setText(_translate("mainWindow", "D"))
        self.pushButton_F.setText(_translate("mainWindow", "F"))
        self.pushButton_G.setText(_translate("mainWindow", "G"))
        self.pushButton_H.setText(_translate("mainWindow", "H"))
        self.pushButton_J.setText(_translate("mainWindow", "J"))
        self.pushButton_K.setText(_translate("mainWindow", "K"))
        self.pushButton_L.setText(_translate("mainWindow", "L"))
        self.pushButton_SS.setText(_translate("mainWindow", "Ş"))
        self.pushButton_II.setText(_translate("mainWindow", "İ"))
        self.pushButton_24.setText(_translate("mainWindow", " "))
        self.pushButton_Z.setText(_translate("mainWindow", "Z"))
        self.pushButton_X.setText(_translate("mainWindow", "X"))
        self.pushButton_C.setText(_translate("mainWindow", "C"))
        self.pushButton_V.setText(_translate("mainWindow", "V"))
        self.pushButton_B.setText(_translate("mainWindow", "B"))
        self.pushButton_N.setText(_translate("mainWindow", "N"))
        self.pushButton_M.setText(_translate("mainWindow", "M"))
        self.pushButton_OO.setText(_translate("mainWindow", "Ö"))
        self.pushButton_CC.setText(_translate("mainWindow", "Ç"))
        self.pushButton_58.setText(_translate("mainWindow", " "))
        self.pushButton_59.setText(_translate("mainWindow", " "))
        self.actionSettings.setText(_translate("mainWindow", "App settings"))
        self.actionSee_online_help.setText(_translate("mainWindow", "See online help"))
        self.actionSee_offline_help.setText(_translate("mainWindow", "See offline help"))
