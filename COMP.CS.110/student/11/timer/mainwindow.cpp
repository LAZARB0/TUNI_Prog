#include "mainwindow.hh"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    timer = new QTimer(this);
    timer->setInterval(1000);

    lcdNumberSec = ui->lcdNumberSec;
    lcdNumberMin = ui->lcdNumberMin;

    connect(timer, SIGNAL(timeout()), this, SLOT(updateLcdNumber()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_startButton_clicked()
{
    timer->start();
}

void MainWindow::on_stopButton_clicked()
{
    timer->stop();
}

void MainWindow::on_resetButton_clicked()
{
    timer->stop();
    lcdNumberSec->display(0);
    lcdNumberMin->display(0);
}

void MainWindow::updateLcdNumber()
{

    elapsedSeconds++;

    if (elapsedSeconds == 60)
    {
        elapsedMinutes++;
        elapsedSeconds = 0;
    }

    lcdNumberSec->display(elapsedSeconds);
    lcdNumberMin->display(elapsedMinutes);
}
