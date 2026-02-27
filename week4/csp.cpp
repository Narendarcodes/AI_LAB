#include <iostream>
#include <vector>
#include <map>
#include <functional>
#include <string>

using namespace std;

class ConstraintSatisfactionProblem {
private:
    vector<string> variables;
    map<string, vector<int>> domains;
    map<string, vector<function<bool(string, int, map<string, int>&)>>> constraints;

public:
    ConstraintSatisfactionProblem(
        vector<string> vars,
        map<string, vector<int>> doms,
        map<string, vector<function<bool(string, int, map<string, int>&)>>> cons)
    {
        variables = vars;
        domains = doms;
        constraints = cons;
    }

    bool is_consistent(string variable, int value, map<string, int>& assignment) {
        for (auto& constraint : constraints[variable]) {
            if (!constraint(variable, value, assignment))
                return false;
        }
        return true;
    }

    map<string, int>* backtrack(map<string, int>& assignment) {
        if (assignment.size() == variables.size()) {
            return new map<string, int>(assignment);
        }

        string var = select_unassigned_variable(assignment);

        for (int value : order_domain_values(var, assignment)) {
            if (is_consistent(var, value, assignment)) {
                assignment[var] = value;

                map<string, int>* result = backtrack(assignment);
                if (result != nullptr)
                    return result;

                assignment.erase(var); // Backtrack
            }
        }
        return nullptr;
    }

    string select_unassigned_variable(map<string, int>& assignment) {
        for (auto& variable : variables) {
            if (assignment.find(variable) == assignment.end())
                return variable;
        }
        return "";
    }

    vector<int> order_domain_values(string variable, map<string, int>& assignment) {
        return domains[variable];
    }
};

int main() {
    // Variables
    vector<string> variables = {"A", "B", "C"};

    // Domains
    map<string, vector<int>> domains = {
        {"A", {1, 2, 3}},
        {"B", {1, 2, 3}},
        {"C", {1, 2, 3}}
    };

    // Constraints
    map<string, vector<function<bool(string, int, map<string, int>&)>>> constraints;

    constraints["A"].push_back([](string var, int val, map<string, int>& ass) {
        return ass.find("B") == ass.end() || ass["B"] != val;
    });

    constraints["B"].push_back([](string var, int val, map<string, int>& ass) {
        return ass.find("A") == ass.end() || ass["A"] != val;
    });

    constraints["C"].push_back([](string var, int val, map<string, int>& ass) {
        return ass.find("A") == ass.end() || ass["A"] != val;
    });

    constraints["C"].push_back([](string var, int val, map<string, int>& ass) {
        return ass.find("B") == ass.end() || ass["B"] != val;
    });

    ConstraintSatisfactionProblem csp(variables, domains, constraints);

    map<string, int> assignment;
    map<string, int>* solution = csp.backtrack(assignment);

    if (solution != nullptr) {
        cout << "Solution found:\n";
        for (auto& pair : *solution) {
            cout << pair.first << ": " << pair.second << endl;
        }
        delete solution;
    } else {
        cout << "No solution found.\n";
    }

    return 0;
}
