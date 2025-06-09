from fpdf import FPDF
import pandas as pd
from datetime import datetime

class PDFExporter:
    def __init__(self, resumen, resumen_chart, proyecciones=None, consejos=None):
        # Estandariza nombres de columnas si es DataFrame
        if isinstance(resumen, pd.DataFrame):
            resumen.columns = resumen.columns.str.strip().str.lower()
            self.resumen = resumen
        else:
            df = pd.DataFrame(resumen)
            df.columns = df.columns.str.strip().str.lower()
            self.resumen = df

        self.resumen_chart = resumen_chart
        self.proyecciones = proyecciones
        self.consejos = consejos

        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.setup_styles()

    def setup_styles(self):
        self.pdf.set_font("Arial", size=12)
        self.pdf.set_text_color(57, 62, 70)

    def add_title(self, title):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.ln(10)

    def add_summary_section(self):
        self.add_title("Resumen de Ventas")
        self.pdf.set_font("Arial", size=12)
        self.pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
        self.pdf.cell(0, 10, f"Total Ventas: ${self.resumen['ventas'].sum():,}", ln=True)
        self.pdf.ln(5)
        # Gráfico de resumen
        self.pdf.image(self.resumen_chart, x=10, w=190)
        self.pdf.ln(10)
        # Tabla de resumen
        self.add_table(self.resumen, ["mes", "ventas"], ["Mes", "Ventas ($)"])

    def add_projections_section(self):
        if self.proyecciones is not None and not self.proyecciones.empty:
            self.add_title("Proyecciones")
            # Puedes ajustar las columnas según tu DataFrame de proyecciones
            self.add_table(self.proyecciones, self.proyecciones.columns, [col.capitalize() for col in self.proyecciones.columns])

    def add_tips_section(self):
        if self.consejos is not None and len(self.consejos) > 0:
            self.add_title("Consejos")
            self.pdf.set_font("Arial", size=12)
            for idx, consejo in enumerate(self.consejos, 1):
                self.pdf.multi_cell(0, 10, f"{idx}. {consejo}")
            self.pdf.ln(5)

    def add_table(self, df, columns, headers):
        self.pdf.set_font("Arial", 'B', 12)
        for header in headers:
            self.pdf.cell(190 // len(headers), 10, header, border=1)
        self.pdf.ln()
        self.pdf.set_font("Arial", size=10)
        for _, row in df.iterrows():
            for col in columns:
                self.pdf.cell(190 // len(headers), 10, str(row[col]), border=1)
            self.pdf.ln()

    def export(self, filename):
        self.add_summary_section()
        self.add_projections_section()
        self.add_tips_section()
        self.pdf.output(filename)

# --- FUNCIÓN UTILITARIA PARA EXPORTAR PDF ---
def exportar_a_pdf(resumen, resumen_chart, proyecciones, consejos, filename):
    """
    Exporta los datos de análisis a un PDF.
    :param resumen: DataFrame de resumen.
    :param resumen_chart: Ruta de la imagen del gráfico de resumen.
    :param proyecciones: DataFrame de proyecciones.
    :param consejos: Lista de consejos.
    :param filename: Ruta donde guardar el PDF.
    """
    pdf = PDFExporter(resumen, resumen_chart, proyecciones, consejos)
    pdf.export(filename)