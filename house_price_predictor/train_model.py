import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset
data = {
    'bedrooms': [2, 3, 4, 5],
    'bathrooms': [1, 2, 2, 3],
    'sqft': [1200, 1500, 1800, 2500],
    'price': [200000, 300000, 400000, 500000]
}
df = pd.DataFrame(data)

# Features and target
X = df[['bedrooms', 'bathrooms', 'sqft']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved!")
