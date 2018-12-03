-- WIP

CREATE TABLE user (
    id serial primary key,
    email varchar(200) UNIQUE NOT NULL 
    name varchar(200),
    password varchar(300) NOT NULL,
    is_active boolean NOT NULL,
)

ALTER TABLE user ALTER COLUMN is_active SET DEFAULT FALSE;
