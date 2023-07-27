from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("foo", views.foo, name="foo"),
#     ]
app_name = "finance_data"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/detail/", views.detail_question, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

