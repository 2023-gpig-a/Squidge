# squidge

Repo that brings the other repos together

## squidging

To obtain and update this whole repo:

```sh
$ git clone git@github.com:2023-gpig-a/squidge.git
$ cd squidge
$ git submodule update --init --recursive
```

## configuring

```sh
$ cp dmas_config.ini.example dmas_config.ini
```

Fill in a plantnet API key.

## Running

```
$ docker-compose up -d
# or to only run specific components (in this case DB and DMAS)
$ docker-compose up -d db dmas
```

### adding a new repo to the squidge

```sh
$ git submodule add git@github.com:2023-gpig-a/magical-new-subproject.git
$ git add magical-new-subproject
$ git commit
$ git push
```
