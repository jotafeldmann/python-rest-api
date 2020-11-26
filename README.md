# Pokemon API

## Purpose

REST API for Pokemons.

## Requirements

- [Python 3.9](https://www.python.org/downloads/)
- [Docker (optional but recommended)](https://docs.docker.com/get-docker/)

For development only:

- [Docker (optional but recommended)](https://docs.docker.com/get-docker/)

Local:

- [pip](https://pip.pypa.io/en/stable/)
- [venv](https://docs.python.org/3/library/venv.html)
- [make](https://www.gnu.org/software/make/manual/make.html)
- [NPM](https://www.npmjs.com/get-npm)

## API

- [Tornado 6.1](https://www.tornadoweb.org/)

## Setup

Copy the `.env.example` to `.env` (NEVER COMMIT the .env file or sensitive data)

```bash
make env/file
```

Docker

```bash
make docker/build
```

Local

```bash
make install
```

## How to run

Docker

```bash
make docker/run
```

Local

```bash
make
```

## How to dev (with venv)

- Create env

```bash
make env/create
```

- Start env

```bash
source .venv/bin/activate

#or

make env
```

- Install

```bash
make install
```

- Run as developer mode (watch and reload)

We use [Nodemon](https://nodemon.io/) for this.

```bash
make dev
```

- Run tests (watch and reload)

```bash
make tests/watch
```

- Run tests once

```bash
make tests
```

Please check the [Makefile](./Makefile) for more options.

## More info

- [How it works](./docs/how-it-works.md)
- [Purpose](./docs/purpose.md)
- [Tech issues](./docs/tech-issues.md)

## Author

- [Jorge Feldmann](https://github.com/jotafeldmann)
