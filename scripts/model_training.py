from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model(data):
    """Train a simple logistic regression model."""
    X = data[['Customer Age', 'Ticket Priority Numeric', 'Sentiment Score']]
    y = data['Resolution']  # Target column

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(solver='liblinear', max_iter=1000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")
    return model
