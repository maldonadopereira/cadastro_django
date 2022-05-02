from django.shortcuts import render

def venda_home(request):
    venda_id = request.session.get("venda_id", None)
    if venda_id is None:
        print('Criar nova venda')
        request.session['venda_id'] = 12
    else:
        print("Venda ID existe")
    return render(request, "vendas/venda.html", {} )