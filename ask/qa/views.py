from ask.django import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')
