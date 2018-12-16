INSERT INTO 
${app_name, flask}_app_user(email, name, password) 
VALUES (${email, null}, ${name, null}, ${password, null}) 
RETURNING id;
