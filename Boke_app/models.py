from django.db import models
from datetime import datetime
from user.models import BlogUser


# Create your models here.

class Works(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作品分类'

        verbose_name_plural = verbose_name


class Tags(models.Model):
    name = models.CharField(verbose_name='标签', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'

        verbose_name_plural = verbose_name


class Post(models.Model):
    user = models.ForeignKey(BlogUser, verbose_name='作者')
    category = models.ForeignKey(Works, verbose_name='作品分类', default=None)
    tags = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField(verbose_name='标题', max_length=30, null=False)
    content = models.CharField(verbose_name='内容', max_length=4000, null=False)
    pub_date = models.DateTimeField(verbose_name='发布时间', default=datetime.now)
    cover = models.ImageField(verbose_name='作品封面', upload_to='static/image/post', default=None)
    views = models.IntegerField(verbose_name='浏览量')
    is_recomment = models.BooleanField(verbose_name='是否推荐作品', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '作品'

        verbose_name_plural = verbose_name


class Enjoy(models.Model):
    content = models.ForeignKey(Post, verbose_name='作品介绍')
    cover = models.ImageField(verbose_name='作品欣赏', upload_to='static/image/post', default=None)
    title = models.CharField(verbose_name='作品名称', max_length=30, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '作品'
        verbose_name_plural = verbose_name

class Ming(models.Model):
    name = models.CharField(verbose_name='名人', max_length=30, null=False)
    cover = models.ImageField(verbose_name='图片', upload_to='static/image/post', default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '名人'

        verbose_name_plural = verbose_name


class Picture(models.Model):
    cover = models.ImageField(verbose_name='图片', upload_to='static/image/post', default=None)

    def __str__(self):
        return self.cover

    class Meta:
        verbose_name = '影集'
        verbose_name_plural = verbose_name
