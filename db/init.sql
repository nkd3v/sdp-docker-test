CREATE TABLE IF NOT EXISTS users (
  uid INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL
);

INSERT INTO users (uid, name, age) VALUES
(121, 'Alice', 18),
(122, 'Bob', 17),
(123, 'Cindy', 25),
(124, 'Dan', 21);
