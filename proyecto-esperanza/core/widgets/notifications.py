import customtkinter as ctk
from ..utils.theme import Theme
from ..utils.animations import Animator

class NotificationManager:
    def __init__(self, root):
        self.root = root
        self.notification_frame = None
    
    def show_notification(self, message, notification_type="info"):
        if self.notification_frame:
            self.notification_frame.destroy()
        
        color_map = {
            "info": Theme.COLORS["primary"],
            "success": Theme.COLORS["success"],
            "warning": Theme.COLORS["warning"],
            "error": "#FF9AA2"  # Rojo pastel
        }
        
        self.notification_frame = ctk.CTkFrame(
            self.root,
            corner_radius=10,
            border_width=2,
            fg_color=color_map[notification_type],
            border_color=Theme.COLORS["text"]
        )
        
        # Posición inicial (fuera de pantalla)
        self.notification_frame.place(
            relx=0.98, rely=0.02,
            anchor="ne", x=200
        )
        
        ctk.CTkLabel(
            self.notification_frame,
            text=message,
            text_color=Theme.COLORS["text"],
            font=("Arial", 12)
        ).pack(padx=20, pady=10)
        
        # Animación de entrada
        Animator.slide_in(self.notification_frame, direction="left")
        
        # Auto-ocultar después de 5 segundos
        self.root.after(5000, self.hide_notification)
    
    def hide_notification(self):
        if self.notification_frame:
            self.notification_frame.destroy()
            self.notification_frame = None