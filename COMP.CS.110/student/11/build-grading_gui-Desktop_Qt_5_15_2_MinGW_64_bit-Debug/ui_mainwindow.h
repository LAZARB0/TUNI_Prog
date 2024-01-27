/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.15.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QSpinBox *spinBoxN;
    QSpinBox *spinBoxG;
    QSpinBox *spinBoxP;
    QSpinBox *spinBoxE;
    QTextBrowser *textBrowser;
    QPushButton *calculatePushButton;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(388, 369);
        QPalette palette;
        QBrush brush(QColor(255, 184, 243, 255));
        brush.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Active, QPalette::Window, brush);
        QBrush brush1(QColor(240, 240, 240, 255));
        brush1.setStyle(Qt::SolidPattern);
        palette.setBrush(QPalette::Inactive, QPalette::Window, brush1);
        palette.setBrush(QPalette::Disabled, QPalette::Window, brush);
        MainWindow->setPalette(palette);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        spinBoxN = new QSpinBox(centralwidget);
        spinBoxN->setObjectName(QString::fromUtf8("spinBoxN"));
        spinBoxN->setGeometry(QRect(210, 40, 61, 25));
        spinBoxG = new QSpinBox(centralwidget);
        spinBoxG->setObjectName(QString::fromUtf8("spinBoxG"));
        spinBoxG->setGeometry(QRect(210, 70, 61, 25));
        spinBoxP = new QSpinBox(centralwidget);
        spinBoxP->setObjectName(QString::fromUtf8("spinBoxP"));
        spinBoxP->setGeometry(QRect(210, 100, 61, 25));
        spinBoxE = new QSpinBox(centralwidget);
        spinBoxE->setObjectName(QString::fromUtf8("spinBoxE"));
        spinBoxE->setGeometry(QRect(210, 130, 61, 25));
        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));
        textBrowser->setGeometry(QRect(110, 170, 211, 101));
        calculatePushButton = new QPushButton(centralwidget);
        calculatePushButton->setObjectName(QString::fromUtf8("calculatePushButton"));
        calculatePushButton->setGeometry(QRect(20, 200, 81, 24));
        label = new QLabel(centralwidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(130, 40, 49, 16));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(130, 70, 51, 16));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(130, 100, 61, 16));
        label_4 = new QLabel(centralwidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(130, 130, 71, 20));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 388, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        calculatePushButton->setText(QCoreApplication::translate("MainWindow", "Calculate", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "N points:", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "G points:", nullptr));
        label_3->setText(QCoreApplication::translate("MainWindow", "P points:", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Exam grade:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
