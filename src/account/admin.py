from django.contrib import admin


from account.models import User


class UserAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'is_active',
        'birth_date',
        'biography',
        'phone',
        'linkedin_link',
        'githab_link',
        'twitter_link',
        'facebook_link'

    ]


admin.site.register(User, UserAdmin)
