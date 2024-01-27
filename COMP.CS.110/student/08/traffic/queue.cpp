#include "queue.hh"
#include <iostream>


Queue::Queue(unsigned int cycle)
{
    cycle_ = cycle;
}

Queue::~Queue()
{

}

void Queue::enqueue(const string &reg)
{
    if (cycle_remaining_ != 0) {
        std::cout << "GREEN: The vehicle " << reg << " need not stop to wait" << std::endl;
        cycle_remaining_ -= 1;
        if (cycle_remaining_ == 0){
            is_green_ = false;
        }
    } else {
        Vehicle* new_car = new Vehicle;
          new_car->reg_num = reg;
          new_car->next = nullptr;

          if (first_ == nullptr) {
            first_ = new_car;
          }
          else {

            Vehicle* current = first_;

            while (current->next != nullptr) {
                current = current->next;
            }

            current->next = new_car;
            current->next->next = nullptr;

          }
    }
}

void Queue::switch_light()
{
    if (is_green_) {
        is_green_ = false;
        std::cout << "RED: No vehicles waiting in traffic lights" << std::endl;
        cycle_remaining_ = 0;
    } else {
        is_green_ = true;

        std::cout << "GREEN:";

        unsigned int i = 0;
        Vehicle* current = first_;

        if (current == nullptr) {
            std::cout << " No vehicles waiting in traffic lights" << std::endl;
            if (is_green_) {
                cycle_remaining_ = cycle_;
            }
        } else {
            std::cout << " Vehicle(s)";
            while (current != nullptr && i < cycle_) {
              std::cout << " " << current->reg_num;
              current = current->next;
              i++;

              Vehicle* old_first = first_;
              first_ = first_->next;
              delete old_first;

              is_green_ = false;

            }
            std::cout << " can go on" << std::endl;

            if (i == cycle_) {
                is_green_ = false;
            } else {
                cycle_remaining_ = cycle_ - i;
            }
        }

    }
}

void Queue::reset_cycle(unsigned int cycle)
{
    cycle_ = cycle;

    if (cycle_remaining_ != 0) {
        cycle_remaining_ = cycle_;
    }
}

void Queue::print() const
{
    if (is_green_) {
        std::cout << "GREEN: No vehicles waiting in traffic lights" << std::endl;
    }else {
        if (first_ == nullptr) {
            std::cout << "RED: No vehicles waiting in traffic lights" << std::endl;
        } else {
            std::cout << "RED: Vehicle(s)";
            int i = 1;
            Vehicle* current = first_;
            while (current != nullptr) {
              std::cout << " " << current->reg_num;
              current = current->next;
              i++;
            }
            std::cout << " waiting in traffic lights" << std::endl;
        }
    }
}
