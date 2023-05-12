# How to use:

1. On the terminal 
$docker run -p 5000:5000 <imageID>       # Example: docker run -p 5000:5000 d0289d148e46      
  
2. On the browser, goto
  
  2.1 Check customers route
  127.0.0.1:5000/customers
  
  2.2 Check specific customer with customer id route
  127.0.0.1:5000/customers/2                     # Here customer id is 2
  
  2.3 View orders of specific customer with customer id route
  127.0.0.1:5000/customers/2/orders             # Here customer id is 2
  
  
  2.4 View specific order of specific customer with customer id, and order id route
  127.0.0.1:5000/customers/4/orders/2   # Here customer id is 4, order id is 2
