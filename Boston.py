from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)
boston = load_boston()

print(boston.keys())

print(boston.data.shape)

print(boston.feature_names)

