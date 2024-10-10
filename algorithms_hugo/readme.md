
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













# ml1
![image](https://github.com/user-attachments/assets/43dd13d6-3271-4bd1-b785-da7a5b9063e5)

![image](https://github.com/user-attachments/assets/efce3dc2-3a0f-4f49-8643-4e6a55f2caee)

















# ml2






The code provided focuses on detecting anomalies in a dataset of transactions using machine learning techniques, including deep learning. Here's an explanation of the key methods, techniques, and steps used in the code:

### 1. Installing and Importing Libraries
- **Libraries Installation**: The code uses various libraries like `xgboost`, `imbalanced-learn`, `plotly`, `optuna`, and `tensorflow`. Each has a specific purpose:
  - `xgboost`: Gradient boosting framework for supervised learning.
  - `imbalanced-learn`: Provides techniques for dealing with imbalanced datasets.
  - `plotly`: Used for interactive visualizations.
  - `optuna`: Hyperparameter optimization framework.
  - `tensorflow`: For building and training deep learning models, particularly LSTM networks in this case.

### 2. Data Loading and Cleaning
- **Data Loading**: Loads the dataset from a CSV file. The file should contain columns like `timestamp`, `value` (transaction amount), and `label` (indicating anomaly or normal).
- **Data Cleaning**: Removes rows with missing `label` values and converts the `timestamp` column to a `datetime` format. The data is then sorted by time to preserve the temporal sequence.

### 3. Feature Engineering
- **Extracting Temporal Features**: Creates new features from the `timestamp`, such as `hour`, `day_of_week`, `day_of_month`, and `month`. These features help capture seasonality and time-based patterns in the data.
- **Normalization**: The transaction amounts are normalized to have a mean of zero and a standard deviation of one. This step standardizes the data for machine learning models.
- **Rolling Statistics**: Computes rolling means and standard deviations over 5 and 10 observation windows. This provides local trend information and can help in detecting unusual patterns.
- **Differencing**: Computes the difference between consecutive values (`value_diff`) to capture the rate of change.
- **Handling Missing Values**: Any remaining missing values are filled using backward filling.

### 4. Preparing Training and Test Data
- **Data Splitting**: Splits the dataset into training and test sets while maintaining the temporal order (80% training, 20% testing).
- **Handling Class Imbalance with SMOTE**: The code uses SMOTE (Synthetic Minority Over-sampling Technique) to oversample the minority class (anomalies). This helps address the imbalance problem, making the dataset more suitable for training machine learning models.

### 5. Data Standardization
- **Standard Scaling**: The features are standardized using `StandardScaler`, ensuring that all features have similar distributions.

### 6. LSTM Model Preparation
- **Creating Sequences for LSTM**: The data is reshaped into sequences of time steps for input into the LSTM model. This step involves creating sliding windows of fixed size (`time_steps`), which are fed into the model to learn temporal dependencies.

### 7. Anomaly Expansion
- **Expanding Anomalies**: The code extends detected anomalies over a given window size. This helps to capture anomalies that persist over several time steps, instead of detecting them as single point events.

### 8. Hyperparameter Optimization using Optuna
- **Objective Function Definition**: An objective function is defined to optimize hyperparameters such as the number of LSTM units, dropout rate, learning rate, and batch size.
- **Optimization Process**: Optuna performs several trials to find the best hyperparameters by maximizing the F1 score on a validation set.

### 9. Training the Final LSTM Model
- **Model Architecture**: The model consists of an LSTM layer followed by a dropout layer and a dense output layer with a sigmoid activation function for binary classification (anomaly or normal).
- **Optimizer**: Uses Adam optimizer with the best learning rate found by Optuna.
- **Early Stopping**: Stops training if the validation loss does not improve for a certain number of epochs (`patience=5`), to prevent overfitting.

### 10. Model Performance Evaluation
- **Loss and Accuracy Curves**: Plots the training and validation loss and accuracy curves to visually assess the model's training process.
- **Predictions on the Test Set**: Makes predictions on the test data to evaluate the model's performance.
- **Performance Metrics**: Uses various metrics for evaluation:
  - **Classification Report**: Precision, recall, F1-score, and support for both normal and anomaly classes.
  - **Confusion Matrix**: Shows the number of true positives, false positives, true negatives, and false negatives.
  - **ROC-AUC and PR-AUC**: The area under the ROC (Receiver Operating Characteristic) curve and Precision-Recall curve. These scores provide insights into the model's ability to distinguish between normal and anomalous transactions.
  - **ROC Curve**: Plots the true positive rate versus the false positive rate.
  - **Precision-Recall Curve**: Shows precision as a function of recall.

### 11. Visualization with Plotly
- **Interactive Visualization**: Uses Plotly to plot the normalized transaction values over time, showing real and predicted anomalies.
- **Zoomable Features**: Allows the user to zoom in on specific time ranges, enhancing the analysis of detected anomalies.

### Key Techniques and Concepts

1. **LSTM (Long Short-Term Memory) Networks**:
   - LSTMs are a type of recurrent neural network (RNN) capable of learning long-term dependencies in time-series data. They are particularly useful for anomaly detection because they can learn patterns over time and detect deviations.

2. **SMOTE (Synthetic Minority Over-sampling Technique)**:
   - SMOTE generates synthetic samples for the minority class to balance the dataset. This technique is effective for improving the performance of classifiers on imbalanced datasets.

3. **Hyperparameter Tuning with Optuna**:
   - Optuna automates the search for optimal hyperparameters using a trial-and-error approach, aiming to maximize a specific metric (e.g., F1-score). It employs techniques like Bayesian optimization for efficient hyperparameter search.

4. **Data Normalization and Standardization**:
   - These are preprocessing steps that transform the data into a common scale, making it suitable for machine learning models. Normalization rescales features, while standardization transforms them to have zero mean and unit variance.

5. **Handling Class Imbalance**:
   - Techniques like SMOTE and weighted loss functions address the problem of imbalanced classes, which can otherwise lead to biased models.

6. **Sequence Creation for Time Series Data**:
   - For LSTM networks, data is converted into overlapping sequences to capture temporal patterns. The `time_steps` parameter controls the length of each sequence.






![image](https://github.com/user-attachments/assets/9f7aef27-6cb8-4d34-bbbb-ca574368bac1)


![image](https://github.com/user-attachments/assets/5274999a-342b-427c-9169-89a2c7d03475)


![image](https://github.com/user-attachments/assets/3ea5556e-7487-48c2-a26a-ae7bf7fd40c9)

![image](https://github.com/user-attachments/assets/5e836b7d-4edc-405a-8cd9-684bf25bec7b)


![image](https://github.com/user-attachments/assets/053dab15-5de6-41e6-9d2c-c20561b12b20)

![image](https://github.com/user-attachments/assets/ce757564-db57-409b-8526-8707609feb78)

