from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at__isnull=True):
        visit_duration = visit.get_duration()
        non_closed_visits.append({
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': visit.format_duration(visit_duration),
            'is_strange': visit.is_visit_long(visit_duration)
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
