# Technical Prompts — Data Science & Machine Learning
**Domain:** Technical | **Subdomain:** Data Science & ML  
**Total Prompts:** 40  
**Evaluation Criteria:** methodological soundness, code quality, statistical correctness, interpretability

---

## Data Analysis & Wrangling

**DS-001**  
`Write a pandas pipeline that ingests a raw sales CSV, removes duplicates, converts date columns, handles null values with domain-appropriate strategies, and outputs a tidy dataframe.`  
*Tags: pandas, data cleaning, pipeline, intermediate*

**DS-002**  
`Given a dataframe with millions of rows, explain three strategies to reduce memory usage. Show a before/after comparison using df.info() and df.memory_usage().`  
*Tags: pandas, memory optimization, performance, intermediate*

**DS-003**  
`Write a Python function that detects statistical outliers in a numerical column using the IQR method and the Z-score method. Discuss when to use each.`  
*Tags: outlier detection, statistics, data quality, intermediate*

**DS-004**  
`Use pandas groupby to compute: total revenue, average order value, and count of orders per customer segment per month. Format the output as a pivot table.`  
*Tags: pandas, groupby, aggregation, intermediate*

**DS-005**  
`Explain the difference between long (tidy) and wide data formats. Use pandas melt() and pivot() to demonstrate converting between them with an example dataset.`  
*Tags: data reshaping, tidy data, pandas, beginner*

**DS-006**  
`Write a regex-based Python function to extract structured fields (date, amount, merchant) from free-text bank transaction descriptions.`  
*Tags: regex, NLP, feature extraction, intermediate*

**DS-007**  
`Perform exploratory data analysis (EDA) on the Titanic dataset. List the exact steps you would take, including visualizations, summary statistics, and key questions to answer.`  
*Tags: EDA, Titanic, visualization, intermediate*

**DS-008**  
`Explain the concept of data leakage in machine learning pipelines. Give three concrete examples and describe how to prevent each.`  
*Tags: data leakage, pipeline design, best practices, advanced*

---

## Visualization

**DS-009**  
`Create a matplotlib figure with 4 subplots showing: a histogram, a boxplot, a scatter plot, and a line chart — all from the same dataset. Add proper labels and titles.`  
*Tags: matplotlib, subplots, visualization, intermediate*

**DS-010**  
`Build an interactive Plotly chart that shows sales trends by region over time. Add a range selector and hover tooltips.`  
*Tags: Plotly, interactive visualization, intermediate*

**DS-011**  
`Explain how to choose between a bar chart, pie chart, and heatmap for presenting categorical data. Give guidelines and anti-patterns for each.`  
*Tags: visualization design, chart selection, conceptual, intermediate*

**DS-012**  
`Create a seaborn pairplot for the Iris dataset. Annotate which feature pairs best separate the three species and explain why.`  
*Tags: seaborn, pairplot, classification insight, beginner*

---

## Machine Learning — Fundamentals

**DS-013**  
`Explain the bias-variance tradeoff with a visual example. How does model complexity affect each, and what is the optimal balance?`  
*Tags: bias-variance, model complexity, conceptual, intermediate*

**DS-014**  
`Implement linear regression from scratch in Python using only NumPy. Derive the normal equation and compare results to sklearn's LinearRegression.`  
*Tags: linear regression, NumPy, from scratch, intermediate*

**DS-015**  
`Train a logistic regression model on a binary classification dataset. Plot the ROC curve, compute AUC, and explain how to choose a decision threshold.`  
*Tags: logistic regression, ROC-AUC, classification, intermediate*

**DS-016**  
`Implement k-fold cross-validation from scratch. Explain why it gives a better estimate of model performance than a single train/test split.`  
*Tags: cross-validation, evaluation, intermediate*

**DS-017**  
`Explain precision, recall, F1-score, and when to prioritize each. Give a medical diagnosis example where recall matters more than precision.`  
*Tags: classification metrics, evaluation, conceptual, intermediate*

**DS-018**  
`Train a decision tree on the Iris dataset. Visualize the tree and explain how the algorithm chooses splits using information gain.`  
*Tags: decision tree, information gain, visualization, intermediate*

**DS-019**  
`Compare Random Forest and Gradient Boosting (XGBoost). When would you choose each? Discuss overfitting risk, interpretability, and training speed.`  
*Tags: ensemble methods, comparison, advanced*

