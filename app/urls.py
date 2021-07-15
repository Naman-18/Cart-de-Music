from app.forms import LoginForm
from django.contrib import auth
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    #path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
   #path('changepassword/', views.change_password, name='changepassword'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class = MyPasswordChangeForm, success_url='/passwordchangedone/'),name='changepassword'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('acousticguitar/', views.acousticguitar, name='acousticguitar'),
    path('acousticguitar/<slug:data>', views.acousticguitar, name='acousticguitardata'),
    path('electricguitar/', views.electricguitar, name='electricguitar'),
    path('electricguitar/<slug:data>', views.electricguitar, name='electricguitardata'),
    path('classicalguitar/', views.classicalguitar, name='classicalguitar'),
    path('classicalguitar/<slug:data>', views.classicalguitar, name='classicalguitardata'),
   # path('login/', views.login, name='login'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),name='login'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class= MyPasswordResetForm),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'),name='password_reset_done'),
    path('password_reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html',form_class= MySetPasswordForm),name='password_reset_confirm'),
        path('password_reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'),name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    #path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
