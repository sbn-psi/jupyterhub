FROM jupyterhub/jupyterhub:latest

RUN pip install dockerspawner jupyterhub-ldapauthenticator
