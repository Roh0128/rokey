import statsmodels.api as sm

data=sm.datasets.get_rdataset("mtcars").data
print(data)