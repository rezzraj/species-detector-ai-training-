# **Iris Dataset Analysis & KNN Classification**

### **Overview**
This project analyzes the **Iris dataset** and builds a **machine learning model** using the **K-Nearest Neighbors (KNN)** algorithm to classify iris flower species based on their measurements.  
It also includes **data visualization** using Seaborn and Matplotlib.

---

## **Features**
✔ Loads and processes the **Iris dataset**  
✔ Visualizes data using **Seaborn & Matplotlib**  
✔ Implements **KNN classifier** for species prediction  
✔ Calculates **model accuracy**  
✔ Predicts **species for new input samples**  

---

## **Workflow**
1. **Data Loading:** Fetches Iris dataset using `sklearn.datasets.load_iris()`.
2. **Data Preparation:** Converts dataset to a pandas DataFrame and maps species names.
3. **Visualization:**  
   - **Species Distribution:** Count plot  
   - **Pair Plot:** Relationships between features  
   - **Scatter Plot:** Sepal length vs. sepal width colored by species  
4. **Model Training:**  
   - Splits dataset into **80% training** and **20% testing**  
   - Trains **K-Nearest Neighbors** classifier (k = 3)  
5. **Evaluation:**  
   - Calculates accuracy score  
   - Predicts species for a sample input  

---

## **Visualizations**
- **Species Distribution:** Shows the number of samples for each species  
- **Pair Plot:** Compares features across species  
- **Scatter Plot:** Sepal length vs. sepal width, colored by species  

---

## **Model Performance**
| Metric      | Value      |
|-------------|-----------|
| **Accuracy**| ~96.67%   |

---

## **Example Prediction**
Input: [1, 3.5, 1.4, 299]
Predicted species: setosa

---

## **Requirements**
- Python 3.x
- **Libraries:**
  - scikit-learn
  - pandas
  - numpy
  - matplotlib
  - seaborn

---

## **Why This Project?**
✅ Great for **beginners in ML & Data Science**  
✅ Covers **data visualization + model training** in one workflow  
✅ Shows **practical use of K-Nearest Neighbors (KNN)**  

---

## **Future Enhancements**
- Try different **k-values** and compare results  
- Implement **other classifiers** like Decision Tree or SVM  
- Deploy as a **simple web app** for live predictions  

---
