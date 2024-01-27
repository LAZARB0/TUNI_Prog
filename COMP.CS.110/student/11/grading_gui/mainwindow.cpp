#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include "gradecalculator.hh"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    ui->spinBoxN->setMinimum(0);
    ui->spinBoxN->setMaximum(MAX_N_POINTS);

    ui->spinBoxG->setMinimum(0);
    ui->spinBoxG->setMaximum(MAX_G_POINTS);

    ui->spinBoxP->setMinimum(0);
    ui->spinBoxP->setMaximum(MAX_P_POINTS);

    ui->spinBoxE->setMinimum(0);
    ui->spinBoxE->setMaximum(5);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_spinBoxN_valueChanged(int arg1)
{
    n_points = arg1;
}


void MainWindow::on_spinBoxG_valueChanged(int arg2)
{
    g_points = arg2;
}


void MainWindow::on_spinBoxP_valueChanged(int arg3)
{
    p_points = arg3;
}


void MainWindow::on_spinBoxE_valueChanged(int arg4)
{
    e_points = arg4;
}


void MainWindow::on_calculatePushButton_clicked()
{
    QString W_score = "W-Score: " + QString::number(score_from_weekly_exercises(n_points, g_points));
    QString P_score = "P-Score: " + QString::number(score_from_projects(p_points));
    QString T_grade = "Total grade: " + QString::number(calculate_total_grade(n_points, g_points, p_points, e_points));

    QString status = W_score + "\n" + P_score + "\n" + T_grade;

    ui->textBrowser->setText(status);

}

