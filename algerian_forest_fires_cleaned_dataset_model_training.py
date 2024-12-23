# -*- coding: utf-8 -*-
"""Algerian Forest Fires Cleaned Dataset_Model Training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ibrR1_2kr4jT_7i3E90B4nyoc6LtYDvh
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import drive
drive.mount('/content/drive')

df=pd.read_csv('/content/drive/MyDrive/CSE366(AI)/lab07/Algerian_forest_fires_cleaned_dataset.csv')

import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv('/content/drive/MyDrive/CSE366(AI)/lab07/Algerian_forest_fires_cleaned_dataset.csv')

# Display initial information about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Handle missing values (drop or fill)
data.dropna(inplace=True)  # or use data.fillna(method='ffill', inplace=True)

# Encode categorical variables (if needed)
data['Classes'] = data['Classes'].str.strip()  # Remove any leading/trailing whitespace
data['Classes'] = data['Classes'].map({'fire': 1, 'not fire': 0})  # Binary encoding

# Drop irrelevant columns if necessary
X = data.drop(['Classes', 'day', 'month', 'year'], axis=1)
y = data['Classes']

# Ensure all features are numeric
X = X.apply(pd.to_numeric, errors='coerce')

# Check for any remaining non-numeric values
print(X.isnull().sum())  # Check again for NaN values after conversion

# Drop any rows with NaN values after conversion
X.dropna(inplace=True)
y = y[X.index]  # Align target variable with features

# Now split the data and fit your models as before
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Proceed with model fitting as previously described

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv('/content/drive/MyDrive/CSE366(AI)/lab07/Algerian_forest_fires_cleaned_dataset.csv')

# Preprocess data (assuming 'Classes' is the target variable)
data['Classes'] = data['Classes'].str.strip()  # Remove any leading/trailing whitespace
data['Classes'] = data['Classes'].map({'fire': 1, 'not fire': 0})  # Binary encoding

# Define features and target variable
X = data.drop(['Classes', 'day', 'month', 'year'], axis=1)
y = data['Classes']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Lasso Regression': Lasso(alpha=0.1),
    'Ridge Regression': Ridge(alpha=0.1),
    'Elastic Net': ElasticNet(alpha=0.1, l1_ratio=0.5)
}

# Fit models and collect predictions
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    results[name] = predictions

# Plotting Predicted vs Actual
plt.figure(figsize=(12, 6))
for name, predictions in results.items():
    plt.scatter(y_test, predictions, label=name)
plt.plot([0, 1], [0, 1], '--r')  # Line of equality
plt.title('Predicted vs Actual')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend()
plt.grid()
plt.show()

# Plotting Residuals
plt.figure(figsize=(12, 6))
for name, predictions in results.items():
    residuals = y_test - predictions
    plt.scatter(predictions, residuals, label=name)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals for Each Model')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.legend()
plt.grid()
plt.show()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load dataset
data = pd.read_csv('/content/drive/MyDrive/CSE366(AI)/lab07/Algerian_forest_fires_cleaned_dataset.csv')

# Preprocess data (assuming 'Classes' is the target variable)
data['Classes'] = data['Classes'].str.strip()  # Remove any leading/trailing whitespace
data['Classes'] = data['Classes'].map({'fire': 1, 'not fire': 0})  # Binary encoding

# Define features and target variable
X = data.drop(['Classes', 'day', 'month', 'year'], axis=1)
y = data['Classes']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Linear Regression': LinearRegression(),
    'Lasso Regression': Lasso(alpha=0.1),
    'Ridge Regression': Ridge(alpha=0.1),
    'Elastic Net': ElasticNet(alpha=0.1, l1_ratio=0.5)
}

# Fit models and collect predictions
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    # Convert predictions to binary (0 or 1) based on a threshold (0.5)
    binary_predictions = (predictions >= 0.5).astype(int)

    # Calculate metrics
    accuracy = accuracy_score(y_test, binary_predictions)
    precision = precision_score(y_test, binary_predictions)
    recall = recall_score(y_test, binary_predictions)
    f1 = f1_score(y_test, binary_predictions)

    results[name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1
    }

# Display results
for model_name, metrics in results.items():
    print(f"{model_name}:")
    print(f"  Accuracy: {metrics['Accuracy']:.4f}")
    print(f"  Precision: {metrics['Precision']:.4f}")
    print(f"  Recall: {metrics['Recall']:.4f}")
    print(f"  F1 Score: {metrics['F1 Score']:.4f}\n")

df.head()

df.columns

##drop month,day and yyear
df.drop(['day','month','year'],axis=1,inplace=True)

df.head()

df['Classes'].value_counts()

## Encoding
df['Classes']=np.where(df['Classes'].str.contains("not fire"),0,1)

df.tail()

df['Classes'].value_counts()

## Independent And dependent features
X=df.drop('FWI',axis=1)
y=df['FWI']

X.head()

y

#Train Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)

X_train.shape,X_test.shape

## Feature Selection based on correlaltion
X_train.corr()

## Check for multicollinearity
plt.figure(figsize=(12,10))
corr=X_train.corr()
sns.heatmap(corr,annot=True)

def correlation(dataset, threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                colname = corr_matrix.columns[i]
                col_corr.add(colname)
    return col_corr

## threshold--Domain expertise
corr_features=correlation(X_train,0.85)

## drop features when correlation is more than 0.85
X_train.drop(corr_features,axis=1,inplace=True)
X_test.drop(corr_features,axis=1,inplace=True)
X_train.shape,X_test.shape

"""## Feature Scaling Or Standardization"""

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

