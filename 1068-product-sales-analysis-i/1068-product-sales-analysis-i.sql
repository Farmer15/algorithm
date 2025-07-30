-- Write your PostgreSQL query statement below

SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
  FULL OUTER JOIN Product
  ON Product.product_id = Sales.product_id
  WHERE NOT Sales.product_id IS NULL