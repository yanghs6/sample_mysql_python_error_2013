-- Select database
USE testDB;

-- Create table
CREATE TABLE emp (
    empno CHAR(20) NOT NULL,
    name CHAR(20) NULL,
    department CHAR(40) NULL,
    phone CHAR(14) NULL,
    PRIMARY KEY (empno)
);
