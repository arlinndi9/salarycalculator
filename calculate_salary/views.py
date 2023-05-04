from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'POST':
        paga_bruto = float(request.POST.get('paga_bruto'))
        if paga_bruto <= 0:
            context = {'error': 'Paga bruto duhet te jete nje numer pozitiv dhe jo-zero.'}
            return render(request, 'index.html', context)
        kontributi_punetorit = 0.05
        kontributi_punedhenesit = 0.05
        paga_tatueshme = paga_bruto - paga_bruto * kontributi_punedhenesit
        # perqindja e tatimeve sipas pages
        t1 = 0.0
        t2 = 0.04
        t3 = 0.08
        t4 = 0.1
        tatimi1 = 0
        tatimi2 = 80
        tatimi3 = 250
        tatimi4 = 450
        paga_neto=0
        if 0 < paga_tatueshme <= 80:
            t = (tatimi2 - tatimi1) * t1
            paga_neto = paga_tatueshme - paga_tatueshme * t1 - t
        elif 80 < paga_tatueshme <= 250:
            t = (paga_tatueshme - tatimi2) * t2 + (tatimi2 - tatimi1) * t1
            paga_neto = paga_tatueshme - t
        elif 250 < paga_tatueshme <= 450:
            t = (paga_tatueshme - tatimi3) * t3 + (tatimi3 - tatimi2) * t2
            paga_neto = paga_tatueshme - t
        elif paga_tatueshme > 450:
            t = (paga_tatueshme - tatimi4) * t4 + (tatimi4 - tatimi3) * t3 + (tatimi3 - tatimi2) * t2
            paga_neto = paga_tatueshme - t

        context = {
            'paga_bruto': paga_bruto,
            'kontributi_punetorit': round(paga_bruto * kontributi_punetorit, 2),
            'kontributi_punedhenesit': round(paga_bruto * kontributi_punedhenesit, 2),
            'paga_tatueshme': round(paga_tatueshme, 2),
            'paga_0_80':round((tatimi2 - tatimi1) * t1, 2),
            'paga_neto': round(paga_neto, 2),
            't': round(t, 2)
        }
        return render(request, 'index.html', context)

    return render(request, 'index.html')