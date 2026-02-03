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
    # JupyterHub user data mount
    '/srv/jupyterhub-user-data/users/{username}': '/home/jovyan/work',

    # PDS Archive Data
    '/dsk8/transfer/dsk1/www/archive/pds3': '/home/jovyan/work/pds.sbn/pds3',
    '/pds4': '/home/jovyan/work/pds.sbn/pds4',
    '/dsk8/catalina/gbo.ast.catalina.survey/': '/home/jovyan/work/pds.sbn/catalina',

    # Demo notebook area
    '/srv/search-api-notebook': '/home/jovyan/work/search-api-notebook',

    # Welcome files
    '/srv/jupyterhub/files/Welcome_to_PDS_SBN.ipynb': '/home/jovyan/work/Welcome_file.ipynb',
    '/srv/jupyterhub/files/CSS_Catalina_Sky_Survey_Demo.ipynb': '/home/jovyan/work/CSS_Survey_Demo.ipynb'
}

# optional: remove containers once they stop
c.DockerSpawner.remove = False

# --- RESOURCE CONTROLS: memory + CPU ---
c.DockerSpawner.extra_host_config = {
    "mem_limit": "4g",
    "mem_reservation": "3g",
    "memswap_limit": "4g",
    "cpu_shares": 1024,
    "pids_limit": 2048
}

# optional: debug logging
c.Spawner.debug = True

# jupyterhub listens on all interfaces
c.JupyterHub.bind_url = 'http://:8000'

def read_allow_list(path):
    """
    Read allow list file into a set of usernames/emails.
    - Ignores blank lines and comments (# ...)
    - Strips whitespace
    """
    users = set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if not s or s.startswith("#"):
                    continue
                users.add(s)
    except FileNotFoundError:
        # Fail closed: no users if the file is missing
        users = set()
    return users

ALLOW_LIST_PATH = os.getenv("JUPYTERHUB_ALLOW_LIST_FILE", "/srv/jupyterhub/access_control/allow_list.txt")
allowed = read_allow_list(ALLOW_LIST_PATH)

# Google OAuth
c.JupyterHub.authenticator_class = GoogleOAuthenticator
c.GoogleOAuthenticator.login_service = "Google"
c.GoogleOAuthenticator.client_id = os.getenv("GOOGLE_CLIENT_ID")
c.GoogleOAuthenticator.client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
c.GoogleOAuthenticator.oauth_callback_url = "https://jupyterhub.psi.edu/hub/oauth_callback"
c.GoogleOAuthenticator.admin_users = {"ckingston"}
c.GoogleOAuthenticator.allowed_users = allowed