import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from Excel file
data = pd.read_excel('spam.xls')


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['Content'], data['Label'], test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer with stopwords removal
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer on the training data
X_train_vec = vectorizer.fit_transform(X_train)

# Train a Decision Tree classifier
clf = DecisionTreeClassifier()

# Fit the classifier on the training data
clf.fit(X_train_vec, y_train)

# Save the trained model to file
with open('model_dtc.sav', 'wb') as f:
    pickle.dump(clf, f)

# Load the saved model from file
with open('model_dtc.sav', 'rb') as f:
    clf = pickle.load(f)

# Transform the test data using the trained vectorizer
X_test_vec = vectorizer.transform(X_test)

# Predict the labels of the test data using the loaded model
y_pred = clf.predict(X_test_vec)

# Calculate the accuracy, precision, recall, f1-score, and support of the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['ham', 'spam'], output_dict=True)
precision = report['weighted avg']['precision']
recall = report['weighted avg']['recall']
f1_score = report['weighted avg']['f1-score']
support = report['weighted avg']['support']

# Print the accuracy, precision, recall, f1-score, and support of the model
print("Accuracy: {:.2%}".format(accuracy))
print("Precision: {:.2%}".format(precision))
print("Recall: {:.2%}".format(recall))
print("F1-score: {:.2%}".format(f1_score))
print("Support: {}".format(support))

# Create a pie chart of the test set labels
labels = ['Ham', 'Spam']
sizes = [len(y_test[y_test=='ham']), len(y_test[y_test=='spam'])]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
plt.title("Distribution of Test Set Labels")
plt.show()

# Create a confusion matrix of the test data using the loaded model
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
