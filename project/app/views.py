from django.shortcuts import render
from app.models import Item
from django.shortcuts import render_to_response, RequestContext

def chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

def cmp(object):
    return int(object.price)

def main(request, offset = None, parameter = None):
    if (offset):    
        off = int(offset)
    else:
        off = 0
    if (off > 0):
        prev = '/' + str(off - 1) + '/'
    else:
        prev = None
    next = None    
    long_items = Item.objects.all()[32 * off: 32 * off + 32]
    if (parameter == 'sortdown'):
        long_items = Item.objects.order_by('-price')[32 * off: 32 * off + 32]
    if (parameter == 'sortup'):
        long_items = Item.objects.order_by('price')[32 * off: 32 * off + 32]
    if (parameter == 'kompdown'):
        long_items = Item.objects.order_by('-komp')[32 * off: 32 * off + 32]
    if (parameter == 'kompup'):
        long_items = Item.objects.order_by('komp')[32 * off: 32 * off + 32]
    if (parameter == 'speeddown'):
        long_items = Item.objects.order_by('-speed')[32 * off: 32 * off + 32]
    if (parameter == 'speedup'):
        long_items = Item.objects.order_by('speed')[32 * off: 32 * off + 32]
    if (parameter == 'uprdown'):
        long_items = Item.objects.order_by('-upr')[32 * off: 32 * off + 32]
    if (parameter == 'uprup'):
        long_items = Item.objects.order_by('upr')[32 * off: 32 * off + 32]
    if (parameter == 'ustdown'):
        long_items = Item.objects.order_by('-ust')[32 * off: 32 * off + 32]
    if (parameter == 'ustup'):
        long_items = Item.objects.order_by('ust')[32 * off: 32 * off + 32]
    if (parameter == 'amordown'):
        long_items = Item.objects.order_by('-amor')[32 * off: 32 * off + 32]
    if (parameter == 'amorup'):
        long_items = Item.objects.order_by('amor')[32 * off: 32 * off + 32]
    if (parameter == 'gibdown'):
        long_items = Item.objects.order_by('-gib')[32 * off: 32 * off + 32]
    if (parameter == 'gibup'):
        long_items = Item.objects.order_by('gib')[32 * off: 32 * off + 32]

    if (Item.objects.all().count() - 32 * off - 32 > 0):
        next = '/' + str(off + 1) + '/'
    if (off == 1):
        prev = '/'
    if (parameter):
        if (next):
            next += parameter
    if (parameter):
        if (prev):
            prev += parameter
    return render_to_response('main.html', {'long_list': long_items, 'offset': off, 'next': next, 'prev': prev, 'par': parameter}, context_instance=RequestContext(request) )


def order(request):
    return render_to_response('order.html', {}, context_instance=RequestContext(request))


def info(request):
    return render_to_response('info.html', {}, context_instance=RequestContext(request))
