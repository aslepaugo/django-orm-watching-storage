from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long()
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
