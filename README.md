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

DMAS requires trained weights to work.
These use the human detection dataset available at: https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset.
Download this and extract it to DMAS/models/human_detection/datasets/human_detection_dataset.
Then, to train the model, run the following commands.
```
$ cd DMAS
$ python3 -m venv venv
$ . venv/bin/activate (linux) or ./venv/Scripts/activate (win)
$ pip install -r requirements.txt
$ cd models/human_detection
$ python3 human_detector.py 
```

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
