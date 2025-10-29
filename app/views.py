from django.shortcuts import redirect, render

from .forms import CategoryForm
from .models import Brand, Category, Product


def index(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = CategoryForm()

    context = {
        "products": products,
        "brands": brands,
        "categories": categories,
        "form": form,
    }
    return render(request, "app/index.html", context)
