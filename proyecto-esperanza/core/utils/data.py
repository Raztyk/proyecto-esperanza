import pandas as pd
import customtkinter as ctk

class SalesData:
    @staticmethod
    def get_monthly_sales():
        return {
            'meses': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
            'ventas': [1200, 1500, 1800, 2100, 5200, 3400, 3800, 4200, 2900, 5100, 4800, 6200]
        }
    
    @staticmethod
    def get_yearly_summary():
        return {
            'total': 46200,
            'mejor_mes': 'Dic',
            'peor_mes': 'Sep',
            'tendencia': '↑ 18%'
        }