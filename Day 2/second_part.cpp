#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using int64 = long long;

std::vector<std::string> load_input_data(const std::string& file_name) {
    std::ifstream file(file_name);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + file_name);
    }

    std::string data;
    std::getline(file, data, '\0');

    std::vector<std::string> input_ranges;
    std::stringstream stream(data);
    std::string input_range;

    while (std::getline(stream, input_range, ',')) {
        if (!input_range.empty() && input_range.back() == '\r') {
            input_range.pop_back();
        }
        if (!input_range.empty()) {
            input_ranges.push_back(input_range);
        }
    }

    return input_ranges;
}

bool is_repeated_pattern(const std::string& value) {
    std::size_t length = value.size();

    for (std::size_t pattern_length = 1; pattern_length <= length / 2; ++pattern_length) {
        if (length % pattern_length != 0) {
            continue;
        }

        std::string pattern = value.substr(0, pattern_length);
        bool matches = true;

        for (std::size_t index = pattern_length; index < length; index += pattern_length) {
            if (value.compare(index, pattern_length, pattern) != 0) {
                matches = false;
                break;
            }
        }

        if (matches) {
            return true;
        }
    }

    return false;
}

int main() {
    std::vector<std::string> input_ranges = load_input_data("input_final.txt");
    int64 counter = 0;

    for (const std::string& input_range : input_ranges) {
        std::size_t separator_index = input_range.find('-');
        if (separator_index == std::string::npos) {
            throw std::invalid_argument("Invalid range: " + input_range);
        }

        int64 start = std::stoll(input_range.substr(0, separator_index));
        int64 end = std::stoll(input_range.substr(separator_index + 1));

        for (int64 number = start; number <= end; ++number) {
            std::string number_text = std::to_string(number);
            if (is_repeated_pattern(number_text)) {
                counter += number;
            }
        }
    }

    std::cout << counter << std::endl;
    return 0;
}