#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>
#include <QTextBrowser>

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
    void on_fileLineEdit_editingFinished();

    void on_keyLineEdit_editingFinished();

    void on_findPushButton_clicked();

private:
    Ui::MainWindow *ui;
    QString text_file;
    QString text_key;
    QTextBrowser* textBrowser;
};
#endif // MAINWINDOW_HH
