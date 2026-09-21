from src.forms.authorisation.authorisation import Authorisation
from src.forms.authorisation.registration import Registration
from src.forms.components_demo import ComponentsDemo

init_page = 'components_demo'
routes = [
    ("components_demo", ComponentsDemo),
    ("login",    Authorisation),
    ("signup",   Registration),
]