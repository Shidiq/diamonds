# Diamonds

## Folder Structure

```
├── README.md
├── data                  # <-- Directory with raw and intermediate data
│   ├── data.xml          # <-- Initial XML StackOverflow dataset (raw data)
│   ├── data.xml.dvc      # <-- .dvc file - a placeholder/pointer to raw data
│   ├── features          # <-- Extracted feature matrices
│   │   ├── test.pkl
│   │   └── train.pkl
│   └── prepared          # <-- Processed dataset (split and TSV formatted)
│       ├── test.tsv
│       └── train.tsv
├── evaluation
│   ├── importance.png    # <-- Feature importance plot
│   └── plots             # <-- Data points for ROC, PRC, confusion matrix
│       ├── confusion_matrix.json
│       ├── precision_recall.json
│       └── roc.json
├── dvc.lock
├── dvc.yaml              # <-- DVC pipeline file
├── model.pkl             # <-- Trained model file
├── params.yaml           # <-- Parameters file
├── evaluation.json       # <-- Binary classifier final metrics (e.g. AUC)
└── src                   # <-- Source code to run the pipeline stages
    ├── evaluate.py
    ├── featurization.py
    ├── prepare.py
    ├── requirements.txt  # <-- Python dependencies needed in the project
    └── train.py
```

## References:

- [10 Things to do when conducting your Exploratory Data Analysis (EDA)  by Alifia C Harmadi  Data Folks Indonesia  Medium](https://medium.com/data-folks-indonesia/10-things-to-do-when-conducting-your-exploratory-data-analysis-eda-7e3b2dfbf812)
- [Exploratory Data Analysis(EDA) Python  by Kaushik Katari  Towards Data Science](https://towardsdatascience.com/exploratory-data-analysis-eda-python-87178e35b14)
- [EDA  Exploratory Data Analysis With Python  What is EDA](https://www.analyticsvidhya.com/blog/2021/06/eda-exploratory-data-analysis-with-python/)
- [A Beginner’s Guide to Exploratory Data Analysis with Python](https://deepnote.com/@code-along-tutorials/A-Beginners-Guide-to-Exploratory-Data-Analysis-with-Python-f536530d-7195-4f68-ab5b-5dca4a4c3579)
- [Detailed exploratory data analysis with python  Kaggle](https://www.kaggle.com/code/ekami66/detailed-exploratory-data-analysis-with-python/notebook)
- [Exploratory Data Analysis EDA For Categorical Data  by Kurtis Pykes  Heartbeat](https://heartbeat.comet.ml/exploratory-data-analysis-eda-for-categorical-data-870b37a79b65)
- [Comprehensive Confidence Intervals for Python Developers  Pythonic Excursions](https://aegis4048.github.io/comprehensive_confidence_intervals_for_python_developers)