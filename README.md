# Diamonds

<blockquote class="quoteback" darkmode="" data-title="Diamonds" data-author="@kaggledatasets" cite="https://www.kaggle.com/datasets/shivam2503/diamonds">
<h2 class="sc-bjUoiL sc-idiyUo sc-dOaiCS fykzbL cAPRbO">About Dataset</h2><h3>Context</h3>
<p>This classic dataset contains the prices and other attributes of almost 54,000 diamonds. It's a great dataset for beginners learning to work with data analysis and visualization.</p>
<h3>Content</h3>
<p><strong>price</strong> price in US dollars (\$326--\$18,823)</p>
<p><strong>carat</strong> weight of the diamond (0.2--5.01)</p>
<p><strong>cut</strong> quality of the cut (Fair, Good, Very Good, Premium, Ideal)</p>
<p><strong>color</strong> diamond colour, from J (worst) to D (best)</p>
<p><strong>clarity</strong> a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))</p>
<p><strong>x</strong> length in mm (0--10.74)</p>
<p><strong>y</strong> width in mm (0--58.9)</p>
<p><strong>z</strong> depth in mm (0--31.8)</p>
<p><strong>depth</strong> total depth percentage = z / mean(x, y) = 2 * z / (x + y) (43--79)</p>
<p><strong>table</strong> width of top of diamond relative to widest point (43--95)</p>
<footer>@kaggledatasets<cite> <a href="https://www.kaggle.com/datasets/shivam2503/diamonds">https://www.kaggle.com/datasets/shivam2503/diamonds</a></cite></footer>
</blockquote><script note="" src="https://cdn.jsdelivr.net/gh/Blogger-Peer-Review/quotebacks@1/quoteback.js"></script>


## Features Carat : 
- Carat weight of the Diamond.
- Cut : Describe cut quality of the diamond. 
    - Quality in increasing order Fair, Good, Very Good, Premium, Ideal . 
- Color : Color of the Diamond. . With D being the best and J the worst. 
- Clarity : Diamond Clarity refers to the absence of the Inclusions and Blemishes. 0 (In order from Best to Worst, FL = flawless, 13= level 3 inclusions) FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, 11, 12, 13
- Depth : The Height of a Diamond, measured from the Culet to the table, divided by its average Girdle Diameter.
- Table: The Width of the Diamond's Table expressed as a Percentage of its Average Diameter.
- Price : the Price of the Diamond. 
- X : Length of the Diamond in mm. 
- Y : Width of the Diamond in mm. 
- Z : Height of the Diamond in mm. 

> Qualitative Features (Categorical) : Cut, Color, Clarity.
> Quantitative Features (Numerical) : Carat, Depth, Table, Price , X, Y, Z.
> Price is the Target Variable.

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
- [Diamonds In-Depth Analysis  Kaggle](https://www.kaggle.com/code/fuzzywizard/diamonds-in-depth-analysis)
- [Diamond Price Prediction  Kaggle](https://www.kaggle.com/code/karnikakapoor/diamond-price-prediction)
- [Regression on Diamonds Dataset (95% score)  Kaggle](https://www.kaggle.com/code/heeraldedhia/regression-on-diamonds-dataset-95-score/notebook)