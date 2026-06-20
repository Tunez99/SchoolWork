

users = {
    "admin_user": "admin",
    "normal_user": "user",
    "guest_user": "guest"
}

permissions = {
    "admin": ["read", "write", "delete", "modify_users"],
    "user": ["read", "write"],
    "guest": ["read"]
}

def check_access(username, action):
    role = users.get(username)

    if not role:
        return "User not found"

    if action in permissions[role]:
        return f"ACCESS GRANTED: {username} can {action}"
    else:
        return f"ACCESS DENIED: {username} cannot {action}"

print(check_access("admin_user", "delete"))
print(check_access("normal_user", "delete"))
print(check_access("guest_user", "read"))
print(check_access("guest_user", "write"))