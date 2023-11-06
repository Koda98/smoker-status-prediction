import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

from xgboost import XGBClassifier

# script parameters
SEED = 42  # Random seed to be used throughout the script
output_file = "model.bin"

# Read and prepare data

# Data from Kaggle competition
comp_data_df_train = pd.read_csv("data/competition-data/train.csv")
df_test = pd.read_csv("data/competition-data/test.csv")

# Original data
orig_data_df = pd.read_csv("data/original-data/smoking.csv")

# drop columns
comp_data_df_train = comp_data_df_train.drop(columns=['id'])
df_test = df_test.drop(columns=['id'])
orig_data_df = orig_data_df.drop(columns=['ID', 'gender', 'oral', 'tartar'])

# combine datasets
df_train = pd.concat([comp_data_df_train, orig_data_df])

# remove duplicate rows
df_train = df_train.drop_duplicates()

# change blindness value to 0
df_train['eyesight(left)'] = df_train['eyesight(left)'].replace(to_replace=9.9, value=0)
df_train['eyesight(right)'] = df_train['eyesight(right)'].replace(to_replace=9.9, value=0)

df_test['eyesight(left)'] = df_test['eyesight(left)'].replace(to_replace=9.9, value=0)
df_test['eyesight(right)'] = df_test['eyesight(right)'].replace(to_replace=9.9, value=0)

# apply log transform
def apply_log_transform(df):
    features = list(df.columns)
    if 'smoking' in features:
        features.remove('smoking')
    for col in features:
        df[col] = df[col].apply(lambda x: np.log1p(x))
    return df

df_train = apply_log_transform(df_train)
df_test = apply_log_transform(df_test)

X_train = df_train.drop(columns=['smoking'])
y_train = df_train['smoking']

# train model
def fit_model_with_skf(X, y, model, n_splits=5, random_state=SEED, shuffle=True):
    """
    Fit a sklearn model using stratified k-fold validation.

    Parameters:
    * X: Training data
    * y: Training labels
    * model: sklearn model to be fitted
    * n_splits: number of folds for cross validation (default 5)
    * random_state: random state to reproduce results (default SEED set at top of notebook)
    # shuffle: whether or not to shuffle the data in the folds (default True)
    
    Returns:
    A list of the average score and standard deviation of the fold
    """
    skf = StratifiedKFold(n_splits=n_splits, random_state=random_state, shuffle=shuffle)
    scores = []
    fold = 1
    for train_idx, val_idx in skf.split(X, y):
        print(f'    Training fold {fold}...', end='\r')
        fold += 1
        X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
        X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]

        model.fit(X_train, y_train)
        y_pred = model.predict_proba(X_val)[:, 1]

        auc = roc_auc_score(y_val, y_pred)
        scores.append(auc)
    print(' '*30, end='\r')
    return (np.mean(scores), np.std(scores))

xgb_params = {
    'learning_rate': 0.1, 
    'max_depth': 10,
    'min_child_weight': 25,
    'n_estimators': 200,
    
    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'seed': SEED,
    'verbosity': 1,
    'n_jobs': -1
}

print("Running KFold validation...")

xgb_model = XGBClassifier(**xgb_params)
model_score, model_std = fit_model_with_skf(X_train, y_train, xgb_model)

print(f'KFold validation mean score: {model_score:.4f}, std: {model_std:.4f}')

# train final model
xgb_model.fit(X_train, y_train)
final_pred = xgb_model.predict_proba(df_test)[:, 1]

# create submission file for kaggle
submission = pd.read_csv("data/competition-data/sample_submission.csv")
submission['smoking'] = final_pred
submission.to_csv('submission.csv', index=False)


# save model
with open(output_file, 'wb') as f_out:
    pickle.dump((xgb_model), f_out)

print(f'The model is saved to {output_file}')
