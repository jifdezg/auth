from werkzeug.security import generate_password_hash

users = {
    "jfer": generate_password_hash("pass1"),
    "gtra": generate_password_hash("pass2"),
    "nmag": generate_password_hash("pass3")
}

roles = {
    "jfer": "user",
    "gtra": "user",
    "nmag": ["user", "admin"],
}