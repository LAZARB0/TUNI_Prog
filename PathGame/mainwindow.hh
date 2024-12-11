#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include "gameboard.hh"
#include <QMainWindow>
#include <QMainWindow>
#include <QtWidgets>
#include <vector>

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

    // Käsittelee jokaisen pelilaudan napin toimintaa.
    // Metodi saa parametrinä napin sijainnin, jota
    // käyttää sisäisen pelilaudan sekä käyttöliittymän
    // pelilaudan päivittämiseen
    void handle_button_click(unsigned int row, unsigned int column);

    // Resetoi pelin alustamalla pelilaudan sekä laskurit
    // ja niihin liittyvät näytöt
    void reset_game();

    // Päivittää käyttöliittymän ajastimen sekä pisteet
    // perustuu QTimer muuttujaan, jonka toiminnan myötä
    // päivittyy joka sekunti
    void updateLcdNumber();

    // Pelin automaattisen animoimisen metodi. Käyttäjän
    // painettua animateButtonia, tämä metodi käyttää
    // mm. automated_move metodia pelin animoimiseen.
    void animate_game();

    // Halutun nappulan löytämiseen käytetty metodi
    // Metodi löytää halutuilla parametreillä kyseisessä
    // sijainnisssa olevan nappulan.
    QPushButton* find_button(QWidget* parent, int desiredRow, int desiredColumn);

    // Automaattinen siirto, jota käytetään pelin animoimiseen.
    // metodi saa parametrina sekä alkuperäisen että kohteen
    // sijainnin koordinaatit.
    void automated_move(int b_1_r, int b_1_c, int b_2_r, int b_2_c);

    // Asettaa kaikki pelilaudan nappulat pois käytettävistä.
    // Käytetään pelin animoimiseen, jotta pelaaja ei voi sekoittaa
    // lautaa ja peliä animoimisen aikana
    void disable_buttons();

    // Asettaa kaikki pelilaudan nappulan käytettäviksi.
    // käytetään reset napin yhteydessä, jotta animoimisen
    // jälkeen nappulat saadaan jälleen käyttöön.
    void enable_buttons();

    // Laskee pisteet käyttäjälle pisteet muuttujaan points.
    void count_points();

private:

    Ui::MainWindow *ui;
    GameBoard* gameBoard_;

    QPushButton *lastClickedButton_;
    QColor *last_color;

    QTimer *timer_;
    QTimer *timer_auto;

    QLCDNumber *timeUsed_;
    QLCDNumber *moveCount_;
    QLCDNumber *points_;
    QLabel *label;
    QTextBrowser *textBrowser_;

    int elapsedSeconds = 0;
    int counter = 0;
    bool game_over = false;
    int points = 9999;
    long long unsigned int counter_auto = 0;

    std::vector<std::vector<int>> params;
};
#endif // MAINWINDOW_HH
