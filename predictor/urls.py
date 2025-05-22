from django.urls import path
from .views import SatisfactionPredictView, prediction_history

urlpatterns = [
    path("predict/", SatisfactionPredictView.as_view(), name="predict"),
    path("history/", prediction_history, name="history"),
]
