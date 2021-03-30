from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    str = ''
    for candidate in candidates:
        str += f'<p>{candidate.name} 기호 {candidate.party_number}번({candidate.area})<br />'
        str += candidate.introduction + "</p>"

    return HttpResponse(str)