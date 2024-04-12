'''
title: 할 일의 제목을 나타내며 최대 100자까지 저장 가능
description: 할 일의 상세 설명을 위한 필드 TextField로 글자 제한을 두지 않음 필수 입력 x
due_date: 할 일의 마감 기한 선택 입력 가능
completed: 할 일 완료 여부 기본 값 false
created: 생성된 날짜와 시간 자동 기록
'''
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  
    due_date = models.DateTimeField(blank=True, null=True)   
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
