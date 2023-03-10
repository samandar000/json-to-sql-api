from django.http import request,JsonResponse,HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from .models import SmartPhone
import json
from pprint import pprint
import requests

def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    if reqeust.method == 'POST':
        # get body from request
        body = reqeust.body
        # get body data
        decoded = body.decode()
        # data to dict
        data = json.loads(decoded)
        # get all properties
        price = data.get('price', False)
        img_url = data.get('img_url', False)
        color = data.get('color', False)
        ram = data.get('ram', False)
        memory = data.get('memory', False)
        name = data.get('name', False)
        model = data.get('model', False)
        pprint(body)
        # check all properties is valid
        if price == False:
            return JsonResponse({"status": "price field is required."})
        if img_url == False:
            return JsonResponse({"status": "img_url field is required."})
        if color == False:
            return JsonResponse({"status": "color field is required."})
        if ram == False:
            return JsonResponse({"status": "ram field is required."})
        if memory == False:
            return JsonResponse({"status": "memory field is required."})
        if name == False:
            return JsonResponse({"status": "name field is required."})
        if model == False:
            return JsonResponse({"status": "model field is required."})

        # create a inctance of SmartPhone 
        smartphone = SmartPhone(
            price=price,
            img_url=img_url,
            color=color,
            ram=ram,
            memory=memory,
            name=name,
            model=model
        )
        # save data
        smartphone.save()

        # return data
        returned = smartphone.to_dict()
        return JsonResponse(returned)
def get_all_product(request:HttpRequest):
    if request.method=='GET':
        # Get all the smartphone objects
        phones = SmartPhone.objects.all()
        

        result = {
            'result':[]
        }
        # Loop through the objects and append them to the result dictionary
        for phone in phones:
            model = phone.model
            result.setdefault(model,[])
            result[model].append({
                'id':phone.id,
                'price':phone.price,
                'img_url':phone.img_url,
                'color':phone.color,
                'ram':phone.ram,
                'memory':phone.memory,
                'name':phone.name,
            })
       
        return JsonResponse(result)

    

def get_product(request:HttpRequest):
    if request.method == 'GET':
        
        
        products = SmartPhone.objects.all()
        result = []
        args = request.GET
        

        for product in products:
            # print(product.name)
            if args.get('ram'):
                # print('ok')
                if product.ram == args['ram']:
                    print(args['ram'])
                    result.append(product.to_dict())
        # print(result)
        return JsonResponse(result,safe=False)
        


def delete_product(request:HttpRequest, pk:int):
    if request.method == 'GET':

        try:
            product = SmartPhone.objects.get(id=pk)
            product.delete()
            return JsonResponse(product.to_dict())
        except ObjectDoesNotExist:
            return JsonResponse({'status':"Object doesn't exist"})

def update_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
    if reqeust.method == "POST":
        try:
            # get body from request
            body = reqeust.body
            # get body data
            decoded = body.decode()
            # data to dict
            data = json.loads(decoded)
            # get all properties
            price = data.get('price', False)
            img_url = data.get('img_url', False)
            color = data.get('color', False)
            ram = data.get('ram', False)
            memory = data.get('memory', False)
            name = data.get('name', False)
            model = data.get('model', False)

            # get product from database by id
            product = SmartPhone.objects.get(id=pk)

            # check all properties is valid
            if price is not False:
                product.price = price
            if img_url:
                product.img_url = img_url
            if color:
                product.color = color
            if ram:
                product.ram = ram
            if memory:
                product.memory = memory
            if name:
                product.name = name
            if model:
                product.model = model

            # save product
            product.save()

            return JsonResponse(product.to_dict())
            
        except ObjectDoesNotExist:
            return JsonResponse({"status": "object doesn't exist"})
