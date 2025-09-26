# jupyterhub_config.py

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

# LDAP configuration
# c.LDAPAuthenticator.debug = True
# c.JupyterHub.authenticator_class = 'ldap'
# c.LDAPAuthenticator.server_address = "sbn-dc-1.psi.edu"

# c.LDAPAuthenticator.lookup_dn = True
# c.LDAPAuthenticator.lookup_dn_search_filter = '({login_attr}={login})'
# c.LDAPAuthenticator.lookup_dn_search_user = 'cn=ldap_search_user_technical_account,'
# c.LDAPAuthenticator.lookup_dn_search_password = 'secret'
# c.LDAPAuthenticator.user_search_base = 'ou=SBNPSI,dc=sbnpsi,dc=local'
# c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
# c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'