#include "player.hh"
#include <iostream>
#include <string>

using namespace std;

Player::Player(const string &name):
    points_(0), name_(name)
{

}

string Player::get_name() const
{
    return name_;
}

int Player::get_points() const
{
    return points_;
}

bool Player::has_won()
{
    if (points_ == 50){
        return true;
    } else {
        return false;
    }
}

void Player::add_points(int points)
{   if (points_ + points > 50){
        cout << name_ << " gets penalty points!" << endl;
        points_ = 25;
    } else {
        points_ += points;
    }

}
