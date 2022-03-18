"""reborn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
##추가
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),

    # ## 추가 (리뷰등록구현)
    # path('list/', views.list, name = "list"),
    # path('create/', views.create, name = "product-create"),
    # path('update/', views.update, name = "product-update"),
    # # path('detail/', views.detail, name = "product-detail"),
    # path('delete/', views.list, name = "product-delete"),
    # path('product/<int:id>/', views.detail,name="product-detail"),
    
]


##github 추가
# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
# 	url(r'^$', 'shopping.views.index'),
# 	url(r'product/(?P<resource_id>\d+)', 'shopping.views.show'),
#     url(r'favorite/(?P<resource_id>\d+)', 'shopping.views.favorite'),
#     url(r'favorites', 'shopping.views.favorites'),
# 	url(r'comment/create', 'shopping.views.comment'),
# 	url(r'comment/delete/(?P<resource_id>\d+)', 'shopping.views.delete_comment'),
#     url(r'accounts/login', 'shopping.views.login'),
#     url(r'accounts/logout', 'shopping.views.logout'),
#     url(r'accounts/authenticate', 'shopping.views.authenticate'),
#     url(r'accounts/signup', 'shopping.views.signup'),
#     url(r'accounts/create', 'shopping.views.create'),
#     # Examples:
#     # url(r'^$', 'minishop.views.home', name='home'),
#     # url(r'^minishop/', include('minishop.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),
# )