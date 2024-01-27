#include "university.hh"
#include <iostream>
#include <algorithm>

University::University(const std::string& email_suffix):
    running_number_(111111), email_suffix_(email_suffix)
{
}

University::~University()
{
    for ( auto course : courses_ )
    {
        delete course.second;
    }

    for ( auto account : accounts_ )
    {
        delete account.second;
    }
}

void University::new_course(Params params)
{
    std::string code = params.at(0);
    std::string name = params.at(1);
    if ( courses_.find(code) != courses_.end() )
    {
        std::cout << ALREADY_EXISTS << std::endl;
        return;
    }
    else
    {
        std::cout << NEW_COURSE << std::endl;
    }

    Course* n_course = new Course(code, name);
    courses_.insert({n_course->get_code(), n_course});
}

void University::print_courses(Params)
{
    for ( auto course : courses_ )
    {
        course.second->print_info(true);
    }
}

void University::print_course(Params params)
{
    std::string code = params.at(0);
    if ( courses_.find(code) == courses_.end() )
    {
        std::cout << CANT_FIND << code << std::endl;
        return;
    }

    courses_.at(code)->print_long_info();
}

void University::new_account(Params params)
{
    std::string full_name = params.at(0);
    int num = 0;
    for ( std::map<int, Account*>::iterator iter = accounts_.begin();
          iter != accounts_.end();
          ++iter )
    {
        if ( iter->second->get_full_name() == full_name )
        {
            std::string email = iter->second->get_email();
            num = Utils::numeric_part(email);
            if(num == 0)
            {
                ++num;
            }
            ++num;
        }
    }

    int account_number = running_number_++;
    Account* n_account = new Account(full_name, account_number, num,
                                     email_suffix_);
    accounts_.insert({account_number, n_account});
    std::cout << NEW_ACCOUNT << std::endl;
    n_account->print();
}

void University::print_accounts(Params)
{
    for ( auto account : accounts_ )
    {
        account.second->print();
    }
}

void University::print_account(Params params)
{
    int account = std::stoi(params.at(0));
    std::map<int, Account*>::iterator iter = accounts_.find(account);
    if ( iter == accounts_.end() )
    {
        std::cout << CANT_FIND << account << std::endl;
        return;
    }
    iter->second->print();
}

void University::add_staff(Params params)
{
    std::string code = params.at(0);
    int account = std::stoi(params.at(1));
    if ( courses_.find(code) == courses_.end() )
    {
        std::cout << CANT_FIND << code << std::endl;
        return;
    }
    if ( accounts_.find(account) == accounts_.end() )
    {
        std::cout << CANT_FIND << account << std::endl;
        return;
    }

    courses_.at(code)->add_staff(accounts_.at(account));
}


void University::sign_up(Params params)
{
    std::string course_code = params.at(0);

    int account_number = std::stoi(params.at(1));

    std::map<int, Account*>::iterator iter_a = accounts_.find(account_number);
    std::map<std::string, Course*>::iterator iter_c = courses_.find(course_code);


    if (iter_c == courses_.end()) {
        std::cout << CANT_FIND << course_code << std::endl;
        return;
    }

    if (iter_a == accounts_.end()) {
        std::cout << CANT_FIND << account_number << std::endl;
        return;
    }


    Account* account_ptr = iter_a->second;

    if (account_ptr->is_graduated()){
        std::cout << ALREADY_GRADUATED << std::endl;
        return;
    }

    std::vector<std::string> signed_courses = account_ptr->get_current_courses();

        if (std::find(signed_courses.begin(), signed_courses.end(),
                      course_code) != signed_courses.end())
        {
            std::cout << ALREADY_SIGNED_UP << std::endl;
            return;
        }

    std::vector<std::string> completed_courses = account_ptr->get_completed_courses();

        if (std::find(completed_courses.begin(), completed_courses.end(),
                      course_code) != completed_courses.end())
        {
            std::cout << ALREADY_COMPLETED << std::endl;
            return;
        }


    Course* course_ptr = iter_c->second;

    course_ptr->sign_up(account_number);
    account_ptr->sign_up(course_code);
    std::cout << SIGNED_UP << std::endl;
}

