#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <stdexcept>

std::vector<std::string> extract_inputs(const std::string& file_name) {
    std::ifstream file(file_name);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + file_name);
    }

    std::vector<std::string> inputs;
    std::string line;
    while (std::getline(file, line)) {
        while (!line.empty() && (line.back() == '\r' || line.back() == ' ' || line.back() == '\t')) {
            line.pop_back();
        }
        std::transform(line.begin(), line.end(), line.begin(), ::toupper);
        if (!line.empty()) {
            inputs.push_back(line);
        }
    }
    return inputs;
}

int count_passing_times(
    const std::vector<std::string>& inputs,
    int start_point,
    int count_point,
    int min_pointer,
    int max_pointer
) {
    int current_point = start_point;
    int counter = 0;
    int range_size = max_pointer - min_pointer;

    for (const std::string& command : inputs) {
        char direction = command[0];
        int distance = std::stoi(command.substr(1));
        int starting_point = current_point;

        if (direction == 'L') {
            current_point -= distance;
            if (current_point < min_pointer) {
                if (distance >= range_size) {
                    counter += distance / range_size;
                    if (starting_point - (distance % range_size) < min_pointer && starting_point != count_point) {
                        counter += 1;
                    }
                } else if (starting_point != count_point) {
                    counter += 1;
                }
            }
        } else if (direction == 'R') {
            current_point += distance;
            if (current_point > max_pointer) {
                if (distance >= range_size) {
                    counter += distance / range_size;
                    if ((starting_point + (distance % range_size)) > max_pointer && starting_point != count_point) {
                        counter += 1;
                    }
                } else if (starting_point != count_point) {
                    counter += 1;
                }
            }
        } else {
            throw std::invalid_argument(std::string("Invalid direction: ") + direction);
        }

        // Python-style modulo (always non-negative)
        int offset = (current_point - min_pointer) % range_size;
        if (offset < 0) offset += range_size;
        current_point = offset + min_pointer;

        if (current_point == count_point) {
            counter++;
        }
    }

    return counter;
}

int main() {
    std::vector<std::string> inputs = extract_inputs("input_final.txt");

    int result = count_passing_times(
        inputs,
        /*start_point=*/50,
        /*count_point=*/0,
        /*min_pointer=*/0,
        /*max_pointer=*/100
    );

    std::cout << result << std::endl;
    return 0;
}
