from django.db import models
import os

def user_profile_avatar_path(instance,filename):
    ext = os.path.splitext(filename)[0]
    return f"{instance.id}/profile/avatar{ext}"

