# squidge

Repo that brings the other repos together

## squidging

To obtain and update this whole repo:

```sh
$ git clone git@github.com:2023-gpig-a/squidge.git
$ cd squidge
$ git submodule update --init --recursive
```

## Running

```
$ docker-compose up -d
```

### adding a new repo to the squidge

```sh
$ git submodule add git@github.com:2023-gpig-a/magical-new-subproject.git
$ git add magical-new-subproject
$ git commit
$ git push
```
