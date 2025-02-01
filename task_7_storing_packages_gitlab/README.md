This script uses packages stored in the cache, takes these packages from cache and then puts them
to Gitlab Package Registry.

Script runs without argument.

For credential used configuration file ~/.pypirc

``````
[distutils]
index-servers =
    gitlab

[gitlab]
repository = https://gitlab.com/api/v4/projects/<id project>/packages/pypi
username = 
password = 
```