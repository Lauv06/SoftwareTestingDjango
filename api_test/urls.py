from django.conf.urls import url, include
from .views import *

# url
urlpatterns = [
    url(r"triangle$", Triangle, ),
    url(r"triangleTest$", TriangleTest, ),
    url(r"computer$", Computer, ),
    url(r"computerTest$", ComputerTest, ),
    url(r"telephone$", Telephone, ),
    url(r"telephoneTest$", TelephoneTest, ),
    url(r"calendar$", Calendar, ),
    url(r"calendarTest$", CalendarTest, ),
    url(r"atm$", ATM, ),
    url(r"atmTest$", ATMTest, ),
]
