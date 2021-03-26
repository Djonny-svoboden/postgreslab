1#######################
SELECT customers.first_name, customers.last_name, products.id
FROM customers
INNER JOIN products ON customers.basket_id=products.id
;	
2########################
SELECT * from customers 
where payment < 50 AND city not in('Batallas','Plavsk') AND id >15
;
3#########################by payment	
select customers.first_name, customers.last_name, basket.cost
from customers
inner join basket on customers.payment = basket.cost
;
4###########################
select customers.first_name, customers.last_name, products.cost from customers
INNER JOIN products ON customers.payment=products.cost
;