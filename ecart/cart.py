from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from .models import *
from django.contrib import messages



#This function is used to addtocart function    
'''If the user click addtocart without signing in it shows Login to continue'''
'''If the user click some product which is already in the cart it shows Product already in cart'''
'''If the user login and clicks add to cart for the first time it shows Product added successfully'''
'''if the user exceeds the quantity in the stock it shows the avaliable stock'''
def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.quantity >=prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"product added successfully"})
                    else:
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+"quantity available"})


            
            else:
                return JsonResponse({'status':'No Such Product Found'})

        else:
            return JsonResponse({'status':'Login To Continue'})
    

    return redirect('home')

#This function is used to view all the products added in the cart
def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart':cart}
    return render(request,'ecart/cart.html',context)