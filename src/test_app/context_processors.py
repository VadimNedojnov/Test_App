from django.conf import settings


def additional_content(request):
    return {'SOME_ADDITIONAL_CONTENT': settings.SOME_ADDITIONAL_CONTENT}
