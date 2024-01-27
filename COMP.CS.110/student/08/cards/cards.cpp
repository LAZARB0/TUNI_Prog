#include "cards.hh"


Cards::Cards(): top_(nullptr)
{

}

Card_data *Cards::get_topmost()
{
    return top_;
}

void Cards::add(int id)
{
  Card_data* new_card = new Card_data;
  new_card->data = id;
  new_card->next = nullptr;

  if (top_ == nullptr) {
    top_ = new_card;
  }
  else {
    new_card->next = top_;
    top_ = new_card;
  }
}

void Cards::print_from_top_to_bottom(std::ostream &s)
{
  int i = 1;
  Card_data* current = top_;
  while (current != nullptr) {
    s << i << ": " << current->data << std::endl;
    current = current->next;
    i++;
  }
}

bool Cards::remove(int &id)
{
  if (top_ == nullptr) {
    return false;
  }

  Card_data* old_top = top_;
  top_ = top_->next;
  id = old_top->data;
  delete old_top;

  return true;
}

bool Cards::bottom_to_top()
{
  if (top_ == nullptr || top_->next == nullptr) {
    return false;
  }

  Card_data* previous = nullptr;
  Card_data* current = top_;

  while (current->next != nullptr) {
    previous = current;
    current = current->next;
  }

  current->next = top_;
  top_ = current;
  previous->next = nullptr;

  return true;
}

bool Cards::top_to_bottom()
{
    if (top_ == nullptr || top_->next == nullptr) {
      return false;
    }

    Card_data* current = top_;

    while (current->next != nullptr) {
      current = current->next;
    }

    current->next = top_;
    top_ = top_->next;
    current->next->next = nullptr;

    return true;
}

void Cards::print_from_bottom_to_top(std::ostream &s)
{
  recursive_print(top_, s);
}

Cards::~Cards()
{

}

int Cards::recursive_print(Card_data* top, std::ostream& s)
{
  if (top == nullptr) {
    return 0;
  }
  int count = recursive_print(top->next, s);
  s << count + 1 << ": " << top->data << std::endl;
  return count + 1;
}
