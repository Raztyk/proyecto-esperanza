import customtkinter as ctk
import matplotlib.pyplot as plt

class Theme:
    COLORS = {
        "primary": "#A8D8EA",  # Azul pastel
        "secondary": "#AA96DA",  # Lila pastel
        "accent": "#FCBAD3",  # Rosa pastel
        "background": "#FFFFD2",  # Amarillo muy claro
        "surface": "#E8F9FD",  # Blanco azulado
        "text": "#393E46",  # Gris oscuro para contraste
        "success": "#A6E3A1",  # Verde pastel
        "warning": "#FFD3B4"  # Naranja pastel
    }

    @classmethod
    def setup_theme(cls):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme(cls.get_ctk_theme())
        cls.setup_matplotlib_theme()

    @classmethod
    def get_ctk_theme(cls):
        return {
            "fg_color": cls.COLORS["background"],
            "button_color": cls.COLORS["primary"],
            "button_hover_color": cls.COLORS["secondary"],
            "text_color": cls.COLORS["text"],
            "entry_fg_color": cls.COLORS["surface"]
        }

    @classmethod
    def setup_matplotlib_theme(cls):
        plt.style.use('ggplot')
        plt.rcParams['axes.facecolor'] = cls.COLORS["surface"]
        plt.rcParams['figure.facecolor'] = cls.COLORS["background"]
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
            cls.COLORS["primary"], 
            cls.COLORS["secondary"], 
            cls.COLORS["accent"],
            cls.COLORS["success"]
        ])