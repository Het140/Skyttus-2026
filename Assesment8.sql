use Website;
--Tasks Add index to improve search on orders.customer_id 
create index idx_orders_customers_id
on Orders(customer_id);

--Use EXPLAIN to analyze query 
select* from orders
where customer_id = 1;

--Optimize a slow join query 
create index idx_customers_city
on customers(city);
select c.customer_id, c.name, o.order_id, 0.amount
from customers c
join orders o
on c.customer_id = o.customer_id
where c.city = 'Mumbai';

select c.customer_id, c.name, o.order_id, o.amount
from customers c
join orders o
on c.customer_id = o.customer_id
where c.city = 'Mumbai'


--Explain when index should not be used	
select* from customers
where lower(city)= 'Mumbai';