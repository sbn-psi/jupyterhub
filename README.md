# SBN-PSI JupyterHub

**JupyterLab environment for PDS Small Bodies Node (SBN) archive data and computation.**

SBN-PSI provides node-supported computation alongside subnode archive data to the public, **free of processing and egress costs**, via a JupyterLab environment.

---

## Quick links

| | |
|---|---|
| **JupyterHub URL** | [https://jupyterhub.psi.edu](https://jupyterhub.psi.edu) |
| **Peppi (data search)** | [nasa-pds.github.io/peppi/](https://nasa-pds.github.io/peppi/) |

---

## Getting access

Access to the SBN-PSI JupyterHub is **restricted to approved users**.

1. **Contact** a member of the subnode staff to request access.
2. Access is granted only to **Google accounts** that are on the allow list maintained by the subnode.
3. Once your account is added, sign in at [https://jupyterhub.psi.edu](https://jupyterhub.psi.edu) with your Google account.

---

## Your JupyterLab environment

- **Isolated:** Your environment is separate from other users. You can install packages and customize your workspace without affecting anyone else.
- **Persistent:** Your work in your home directory is saved across sessions. Log out and come back later to continue where you left off.
- **Read-only archive:** PDS archive data is mounted read-only. Your own files and notebooks live in your writable workspace.

### Where to find the data

| Content | Location |
|--------|-----------|
| **PDS archive (PDS3 & PDS4)** | `pds.sbn` (read-only) |
| **Catalina Sky Survey data** | Inside `pds.sbn` (see demo notebook) |
| **Your workspace** | Home directory (writable; use a `projects/` folder for notebooks and results) |

### Pre-installed Python packages

The following packages are available in every user environment:

| Package | Purpose |
|---------|---------|
| `astropy` | Astronomy and astrophysics |
| `leafmap` | Interactive mapping |
| `matplotlib` | Plotting |
| `numpy` | Numerical computing |
| `pandas` | Data analysis |
| `pdr` | PDS Data Registry |
| `pds.peppi` | **Peppi** — search and access PDS data products |
| `pds4-tools` | Read PDS4 data |
| `pywwt` | WorldWide Telescope in Jupyter |
| `spiceypy` | SPICE toolkit for Python |

**Tip:** Use **Peppi** (`pds.peppi`) to search for and work with PDS data products. Documentation: [nasa-pds.github.io/peppi/](https://nasa-pds.github.io/peppi/).

### Getting started in JupyterLab

When you first log in, you’ll see:

- **Welcome notebook** — Short tour of your environment, where the SBN archive is, and how to use Peppi.
- **CSS Survey Demo** — Example notebook for Catalina Sky Survey data.

Run the Welcome notebook (Shift+Enter to run cells) to verify archive access and your workspace.

---

## Compute resources

| Resource | Limit |
|----------|--------|
| **Memory** | 4 GB |
| **CPU** | Standard allocation (see subnode for details) |
| **Storage** | 50 GB per user |

*Additional resource details may be defined by the subnode and reflected in the environment.*

---

## Repository contents (for maintainers)

This repository holds configuration and assets for the SBN-PSI JupyterHub deployment:

- **`jupyterhub_config.py`** — JupyterHub and Docker Spawner configuration.
- **`jupyterhub/`** — JupyterHub server image (Dockerfile).
- **`user-notebook/`** — User notebook server image (Dockerfile).
- **`files/`** — Welcome and demo notebooks (e.g. `Welcome_to_PDS_SBN.ipynb`, `CSS_Catalina_Sky_Survey_Demo.ipynb`).
- **`access_control/`** — Allow-list and access control assets.
- **`docker-compose.yml`** — Orchestration for local or deployment use.

---

*User guide source: KBase JupyterHub User Guide. Last updated: January 2026.*
