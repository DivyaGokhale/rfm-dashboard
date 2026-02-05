DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_value DECIMAL(10,2) NOT NULL,
    country VARCHAR(50)
);

CREATE INDEX idx_customer ON orders(customer_id);
CREATE INDEX idx_order_date ON orders(order_date);
