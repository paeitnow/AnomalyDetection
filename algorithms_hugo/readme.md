
# RandomForestClassifier1

--> The recall is abnormally high, because it also takes into account normal points, not just anomalies, so the anomalies are diluted in the large number of points, which is corrected in subsequent versions.





 ![newplot](https://github.com/user-attachments/assets/b9a87cd2-2ed9-4dfc-927f-e476b45747ed)



# RandomForestClassifier2


![image](https://github.com/user-attachments/assets/10132731-c2df-4cf6-97eb-75320d0116c2)

![newplot (1)](https://github.com/user-attachments/assets/7fc0bf06-37ad-440a-a8a7-f849e36a53dd)













# ml1
![image](https://github.com/user-attachments/assets/43dd13d6-3271-4bd1-b785-da7a5b9063e5)

![image](https://github.com/user-attachments/assets/efce3dc2-3a0f-4f49-8643-4e6a55f2caee)

















# ml2





[Average time to run the code: 1 hour]

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























# RandomForestClassifierFINAL


![image](https://github.com/user-attachments/assets/ec0fed3f-ed68-4f5f-be9f-131b50443c94)


![image](https://github.com/user-attachments/assets/c8234c91-e42c-4492-a6c8-40af5f66b301)


![image](https://github.com/user-attachments/assets/b4c15c21-d4ff-4df8-9b89-11a8d24d37f1)


![image](https://github.com/user-attachments/assets/441d5950-59e0-4b29-a369-8fafd2c2c965)


## Code Overview



### Data Preparation

1. **Importing Libraries**: 
   - Libraries like `pandas` and `numpy` are used for data manipulation, while `plotly` is chosen for visualization because it allows for interactive plots, which can be helpful in exploring the data and understanding the results.
   - `scikit-learn` is a well-established library for machine learning in Python, offering tools for training models and evaluating their performance.

2. **Activating Plotly for Offline Mode**:
   - Plotly's offline mode is used because it enables interactive plotting in environments like Jupyter notebooks without needing an internet connection. This makes it suitable for exploratory data analysis.

3. **Loading the Dataset**:
   - The dataset is loaded from a CSV file because this format is widely used for storing tabular data, making it easy to work with in data science workflows.

4. **Cleaning Data**:
   ```python
   data_cleaned = data.dropna(subset=['label']).copy()
   ```
   - **Why?** Removing rows with missing 'label' values ensures that we only train the model on data where we know whether the transaction is normal or anomalous. This is important because supervised learning algorithms, like Random Forest, require labeled data for training.

5. **Feature Extraction**:
   ```python
   data_cleaned['timestamp'] = pd.to_datetime(data_cleaned['timestamp'], unit='s')
   data_cleaned['hour'] = data_cleaned['timestamp'].dt.hour
   data_cleaned['day_of_week'] = data_cleaned['timestamp'].dt.dayofweek
   data_cleaned['day_of_month'] = data_cleaned['timestamp'].dt.day
   data_cleaned['month'] = data_cleaned['timestamp'].dt.month
   ```
   - **Why?** Time-based features can be very useful in anomaly detection because patterns in transactions often correlate with time. For example, certain activities may be more likely to happen at specific hours or on particular days (e.g., higher transaction volumes on weekdays). Including these features allows the model to detect anomalies based on when they occur.

6. **Normalization**:
   ```python
   data_cleaned['value_normalized'] = (data_cleaned['value'] - data_cleaned['value'].mean()) / data_cleaned['value'].std()
   ```
   - **Why?** Normalizing the 'value' column helps to standardize the range of the data. This is important for machine learning models because features with larger ranges could dominate the learning process. By bringing all features to a similar scale, the model can better learn patterns across different types of features.

7. **Calculating Rolling Statistics**:
   ```python
   data_cleaned['rolling_mean_5'] = data_cleaned['value'].rolling(window=5).mean()
   data_cleaned['rolling_std_5'] = data_cleaned['value'].rolling(window=5).std()
   data_cleaned['rolling_mean_10'] = data_cleaned['value'].rolling(window=10).mean()
   data_cleaned['rolling_std_10'] = data_cleaned['value'].rolling(window=10).std()
   ```
   - **Why?** Rolling statistics are calculated over different window sizes (5 and 10) to capture short-term trends in the data. These features help the model identify unusual behavior based on recent transaction history. If a transaction significantly deviates from recent trends, it could be a sign of an anomaly.

8. **Handling Missing Values**:
   ```python
   data_cleaned.fillna(data_cleaned.mean(), inplace=True)
   ```
   - **Why?** Rolling calculations produce NaN values at the start of the dataset, where there isn't enough data to calculate the statistics. Filling these missing values with the column mean helps to avoid problems during model training and ensures that no data is discarded.

### Machine Learning

9. **Defining Features and Target**:
   ```python
   features = ['value_normalized', 'hour', 'day_of_week', 'day_of_month', 'month', 
               'rolling_mean_5', 'rolling_std_5', 'rolling_mean_10', 'rolling_std_10']
   X = data_cleaned[features]
   y = data_cleaned['label'].astype(int)
   ```
   - **Why?** The chosen features include time-based, statistical, and normalized transaction data. This combination helps the model understand both the magnitude of the transactions and their temporal patterns. The target variable `y` is the 'label' indicating whether a transaction is normal or an anomaly.

10. **Splitting the Data**:
    ```python
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    ```
    - **Why?** Splitting the data into training (80%) and testing (20%) sets ensures that we can evaluate the model's performance on unseen data, which is crucial for assessing its generalization ability.

11. **Feature Standardization**:
    ```python
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    ```
    - **Why?** Standardizing the features helps the model perform better by ensuring all features contribute equally to the learning process. It prevents features with large values from dominating those with smaller values.

### Functions

12. **expand_anomalies Function**:
    ```python
    def expand_anomalies(anomaly_indices, window_size, total_length):
        ...
    ```
    - **Why?** This function expands the range of detected anomalies to include neighboring data points. This is based on the idea that anomalies often occur in clusters or bursts, where surrounding transactions may also be unusual. By expanding the detected anomalies, we increase the chances of capturing all related suspicious activities.

13. **train_evaluate_model Function**:
    ```python
    def train_evaluate_model(X_train_scaled, y_train, X_test_scaled, y_test, data_cleaned, threshold=0.5, window_size=0,
                             n_estimators=100, max_depth=None, class_weight='balanced'):
        ...
    ```
    - **Why use RandomForestClassifier?** A Random Forest is chosen because it is an ensemble model that combines multiple decision trees to improve prediction accuracy. It handles both numerical and categorical data well and is less prone to overfitting compared to individual decision trees.
    - **Why use class_weight='balanced'?** Class weighting addresses the imbalance between normal and anomalous transactions by giving more importance to the minority class (anomalies). This helps improve the model's ability to detect rare events.
    - **Why allow adjusting the threshold?** Adjusting the classification threshold enables fine-tuning of the model's sensitivity. Lowering the threshold can help catch more anomalies, but may also increase false positives. The choice of threshold allows for finding a balance between precision and recall.
    - **Why calculate precision, recall, and F1-score?** These metrics provide insight into the model's performance:
      - **Precision** measures the proportion of detected anomalies that are true anomalies.
      - **Recall** measures the proportion of actual anomalies that were detected.
      - **F1-score** balances precision and recall, giving a single metric for evaluating the model.

### Model Training and Evaluation

14. **Parameter Settings**:
    - Setting `threshold = 0.3` and `window_size = 5` allows for more sensitive anomaly detection and captures nearby suspicious transactions. These values can be tuned to improve the model’s performance.

15. **Train and Evaluate the Model**:
    ```python
    rf_model, data_cleaned, precision, recall, f1 = train_evaluate_model(...)
    ```
    - **Why train and evaluate together?** This function encapsulates the entire process, ensuring that we get the model, predictions, and performance metrics in a single call, making the code cleaner and easier to manage.









