from django.db import models

# Create your models here.
# articles를 등록할 수 있는 model
# db에 만들 table
# table을 구성하는 migration파일 만들기

class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=16)
    contents = models.TextField()
    creator = models.CharField(max_length=8)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f'[{self.title}] - created by {self.creator} at {self.created_at.strftime("%Y-%m-%d")}'

    def created_by(self):
        return "created by " + self.creator
    
    def datetime_to_string(self):
        return self.created_at.strftime("%Y-%m-%d")

# python manage.py makemigrations
# python manage.py migrate