-- @tmajk
/*
params:
0 - APP_NAME
*/

-- script
CREATE TABLE {0}_app_user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(200) UNIQUE NOT NULL,
    name VARCHAR(200),
    password VARCHAR(300) NOT NULL,
    is_active boolean NOT NULL
);

ALTER TABLE {0}_app_user ALTER COLUMN is_active SET DEFAULT FALSE;

CREATE TABLE {0}_app_role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description VARCHAR(300)
);

CREATE TABLE {0}_app_user_role (
    app_user_id INTEGER NOT NULL REFERENCES {0}_app_user(id),
    app_role_id INTEGER NOT NULL REFERENCES {0}_app_role(id),
    granted_date TIMESTAMPTZ NOT NULL,
    granted_by_user_id INTEGER REFERENCES {0}_app_user(id)
);

INSERT INTO {0}_app_role(name, description) 
VALUES 
('admin', 'administrator role'),
('user', 'regular user');
