CREATE TABLE data_recon_config
(
data_recon_config_id NUMBER,
process_name VARCHAR2(100),
compare_type VARCHAR2(100),
src_db_sid VARCHAR2(255),
src_sql_text CLOB,
src_file_name VARCHAR2(255),
src_key_id VARCHAR2(255),
tgt_db_sid VARCHAR2(255),
tgt_sql_text CLOB,
tgt_file_name VARCHAR2(255),
tgt_key_id VARCHAR2(255),
insert_dt DATE,
insert_usr VARCHAR2(100)
);

DROP TABLE data_recon_config;

ALTER TABLE data_recon_config ADD compare_type VARCHAR2(100);

CREATE SEQUENCE data_recon_config_id;

SELECT *
  FROM data_recon_config;

INSERT INTO data_recon_config
            (data_recon_config_id, process_name, compare_type,
             src_db_sid, src_sql_text,
             src_file_name, src_key_id, tgt_db_sid,
             tgt_sql_text, tgt_file_name, tgt_key_id, insert_dt,
             insert_usr
            )
     VALUES (data_recon_config_id.NEXTVAL, 'OBJECTS', 'DB_TO_DB',
             'HR/HR@LAPTOP-21RC5VEQ:1521/XE', q'[select * from all_objects]',
             NULL, 'OBJECT_ID', 'HR/HR@LAPTOP-21RC5VEQ:1521/XE',
             q'[select * from all_objects]', NULL, 'OBJECT_ID', SYSDATE,
             'SYSTEM'
            );

INSERT INTO data_recon_config
            (data_recon_config_id, process_name, compare_type,
             src_db_sid,
             src_sql_text, src_file_name, src_key_id,
             tgt_db_sid,
             tgt_sql_text, tgt_file_name, tgt_key_id, insert_dt,
             insert_usr
            )
     VALUES (data_recon_config_id.NEXTVAL, 'USER_OBJECTS', 'DB_TO_DB',
             'HR/HR@LAPTOP-21RC5VEQ:1521/XE',
             q'[select * from user_objects]', NULL, 'OBJECT_ID',
             'HR/HR@LAPTOP-21RC5VEQ:1521/XE',
             q'[select * from user_objects]', NULL, 'OBJECT_ID', SYSDATE,
             'SYSTEM'
            );


COMMIT ;

SELECT *
  FROM user_objects
 WHERE object_type = 'TABLE';

SELECT *
  FROM data_recon_config
 WHERE process_name = 'OBJECTS';

UPDATE data_recon_config
   SET src_sql_text =
          q'[select * from user_objects where object_type='TABLE' and object_id in (16401,16403,16406,31297)]',
       tgt_sql_text =
          q'[select * from user_objects where object_type='TABLE' and object_id in (16401,16403,16406,30654)]'
 WHERE process_name = 'OBJECTS';