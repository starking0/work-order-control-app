ORDERS SYSTEM APP

The project consists of on a system that manahe the flow of the orders, facilitating the process of order creation, order validation, and order fulfillment. Also add features la dashboard visulization, pdf  report generation, inventory management, anda  acustom calculator for personalization.
![alt text](./img/ocw_cover.webp)

- Electron + Vite + React
- Tailwind CSS
- ESLint
- Prettier
- Django Rest Framework
- PostgreSQL
- Docker

Usage

To usage run the next commands:


BACKEND

Docker compose up --build

Only the first time!
- docker-compose exec backend python manage.py migrate
- docker-compose exec backend python manage.py loaddata orders/fixtures/priority.json
- docker-compose exec backend python manage.py loaddata orders/fixtures/service.json
- docker-compose exec backend python manage.py loaddata orders/fixtures/shifts.json
- docker-compose exec backend python manage.py loaddata orders/fixtures/status.json

FRONTEND

cd .\ocw-frontend\

Then:

npm run build

Operation:

We have 4 sections in the app:

1. Orders
2. Dashboard
3. Calulator
4. Inventory

in orders yo can create orders finished active orders.
![alt text](./img/image-3.png)

When you create an order you can select the service if this will be send to cut material or processed orders (when pass to cut material and finished this will also be send to processed orders).

On cut material you create a new cut order and finished this, also you can check the cuts assigned
![alt text](./img/image.png)
![alt text](./img/image-1.png)
![alt text](./img/image-2.png)

then to process orders you can create a new process order and finished this.
![alt text](./img/image-4.png)
![alt text](./img/image-5.png)
then you have to finalize the order
![alt text](./img/image-6.png)

and with this you can download the pdf report
![alt text](./img/image-7.png)
![alt text](./img/image-8.png)


2 - DASHBOARD

here is where you can see the graphics of the orders
![alt text](./img/image-9.png)

3 - CALCULATOR

This is only an extra feature this can be costumized to the needs 
![alt text](./img/image-10.png)

4 - INVENTORY

This is the inventory management, you can see the inventory and the orders that are assigned to the inventory
the steps to geenrate a stock are the following:

1. Create a new product
![alt text](./img/image-11.png)
you can also delete or updata the product data
![alt text](./img/image-12.png)
![alt text](./img/image-13.png)
2. Create a new location
![alt text](./img/image-14.png)
at the same form you can also delete or update the location data
![alt text](./img/image-15.png)
![alt text](./img/image-16.png)

then you have can create a new stock
![alt text](./img/image-18.png)

also you can add, delete stock 
![alt text](./img/image-19.png)
![alt text](./img/image-20.png)

or generate a movements beetween the stocks
![alt text](./img/image-21.png)
![alt text](./img/image-22.png)

in the movements you can dowenload an exel with all the data from de movements
![alt text](./img/image-23.png)
![alt text](./img/image-24.png)