CREATE DATABASE IF NOT EXISTS ProjectOneCaffeineLog;
USE ProjectOneCaffeineLog;

CREATE TABLE IF NOT EXISTS Caffeine_source (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(255),
    flavor VARCHAR(255),
    cost_per_serving DECIMAL(5,2),
    cost_per_100mg DECIMAL(5,2)
);

CREATE TABLE IF NOT EXISTS Caffeine_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    source_id INT,
    date DATE,
    time TIME,
    caffeine_mg INT,
    serving_size VARCHAR(255),
    effect INT,
    taste INT,
    context VARCHAR(255),
    FOREIGN KEY (source_id) REFERENCES Caffeine_source(id)
);
