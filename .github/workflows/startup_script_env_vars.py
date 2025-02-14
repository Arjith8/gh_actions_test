import os

print(f"""
export AWS_ACCESS_KEY_ID={os.environ.get('AWS_ACCESS_KEY_ID')}
export AWS_SECRET_ACCESS_KEY={os.environ.get('AWS_SECRET_ACCESS_KEY')}
export AWS_REGION={os.environ.get('AWS_REGION')}
export DATABASE_NAME={os.environ.get('DATABASE_NAME')}
export DATABASE_USER={os.environ.get('DATABASE_USER')}
export DATABASE_PASSWORD={os.environ.get('DATABASE_PASSWORD')}
export DATABASE_HOST={os.environ.get('DATABASE_HOST')}
export DATABASE_PORT={os.environ.get('DATABASE_PORT')}
export REDIS_HOST={os.environ.get('REDIS_HOST')}
export REDIS_PORT={os.environ.get('REDIS_PORT')}
export DJANGO_SECRET_KEY={os.environ.get('DJANGO_SECRET_KEY')}
export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY={os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')}
export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET={os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')}
export STATIC_URL={os.environ.get('STATIC_URL')}
export AWS_STORAGE_BUCKET_NAME={os.environ.get('AWS_STORAGE_BUCKET_NAME')}
export AWS_S3_REGION_NAME={os.environ.get('AWS_S3_REGION_NAME')}
export AWS_DEFAULT_ACL={os.environ.get('AWS_DEFAULT_ACL')}
export AWS_QUERYSTRING_AUTH={os.environ.get('AWS_QUERYSTRING_AUTH')}
""")

