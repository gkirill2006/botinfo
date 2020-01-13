from django.http import Http404, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Draw, DrawBets
#

# def draw(request):
#     last_draws = Draw.objects.order_by('block_number')[:15]
#     return render(request, 'draws/list.html', {'last_draws' : last_draws})

def index(request):
    # last_draws = DrawBets.objects.select_related('Draw', 'DrawBets')
    Total = Draw.objects.filter().count()
    if Total > 10:
        last_draws = Draw.objects.order_by('id')[Total-25:Total]
    else:
        last_draws = Draw.objects.order_by('id')[0:10]
    # last_draws = Draw.objects.order_by('id')
    last_draws.winner_number = int(last_draws.winner_number)
    return render(request, 'draws/list.html', {'last_draws' : last_draws})
    # return HttpResponse("Hello world")

def detail(request,draw_id):
    try:
        a = Draw.objects.get(id = draw_id)
    except:
        raise Http404('Not found')
    all_bets = DrawBets.objects.filter(draw = draw_id)
    return render(request, 'draws/detail.html', {'draw':a, 'bets':all_bets})