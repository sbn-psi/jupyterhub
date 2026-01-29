# jupyterhub_config.py
import os
import shutil
from oauthenticator.google import GoogleOAuthenticator
from dotenv import load_dotenv

load_dotenv()

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# the docker image to spawn for each user
c.DockerSpawner.image = "sbnpsi/user-notebook:latest"

# use the internal docker network
c.DockerSpawner.network_name = "jupyterhub_jupyterhub_network"
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.JupyterHub.hub_connect_url = 'http://jupyterhub:8081'

# notebook directory inside the container
c.DockerSpawner.notebook_dir = "/home/jovyan/work"

# mount a volume for each user
c.DockerSpawner.volumes = {
    'jupyterhub-user-{username}': '/home/jovyan/work',
    '/dsk8/transfer/dsk1/www/archive/pds3': '/home/jovyan/work/pds.sbn/pds3',
    '/pds4': '/home/jovyan/work/pds.sbn/pds4',
    '/dsk8/catalina/gbo.ast.catalina.survey/': '/home/jovyan/work/pds.sbn/catalina',
    '/srv/search-api-notebook': '/home/jovyan/work/search-api-notebook',
    '/srv/jupyterhub/files/Welcome_to_PDS_SBN.ipynb': '/home/jovyan/work/Welcome_file.ipynb'
}

# optional: remove containers once they stop
c.DockerSpawner.remove = False

# optional: debug logging
c.Spawner.debug = True

# jupyterhub listens on all interfaces
c.JupyterHub.bind_url = 'http://:8000'

# Google OAuth
c.JupyterHub.authenticator_class = GoogleOAuthenticator
c.GoogleOAuthenticator.login_service = "Google"
c.GoogleOAuthenticator.client_id = os.getenv("GOOGLE_CLIENT_ID")
c.GoogleOAuthenticator.client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
c.GoogleOAuthenticator.oauth_callback_url = "https://jupyterhub.psi.edu/hub/oauth_callback"
c.GoogleOAuthenticator.admin_users = {"ckingston"}
c.GoogleOAuthenticator.allowed_users = {
    "ckingston@psi.edu","jstone@psi.edu","mdrum@psi.edu","epalmer@psi.edu",
    "neese@psi.edu","mueller@psi.edu","klopez@psi.edu"
}