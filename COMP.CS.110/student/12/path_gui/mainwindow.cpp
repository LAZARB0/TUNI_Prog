/* Polku-peli
 *
 * Kuvaus:
 *
 * Ohjeman käynnistyessä aukeaa käyttöliittymä, joka
 * sisältää pelilaudan sekä toiminto nappuloita.
 * Pelaaja voi aloittaa pelin pelaamisen ilman
 * alkutoimintoja ja suorittaa toimintoja pelilaudan
 * viereisistä oheinapeista. Ohjelma tarkastaa siirrot
 * ja toiminnot ja jokaisen siirron jälkeen käyttöliittymä
 * päivittyy.
 *
 * Peli perustuu Gameboard pohjakoodiin, joka löytyy
 * ohjelmasta luokkana gameBoard_. Käyttöliittymä on
 * rakennettu pohjakoodin ympärille ja näyttää mitä
 * pohjakoodin pelissä tapahtuu ja antaa käyttäjän
 * ohjata tapahtumia.
 *
 * Pelin ohjeet sekä lisätietoa löytyy tiedostosta:
 * instructions.txt
 *
 * Ohjelman kirjoittaja
 * Nimi: Lassi Cederlöf
 * Opiskelijanumero: 150351065
 * Käyttäjätunnus: tklace
 * E-Mail: lassi.cederlof@tuni.fi
 *
 * */

#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include "gameboard.hh"
#include <QtWidgets>
#include <QDebug>
#include <iostream>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

        QGridLayout *layout = new QGridLayout(ui->centralwidget);

        gameBoard_ = new GameBoard();

        layout->setSpacing(10);


        // Pelinappulan luonti jokaiselle laytoutin ruudulle.

        for (unsigned int i = 0; i < ROWS; ++i) {
            for (unsigned int j = 0; j < COLUMS; ++j) {
                QPushButton *button = new QPushButton(this);
                button->setEnabled(true);
                button->setSizePolicy
                        (QSizePolicy::Expanding, QSizePolicy::Expanding);
                button->setStyleSheet
                        ("background-color: white; border: 1px solid black");
                button->setProperty("row", i);
                button->setProperty("column", j);
                layout->addWidget(button, i, j);
                connect(button, &QPushButton::clicked, this, [&, i, j]() {
                    handle_button_click(i, j);
                });
                switch (gameBoard_->which_slot(Point(j, i))) {
                    case GREEN:
                        button->setStyleSheet("background-color: green;");
                        break;
                    case RED:
                        button->setStyleSheet("background-color: red;");
                        break;
                    case EMPTY:
                        button->setStyleSheet("background-color: white;");
                        break;
                    case UNUSED:
                        button->setStyleSheet("background-color: gray;");
                        button->setEnabled(false);
                        break;
                }
            }
        }

        this->centralWidget()->setLayout(layout);


        // Close napin alustus

        QPushButton* closeButton = new QPushButton("Close", this);
        closeButton->setFixedSize(100, 100);
        layout->addWidget(closeButton, 4, COLUMS+1);
        connect(closeButton, &QPushButton::clicked,
                this, &QWidget::close);


        // Reset napin alustus ja ominaisuuksien luonti

        QPushButton* resetButton = new QPushButton("Reset", this);
        resetButton->setFixedSize(100, 100);
        layout->addWidget(resetButton, 0, COLUMS+1);
        connect(resetButton, &QPushButton::clicked,
                this, &MainWindow::reset_game);


        // Animate napin alustus ja ominaisuuksien luonti

        QPushButton* animateButton = new QPushButton("Animate", this);
        animateButton->setFixedSize(50, 100);
        layout->addWidget(animateButton, 0, COLUMS);
        connect(animateButton, &QPushButton::clicked,
                this, &MainWindow::reset_game);
        connect(animateButton, &QPushButton::clicked,
                this, &MainWindow::animate_game);


        // Ajastimen näytön sekä aika iconin alustus

        QPushButton* timeButton = new QPushButton();
        timeButton->setEnabled(false);
        timeButton->setFixedSize(50, 50);
        QPixmap image(":/icons/timer.jpg");
        image = image.scaled(100, 100);
        layout->addWidget(timeButton, 1, COLUMS);
        timeButton->setIcon(image);
        timeUsed_ = new QLCDNumber(this);
        timeUsed_->setSegmentStyle(QLCDNumber::Filled);
        timeUsed_->display("0");
        timeUsed_->setFixedSize(100, 50);
        layout->addWidget(timeUsed_, 1, COLUMS+1);


        // Siirtojen näytön sekä siirto iconin alustus

        QPushButton* movesButton = new QPushButton();
        movesButton->setEnabled(false);
        movesButton->setFixedSize(50, 50);
        QPixmap image1(":/icons/move_39551.png");
        image1 = image1.scaled(100, 100);
        layout->addWidget(movesButton, 2, COLUMS);
        movesButton->setIcon(image1);
        moveCount_ = new QLCDNumber(this);
        moveCount_->setSegmentStyle(QLCDNumber::Filled);
        moveCount_->display("0");
        moveCount_->setFixedSize(100, 50);
        layout->addWidget(moveCount_, 2, COLUMS+1);


        // Pisteiden näytön sekä piste iconin alustus

        QPushButton* pointsButton = new QPushButton();
        pointsButton->setEnabled(false);
        pointsButton->setFixedSize(50, 50);
        QPixmap image2(":/icons/icon-04.png");
        image2 = image2.scaled(100, 100);
        layout->addWidget(pointsButton, 3, COLUMS);
        pointsButton->setIcon(image2);
        points_ = new QLCDNumber(this);
        points_->setSegmentStyle(QLCDNumber::Filled);
        points_->display("0");
        points_->setFixedSize(100, 50);
        layout->addWidget(points_, 3, COLUMS+1);


        // Pelintila textBrowserin alustus sekä määritys

        label = new QLabel(this);
        label->setText("Pelintila:");
        label->setFont(QFont("Times New Roman", 14));
        layout->addWidget(label, ROWS + 1, 0, 1, COLUMS + 2);
        textBrowser_ = new QTextBrowser(this);
        textBrowser_->setFixedSize(200, 25);
        layout->addWidget(textBrowser_, ROWS + 1, 1, 1, COLUMS + 2);


        // Muiden muuttujien sekä ajastimien alustus ja määritys

        lastClickedButton_ = nullptr;

        timer_ = new QTimer(this);
        connect(timer_, &QTimer::timeout, this, &MainWindow::updateLcdNumber);

        timer_auto = new QTimer(this);
        connect(timer_auto, &QTimer::timeout, this, &MainWindow::animate_game);

        params = {{0, 1, 2, 2}, {4, 1, 0, 1}, {4, 0, 1, 1}, {2, 2, 4, 0},
                  {1, 1, 4, 1}, {0, 1, 2, 2}, {0, 0, 3, 1}, {2, 2, 0, 0},
                  {3, 1, 2, 2}, {4, 1, 0, 1}, {4, 2, 1, 1}, {4, 3, 2, 1},
                  {4, 0, 4, 3}, {2, 1, 4, 0}, {2, 2, 4, 2}, {1, 1, 4, 1},
                  {0, 1, 3, 1}, {0, 2, 2, 2}, {0, 3, 2, 1}, {0, 0, 0, 3},
                  {2, 1, 0, 0}, {3, 1, 0, 2}, {4, 1, 0, 1}, {4, 0, 1, 1},
                  {2, 2, 4, 0}, {1, 1, 4, 1}, {0, 1, 3, 1}, {0, 0, 2, 2},
                  {3, 1, 0, 0}, {4, 1, 0, 1}, {2, 2, 4, 1}};
}


MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::handle_button_click(unsigned int row, unsigned int column)
{
    QPushButton *clickedButton = qobject_cast<QPushButton*>(sender());

    if (elapsedSeconds == 0){
        timer_->start(1000);
    }

    if (lastClickedButton_ == clickedButton) {
        QString styleSheet = QString
                ("background-color: %1").arg(last_color->name());
        lastClickedButton_->setStyleSheet(styleSheet);

        textBrowser_->setText("Siirto peruttu");
        lastClickedButton_ = nullptr;
    } else {

        if (lastClickedButton_) {
            Point start(lastClickedButton_->property("column").toInt(),
                        lastClickedButton_->property("row").toInt());
            Point dest(column, row);
            if(gameBoard_->move(start, dest)) {
                lastClickedButton_->setStyleSheet
                        ("background-color: white; border: 1px solid black");
                QString styleSheet = QString
                        ("background-color: %1").arg(last_color->name());
                clickedButton->setStyleSheet(styleSheet);

                textBrowser_->setText("Onnistunut siirto!");

                counter ++;
                moveCount_->display(counter);

                if (gameBoard_->is_game_over()){
                    textBrowser_->setText("Voitit pelin!");

                    disable_buttons();

                    if (counter == 31) {
                        setStyleSheet("background-color: gold;");
                        textBrowser_->setText("Voitit pelin minimisiirroilla!");
                    }
                }
            } else {
                QString styleSheet = QString
                        ("background-color: %1").arg(last_color->name());
                lastClickedButton_->setStyleSheet(styleSheet);

                textBrowser_->setText("Mahdoton siirto");
            }

            lastClickedButton_ = nullptr;
        } else {
            lastClickedButton_ = clickedButton;
            last_color = new QColor
                    (lastClickedButton_->palette().color(QPalette::Button));
            clickedButton->setStyleSheet("background-color: yellow;");
            textBrowser_->setText("Valitse kohde");
        }
    }
}


