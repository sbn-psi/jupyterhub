FROM jupyterhub/jupyterhub:latest

RUN pip install dockerspawner oauthenticator python-dotenv
