import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from ..utils.theme import Theme
import customtkinter as ctk

class SalesPredictor:
    def __init__(self, data):
        # Si es DataFrame, estandariza nombres de columnas
        if isinstance(data, pd.DataFrame):
            data.columns = data.columns.str.strip().str.lower()
            self.data = data
        else:
            # Si es dict o similar, convierte a DataFrame y estandariza
            df = pd.DataFrame(data)
            df.columns = df.columns.str.strip().str.lower()
            self.data = df

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
        df = self.data.copy()
        # Asegura que la columna sea 'meses' en minúsculas
        if 'meses' in df.columns:
            df['month'] = pd.to_datetime(df['meses'], format='%b').dt.month
            seasonal = df.groupby('month')['ventas'].mean()
            return seasonal
        else:
            raise KeyError("La columna 'meses' no está presente en los datos.")
    
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