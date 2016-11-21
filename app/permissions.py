from rest_framework.permissions import BasePermission
from rest_framework.compat import is_authenticated
from django.contrib.auth.models import User, Group

class AllowAll(BasePermission):

   #Allows access only to authenticated users.

	def has_permission(self, request, view):
		return request.user and is_authenticated(request.user)

class AdminOnly(BasePermission):
    
    #Allows access only to authenticated Admins.
	def has_permission(self, request, view):
		#group = request.user.groups.all()[0].pk

		if  request.user and is_authenticated(request.user):
			return request.user.groups.filter(pk='5').exists() or request.user.groups.filter(pk='6').exists()
		else:
			return False


class SuperAdminOnly(BasePermission):
   
   #Allows access only to authenticated SuperAdmin.

	def has_permission(self, request, view):
		#group = request.user.groups.all()[0].pk
		
		if  request.user and is_authenticated(request.user):
			return request.user.groups.filter(pk='5').exists()
		else:
			return False

