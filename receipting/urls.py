from . import views as view
from django.urls import include, path

urlpatterns = [
    path('signup/',  view.signup, name='signup'),
    path('login/', view.login_user , name='login'),
    path('logout/',  view.logout_user, name='logout'),
    path('',  view.home, name='home'),
    path('receipts/',  view.receipts, name='receipts'),
    path('receipts/new-receipt',  view.newReceipt, name='new-receipt'),
    path('receipts/<int:pk>',  view.detailsReceipt, name='details-receipt'),
    path('receipts/<int:pk>/update',  view.updateReceipt, name='update-receipt'),
    path('receipts/<int:pk>/delete',  view.deleteReceipt, name='delete-receipt'),
]