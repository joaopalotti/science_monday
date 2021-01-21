#!/usr/bin/env python
# coding: utf-8

# ## PyCaret provides support for:
# - Classification (‘lr’, ‘knn’, ‘nb’, ’dt’, ‘svm’, ‘rbfsvm’, ‘gpc’, ‘mlp’, ‘ridge’, ‘rf’...‘xgboost’, ‘lightgbm’, ‘catboost’)
# - Regression (‘lr’, ‘lasso’, ‘ridge’, ‘en’, ‘lar’, ‘llar’, ... ‘kr’, ‘svm’, ‘knn’, ‘dt’, ‘rf’, ‘et’, ‘ada’, ‘gbr’, ‘mlp’, ‘xgboost’, ‘lightgbm’, ‘catboost’)
# - Clustering (‘kmeans’, ‘ap’, ‘meanshift’, 'sc’, ‘hclust’, ‘dbscan’, ‘optics’, ‘birch’, ‘kmodes’)
# - Anomaly Detection (‘abod’, ‘iforest’, ‘cluster’, ‘cof’, ‘histogram’, ‘knn’, ‘lof’, ‘svm’, ‘pca’, ‘mcd’, ‘sod’, ‘sos‘)
# - Natural Language Processing (‘lda’, ‘lsi’, ‘hdp’, ‘rp’, ‘nmf’)
# 
# #### Some features:
# - Highly configurable, but default parameters are already great
# - Extremely easy way to compare a large number of methods
# - Easy to develop the whole experimental methodology of your paper (CV-Folds, Parameter optimization, Result Analysis, ...)
# - GPU friendly
# 

# In[3]:


from pycaret.datasets import get_data
data = get_data('diabetes')


# In[50]:


# initializing setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable')


# In[5]:


best_model = compare_models()


# In[7]:


# List the currently available models
models()


# In[8]:


lr = create_model('lr')


# In[9]:


tuned_model = tune_model(lr)


# In[13]:


# Options include:
# - optimize (metric you want to optimize, allows user created metric to be used)
# - fold strategy
# - n_iter (max number of tries for random, bayesian search)
# - custom_grid (in case you know what you want to optimize)
# - search_library: scikit-learn, scikit-optimize, tune-sklearn, optuna
# - search_algorithm: random grid search, grid search, bayesian, etc
# - early_stopping

tuned_model = tune_model(lr, n_iter=100, early_stopping=5, optimize="F1")


# 15 out-of-the-box plots:
#    - 'auc' - Area Under the Curve
#    - 'threshold' - Discrimination Threshold
#    - 'pr' - Precision Recall Curve
#    - 'confusion_matrix' - Confusion Matrix
#    - 'error' - Class Prediction Error
#    - 'class_report' - Classification Report
#    - 'boundary' - Decision Boundary
#    - 'rfe' - Recursive Feature Selection
#    - 'learning' - Learning Curve
#    - 'manifold' - Manifold Learning
#    - 'calibration' - Calibration Curve
#    - 'vc' - Validation Curve
#    - 'dimension' - Dimension Learning
#    - 'feature' - Feature Importance
#    - 'feature_all' - Feature Importance (All)
#    - 'parameter' - Model Hyperparameter
#    - 'lift' - Lift Curve
#    - 'gain' - Gain Chart
#    - 'tree' - Decision Tree

# In[17]:


plot_model(tuned_model, plot="auc")


# In[18]:


plot_model(tuned_model, plot="feature")


# In[25]:


plot_model(tuned_model, plot="feature_all")


# In[20]:


plot_model(tuned_model, plot="class_report")


# In[22]:


plot_model(tuned_model, plot="confusion_matrix")


# In[23]:


plot_model(tuned_model, plot="threshold")


# In[29]:


# Or you can see all plots with 'evaluate_model'
evaluate_model(tuned_model)


# In[30]:


# Predictions on the heldout dataset
predict_model(tuned_model)


# Other features:
# - SHAP values with interpret_model
# - Possibility to stack/bag/ensemble models
# - Any classifier that uses the same api as sklean can be used with pycaret
# - Save/Load

# In[33]:


rf = create_model('rf')
interpret_model(rf) # SHAP Values


# In[48]:


dt = create_model('dt')


# In[52]:


ensemble_model(dt, n_estimators=20, method='Bagging')


# In[53]:


lightgbm = create_model('lightgbm', verbose = False)
dt = create_model('dt', verbose = False)
lr = create_model('lr', verbose = False)

# blend individual models (ie., majority votting)
blend_soft = blend_models(estimator_list = [lightgbm, dt, lr], method = 'soft')


# In[55]:


# Using a meta learner
top3 = compare_models(n_select = 3)

xgboost = create_model('xgboost')
stack_soft2 = stack_models(top3, meta_model=xgboost)


# In[57]:


# Using another external classifier
# Example Stanford's NGBoost: https://github.com/stanfordmlgroup/ngboost 
# NGB is not included on the default modules of pycaret
# NGBoost: a Natural Gradient Boosting for Probabilistic Prediction

from ngboost import NGBClassifier 
ngboost = NGBClassifier()
create_model(ngboost)

