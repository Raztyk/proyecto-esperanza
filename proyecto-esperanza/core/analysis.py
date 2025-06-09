import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime
import customtkinter as ctk

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
        self.clean_data()
    
    def clean_data(self):
        # Convertir fechas y crear columnas de análisis
        self.data['Fecha'] = pd.to_datetime(self.data['Fecha'])
        self.data['Mes'] = self.data['Fecha'].dt.month_name()
        self.data['Año'] = self.data['Fecha'].dt.year
        self.data['Dia_Semana'] = self.data['Fecha'].dt.day_name()
    
    def get_summary(self):
        return {
            'best_month': self.data.groupby('Mes')['Ventas'].sum().idxmax(),
            'worst_month': self.data.groupby('Mes')['Ventas'].sum().idxmin(),
            'total_sales': self.data['Ventas'].sum()
        }
    
    def predict_sales(self, periods):
        model = LinearRegression()
        X = np.array(range(len(self.data))).reshape(-1, 1)
        y = self.data['Ventas'].values
        
        model.fit(X, y)
        future = np.array(range(len(self.data), len(self.data) + periods)).reshape(-1, 1)
        return model.predict(future)