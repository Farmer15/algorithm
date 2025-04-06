-- Write your PostgreSQL query statement below
SELECT
  product_name,
  sum(unit) AS unit
FROM Products
RIGHT OUTER JOIN Orders
ON Products.product_id = Orders.product_id
WHERE EXTRACT(MONTH FROM Orders.order_date) = '2' 
    AND EXTRACT(YEAR FROM Orders.order_date) = '2020'
GROUP BY product_name
HAVING sum(unit) >= 100