#include "mainwindow.hh"
#include "ui_mainwindow.h"

#include <fstream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_fileLineEdit_editingFinished()
{
    text_file = ui->fileLineEdit->text();
}

void MainWindow::on_keyLineEdit_editingFinished()
{
    text_key = ui->keyLineEdit->text();
}


void MainWindow::on_findPushButton_clicked()
{
    QString status = "";
    std::ifstream file(qPrintable(text_file));
    if (!file) {
        status = "File not found";
        ui->textBrowser->setText(status);
        return;
    }

    if (text_key.isEmpty()) {
        status = "File found";
        ui->textBrowser->setText(status);
        return;
    }

    QString to_find;

    if (ui->matchCheckBox->isChecked()) {
        to_find = text_key.toLower();
    } else {
        to_find = text_key;
    }

    std::string line;
    bool found = false;
    while (std::getline(file, line)) {
        QString qLine = QString::fromStdString(line);
        if (ui->matchCheckBox->isChecked()) {
            qLine = qLine.toLower();
        }
        if (qLine.contains(to_find, Qt::CaseSensitive)) {
            found = true;
            break;
        }
    }

    file.close();

    if (found) {
        status = "Word found";
    } else {
        status = "Word not found";
    }

    ui->textBrowser->setText(status);
}

