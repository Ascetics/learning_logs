from django.urls import path
from learning_logs import views

app_name = 'learning_logs'

urlpatterns = [
    # learning log首页
    path('', views.index, name='index'),
    # topics页面显示所有topics
    path('topics/', views.topics, name='topics'),
    # topic页面显示一个主题及所有条目
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # new_topic页面添加新主题
    path('new_topic/', views.new_topic, name='new_topic'),
    # new_entry页面给特定主题添加条目
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit_entry编辑条目
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
