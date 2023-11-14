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


## External Resources

* https://docs.python.org/3/library/difflib.html
* https://www.geeksforgeeks.org/sequencematcher-in-python-for-longest-common-substring/ 
* https://stackoverflow.com/questions/12436672/how-does-sequencematcher-ratio-works-in-difflib 


## Additional Approaches

With more time, we would delve deeper into the realm of machine learning, focusing on models that specialize in understanding natural language (NLP) and recognizing intricate patterns. Our goal is to elevate the accuracy of our system. We plan to explore ensemble methods, combining the strengths of multiple algorithms. Additionally, we aim to fine-tune our similarity metrics, experiment with different threshold values, and actively seek user feedback. This iterative process will contribute to the ongoing refinement of our models, ensuring they align more closely with user needs and expectations.