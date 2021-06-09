from django.shortcuts import render
from .models import Product
from .models import Comment
from .forms import CommentForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate
from functools import reduce
from cloudipsp import Api, Checkout
from django.contrib.auth.models import User




# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "main/index.html", {"ps": products})


def authorize(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect(reverse("main:cabinet"))
        else:
            return redirect(reverse("main:auth_page"))
    return render(request, "main/auth.html", {})


def detail(request, id):
    product = Product.objects.get(pk=id)
    comments = Comment.objects.filter(product__pk=id)

    if request.method == "POST" and request.user.is_authenticated:
        username =request.user.username

        d = {"username": username,
             "text": request.POST["text"],
             "product": product
        }
        comment_form = CommentForm(d, request.FILES)
        print(comment_form)
        if comment_form.is_valid():
            comment_form.save()
        return redirect(reverse('main:detail_page', args=(id,)))
    return render(request, "main/detail.html", {"p": product, "comments": comments})

def  register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        try:
            user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name
                                        )
            user.save()
        except Exception as e:
            print(e)
            return redirect(reverse("main:register"))
        return redirect(reverse("main:auth_page"))

    return render(request, 'main/register.html')




def cabinet_view(request):
    if request.user.is_authenticated:
        return render(request, "main/cabinet.html", {})
    else:
        return redirect(reverse("main.index_page"))



def logout_view(request):
    logout(request)
    return redirect(reverse("main:index_page"))


def pay_cart(request):
    cart = request.session.get("cart",[])
    print(cart)
    products = Product.objects.filter(pk__in=cart)
    overall_cost = reduce(lambda x,y: x+y, [product.cost for product in products],0)
    api = Api(merchant_id=1396424, secret_key="test")
    checkout = Checkout(api)
    data = {"currency":"KZT", "amount":int(overall_cost*100)}
    url = checkout.url(data).get("checkout_url")
    return redirect(url)


def add_cart(request, id):
    cart = request.session.get("cart", [])
    cart.append(id)
    print(cart)
    request.session["cart"] = cart
    return redirect(reverse("main:index_page"))


def delete_cart_item(request, id):
    cart = request.session.get("cart", [])
    cart.remove(id)
    request.session["cart"] = cart
    return redirect(reverse("main:korzina"))

def korzina(request):
    return render(request, 'main/korzina.html')




