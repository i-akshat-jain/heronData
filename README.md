# heronData

## Q1: Approach to Identifying Recurring Transactions

Data Preprocessing: 

* Load data from a reliable source (JSON/CSV).
* Validate essential fields: description, amount, date.

Transaction Analysis:

*  Group transactions by description or merchant.
* Temporal analysis for frequency patterns.

Criteria for Identification:

* Identify fixed interval transactions (monthly, weekly).
* Use similarity metrics for clustering.

Algorithmic Identification:

* Implement Sequential Pattern Mining.
* Set temporal difference threshold.
* Predictive Modeling (Optional):


Output Formatting:

Present identified transactions with amounts, dates, predictions.

## Testing and Validation:

Test cases are provided in the /tests directory. Feel free to use and modify these cases to validate the utility's functionality.
