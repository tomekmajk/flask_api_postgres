-- create super user
DO $$
DECLARE 
user_id bigint;
regular_user_role_id bigint;
admin_user_role_id bigint;
BEGIN
  	INSERT INTO flap_app_user(email, name, password, is_active)
	VALUES ('tmajk@sas.pl', 'sosel', '1234', true) RETURNING id INTO user_id;
	
	SELECT id from flap_app_role where name = 'user' INTO regular_user_role_id;
	SELECT id from flap_app_role where name = 'admin' INTO admin_user_role_id;
	INSERT INTO flap_app_user_role(app_user_id, app_role_id, granted_date)
	VALUES (user_id, regular_user_role_id, NOW()), (user_id, admin_user_role_id, NOW());
END $$;

-- create regular user
DO $$
DECLARE 
user_id bigint;
regular_user_role_id bigint;
BEGIN
  	INSERT INTO flap_app_user(email, name, password)
	VALUES ('sas@sass.pl', 'tomek', '1234') RETURNING id INTO user_id;
	
	SELECT id from flap_app_role where name = 'user' INTO regular_user_role_id;
	INSERT INTO flap_app_user_role(app_user_id, app_role_id, granted_date)
	VALUES (user_id, regular_user_role_id, NOW());
END $$;
			
-- activate regular user
UPDATE flap_app_user SET is_active = true WHERE email = 'sas@sass.pl';
