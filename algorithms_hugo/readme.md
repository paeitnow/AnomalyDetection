
# RandomForestClassifier1

--> The recall is abnormally high, because it also takes into account normal points, not just anomalies, so the anomalies are diluted in the large number of points, which is corrected in subsequent versions.


The provided code uses various machine learning algorithms to detect anomalies in a dataset of banking transactions. Here is a detailed explanation of the steps and concepts used:

### 1. Data Loading and Preparation

- **Loading the data**: The CSV file containing the transactions is loaded into a Pandas DataFrame. This file includes columns such as `timestamp`, `value` (transaction amount), and `label` (indicating whether the transaction is an anomaly or not).
- **Data cleaning**: Rows without a label (anomaly or not) are removed.
- **Timestamp conversion**: The `timestamp` column is converted to `datetime` format to enable the extraction of time-based features.

### 2. Feature Engineering

- **Extracting temporal features**: Additional information like the hour (`hour`), day of the week (`day_of_week`), day of the month (`day_of_month`), and month (`month`) are extracted from the `timestamp`.
- **Normalization of values**: The transaction amounts are normalized to have a mean of zero and a standard deviation of one. This standardizes the data for the machine learning algorithms, making them more robust to differences in scale.
- **Rolling statistics**: Moving averages (`rolling_mean`) and moving standard deviations (`rolling_std`) are calculated over windows of 5 and 10 observations to capture local trends in the data.

### 3. Preparing the Training Data

- **Feature selection**: The created features are combined to form the input matrix `X`.
- **Data splitting**: The data is split into training and test sets, with 80% used for training and 20% for testing.
- **Standardization**: The data is standardized to ensure all features contribute equally to the models.

### 4. Training the Machine Learning Models

Three different models are used:

1. **Random Forest Classifier**:
   - An ensemble algorithm that builds multiple decision trees and combines their results to obtain a final prediction. It is robust to imbalanced data.
   - The probability of each observation being an anomaly is calculated (`rf_proba`).

2. **XGBoost Classifier**:
   - A boosting algorithm that builds decision trees sequentially to correct the errors of the previous trees. It is efficient for large datasets.
   - The prediction probabilities (`xgb_proba`) are obtained.

3. **Isolation Forest**:
   - An unsupervised anomaly detection algorithm. It works by isolating observations by randomly partitioning the data.
   - Anomaly scores are obtained, and a threshold is set to classify observations as anomalies or not.

### 5. Combining Predictions and Adjusting Thresholds

- The predictions from the three models are combined by averaging the probabilities (`average_proba`). This creates an ensemble model that leverages the strengths of each algorithm.
- An adjusted threshold of 0.4 is used to determine if an observation is considered an anomaly.

### 6. Filtering Predictions to Reduce Noise

- **Smoothing filter**: The anomaly predictions are smoothed using a moving average filter (`uniform_filter1d`). This reduces false positives by treating anomalies as persistent events rather than simple point fluctuations.

### 7. Performance Evaluation

- **Classification report**: Provides metrics such as precision, recall, and F1-score to evaluate the detection performance.
- **Confusion matrix**: Allows analysis of the correct and incorrect predictions of anomalies and normal observations.
- **ROC-AUC and PR-AUC scores**: Measure the overall performance of the model in terms of anomaly detection.

### 8. Interactive Visualization

The code uses Plotly to create an interactive plot to visualize the normalized values of the transactions over time, comparing actual anomalies (red markers) and predicted anomalies (green markers). This helps to visually assess the model's effectiveness in detecting anomalies in the dataset.


 ![image](https://github.com/user-attachments/assets/abb92fbf-91d3-4b29-9b8b-e5e9223170d7)


 ![newplot](https://github.com/user-attachments/assets/b9a87cd2-2ed9-4dfc-927f-e476b45747ed)



# RandomForestClassifier2


![image](https://github.com/user-attachments/assets/10132731-c2df-4cf6-97eb-75320d0116c2)

![newplot (1)](https://github.com/user-attachments/assets/7fc0bf06-37ad-440a-a8a7-f849e36a53dd)
