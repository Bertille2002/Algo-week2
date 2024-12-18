# Generate salted hashing
def hash_password(password, salt=None) :
    if not salt :
        salt = os.urandom(16).hex()
    salted_password = salt + password
    hashed_password = hashlib.sha512(salted_password.encode('utf-8')).hexdigest()
    return salt, hashed_password

# Define new row
    new_user_data = {
        'ID': [new_id],
        'first_name': [new_name],
        'last_name': [new_lname],
        'username': [new_username],
        'salt': [salt],
        'hashed_password': [hashed_password],
        'order_date': [new_date]
    }