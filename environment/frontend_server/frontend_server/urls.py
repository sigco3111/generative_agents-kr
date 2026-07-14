"""frontend_server URL Configuration (Django 4.x compatible)

원본: joonspk-research/generative_agents
변경 (sigco3111):
- Django 2.2의 `django.conf.urls.url` → Django 4.x의 `re_path` (url은 4.0에서 제거됨)
- 모든 url 패턴을 re_path()로 마이그레이션
"""
from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from translator import views as translator_views

urlpatterns = [
    re_path(r'^$', translator_views.landing, name='landing'),
    re_path(r'^simulator_home$', translator_views.home, name='home'),
    re_path(r'^demo/$', translator_views.demo_index, name='demo_index'),
    re_path(r'^demo/(?P<sim_code>[\w-]+)/(?P<step>[\w-]+)/(?P<play_speed>[\w-]+)/$', translator_views.demo, name='demo'),
    re_path(r'^replay/(?P<sim_code>[\w-]+)/(?P<step>[\w-]+)/$', translator_views.replay, name='replay'),
    re_path(r'^replay_persona_state/(?P<sim_code>[\w-]+)/(?P<step>[\w-]+)/(?P<persona_name>[\w-]+)/$', translator_views.replay_persona_state, name='replay_persona_state'),
    re_path(r'^process_environment/$', translator_views.process_environment, name='process_environment'),
    re_path(r'^update_environment/$', translator_views.update_environment, name='update_environment'),
    re_path(r'^path_tester/$', translator_views.path_tester, name='path_tester'),
    re_path(r'^path_tester_update/$', translator_views.path_tester_update, name='path_tester_update'),
    path('admin/', admin.site.urls),
]
