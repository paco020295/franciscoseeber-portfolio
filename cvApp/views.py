from django.http import HttpResponse, JsonResponse, BadHeaderError, HttpResponseBadRequest
from django.shortcuts import render
from django.db.models.functions import Length

from cvApiReviews.models import Review
from .models import Competence
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings


class IndexView(TemplateView):
    template_name = "cvApp/index.html"
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        try:
            data["total_reviews"] = Review.objects.count()
        except:
            data["total_reviews"] = 0
        data["competences"] = Competence.objects.all().order_by("id")
        return data


class MailView(View):
    def post(self, request):
        name = request.POST.get("Name")
        subject = request.POST.get("Subject")
        from_email = request.POST.get("MailFrom")
        message = request.POST.get("Message")

        if subject and message and from_email and name:
            try:
                recipient_list = [settings.EMAIL_HOST_USER, ]
                send_mail(subject, message, from_email, recipient_list)
                pass
            except BadHeaderError:
                return HttpResponseBadRequest('Invalid header found.')
            return HttpResponse('Congratulations')
        
        return HttpResponseBadRequest('Please fill all the fields')

    