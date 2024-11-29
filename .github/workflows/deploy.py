import os

# Get an environment variable
value = os.environ.get('MY_ENV_VAR')
print(f"The value of MY_ENV_VAR is: {value}")

# Access environment variables directly (throws a KeyError if not set)
value_direct = os.environ['MY_ENV_VAR']
print(f"The value of MY_ENV_VAR is:
