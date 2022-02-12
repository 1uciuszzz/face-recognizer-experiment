# Face-Recognizer-Experiment

## About

This is a simple experiment of face recognition system.

### Built With

- [opencv](https://github.com/opencv/opencv)
- [numpy](https://github.com/numpy/numpy)
- [keras](https://github.com/keras-team/keras)
- [serial](https://github.com/wjwwood/serial)

## Getting Started

### Prerequisites

Make sure you have installed python(recommand version 3.8).

### Installation

1. Download the project source. And then go into project folder.

2. I have used `pipenv` as my package manager. So running enviroment could be installed easily.

```sh
pip install pipenv
```

```sh
pipenv install
```

## Usage

1. Collect the face photo who you want. These photo will be used as face templates.

```sh
pipenv run data_gen.py
```

When you running the code, a name(or code) string should be input by you.

> Maybe you should check code line 3 in `data_gen.py`, you should make sure the `haarcascade_frontalface_alt.xml` is correct path.

When you finish this step. You will see a folder called `dataSet` created. In this folder, there is a User.[name] folder that storaged 100 pieces your face photos you just collect.

2. Then transfer the photo you just collect to data.

```sh
pipenv run trainner.py
```

When you finish this step, you can see a file named `trainner.yml` was created which storaged all the data of face photos.

3. Setup the final procedure:

```sh
pipenv run reco.py
```

## Contributers

- [jessnzz](https://github.com/jessnzz)
- [ydumund](https://github.com/ydumund)
- [KyrieZHR](https://github.com/KyrieZHR)
- [edragonz](https://github.com/edragonz)

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.
