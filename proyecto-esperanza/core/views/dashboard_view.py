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
    def __init__(self, parent, analysis, volver_callback=None):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        self.analysis = analysis
        self.volver_callback = volver_callback

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

        # --- Botones centrados en la parte inferior ---
        boton_frame = ctk.CTkFrame(resumen_tab, fg_color="transparent")
        boton_frame.pack(side="bottom", pady=30)

        ctk.CTkButton(
            boton_frame,
            text="Descargar reporte PDF",
            command=self.descargar_pdf
        ).pack(side="left", padx=20)

        ctk.CTkButton(
            boton_frame,
            text="Volver al inicio",
            command=self.volver_inicio
        ).pack(side="left", padx=20)

    def descargar_pdf(self):
        from tkinter import filedialog, messagebox
        from core.utils.pdf_exporter import exportar_a_pdf
        import os

        ruta = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar reporte como PDF"
        )
        if ruta:
            try:
                # Guardar gráfico de resumen como imagen temporal
                resumen_chart_path = "resumen_chart_temp.png"
                self.guardar_grafico_resumen(resumen_chart_path)

                # Obtén proyecciones y consejos desde analysis (ajusta según tu estructura)
                proyecciones = getattr(self.analysis, "proyecciones", None)
                consejos = getattr(self.analysis, "consejos", None)

                exportar_a_pdf(
                    resumen=self.analysis.data,
                    resumen_chart=resumen_chart_path,
                    proyecciones=proyecciones,
                    consejos=consejos,
                    filename=ruta
                )
                # Elimina el archivo temporal después de usarlo
                if os.path.exists(resumen_chart_path):
                    os.remove(resumen_chart_path)
                messagebox.showinfo("Éxito", f"Reporte guardado en:\n{ruta}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el PDF:\n{e}")

    def guardar_grafico_resumen(self, path):
        import matplotlib.pyplot as plt
        data = self.analysis.data
        ventas_por_mes = data.groupby('mes')['ventas'].sum()
        meses_es = [MESES_ES.get(m, m) for m in ventas_por_mes.index]
        fig, ax = plt.subplots(figsize=(8, 2))
        ventas_por_mes.plot(kind='bar', ax=ax, color='#4e79a7')
        ax.set_title("Ventas por Mes", fontsize=10)
        ax.set_ylabel("Ventas")
        ax.set_xticklabels(meses_es)
        ax.grid(True, linestyle='--', alpha=0.6)
        fig.tight_layout()
        fig.savefig(path, bbox_inches='tight')
        plt.close(fig)

    def volver_inicio(self):
        if self.volver_callback:
            self.volver_callback()