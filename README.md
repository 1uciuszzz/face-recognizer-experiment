<h1 align="center">
  <a href="https://github.com/n1ckzhao/face-recognizer-experiment">
    <!-- Please provide path to your logo here -->
  </a>
</h1>

<div align="center">
  Face-Recognizer-Experiment
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
  <br />
  <a href="https://github.com/n1ckzhao/face-recognizer-experiment/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/n1ckzhao/face-recognizer-experiment/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/n1ckzhao/face-recognizer-experiment/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Ask a Question</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/n1ckzhao/face-recognizer-experiment.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/n1ckzhao/face-recognizer-experiment/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by n1ckzhao](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-n1ckzhao-ff1414.svg?style=flat-square)](https://github.com/n1ckzhao)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project assistance](#project-assistance)
- [Contributing](#contributing)
- [Authors & contributors](#authors--contributors)
- [Security](#security)
- [License](#license)

</details>

---

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

## Project assistance

If you want to say **thank you** or/and support active development of Face-Recognizer-Experiment:

- Add a [GitHub Star](https://github.com/n1ckzhao/face-recognizer-experiment) to the project.
- Tweet about the Face-Recognizer-Experiment.
- Write interesting articles about the project on [Dev.to](https://dev.to/), [Medium](https://medium.com/) or your personal blog.

Together, we can make Face-Recognizer-Experiment **better**!

## Contributing

First off, thanks for taking the time to contribute! Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

Please read [our contribution guidelines](docs/CONTRIBUTING.md), and thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Nick Zhao](https://github.com/n1ckzhao).

For a full list of all authors and contributors, see [the contributors page](https://github.com/n1ckzhao/face-recognizer-experiment/contributors).

## Security

Face-Recognizer-Experiment follows good practices of security, but 100% security cannot be assured.
Face-Recognizer-Experiment is provided **"as is"** without any **warranty**. Use at your own risk.

_For more information and to report security issues, please refer to our [security documentation](docs/SECURITY.md)._

## License

This project is licensed under the **MIT license**.

See [LICENSE](LICENSE) for more information.
