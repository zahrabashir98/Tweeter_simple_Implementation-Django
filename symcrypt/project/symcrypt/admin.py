from django.contrib import admin
from symcrypt.models import Sms,TokenPhone,Contact
# Register your models here.

admin.site.register(Sms)
admin.site.register(TokenPhone)
admin.site.register(Contact)