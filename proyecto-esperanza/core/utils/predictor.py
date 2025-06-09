import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from ..utils.theme import Theme

class SalesPredictor:
    def __init__(self, data):
        self.data = data
        self.model = LinearRegression()
        self.poly = PolynomialFeatures(degree=2)
    
    def predict_year(self):
        X = np.array(range(len(self.data['ventas']))).reshape(-1, 1)
        y = np.array(self.data['ventas'])
        
        # Entrenar modelo
        X_poly = self.poly.fit_transform(X)
        self.model.fit(X_poly, y)
        
        # Predecir próximo año
        future = np.array(range(len(self.data['ventas']), len(self.data['ventas']) + 12)).reshape(-1, 1)
        future_poly = self.poly.transform(future)
        predictions = self.model.predict(future_poly)
        
        return predictions
    
    def seasonal_analysis(self):
        df = pd.DataFrame(self.data)
        df['month'] = pd.to_datetime(df['meses'], format='%b').dt.month
        seasonal = df.groupby('month')['ventas'].mean()
        return seasonal
    
    def detect_outliers(self):
        q1 = np.percentile(self.data['ventas'], 25)
        q3 = np.percentile(self.data['ventas'], 75)
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        
        outliers = [
            (mes, venta) for mes, venta in zip(self.data['meses'], self.data['ventas'])
            if venta < lower_bound or venta > upper_bound
        ]
        
        return outliers