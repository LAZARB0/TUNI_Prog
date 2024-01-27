/* Class: Account
 * --------------
 * COMP.CS.110 Ohjelmointi 2: Rakenteet / Programming 2: Structures
 * -------------
 * Class representing a student or a staff account in the university system.
 *
 * In the project, this class should be expanded to
 * include necessary methods and attributes.
 * */
#ifndef ACCOUNT_HH
#define ACCOUNT_HH

#include <string>
#include <vector>

class Course;

const std::string NO_SIGNUPS = "No signups found on this course.";
const std::string SIGNED_UP = "Signed up on the course.";
const std::string COMPLETED = "Course completed.";
const std::string GRADUATED = "Graduated, all courses completed.";

class Account
{
public:
    /**
     * @brief Account constructor
     * @param full_name as "firstname lastname"
     * @param account_number
     * @param duplicates tells the number of full namesakes
     * @param university_suffix is the e-mail suffix e.g. "tuni.fi"
     */
    Account(const std::string& full_name, int account_number, int duplicates,
            const std::string& university_suffix);

    /**
     * @brief Account destructor
     */
    ~Account();

    /**
     * @brief print account info on one line
     */
    void print() const;

    /**
     * @brief get_email
     * @return email linked to this account
     */
    std::string get_email() const;

    /**
     * @brief get_full_name
     * @return full name of this account
     */
    std::string get_full_name() const;

    /**
     * @brief get_account_number
     * @return account number linked to this account
     */
    int get_account_number() const;

    /**
     * @brief get_current_courses
     * @return all courses of this account
     */
    std::vector<std::string> get_current_courses() const;

    /**
     * @brief get_completed_courses
     * @return all completed courses of this account
     */
    std::vector<std::string> get_completed_courses() const;

    /**
     * @brief sign up to course with param code
     */
    void sign_up(std::string course_code);

    /**
     * @brief complete course with param code
     */
    void complete(std::string course_code);

    /**
     * @brief complete accounts courses and set boolean
     */
    void graduate();

    /**
     * @brief is_graduated
     * @return get boolean if or not account has graduated
     */
    bool is_graduated() const;

private:
    std::string full_name_;
    std::string last_name_;
    std::string first_name_;
    std::string email_;
    const int account_number_;

    std::vector<std::string> current_courses_;
    std::vector<std::string> completed_courses_;

    bool graduated = false;

};

#endif // ACCOUNT_HH


