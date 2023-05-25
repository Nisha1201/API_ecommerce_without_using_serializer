from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Customer, Products, Order
from django.contrib.sites.shortcuts import get_current_site

class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        # data = [{'id': category.id, 'name': category.name} for category in categories]
        data=[]
        for category in categories:
            category_data={'id': category.id, 'name': category.name}
            data.append(category_data)
        return Response(data)

    def post(self, request):
        # print("lllllllllllllllllllllllllllllllllllllllllllllll")
        name = request.data.get('name')
        if name:
            category = Category.objects.create(name=name)
            return Response({'id': category.id, 'name': category.name}, status=201)
        return Response({'error': 'Missing required fields'}, status=400)


class CategoryRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if category:
            data = {'id': category.id, 'name': category.name}
            return Response(data)
        return Response({'error': 'Category not found'}, status=404)

    def put(self, request, pk):
        category = self.get_object(pk)
        if category:
            name = request.data.get('name')
            if name:
                category.name = name
                category.save()
                return Response({'id': category.id, 'name': category.name})
            return Response({'error': 'Missing required fields'}, status=400)
        return Response({'error': 'Category not found'}, status=404)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category:
            category.delete()
            return Response(status=204)
        return Response({'error': 'Category not found'}, status=404)


class CustomerListCreateAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        # data = [{'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,'phone':customer.phone,'email':customer.email,'password':customer.password} for customer in customers]
        data=[]
        for customer in customers:
            customer_data={'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,'phone':customer.phone,'email':customer.email,'password':customer.password}
            data.append(customer_data)
        return Response(data)

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        password=request.data.get('password')
        if first_name and last_name:
            customer = Customer.objects.create(first_name=first_name, last_name=last_name,phone=phone,email=email,password=password)
            return Response({'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,'phone':customer.phone,'email':customer.email,'password':customer.password}, status=201)
        return Response({'error': 'Missing required fields'}, status=400)


class CustomerRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None

    def get(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            data = {'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,'phone':customer.phone,'email':customer.email,'password':customer.password}
            return Response(data)
        return Response({'error': 'Customer not found'}, status=404)

    def put(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            phone = request.data.get('phone')
            email = request.data.get('email')
            password=request.data.get('password')
            if first_name and last_name:
                customer.first_name = first_name
                customer.last_name = last_name
                customer.phone=phone
                customer.email=email
                customer.password=password
                customer.save()
                return Response({'id': customer.id, 'first_name': customer.first_name, 'last_name': customer.last_name,'phone':customer.phone,'email':customer.email,'password':customer.password})
            return Response({'error': 'Missing required fields'}, status=400)
        return Response({'error': 'Customer not found'}, status=404)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        if customer:
            customer.delete()
            return Response(status=204)
        return Response({'error': 'Customer not found'}, status=404)


class ProductsListCreateAPIView(APIView):
    def get(self, request):
        products = Products.objects.all()
        current_site = get_current_site(request)
        # data = [{'id': product.id, 'name': product.name, 'price': product.price, 'category': product.category.name, 'description': product.description, 'image': f"{current_site.domain}{product.image.url}"} for product in products]
        data=[]
        for product in products:
            product_data={'id': product.id, 'name': product.name, 'price': product.price, 'category': product.category.name, 'description': product.description, 'image': f"{current_site.domain}{product.image.url}"}
            data.append(product_data)
        return Response(data)

    def post(self, request):
        name = request.data.get('name')
        price = request.data.get('price')
        category_id = request.data.get('category')
        description = request.data.get('description')
        image = request.FILES.get('image')
        
        if name and price and category_id:
            category = Category.objects.get(id=category_id)
            product = Products(name=name, price=price, category=category, description=description, image=image)
            product.save()
            return Response({'id': product.id, 'name': product.name, 'price': product.price, 'category': product.category.name, 'description': product.description, 'image': product.image.url}, status=201)
        return Response({'error': 'Missing required fields'}, status=400)

class ProductsRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404
            # return None

    def get(self, request, pk):
        product = self.get_object(pk)
        data = {'id': product.id, 'name': product.name, 'price': product.price, 'category': product.category.name, 'description': product.description, 'image': product.image.url}
        return Response(data)

    def put(self, request, pk):
        product = self.get_object(pk)
        name = request.data.get('name')
        price = request.data.get('price')
        category_id = request.data.get('category')
        description = request.data.get('description')
        image = request.FILES.get('image')
        
        if name and price and category_id:
            category = Category.objects.get(id=category_id)
            product.name = name
            product.price = price
            product.category = category
            product.description = description
            if image:
                product.image = image
            product.save()
            return Response({'id': product.id, 'name': product.name, 'price': product.price, 'category': product.category.name, 'description': product.description, 'image': product.image.url})
        return Response({'error': 'Missing required fields'}, status=400)


    def delete(self, request, pk):
        product = self.get_object(pk)
        if product:
            product.delete()
            return Response(status=204)
        return Response({'error': 'Product not found'}, status=404)



class OrderListCreateAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        # data = [{'id': order.id, 'product': order.product.name, 'customer': f"{order.customer.first_name} {order.customer.last_name}", 'quantity': order.quantity, 'price': order.price, 'address': order.address, 'phone': order.phone, 'date': order.date, 'status': order.status} for order in orders]
        data = []
        for order in orders:
        #   if order.id!=1:  #if we dont want data of id ==1 then
            order_data = {
                'id': order.id,
                'product': order.product.name,
                'customer': f"{order.customer.first_name} {order.customer.last_name}",
                'quantity': order.quantity,
                'price': order.price,
                'address': order.address,
                'phone': order.phone,
                'date': order.date,
                'status': order.status
            }
            
            data.append(order_data)
            print(data)

        return Response(data)

    def post(self, request):
        product_id = request.data.get('product')
        customer_id = request.data.get('customer')
        quantity = request.data.get('quantity')
        price = request.data.get('price')
        address = request.data.get('address')
        phone = request.data.get('phone')
        date = request.data.get('date')
        status = request.data.get('status')
        
        if product_id and customer_id and quantity and price:
            product = Products.objects.get(id=product_id)
            customer = Customer.objects.get(id=customer_id)
            order = Order(product=product, customer=customer, quantity=quantity, price=price, address=address, phone=phone, date=date, status=status)
            order.save()
            return Response({'id': order.id, 'product': order.product.name, 'customer': f"{order.customer.first_name} {order.customer.last_name}", 'quantity': order.quantity, 'price': order.price, 'address': order.address, 'phone': order.phone, 'date': order.date, 'status': order.status}, status=201)
        return Response({'error': 'Missing required fields'}, status=400)

class OrderRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        data = {'id': order.id, 'product': order.product.name, 'customer': f"{order.customer.first_name} {order.customer.last_name}", 'quantity': order.quantity, 'price': order.price, 'address': order.address, 'phone': order.phone, 'date': order.date, 'status': order.status}
        return Response(data)

    def put(self, request, pk):
        order = self.get_object(pk)
        product_id = request.data.get('product')
        customer_id = request.data.get('customer')
        quantity = request.data.get('quantity')
        price = request.data.get('price')
        address = request.data.get('address')
        phone = request.data.get('phone')
        date = request.data.get('date')
        status = request.data.get('status')
        
        if product_id and customer_id and quantity and price:
            product = Products.objects.get(id=product_id)
            customer = Customer.objects.get(id=customer_id)
            order.product = product
            order.customer = customer
            order.quantity = quantity
            order.price = price
            order.address = address
            order.phone = phone
            order.date = date
            order.status = status
            order.save()
            return Response({'id': order.id, 'product': order.product.name, 'customer': f"{order.customer.first_name} {order.customer.last_name}", 'quantity': order.quantity, 'price': order.price, 'address': order.address, 'phone': order.phone, 'date': order.date, 'status': order.status})
        return Response({'error': 'Missing required fields'}, status=400)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=204)