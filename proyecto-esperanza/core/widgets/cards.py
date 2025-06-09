import customtkinter as ctk

class InfoCard(ctk.CTkFrame):
    def __init__(self, parent, title, value, trend):
        super().__init__(parent, corner_radius=10)
        
        self.title_label = ctk.CTkLabel(
            self, 
            text=title,
            font=("Arial", 12),
            text_color="#aaaaaa"
        )
        self.title_label.pack(pady=(10, 0))
        
        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=("Arial", 24, "bold")
        )
        self.value_label.pack(pady=5)
        
        self.trend_label = ctk.CTkLabel(
            self,
            text=trend,
            font=("Arial", 12),
            text_color="#59a14f" if "↑" in trend else "#e15759"
        )
        self.trend_label.pack(pady=(0, 10))
        
        self.configure(
            fg_color="#3e3e3e",
            border_width=1,
            border_color="#4e4e4e"
        )