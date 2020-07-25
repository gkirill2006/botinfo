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
    return render(request, 'draws/list.html', {'last_draws' : last_draws})
    # return HttpResponse("Hello world")

def detail(request,draw_id):
    try:
        a = Draw.objects.get(id = draw_id)
        # a.winner_number = int(a.winner_number)

    except:
        raise Http404('Not found')
    try:
        a.winner_number = int(a.winner_number)
    except:
        pass
    all_bets = DrawBets.objects.filter(draw = draw_id)
    new_bets = []
    pn = 1
    count_win = 0
    with_wallet = 0
    with_wallet_win = 0
    for item in all_bets:
        new_bets.append({'pn': pn, 'btc_address': item.btc_address, 'number': item.number})
        pn += 1
        if item.btc_address:
            with_wallet +=1
        if a.winner_number == item.number:
            count_win +=1
            if item.btc_address:
                with_wallet_win +=1
    stata = {'pn' : pn, 'count_win' : count_win, 'with_wallet' : with_wallet, 'with_wallet_win': with_wallet_win, }
    return render(request, 'draws/detail.html', {'draw': a, 'bets': new_bets, 'stata' : stata})