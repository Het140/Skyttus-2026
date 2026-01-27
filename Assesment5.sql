use Company_DB
-- Users table
CREATE TABLE users(
    user_id INT PRIMARY KEY,
    email VARCHAR(50),
    password VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

SELECT * FROM users;
INSERT INTO users values
(1,'Het Patel','het@gmail.com',7788),
(2,'Sujal Tandel','sujal@gmail.com',8877),
(3,'Jay Patel','jay@gmail.com',3344),
(4,'Meet Patel','meet@gmail.com',4433);


-- Orders table
CREATE TABLE Orders (
    OrderId INT PRIMARY KEY,
    user_id INT,
     Amount DECIMAL(10,2),
    OrderDate DATETIME DEFAULT GETDATE(),
    

    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
Select * From Orders;
INSERT INTO Orders (OrderId,user_id,Amount) values
(12,1,340),
(14,2,550),
(13,3,450),
(17,4,750);

 
 --Create index on email column 
 CREATE UNIQUE INDEX idx_users_email
 ON users(email);
 --Create view to display user order summary
 CREATE VIEW users_Order_summary
AS
SELECT
    u.user_id,
    u.email,
    COUNT(o.OrderId) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_amount
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.email;

 SELECT* From users_Order_summary