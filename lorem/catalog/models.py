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
    tag   = models.ForeignKey('self', null = True, related_name="Parent Tag")


class Item(models.Model):
	mainPhoto	=	ImageWithThumbsField(upload_to='images', sizes=((125,125),(300,300)), blank=True, verbose_name=u"Фото")
	title		=	models.CharField(max_length=255, verbose_name=u"Заголовок")
	alias		=	AutoSlugField(populate_from='title')
	text		=	models.TextField(max_length=255,verbose_name=u"Описание")
	pub_date	=	models.DateTimeField(auto_now_add = True, verbose_name=u"Дата создания")
	upd_date	=	models.DateTimeField(auto_now_add = True, verbose_name=u"Дата изменения1")
	tags            =       models.ManyToManyField(Tag)
        html_title      =       models.TextField(max_length=255,verbose_name="Заголовок страницы", null=True, blank=True)
        html_description=       models.TextField(max_length=255,verbose_name="Описание страницы", null=True, blank=True)
        meta_keywords   =       models.TextField(max_length=255,verbose_name="meta_keywords")

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = " Объявление "
		verbose_name_plural = " Объявления "
    

class InfoCategory(models.Model):
    title = models.TextField(max_length=255)
    alias = models.TextField(max_length=255)

class InfoValue(models.Model):
    value       = models.TextField(max_length=255)
    category    = models.ForeignKey(InfoCategory,)
    item        = models.ForeignKey(Item,)

#class AdvertismentForm(ModelForm):
#	class Meta:
#		model	=	Item
#		fields	=	['category','mainPhoto','title','text']

