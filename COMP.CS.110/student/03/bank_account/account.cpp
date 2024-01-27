#include "account.hh"
#include <iostream>

Account::Account(const std::string& owner, bool has_credit):
owner_(owner), has_credit_(has_credit){

    generate_iban();
}

// Setting initial value for the static attribute running_number_
int Account::running_number_ = 0;

void Account::generate_iban()
{
    ++running_number_;
    std::string suffix = "";
    if(running_number_ < 10)
    {
        suffix.append("0");
    }
    else if(running_number_ > 99)
    {
        std::cout << "Too many accounts" << std::endl;
    }
    suffix.append(std::to_string(running_number_));

    iban_ = "FI00 1234 ";
    iban_.append(suffix);
}

int Account::take_money(int amount)
{
    if( has_credit_ == true){
        if (balance_ - amount < 0 - credit_limit_){
            std::cout << "Cannot take money: credit limit overflow" << std::endl;
            return 1;
        } else{
            balance_ -= amount;
            return 0;
        }

    } else {
        if(balance_ < amount){
            std::cout << "Cannot take money: balance underflow" << std::endl;
            return 1;
        } else{
            balance_ -= amount;
            return 0;
        }
    }
}

void Account::save_money(int amount)
{
    balance_ += amount;
}

void Account::transfer_to(class Account& other_account, int amount)
{
    if (take_money(amount) == 0){
        other_account.save_money(amount);
    } else {
        std::cout << "Transfer from " << iban_  << " failed" << std::endl;
    }
}

void Account::print() const
{
    std::cout << owner_ << " : " << iban_ << " : " << balance_ << " euros" << std::endl;
}

void Account::set_credit_limit(int value)
{
    if(has_credit_ == true){
        credit_limit_ = value;
    }
    else {
        std::cout << "Cannot set credit limit: the account has no credit card" << std::endl;
    }
}
