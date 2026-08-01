from django.db import models
# Create your models here.

class BookInfo(models.Model):
  name = models.CharField(max_length=200, verbose_name='名称', unique=True)
  pub_date = models.DateField(verbose_name='发布日期', null=True)
  readcount = models.IntegerField(verbose_name='阅读量', default=0)
  commentcount = models.IntegerField(verbose_name='评论量', default=0)
  is_delete = models.BooleanField(verbose_name='是否删除', default=False)
  
  class Meta:
    db_table = 'bookinfo'  # 数据库表名
    verbose_name = '图书'  # 在admin中显示的名称
    verbose_name_plural = '图书'  # 在admin中显示的名称的复数形式

  def __str__(self):
    return self.name

class PeopleInfo(models.Model):
  GENDER_CHOICES = (
    (1, 'male'),
    (2, 'female'),
  )
  name = models.CharField(max_length=100, verbose_name='名字', unique=True)
  gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=1, verbose_name='性别')
  description = models.TextField(verbose_name='描述', null=True)
  is_delete = models.BooleanField(verbose_name='是否删除', default=False)
  book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
  
  class Meta:
    db_table = 'peopleinfo'  # 数据库表名
    verbose_name = '人物'  # 在admin中显示的名称
    verbose_name_plural = '人物'  # 在admin中显示的名称的复数形式 

  def __str__(self):
    return self.name