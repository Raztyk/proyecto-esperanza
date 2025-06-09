import customtkinter as ctk
from .projections_view import ProjectionsView
from .tips_view import TipsView
from .graficos import GraficosView

# Diccionario de traducción de meses
MESES_ES = {
    "January": "Enero", "February": "Febrero", "March": "Marzo", "April": "Abril",
    "May": "Mayo", "June": "Junio", "July": "Julio", "August": "Agosto",
    "September": "Septiembre", "October": "Octubre", "November": "Noviembre", "December": "Diciembre",
    "Jan": "Ene", "Feb": "Feb", "Mar": "Mar", "Apr": "Abr",
    "May": "May", "Jun": "Jun", "Jul": "Jul", "Aug": "Ago",
    "Sep": "Sep", "Oct": "Oct", "Nov": "Nov", "Dec": "Dic"
}

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent, analysis):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        self.analysis = analysis

        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True)

        self.tabview.add("Resumen")
        self.tabview.add("Proyecciones")
        self.tabview.add("Consejos")
        self.tabview.add("Gráficos")

        self.setup_summary_tab()

        projections = ProjectionsView(self.tabview.tab("Proyecciones"), analysis)
        projections.pack(fill="both", expand=True)

        tips = TipsView(self.tabview.tab("Consejos"), analysis)
        tips.pack(fill="both", expand=True)

        graficos = GraficosView(self.tabview.tab("Gráficos"))
        graficos.pack(fill="both", expand=True)

    def setup_summary_tab(self):
        resumen_tab = self.tabview.tab("Resumen")
        data = self.analysis.data

        total_ventas = data['ventas'].sum()
        ventas_por_mes = data.groupby('mes')['ventas'].sum()
        mejor_mes = ventas_por_mes.idxmax()
        peor_mes = ventas_por_mes.idxmin()
        mejor_mes_es = MESES_ES.get(mejor_mes, mejor_mes)
        peor_mes_es = MESES_ES.get(peor_mes, peor_mes)

        ctk.CTkLabel(resumen_tab, text=f"Total de Ventas: ${total_ventas:,.2f}", font=("Arial", 16, "bold")).pack(pady=10)
        ctk.CTkLabel(resumen_tab, text=f"Mejor Mes: {mejor_mes_es}", font=("Arial", 14)).pack(pady=5)
        ctk.CTkLabel(resumen_tab, text=f"Peor Mes: {peor_mes_es}", font=("Arial", 14)).pack(pady=5)

        # Gráfico resumen de ventas por mes
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

        meses_es = [MESES_ES.get(m, m) for m in ventas_por_mes.index]
        fig, ax = plt.subplots(figsize=(8, 2))
        ventas_por_mes.plot(kind='bar', ax=ax, color='#4e79a7')
        ax.set_title("Ventas por Mes", fontsize=10)
        ax.set_ylabel("Ventas")
        ax.set_xticklabels(meses_es)
        ax.grid(True, linestyle='--', alpha=0.6)
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=resumen_tab)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="x", padx=10, pady=10)