void University::complete(Params params)
{
    std::string course_code = params.at(0);
    int account_number = std::stoi(params.at(1));

    std::map<int, Account*>::iterator iter_a = accounts_.find(account_number);
    std::map<std::string, Course*>::iterator iter_c = courses_.find(course_code);

    if (iter_c == courses_.end()) {
        std::cout << CANT_FIND << course_code << std::endl;
        return;
    }

    if (iter_a == accounts_.end()) {
        std::cout << CANT_FIND << account_number << std::endl;
        return;
    }


    Account* account_ptr = iter_a->second;

    // check if the account has signed up for the course
    std::vector<std::string> signed_courses = account_ptr->get_current_courses();
    if (std::find(signed_courses.begin(), signed_courses.end(),
                  course_code) == signed_courses.end())
    {
        std::cout << NOT_SIGNED_UP << std::endl;
        return;
    }

    // check if the account has already completed the course
    std::vector<std::string> completed_courses = account_ptr->get_completed_courses();
    if (std::find(completed_courses.begin(), completed_courses.end(),
                  course_code) != completed_courses.end())
    {
        std::cout << ALREADY_COMPLETED << std::endl;
        return;
    }

    // mark the course as completed for the account
    account_ptr->complete(course_code);

    std::cout << COMPLETED << std::endl;
}

void University::print_signups(Params params)
{
    std::string course_code = params.at(0);
    std::map<std::string, Course*>::iterator iter_c = courses_.find(course_code);

    if (iter_c == courses_.end()) {
        std::cout << CANT_FIND << course_code << std::endl;
        return;
    }

    Course* course_ptr = iter_c->second;
    std::vector<int> signed_accounts = course_ptr->get_sign_ups();
    for (auto account : signed_accounts) {
        std::map<int, Account*>::iterator iter_a = accounts_.find(account);
        Account* account_ptr = iter_a->second;
        account_ptr->print();
        }

}
void University::print_completed(Params params)
{
    int account_number = std::stoi(params.at(0));
    std::map<int, Account*>::iterator iter = accounts_.find(account_number);

    if (iter == accounts_.end()) {
        std::cout << CANT_FIND << account_number << std::endl;
        return;
    }

    Account* account_ptr = iter->second;

    std::vector<std::string> completed_courses = account_ptr->get_completed_courses();
    for (const auto& course_code : completed_courses) {
        std::cout << course_code << " : " <<
                     courses_.at(course_code)->get_name() << std::endl;
    }

    int total = 0;
    for (const auto& course_code : completed_courses) {
        int cred = courses_.at(course_code)->get_credits();
        total += cred;
    }
    std::cout << "Total credits: " << total << std::endl;

}

void University::print_study_state(Params params)
{
    int account_number = std::stoi(params.at(0));
    std::map<int, Account*>::iterator iter = accounts_.find(account_number);
    Account* account_ptr = iter->second;

    if (iter == accounts_.end()) {
        std::cout << CANT_FIND << account_number << std::endl;
        return;
    }

    std::cout << "Current:" << std::endl;
    std::vector<std::string> signed_courses = account_ptr->get_current_courses();
    for (const auto& course_code : signed_courses) {
        std::cout << course_code << " : " <<
                     courses_.find(course_code)->second->get_name() << std::endl;
    }
    std::cout << "Completed:" << std::endl;
    std::vector<std::string> completed_courses = account_ptr->get_completed_courses();
    for (const auto& course_code : completed_courses) {
        std::cout << course_code << " : " <<
                     courses_.find(course_code)->second->get_name() << std::endl;
    }

    int total = 0;
    for (const auto& course_code : completed_courses) {
        int cred = courses_.find(course_code)->second->get_credits();
        total += cred;
    }
    std::cout << "Total credits: " << total << std::endl;

}

void University::graduate(Params params)
{
    int account_number = std::stoi(params.at(0));
    std::map<int, Account*>::iterator iter = accounts_.find(account_number);

    if (iter == accounts_.end()) {
        std::cout << CANT_FIND << account_number << std::endl;
        return;
    }

    Account* account_ptr = iter->second;

    account_ptr->graduate();

    std::cout << "Graduated, all courses completed." << std::endl;
}
