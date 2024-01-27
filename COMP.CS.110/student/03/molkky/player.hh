#ifndef PLAYER_HH
#define PLAYER_HH
#include <string>

class Player
{
public:
    Player(std::string const& name);
    std::string get_name() const;
    int get_points() const;
    bool has_won();
    void add_points(int points);
private:
    int points_;
    std::string name_;

};

#endif // PLAYER_HH
