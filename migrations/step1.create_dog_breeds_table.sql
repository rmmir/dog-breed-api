CREATE TABLE dog_breeds (
    id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(16)))),
    metric_weight VARCHAR(50) NOT NULL,
    imperial_weight VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    temperament VARCHAR(50) NOT NULL,
    origin VARCHAR(50) NOT NULL,
    life_span VARCHAR(50) NOT NULL,
    reference_image_id VARCHAR(50) NOT NULL 
);