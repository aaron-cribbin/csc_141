# This is my work (^_^)
# Some of this is taken from the book, some of this is by me
# Aaron Cribbin

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile('Aaron', 'Cribbin', 
                             age='18', height="6'", 
                             weight='220lb')

print(user_profile)