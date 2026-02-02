# Class Imbalance

---

This is a placeholder document for **Class Imbalance**.

**Class Imbalance** is a common problem in machine learning classification tasks where the number of observations per class is not equally distributed. For example, in fraud detection, the vast majority of transactions are non-fraudulent, creating a highly imbalanced dataset.

You can add more content here explaining:
- Why class imbalance is a problem (e.g., models can achieve high accuracy by simply predicting the majority class, but fail to predict the minority class).
- Common techniques to handle class imbalance:
    - **Resampling**: Oversampling the minority class (e.g., SMOTE) or undersampling the majority class.
    - **Cost-sensitive learning**: Assigning a higher misclassification cost to the minority class.
    - **Specialized loss functions**: Using functions like Focal Loss that focus more on hard-to-classify examples.
- Its prevalence in real-world applications like medical diagnosis, anomaly detection, and object detection.

---

## 연관 개념

- [[Hard Negative Mining]]
- [[OHEM]]
- [[Focal Loss]]
- [[SMOTE]]
