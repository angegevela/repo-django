"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,  BoatListView, BoatCreateView, BoatUpdateView, BoatDeleteView
from django.contrib.auth import views as auth_views

from fire.views import HomePageView, ChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart/', ChartView.as_view(), name='dashboard-chart'),
    
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),


    path('orgmember-list', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember-list/add',OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember-list/<pk>',OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember-list/<pk>/delete',OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    path('student-list', StudentList.as_view(), name='student-list'),
    path('student-list/add', StudentCreateView.as_view(), name='student-add'),
    path('student-list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('student-list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),


    path('college/', CollegeList.as_view(), name='college-list'),
    path('college/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college/<pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college/<pk>/delete/', CollegeDeleteView.as_view(), name='college-delete'),

    path('program/', ProgramList.as_view(), name='program-list'),
    path('program/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program/<pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program/<pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),


    #path for login and logout
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),


     # Chart view path (using ChartView here as the view)
    path('chart/', ChartView.as_view(), name='chart_view'), 

    path('boats/', BoatListView.as_view(), name='boat-list'),
    path('boats/add/', BoatCreateView.as_view(), name='boat-add'),
    path('boats/<int:pk>/edit/', BoatUpdateView.as_view(), name='boat-edit'),
    path('boats/<int:pk>/delete/', BoatDeleteView.as_view(), name='boat-delete'),
]
