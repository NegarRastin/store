create database mft;

create table mft.customer_tbl
(
    id            int primary key auto_increment,
    name          varchar(30),
    family        varchar(30),
    national_code varchar(10),
    phone_number  varchar(11)
);