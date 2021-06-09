from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "main"
urlpatterns = [
    path("index", views.index, name="index_page"),
    path("authorize", views.authorize, name="auth_page"),
    path("detail/<int:id>", views.detail, name="detail_page"),
    path("cabinet", views.cabinet_view, name="cabinet"),
    path("logout", views.logout_view, name="logout_view"),
    path("register", views.register, name="register"),
    path("pay_cart", views.pay_cart, name="pay_cart"),
    path("add_cart/<int:id>", views.add_cart, name="add_cart"),
    path("korzina", views.korzina, name="korzina"),
    path("delete_cart_item/<int:id>", views.delete_cart_item, name="delete_cart_item")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)