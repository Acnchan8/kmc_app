CREATE TABLE learners(
    id INT AUTO_INCREMENT primary key DEFAULT 1, 
    QR_ID INT(10) not null, 
    time_in DATETIME not null,
    first_name CHAR(100) not null, 
    last_name CHAR(100) not null, 
    email VARCHAR(100) not null, 
    class_name CHAR(100), 
    institution CHAR(100) not null, 
    current_role CHAR(100) not null, 
    department CHAR(100) not null, 
    specialization CHAR(100)
);