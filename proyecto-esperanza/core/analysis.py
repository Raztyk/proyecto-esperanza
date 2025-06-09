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
        # Estandariza los nombres de las columnas a minúsculas y sin espacios
        self.data.columns = self.data.columns.str.strip().str.lower()
        # Validación de columnas requeridas
        required = {'cantidad', 'precio', 'fecha'}
        if not required.issubset(self.data.columns):
            raise ValueError(f"Faltan columnas requeridas: {required - set(self.data.columns)}. Columnas encontradas: {self.data.columns.tolist()}")
        self.data['fecha'] = pd.to_datetime(self.data['fecha'], dayfirst=True, errors='coerce')
        if self.data['fecha'].isnull().any():
            print("Advertencia: Hay fechas no válidas en los datos.")
        self.data['mes'] = self.data['fecha'].dt.month_name()
        self.data['año'] = self.data['fecha'].dt.year
        self.data['dia_semana'] = self.data['fecha'].dt.day_name()
        self.data['cantidad'] = pd.to_numeric(self.data['cantidad'], errors='coerce')
        self.data['precio'] = pd.to_numeric(self.data['precio'], errors='coerce')
        self.data['ventas'] = self.data['cantidad'] * self.data['precio']
        # --- DEPURACIÓN ---
        print("Columnas:", self.data.columns.tolist())
        print("Primeras filas:\n", self.data.head())
        print("¿'ventas' en columnas?:", 'ventas' in self.data.columns)
            
    def get_summary(self):
        return {
            'best_month': self.data.groupby('mes')['ventas'].sum().idxmax(),
            'worst_month': self.data.groupby('mes')['ventas'].sum().idxmin(),
            'total_sales': self.data['ventas'].sum()
        }
    
    def predict_sales(self, periods):
        model = LinearRegression()
        X = np.array(range(len(self.data))).reshape(-1, 1)
        y = self.data['ventas'].values
        model.fit(X, y)
        future = np.array(range(len(self.data), len(self.data) + periods)).reshape(-1, 1)
        return model.predict(future)

    def get_projection(self, months):
        """Devuelve la proyección de ventas para los próximos 'months' meses."""
        return self.predict_sales(months)