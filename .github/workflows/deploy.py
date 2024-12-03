import os

# Get an environment variable
value = os.environ.get('val')
#print(f"The value of MY_ENV_VAR is: {value}")

print(f"""
        export VAR={value}
        export SOMETHING={value}
      """)