**DS-020**  
`Perform feature engineering on a tabular dataset: create interaction features, encode categoricals, scale numerics, and select features using mutual information. Use sklearn.`  
*Tags: feature engineering, preprocessing, sklearn, intermediate*

---

## Machine Learning — Advanced

**DS-021**  
`Explain how backpropagation works in a neural network. Derive the gradient update for a single hidden-layer network with one output node.`  
*Tags: neural networks, backpropagation, derivation, advanced*

**DS-022**  
`Build a convolutional neural network (CNN) in PyTorch to classify CIFAR-10 images. Report training/validation accuracy and discuss overfitting.`  
*Tags: CNN, PyTorch, image classification, advanced*

**DS-023**  
`Explain the attention mechanism in transformers. How does self-attention differ from cross-attention? Use an NLP example.`  
*Tags: transformers, attention, NLP, advanced*

**DS-024**  
`Implement a simple LSTM in PyTorch for time-series forecasting on a sine wave. Plot predicted vs actual values.`  
*Tags: LSTM, time-series, PyTorch, advanced*

**DS-025**  
`Describe transfer learning and fine-tuning. When would you freeze layers vs. train the entire model? Give an example using HuggingFace.`  
*Tags: transfer learning, NLP, fine-tuning, advanced*

**DS-026**  
`Explain k-means clustering and its limitations. Show how the elbow method and silhouette score can help choose the optimal number of clusters.`  
*Tags: clustering, k-means, unsupervised, intermediate*

**DS-027**  
`Implement principal component analysis (PCA) from scratch using NumPy. Then apply it to reduce a high-dimensional dataset and visualize the result.`  
*Tags: PCA, dimensionality reduction, NumPy, advanced*

**DS-028**  
`Build a recommendation system using collaborative filtering with matrix factorization. Explain implicit vs explicit feedback.`  
*Tags: recommendation systems, matrix factorization, advanced*

---

## NLP

**DS-029**  
`Explain TF-IDF: how it is computed, why it outperforms raw word counts, and how to implement it using sklearn's TfidfVectorizer.`  
*Tags: NLP, TF-IDF, text features, intermediate*

**DS-030**  
`Build a text classification pipeline in Python: preprocess tweets, vectorize with TF-IDF, train a Naive Bayes classifier, evaluate with a classification report.`  
*Tags: NLP, text classification, pipeline, intermediate*

**DS-031**  
`Explain word embeddings (Word2Vec, GloVe, FastText). How do they capture semantic meaning? Demonstrate with word analogy examples.`  
*Tags: word embeddings, semantics, NLP, intermediate*

**DS-032**  
`Describe named entity recognition (NER). Implement a rule-based NER system with spaCy and an ML-based one with HuggingFace. Compare outputs.`  
*Tags: NER, spaCy, HuggingFace, advanced*

---

## Model Deployment & MLOps

**DS-033**  
`Wrap a trained scikit-learn model in a FastAPI endpoint. The endpoint should accept JSON input, run inference, and return predictions with confidence scores.`  
*Tags: deployment, FastAPI, REST API, intermediate*

**DS-034**  
`Explain model drift and data drift. How do you detect them in production? Describe a monitoring strategy using statistical tests.`  
*Tags: MLOps, model drift, monitoring, advanced*

**DS-035**  
`Describe an end-to-end MLOps pipeline for a production ML system: from data ingestion to model serving. Include versioning, experiment tracking, and CI/CD for models.`  
*Tags: MLOps, pipeline design, advanced*

**DS-036**  
`Implement experiment tracking using MLflow for a classification task. Log parameters, metrics, and artifacts for 3 model variants. Compare runs.`  
*Tags: MLflow, experiment tracking, intermediate*

---

## Ethics & Fairness

**DS-037**  
`Explain algorithmic bias in machine learning. Give a real-world case study (e.g., hiring, lending, criminal justice) and propose mitigation strategies.`  
*Tags: AI ethics, bias, fairness, advanced*

**DS-038**  
`What is demographic parity vs equalized odds as fairness metrics? Implement both for a loan approval model and discuss the tradeoff between them.`  
*Tags: fairness metrics, ethics, advanced*

**DS-039**  
`Explain differential privacy and why it matters for ML on sensitive data. How does it apply to federated learning?`  
*Tags: privacy, differential privacy, federated learning, advanced*

**DS-040**  
`Describe explainability methods for black-box models: SHAP, LIME, and integrated gradients. When is model explainability a legal or ethical requirement?`  
*Tags: explainability, SHAP, LIME, XAI, advanced*
