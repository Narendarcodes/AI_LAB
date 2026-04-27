from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import ParameterEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Sample data
data = pd.DataFrame(data={
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

# Define the Bayesian network structure
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Fit the model to the data using Maximum Likelihood Estimation
model.fit(data)

# Print conditional probability distributions
print(model.get_cpds())

# Perform inference
inference = VariableElimination(model)
query_result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)

print(query_result)