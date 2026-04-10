# ================================
# IMPORT LIBRARIES
# ================================
import numpy as np
import pandas as pd
import time

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# ================================
# PHASE 1: DATA ARCHITECTURE
# ================================

# Generate Dataset
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    n_classes=2,
    weights=[0.9, 0.1],   # Imbalanced dataset
    random_state=42
)

# Train-Test Split (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Feature Scaling (NO DATA LEAKAGE)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("\nDataset Ready!")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])

# ================================
# PHASE 2: BASELINE MODEL
# ================================

baseline_model = RandomForestClassifier(random_state=42)
baseline_model.fit(X_train, y_train)

y_pred = baseline_model.predict(X_test)

baseline_acc = accuracy_score(y_test, y_pred)
baseline_f1 = f1_score(y_test, y_pred)

print("\n=== BASELINE MODEL ===")
print("Accuracy:", baseline_acc)
print("F1 Score:", baseline_f1)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ================================
# GRID SEARCH (ACCURACY)
# ================================

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_acc = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    scoring='accuracy',
    cv=5,
    n_jobs=-1
)

grid_acc.fit(X_train, y_train)

print("\n=== GRID SEARCH (ACCURACY) ===")
print("Best Parameters:", grid_acc.best_params_)
print("Best Accuracy Score:", grid_acc.best_score_)

# ================================
# GRID SEARCH (F1 SCORE)
# ================================

grid_f1 = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    scoring='f1',
    cv=5,
    n_jobs=-1
)

grid_f1.fit(X_train, y_train)

print("\n=== GRID SEARCH (F1 SCORE) ===")
print("Best Parameters:", grid_f1.best_params_)
print("Best F1 Score:", grid_f1.best_score_)

# ================================
# PHASE 3: EFFICIENCY WARFARE
# ================================

# GRID SEARCH TIMING
start_time = time.time()

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    scoring='f1',
    cv=5,
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

grid_time = time.time() - start_time
grid_best_f1 = grid_search.best_score_

print("\n=== GRID SEARCH PERFORMANCE ===")
print("Time Taken:", round(grid_time, 2), "seconds")
print("Best F1 Score:", grid_best_f1)

# ================================
# RANDOMIZED SEARCH
# ================================

param_dist = {
    'n_estimators': np.arange(10, 500),
    'max_depth': [None, 10, 20, 30, 40],
    'min_samples_split': np.arange(2, 20)
}

start_time = time.time()

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=20,
    scoring='f1',
    cv=5,
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

random_time = time.time() - start_time
random_best_f1 = random_search.best_score_

print("\n=== RANDOMIZED SEARCH PERFORMANCE ===")
print("Time Taken:", round(random_time, 2), "seconds")
print("Best F1 Score:", random_best_f1)

# ================================
# FINAL COMPARISON TABLE
# ================================

comparison = pd.DataFrame({
    "Method": ["Grid Search", "Randomized Search"],
    "Time (seconds)": [round(grid_time, 2), round(random_time, 2)],
    "Best F1 Score": [grid_best_f1, random_best_f1]
})

print("\n=== FINAL COMPARISON ===")
print(comparison)