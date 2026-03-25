#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

std::vector<std::string> load_battery_banks(const std::string& file_name) {
    std::ifstream file(file_name);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + file_name);
    }

    std::vector<std::string> battery_banks;
    std::string line;
    while (std::getline(file, line)) {
        if (!line.empty() && line.back() == '\r') {
            line.pop_back();
        }
        if (!line.empty()) {
            battery_banks.push_back(line);
        }
    }

    return battery_banks;
}

std::pair<int, std::size_t> find_biggest_element(const std::string& input) {
    int biggest = input[0] - '0';
    std::size_t biggest_index = 0;

    for (std::size_t index = 0; index < input.size(); ++index) {
        int element = input[index] - '0';
        if (element > biggest) {
            biggest = element;
            biggest_index = index;
        }
    }

    return {biggest, biggest_index};
}

int calculate_total_voltage(const std::vector<std::string>& battery_banks) {
    int total_voltage = 0;

    for (const std::string& bank : battery_banks) {
        int voltage = 0;
        auto [biggest, biggest_index] = find_biggest_element(bank);

        if (biggest_index == bank.size() - 1) {
            voltage += biggest;
            auto [second_biggest, second_biggest_index] = find_biggest_element(bank.substr(0, biggest_index));
            (void)second_biggest_index;
            voltage += second_biggest * 10;
        } else {
            auto [second_biggest, second_biggest_index] =
                find_biggest_element(bank.substr(biggest_index + 1));
            (void)second_biggest_index;
            voltage += biggest * 10 + second_biggest;
        }

        total_voltage += voltage;
    }

    return total_voltage;
}

int main() {
    std::vector<std::string> battery_banks = load_battery_banks("input_final.txt");
    int total_voltage = calculate_total_voltage(battery_banks);

    std::cout << total_voltage << std::endl;
    return 0;
}