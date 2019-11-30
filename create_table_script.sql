CREATE TABLE dbo.json_flatten  
(  
item_no int ,
item_name varchar(1000),
parent_item_no int,
insert_date date
);  


CREATE TABLE dbo.json_flatten_raw  
(  
item_no int ,
item_name varchar(2000),
item_value varchar(1000),
insert_date date
);  
