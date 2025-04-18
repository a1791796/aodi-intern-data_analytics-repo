Why is it more secure to use a .env file for database credentials instead of hardcoding them?

Storing sensitive data  in a .env file separates configuration from the actual application code.
When credentials are hardcoded directly into the code, they become part of the source code, which might be checked into version control.

How can python-dotenv simplify managing environment variables in Jupyter?

easy to use, Loading environment variables is as simple as calling load_dotenv() once in your notebook, 
after which you can access the variables using os.getenv(). This is much cleaner than manually setting environment variables.
Store sensitive credential in a .env file, keeping them separate from your code.
