#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>
#include <QTimer>
#include <QLCDNumber>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    // Normally this member should be in private part of the
    // class, but due to the automated tests it must be more
    // accessible.
    QTimer* timer;

    QLCDNumber* lcdNumberSec;

    QLCDNumber* lcdNumberMin;

private slots:
    // Add your slots here

    void on_startButton_clicked();

    void on_stopButton_clicked();

    void on_resetButton_clicked();

    void updateLcdNumber();

private:
    Ui::MainWindow *ui; 

    int elapsedSeconds = 0;
    int elapsedMinutes = 0;
};

#endif // MAINWINDOW_HH
