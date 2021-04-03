create table FB_USERS(
    ID int auto_increment primary key,
    USER_ID varchar(250) not null,
    USERNAME varchar (250) not null,
    PASSWORD varchar (250) not null,
    IPADDRESS varchar(32) null,
    FLAG varchar(10) null,
    DATE TIMESTAMP
);

