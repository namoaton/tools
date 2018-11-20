import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
print(packages)
for i in range(len(packages)):
    try:
        call("pip3 install --upgrade " + packages[i], shell=True)
    except:
        print("Ups!!! " + packages[i])
