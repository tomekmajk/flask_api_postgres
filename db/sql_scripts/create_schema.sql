CREATE TABLE IF NOT EXISTS app_user (
    id serial primary key,
    email varchar(200) UNIQUE NOT NULL,
    name varchar(200),
    password varchar(300) NOT NULL,
    is_active boolean NOT NULL
);

ALTER TABLE app_user ALTER COLUMN is_active SET DEFAULT FALSE;
