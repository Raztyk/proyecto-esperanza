from .views.upload_view import UploadView
from .views.results_view import ResultsView
from .analysis import SalesAnalyzer

class App(ctk.CTk):
    def __init__(self):
        # ... (código existente)
        self.current_data = None
        self.show_upload()
    
    def show_upload(self):
        self.clear_main_frame()
        UploadView(self.main_frame, self)
    
    def process_data(self, df):
        self.current_data = SalesAnalyzer(df)
        self.show_results()
    
    def show_results(self):
        self.clear_main_frame()
        ResultsView(self.main_frame, self.current_data)