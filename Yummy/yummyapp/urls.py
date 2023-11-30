
from django.contrib import admin
from django.urls import path
from yummyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('hero/', views.index, name="hero"),
    # path('employee/', views.employee, name="employee"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('chefs/', views.chefs, name="chefs"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('order/', views.order, name="order"),
    path('pay/', views.pay, name="pay"),
    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
    path('success/', views.success, name='success'),
    # path('show/', views.show, name="show"),
    # path('delete/<int:id>', views.delete),
    # path('edit/<int:id>', views.edit),
    # path('update/<int:id>', views.update),
]
