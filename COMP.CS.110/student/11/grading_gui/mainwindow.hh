#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_spinBoxN_valueChanged(int arg1);

    void on_spinBoxG_valueChanged(int arg2);

    void on_spinBoxP_valueChanged(int arg3);

    void on_spinBoxE_valueChanged(int arg4);

    void on_calculatePushButton_clicked();

private:
    Ui::MainWindow *ui;
    int n_points = 0;
    int g_points = 0;
    int p_points = 0;
    int e_points = 0;
};
#endif // MAINWINDOW_HH
