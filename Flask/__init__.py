# Do that in terminal
    # pip install flask
    # from flask import Flask, render_template
    # mysql -u <username> -import pdb; pdb.set_trace()
    # CREATE DATABASE BucketList;
    # CREATE TABLE 'BucketList'.'tbl_user' (
    #   'user_id' BIGINT Null AUTO_INCREMENT,
    #   'user_name' VARCHAR(45) Null,
    #   'user_password' VARCHAR(45) Null,
    #   PRIMARY KEY ('user_id'));
    )

from flask import Flask; render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


# Begin Check if user exists

DELIMITER $$
CREATE DEFINER='root'@'localhost' PROCEDURE 'sp_createUser'(
    IN p_name VARCHAR(20),
    IN p_username VARCHAR(20),
    IN p_password VARCJHAR(20)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username)) THEN

        select 'Username Exists !!';

    ELSE

        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        );

    END If;
END$$
DELIMITER ;

# End check if user exists


if __name__ == "__main__":
    app.run()