X_train_scaled

"""## Box Plots To understand Effect Of Standard Scaler"""

plt.subplots(figsize=(15, 5))
plt.subplot(1, 2, 1)
sns.boxplot(data=X_train)
plt.title('X_train Before Scaling')
plt.subplot(1, 2, 2)
sns.boxplot(data=X_train_scaled)
plt.title('X_train After Scaling')

"""## Linear Regression Model"""

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
linreg=LinearRegression()
linreg.fit(X_train_scaled,y_train)
y_pred=linreg.predict(X_test_scaled)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)
plt.scatter(y_test,y_pred)

"""## Lasso Regression"""

from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
lasso=Lasso()
lasso.fit(X_train_scaled,y_train)
y_pred=lasso.predict(X_test_scaled)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)
plt.scatter(y_test,y_pred)

"""### Cross Validation Lasso"""

from sklearn.linear_model import LassoCV
lassocv=LassoCV(cv=5)
lassocv.fit(X_train_scaled,y_train)

lassocv.alpha_

lassocv.alphas_

lassocv.mse_path_

y_pred=lassocv.predict(X_test_scaled)
plt.scatter(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

"""## Ridge Regression model"""

from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
ridge=Ridge()
ridge.fit(X_train_scaled,y_train)
y_pred=ridge.predict(X_test_scaled)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)
plt.scatter(y_test,y_pred)

from sklearn.linear_model import RidgeCV
ridgecv=RidgeCV(cv=5)
ridgecv.fit(X_train_scaled,y_train)
y_pred=ridgecv.predict(X_test_scaled)
plt.scatter(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

ridgecv.get_params()

"""## Elasticnet Regression"""

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
elastic=ElasticNet()
elastic.fit(X_train_scaled,y_train)
y_pred=elastic.predict(X_test_scaled)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)
plt.scatter(y_test,y_pred)

from sklearn.linear_model import ElasticNetCV
elasticcv=ElasticNetCV(cv=5)
elasticcv.fit(X_train_scaled,y_train)
y_pred=elasticcv.predict(X_test_scaled)
plt.scatter(y_test,y_pred)
mae=mean_absolute_error(y_test,y_pred)
score=r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 Score", score)

elasticcv.alphas_





