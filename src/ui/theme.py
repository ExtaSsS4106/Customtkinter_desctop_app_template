import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Цвета
BG = "transparent"
CARD_BG = ("#f0f0f0", "#1f1f1f")
ERROR_COLOR = "#e05252"
SUCCESS_COLOR = "#4caf50"

# Размеры
ENTRY_WIDTH = 280
ENTRY_HEIGHT = 38
BUTTON_HEIGHT = 38
PAD = 8


def make_entry(parent, placeholder, show=None):
    return ctk.CTkEntry(
        parent,
        width=ENTRY_WIDTH,
        height=ENTRY_HEIGHT,
        placeholder_text=placeholder,
        show=show,
        corner_radius=8,
    )


def make_button(parent, text, command, **kwargs):
    return ctk.CTkButton(
        parent,
        text=text,
        command=command,
        width=ENTRY_WIDTH,
        height=BUTTON_HEIGHT,
        corner_radius=8,
        **kwargs,
    )


def make_error_label(parent):
    return ctk.CTkLabel(
        parent,
        text="",
        text_color=ERROR_COLOR,
        font=("", 12),
    )