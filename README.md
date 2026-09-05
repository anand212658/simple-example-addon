# \# Blender Extension Template

# 

# \## Reusing this for a new plugin

# 1\. Rename `simple\_example\_addon/` to your new addon's name.

# 2\. Edit `blender\_manifest.toml`: `id`, `version`, `name`, `tagline`.

# 3\. Replace `core.py` with your real code — keep the `classes` tuple and

# &#x20;  `register()`/`unregister()` shape.

# 4\. Leave `\_\_init\_\_.py` and the workflow untouched.

# 

# \## Releasing

# &#x20;   git add -A

# &#x20;   git commit -m "vX.Y.Z"

# &#x20;   git tag vX.Y.Z

# &#x20;   git push \&\& git push --tags

# 

# \## One-time setup

# \- Settings > Pages → source = `gh-pages` branch

# \- Install URL: https://<you>.github.io/<repo>/index.json

# \- In Blender: Edit > Preferences > Get Extensions > Add Remote Repository

