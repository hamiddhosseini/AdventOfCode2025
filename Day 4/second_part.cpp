#include <algorithm>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

std::vector<std::vector<int>> load_grid_from_file(const std::string& file_name) {
    std::ifstream file(file_name);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + file_name);
    }

    std::vector<std::vector<int>> grid;
    std::string line;

    while (std::getline(file, line)) {
        if (!line.empty() && line.back() == '\r') {
            line.pop_back();
        }

        std::vector<int> row;
        row.reserve(line.size());
        for (char c : line) {
            row.push_back(c == '@' ? 1 : 0);
        }
        grid.push_back(row);
    }

    return grid;
}

int count_neighbors(const std::vector<std::vector<int>>& grid, int row, int col) {
    int min_col = std::max(0, col - 1);
    int max_col = std::min(static_cast<int>(grid[row].size()) - 1, col + 1);
    int min_row = std::max(0, row - 1);
    int max_row = std::min(static_cast<int>(grid.size()) - 1, row + 1);

    int count = 0;
    for (int c = min_col; c <= max_col; ++c) {
        for (int r = min_row; r <= max_row; ++r) {
            if (grid[r][c] == 1) {
                ++count;
            }
        }
    }

    return count;
}

int count_and_remove_accessible_rolls(std::vector<std::vector<int>>& grid) {
    int accessible_rolls = 0;
    std::vector<std::vector<int>> grid_copy = grid;

    for (int row = 0; row < static_cast<int>(grid.size()); ++row) {
        for (int col = 0; col < static_cast<int>(grid[row].size()); ++col) {
            if (grid[row][col] == 1) {
                int count = count_neighbors(grid, row, col) - 1;
                if (count < 4) {
                    ++accessible_rolls;
                    grid_copy[row][col] = 9;
                }
            }
        }
    }

    if (accessible_rolls == 0) {
        return accessible_rolls;
    }

    for (int row = 0; row < static_cast<int>(grid.size()); ++row) {
        for (int col = 0; col < static_cast<int>(grid[row].size()); ++col) {
            if (grid_copy[row][col] == 9) {
                grid[row][col] = 0;
            }
        }
    }

    return accessible_rolls + count_and_remove_accessible_rolls(grid);
}

int main() {
    std::vector<std::vector<int>> grid = load_grid_from_file("input_final.txt");
    int result = count_and_remove_accessible_rolls(grid);
    std::cout << result << std::endl;
    return 0;
}