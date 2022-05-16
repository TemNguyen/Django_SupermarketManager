from ast import MatchAs
from django.shortcuts import redirect, render, get_object_or_404
from .models import MatHang
from .form import MatHangForm

def list_view(request):
    keyword = request.GET.get('keyword')
    if keyword:
        mathangs = MatHang.objects.filter(name__icontains=keyword)
    else:
        mathangs = MatHang.objects.all()
    context = {
        'mathangs': mathangs.order_by('name'),
        'keyword': keyword
    }

    return render(request, 'list_view.html', context)

def create_view(request):
    form = MatHangForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MatHangForm()
        return redirect('/')
    
    context = {
        'form': form
    }

    return render(request, 'create.html', context)

def update_view(request, id):
    mathang = get_object_or_404(MatHang, id=id)
    form = MatHangForm(request.POST or None, instance=mathang)

    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def delete_view(request, id):
    mathang = get_object_or_404(MatHang, id=id)
    if(request.method == 'POST'):
        mathang.delete()
        return redirect('/')
    context = {
        'mathang': mathang
    }
    return render(request, 'delete.html', context)

def detail_view(request, id):
    # student = Student.objects.get(id=id)
    mathang = get_object_or_404(MatHang, id=id)
    context = {
        'mathang': mathang
    }
    return render(request, 'detail.html', context)

# Create your views here.
