#todo 모델을 관리자 페이지에서 볼 수 있도록 설계

from django.contrib import admin
from .models import Todo

admin.site.register(Todo)