from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """主题Model"""
    text = models.CharField(max_length=200)  # 主题内容
    date_added = models.DateTimeField(auto_now_add=True)  # 创建时间
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # 所属用户

    def __str__(self):
        """字符表达返回主题"""
        return self.text


class Entry(models.Model):
    """条目Model"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)  # 外键
    text = models.TextField()  # 条目内容
    date_added = models.DateTimeField(auto_now_add=True)  # 创建时间

    class Meta:
        """复数形式不是entrys"""
        verbose_name_plural = 'entries'

    def __str__(self):
        """字符表达返回条目缩略"""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return self.text
