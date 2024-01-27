#include "account.hh"
#include "utils.hh"
#include "course.hh"
#include <iostream>
#include <vector>
#include <algorithm>

Account::Account(const std::string& full_name, int account_number,
                 int duplicates, const std::string& university_suffix):
    full_name_(full_name),
    last_name_(""),
    first_name_(""),
    account_number_(account_number)
{
    std::vector<std::string> name = Utils::split(full_name_, ' ');
    last_name_ = name.back();
    first_name_ = name.front();

    // Constructing e-mail address
    email_ = Utils::to_lower(first_name_);
    email_ += ".";
    if ( duplicates > 0 )
    {
        email_ += std::to_string(duplicates);
        email_ += ".";
    }
    email_ += Utils::to_lower(last_name_);
    email_ += "@";
    email_ += university_suffix;
}

Account::~Account()
{
}

void Account::print() const
{
    std::cout << account_number_ << ": "
              << first_name_ << " "
              << last_name_  << ", "
              << email_ << std::endl;
}

std::string Account::get_email() const
{
    return email_;
}

std::string Account::get_full_name() const
{
    return full_name_;
}

int Account::get_account_number() const
{
    return account_number_;
}

std::vector<std::string> Account::get_current_courses() const
{
    return current_courses_;
}

std::vector<std::string> Account::get_completed_courses() const
{
    return completed_courses_;
}

void Account::sign_up(std::string course_code)
{
    current_courses_.push_back(course_code);
}

void Account::complete(std::string course_code)
{
    completed_courses_.push_back(course_code);
    auto it = std::find(current_courses_.begin(),
                        current_courses_.end(), course_code);
    current_courses_.erase(it);
}

void Account::graduate()
{

    std::move(current_courses_.begin(), current_courses_.end(),
              std::back_inserter(completed_courses_));

    current_courses_.clear();

    graduated = true;
}

bool Account::is_graduated() const
{
    return graduated;
}
