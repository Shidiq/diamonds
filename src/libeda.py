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
