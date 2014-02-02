# -*- coding: utf-8 -*-
from django.utils.importlib import import_module
from django.utils.functional import wraps
from django.core.urlresolvers import reverse
import unicodedata
from django.db.models.query import QuerySet
#from catalog.views import Category
#from catalog.views import Item
VERSION	= '0.1'







def t_bread(field=None,	item_model=None,		foreignKey=None, foreignView=None,*args,**kwargs):	
	def add_crumb(field,item_model,foreignKey,foreignView,functionName,*args):
		print "add crumb:"
		print "field: "			+field
		print "item_model: "	+str(item_model)
		print "foreign key: 1: "+str(foreignKey[0])+" 2: "+str(foreignKey[1])
		print "foreignView: "	+str(foreignView)
		print "functionName: "	+str(functionName)
		print "args: "
		for i in (args[0]):
			print i
			
		key = args[0][0]
		
		fname =  functionName.__module__+"."+functionName.__name__
		if foreignView == True: foreignView=functionName
		element=item_model.objects.select_related().filter(**{field:key})[0]
		print "element query result:"
		print element
		foreign_alias = getattr(element,field)
		 
		#if (isinstance(element, QuerySet)):
		#	element=element[0]
		#else:
		#	pass
		
		e = {"url":reverse(fname, args=(foreign_alias,)),"name":str(element.__unicode__())}
		cr =(e,)
		
		if foreignKey[1]:
			if foreignView==functionName:
				cr=getSeflParent(item_model,field,foreignKey,fname,element)+cr
				print "foreignView==functionName"
				print "for "+str(functionName)
			else:
				cr=foreignView(None,getattr(getattr(element,foreignKey[1]),foreignKey[0]))+cr
				print "foreignView!=functionName"
		return cr
	
	def getSeflParent(item_model,field,foreignKey,fname,element):
		foreign_alias = getattr(element,field)
		
		print " 1):	item_model =  "+str(item_model)
		print " 2):	field =	"+ str(field)
		print " 3):	foreignKey = "+ str(foreignKey[0])+", "+str(foreignKey[1])
		print " 4):	fname = "+str(fname)
		print " 5):	element = "+ str(element)
		print " 6):	foreign alias = "+ str(foreign_alias)
		print " 6.1):	element parent = "+ str(element.parent)
		
		if element.parent == None: return ()
		
		element = getattr(element,foreignKey[1])
		#foreign_alias = getattr(element,field)
		key =  getattr(element,field)
		print " 6.2):	key = "+ str(key)
		e = ({"url":reverse(fname, args=(key,)),"name":str(element.__unicode__())},)+ getSeflParent(item_model,field,foreignKey,fname,element)
		print " 6.3):	e = "+str(e)
		
		#element=item_model.objects.select_related().filter(**{foreignKey[1]+'__'+field:foreign_alias})[0]
		#print " 7):	new element = "+ str(element)
		return e		
		
		#print "___________"
		#print getattr(element,'parent')
		
		#print foreignKey
		#print field
		#print key
		#print item_model
		#element=item_model.objects.select_related().filter(**{field:key})
		#print element
		#element=element[0]
		#e = ({"url":reverse(fname, args=(key,)),"name":str(element)},)
		
		#if(element):
		#	e=getSeflParent(item_model,field,foreignKey,fname,element)+e
		#
		return e
				

	def _bread(func):
		@wraps(func)
		def wrapper(request, *args, **kwargs):
			if field!=None:		
					
				crumb =	add_crumb(field,item_model,foreignKey,foreignView,func,args)
				print crumb
			
			# если не приходит реквест (т.е.) если не декорируемая функция. если вызвается дальше по дереву
			# то возвразить крошки
			# иначе добавить крошки в реквестр и вернуть его
			if not request or request == None:
				return crumb
			else:
				if not hasattr(request, 'bread'):	request.breads=()
				request.breads+=(crumb,)
				#print crumb
				return	func(request,*args,**kwargs)
		return wrapper
	return _bread

