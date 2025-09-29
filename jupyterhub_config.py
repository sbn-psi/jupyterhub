# jupyterhub_config.py
import os
import shutil

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# the docker image to spawn for each user
c.DockerSpawner.image = "jupyter/scipy-notebook:latest"

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
    '/srv/files/Welcome_to_PDS_SBN.ipynb': '/home/jovyan/work/Welcome.ipynb'
}

# optional: remove containers once they stop
c.DockerSpawner.remove = False

# optional: debug logging
c.Spawner.debug = True

# jupyterhub listens on all interfaces
c.JupyterHub.bind_url = 'http://:8000'

# authentication (simple for testing)
c.JupyterHub.authenticator_class = 'dummy'
c.DummyAuthenticator.password = 'dummy123'
c.Authenticator.allowed_users = {'conor', 'jstone', 'mdrum', 'epalmer'}
