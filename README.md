# Diamonds

## Folder Structure

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