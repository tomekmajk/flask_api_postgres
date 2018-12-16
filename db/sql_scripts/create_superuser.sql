-- @tmajk
/*
params:
0 - APP_NAME
1 - email
2 - name
3 - password
*/

-- script
DO $$
DECLARE 
user_id bigint;
regular_user_role_id bigint;
admin_user_role_id bigint;
BEGIN
  	INSERT INTO {0}_app_user(email, name, password, is_active)
	VALUES ('{1}', '{2}', '{3}', true) RETURNING id INTO user_id;
	
	SELECT id from flap_app_role where name = 'user' INTO regular_user_role_id;
	SELECT id from flap_app_role where name = 'admin' INTO admin_user_role_id;
	INSERT INTO flap_app_user_role(app_user_id, app_role_id, granted_date)
	VALUES (user_id, regular_user_role_id, NOW()), (user_id, admin_user_role_id, NOW());
END $$;
