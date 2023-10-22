from django.urls import path
from .import views
from .import cart

urlpatterns =[
    path('',views.home,name='home'),#home page ur;
    path('collections',views.collections,name="collections"),#collections page url  
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),#all collections page url       
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),#url to view the particular product
    path('register',views.register,name='register'),#url for registering users  
    path('login',views.user_login,name='login'),#url for login the users    
    path('logout',views.user_logout,name='logoutof'),#url for logout the users  
    path('add-to-cart',cart.addtocart,name='addtocart'),#url for addtocart functionality    
    path('cart',cart.viewcart,name='cart'),#url to view the cart
 


    
]