# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField
from autoslug.fields import AutoSlugField
#для миграций превьюшек
from south.modelsinspector import add_introspection_rules
from django.forms import ModelForm
#from myadpp.models import Article
#from mptt.models import MPTTModel, TreeForeignKey

from redactor.fields import RedactorField

#from lib.thumbs import ImageWithThumbsField
if 1:
    add_introspection_rules([
        (
            [ImageWithThumbsField], # Class(es) these apply to
            [],         # Positional arguments (not used)
            {           # Keyword argument
                "sizes": ["sizes", {}],
            },
        ),
    ], ["^django_thumbs\.db\.models\.ImageWithThumbsField"])




class Tag(models.Model):
    title = models.CharField(max_length=255)
    alias = AutoSlugField(max_length=255)
    tag   = models.ForeignKey('self', null = True, blank = True, related_name="Parent Tag")
    def __unicode__(self):
        return self.title




class Item(models.Model):
	mainPhoto	=	ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,300)), blank=True, verbose_name=u"Фото")
	title		=	models.CharField(max_length=255, verbose_name=u"Заголовок")
	alias		=	AutoSlugField(populate_from='title')
	text		=	RedactorField(verbose_name=u"Описание")
	pub_date	=	models.DateTimeField(auto_now_add = True, verbose_name=u"Дата создания")
	upd_date	=	models.DateTimeField(auto_now_add = True, verbose_name=u"Дата изменения1")
	tags            =       models.ManyToManyField(Tag)
        html_title      =       models.TextField(max_length=255,verbose_name="Заголовок страницы", null=True, blank=True)
        html_description=       models.TextField(max_length=255,verbose_name="Описание страницы", null=True, blank=True)
        meta_keywords   =       models.TextField(max_length=255,verbose_name="meta_keywords", null=True, blank=True)
        item_type       =       models.CharField(max_length=255,verbose_name="Тип статьи",choices = (('n','Новая'),('g','Хорошая'),('b','Лучшая')), default='n');
	def __unicode__(self):
		return self.title
        def get_absolute_url(self):
            return "/boobs/%s" % self.alias
	class Meta:
		verbose_name = " Сиськи "
		verbose_name_plural = " Сиськи  "
    

class InfoCategory(models.Model):
    title = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    def __unicode__(self):
        return self.title

class InfoValue(models.Model):
    value       = models.CharField(max_length=255)
    category    = models.ForeignKey(InfoCategory,)
    item        = models.ForeignKey(Item,)
#class AdvertismentForm(ModelForm):
#	class Meta:
#		model	=	Item
#		fields	=	['category','mainPhoto','title','text']

