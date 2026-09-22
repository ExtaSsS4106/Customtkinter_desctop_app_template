from src.forms.authorisation.authorisation import Authorisation
from src.forms.authorisation.registration import Registration
from src.forms.components_demo import ComponentsDemo
from src.forms.test import testview

init_page = 'testview'
routes = [
    ("testview", testview),
    ("login",    Authorisation),
    ("signup",   Registration),
]