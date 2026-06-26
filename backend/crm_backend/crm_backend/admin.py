from django.contrib import admin
from lead.models import Lead
from products.models import Product
from team.models import Team
from client.models import Client


admin.site.register(Lead)
admin.site.register(Team)
admin.site.register(Client)
admin.site.register(Product)
