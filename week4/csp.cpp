import java.util.*;

class ConstraintSatisfactionProblem {

    private List<String> variables;
    private Map<String, List<Integer>> domains;
    private Map<String, List<Constraint>> constraints;

    // Functional interface for constraints
    interface Constraint {
        boolean isSatisfied(String variable, int value, Map<String, Integer> assignment);
    }

    public ConstraintSatisfactionProblem(
            List<String> variables,
            Map<String, List<Integer>> domains,
            Map<String, List<Constraint>> constraints) {

        this.variables = variables;
        this.domains = domains;
        this.constraints = constraints;
    }

    // Check if assignment is consistent
    private boolean isConsistent(String variable, int value, Map<String, Integer> assignment) {
        if (!constraints.containsKey(variable)) return true;

        for (Constraint constraint : constraints.get(variable)) {
            if (!constraint.isSatisfied(variable, value, assignment)) {
                return false;
            }
        }
        return true;
    }

    // Backtracking algorithm
    public Map<String, Integer> backtrack(Map<String, Integer> assignment) {

        // If assignment complete, return solution
        if (assignment.size() == variables.size()) {
            return new HashMap<>(assignment);
        }

        // Select unassigned variable
        String var = selectUnassignedVariable(assignment);

        // Try all domain values
        for (int value : orderDomainValues(var)) {

            if (isConsistent(var, value, assignment)) {
                assignment.put(var, value);

                Map<String, Integer> result = backtrack(assignment);

                if (result != null) {
                    return result;
                }

                // Backtrack
                assignment.remove(var);
            }
        }

        return null; // Failure
    }

    private String selectUnassignedVariable(Map<String, Integer> assignment) {
        for (String variable : variables) {
            if (!assignment.containsKey(variable)) {
                return variable;
            }
        }
        return null;
    }

    private List<Integer> orderDomainValues(String variable) {
        return domains.get(variable);
    }
}

public class Main {

    public static void main(String[] args) {

        // Variables
        List<String> variables = Arrays.asList("A", "B", "C");

        // Domains
        Map<String, List<Integer>> domains = new HashMap<>();
        domains.put("A", Arrays.asList(1, 2, 3));
        domains.put("B", Arrays.asList(1, 2, 3));
        domains.put("C", Arrays.asList(1, 2, 3));

        // Constraints
        Map<String, List<ConstraintSatisfactionProblem.Constraint>> constraints = new HashMap<>();

        // A != B
        constraints.put("A", new ArrayList<>());
        constraints.get("A").add((var, val, ass) ->
                !ass.containsKey("B") || ass.get("B") != val
        );

        constraints.put("B", new ArrayList<>());
        constraints.get("B").add((var, val, ass) ->
                !ass.containsKey("A") || ass.get("A") != val
        );

        constraints.put("C", new ArrayList<>());
        constraints.get("C").add((var, val, ass) ->
                !ass.containsKey("A") || ass.get("A") != val
        );
        constraints.get("C").add((var, val, ass) ->
                !ass.containsKey("B") || ass.get("B") != val
        );

        // Create CSP object
        ConstraintSatisfactionProblem csp =
                new ConstraintSatisfactionProblem(variables, domains, constraints);

        Map<String, Integer> solution = csp.backtrack(new HashMap<>());

        if (solution != null) {
            System.out.println("Solution found:");
            for (Map.Entry<String, Integer> entry : solution.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }
        } else {
            System.out.println("No solution found.");
        }
    }
}