from django.http import JsonResponse


def testView(request):
    return JsonResponse({"dcdc":"123"})