import customtkinter as ctk
from tkinter import filedialog
from core.utils.pdf_exporter import exportar_a_pdf

class ResultsView(ctk.CTkFrame):
    def __init__(self, parent, analysis, volver_callback=None):
        super().__init__(parent, fg_color="transparent")
        self.pack(fill="both", expand=True)
        self.analysis = analysis
        self.volver_callback = volver_callback

        ctk.CTkLabel(
            self,
            text="Análisis de Ventas Cargado Correctamente",
            font=("Arial", 20)
        ).pack(pady=50)

        # Botón para descargar PDF
        ctk.CTkButton(
            self,
            text="Descargar reporte PDF",
            command=self.descargar_pdf
        ).pack(pady=10)

        # Botón para volver al inicio
        ctk.CTkButton(
            self,
            text="Volver al inicio",
            command=self.volver_inicio
        ).pack(pady=10)

    def descargar_pdf(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Guardar reporte como PDF"
        )
        if ruta:
            exportar_a_pdf(self.analysis, ruta)

    def volver_inicio(self):
        if self.volver_callback:
            self.volver_callback()