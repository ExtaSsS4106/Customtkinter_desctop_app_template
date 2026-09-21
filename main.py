# Requires CustomTkinter:  pip install customtkinter
from src.forms.authorisation.authorisation import Authorisation
from src.forms.authorisation.registration import Registration
from conf.app import App


if __name__ == "__main__":
    app = App()
    app.init_page()
    app.mainloop()