import pandas as pd


class EDA:
    @staticmethod
    def cat_value_counts(data):
        categorical_features = [
            i for i, j in dict(data.dtypes).items() if j == object
        ]

        for f in categorical_features:
            print("\nCategorical feature: ", f)
            print(" ")
            print(data[f].value_counts())

    @staticmethod
    def checknum_skew_kurtosis(data):
        data_num = data.select_dtypes(include=["float64", "int64"])

        res = pd.DataFrame()

        for f in list(data_num):
            out = dict(data[f].agg(["skew", "kurtosis"]))
            res.loc[f, "Skewness"] = out["skew"]
            res.loc[f, "Kurtosis"] = out["kurtosis"]

        return res
