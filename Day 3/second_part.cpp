#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using int64 = long long;

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

int64 calculate_total_voltage(const std::vector<std::string>& battery_banks) {
    int64 total_voltage = 0;

    for (const std::string& bank : battery_banks) {
        int64 voltage = 0;
        int remaining_length = 12;
        std::string search_area = bank;

        while (remaining_length > 0) {
            std::size_t window_size = (search_area.size() - static_cast<std::size_t>(remaining_length)) + 1;
            auto [biggest, biggest_index] = find_biggest_element(search_area.substr(0, window_size));

            voltage = voltage * 10 + biggest;
            --remaining_length;
            search_area = search_area.substr(biggest_index + 1);
        }

        total_voltage += voltage;
    }

    return total_voltage;
}

int main() {
    std::vector<std::string> battery_banks = load_battery_banks("input_final.txt");
    int64 total_voltage = calculate_total_voltage(battery_banks);

    std::cout << total_voltage << std::endl;
    return 0;
}