void MainWindow::reset_game()
{
    gameBoard_->reset();

    QGridLayout* layout = qobject_cast<QGridLayout*>(centralWidget()->layout());
        for (unsigned int i = 0; i < ROWS; ++i) {
            for (unsigned int j = 0; j < COLUMS; ++j) {
                QLayoutItem* item = layout->itemAtPosition(i, j);
                QPushButton *button = qobject_cast<QPushButton*>(item->widget());
                switch (gameBoard_->which_slot(Point(j, i))) {
                    case GREEN:
                        button->setStyleSheet("background-color: green;");
                        break;
                    case RED:
                        button->setStyleSheet("background-color: red;");
                        break;
                    case EMPTY:
                        button->setStyleSheet("background-color: white;");
                        break;
                    case UNUSED:
                        button->setStyleSheet("background-color: gray;");
                        button->setEnabled(false);
                        break;
                }
            }
        }

        enable_buttons();
        timer_auto->stop();
        counter_auto = 0;
        elapsedSeconds = 0;
        counter = 0;
        timer_->stop();
        timeUsed_->display(0);
        moveCount_->display(0);
        points_->display(9999);

        lastClickedButton_ = nullptr;

        setStyleSheet("background-color: white;");

        textBrowser_->setText("Pöytä nollattu!");
}


void MainWindow::count_points()
{
    points = 9999 - elapsedSeconds * 25;
    points = points - counter * 100;
}


void MainWindow::updateLcdNumber()
{
    elapsedSeconds++;

    timeUsed_->display(elapsedSeconds);

    count_points();
    points_->display(points);
}


QPushButton* MainWindow::find_button(QWidget* parent,
                                     int desiredRow, int desiredColumn)
{
    QList<QPushButton*> buttonList = parent->findChildren<QPushButton*>();
    for (int k = 0; k < buttonList.size(); ++k) {
        QPushButton* foundButton = qobject_cast<QPushButton*>(buttonList.at(k));
        if (foundButton != nullptr &&
            foundButton->property("row") == desiredRow &&
            foundButton->property("column") == desiredColumn) {
            return foundButton;
        }
    }
    return nullptr;
}


void MainWindow::automated_move(int b_1_r, int b_1_c, int b_2_r, int b_2_c)
{
    textBrowser_->setText("Animoidaan....");

    QPushButton *button_1 = find_button(this, b_1_r, b_1_c);
    QPushButton *button_2 = find_button(this, b_2_r, b_2_c);

    Point start(button_1->property("column").toInt()
                , button_1->property("row").toInt());
    Point dest(button_2->property("column").toInt()
               , button_2->property("row").toInt());

    gameBoard_->move(start, dest);

    last_color = new QColor(button_1->palette().color(QPalette::Button));

    button_1->setStyleSheet
            ("background-color: white; border: 1px solid black");
    QString styleSheet = QString
            ("background-color: %1").arg(last_color->name());
    button_2->setStyleSheet(styleSheet);

    counter ++;
    moveCount_->display(counter);

    if (gameBoard_->is_game_over()){
        textBrowser_->setText("Animointi suoritettu!");
    }
}


void MainWindow::animate_game()
{
    disable_buttons();

    timer_auto->start(1000);
    if (counter_auto != params.size()){
        std::vector<int> current_params = params[counter_auto];
        automated_move(current_params[0],
                current_params[1], current_params[2], current_params[3]);
        counter_auto++;
    } else {
        timer_auto->stop();
        counter_auto = 0;
    }
}


void MainWindow::disable_buttons()
{
    QGridLayout* layout = qobject_cast<QGridLayout*>(centralWidget()->layout());
        for (unsigned int i = 0; i < ROWS; ++i) {
            for (unsigned int j = 0; j < COLUMS; ++j) {
                QLayoutItem* item = layout->itemAtPosition(i, j);
                QPushButton *button = qobject_cast<QPushButton*>(item->widget());
                switch (gameBoard_->which_slot(Point(j, i))) {
                    case GREEN:
                        button->setEnabled(false);
                        break;
                    case RED:
                        button->setEnabled(false);
                        break;
                    case EMPTY:
                        button->setEnabled(false);
                        break;
                    case UNUSED:
                        button->setEnabled(false);
                        break;
                }
            }
        }
}


void MainWindow::enable_buttons()
{
    QGridLayout* layout = qobject_cast<QGridLayout*>(centralWidget()->layout());
        for (unsigned int i = 0; i < ROWS; ++i) {
            for (unsigned int j = 0; j < COLUMS; ++j) {
                QLayoutItem* item = layout->itemAtPosition(i, j);
                QPushButton *button = qobject_cast<QPushButton*>(item->widget());
                switch (gameBoard_->which_slot(Point(j, i))) {
                    case GREEN:
                        button->setEnabled(true);
                        break;
                    case RED:
                        button->setEnabled(true);
                        break;
                    case EMPTY:
                        button->setEnabled(true);
                        break;
                    case UNUSED:
                        button->setEnabled(false);
                        break;
                }
            }
        }
}
