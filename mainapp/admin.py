from django.contrib import admin
from .models import Project, Partner, Review, Recall, SendCatalog, SendCatandprice, Quiz, Subscribe


# Register your models here.

class ProjectConfig(admin.ModelAdmin):
    fields = ('object', 'address', 'date', 'task', 'jobs', 'price', 'img1', 'thumb1', 'img2', 'thumb2', 'img3',
              'thumb3', 'img4', 'thumb4', 'img5', 'thumb5', 'img6', 'thumb6')
    list_display = ('object', 'address', 'price',)


admin.site.register(Project, ProjectConfig)


class PartnerConfig(admin.ModelAdmin):
    fields = ('name', 'img',)
    list_display = ('name',)


admin.site.register(Partner, PartnerConfig)


class ReviewConfig(admin.ModelAdmin):
    fields = ('name', 'city', 'img', 'text',)
    list_display = ('name',)


admin.site.register(Review, ReviewConfig)


class RecallConfig(admin.ModelAdmin):
    fields = ('name', 'phone',)
    list_display = ('name', 'phone', 'date')


admin.site.register(Recall, RecallConfig)


class SendCatalogConfig(admin.ModelAdmin):
    fields = ('mail',)
    list_display = ('mail', 'date')


admin.site.register(SendCatalog, SendCatalogConfig)


class SendCatandpriceConfig(admin.ModelAdmin):
    fields = ('name', 'phone', 'mail')
    list_display = ('name', 'phone', 'mail', 'date')


admin.site.register(SendCatandprice, SendCatandpriceConfig)


class QuizConfig(admin.ModelAdmin):
    fields = ('name', 'phone', 'mail', 'door_type', 'price_type', 'style_type', 'size_type', 'material_type')
    list_display = ('name', 'phone', 'mail', 'date')


admin.site.register(Quiz, QuizConfig)


class SubscribeConfig(admin.ModelAdmin):
    fields = ('mail',)
    list_display = ('mail', 'date')


admin.site.register(Subscribe, SubscribeConfig)
