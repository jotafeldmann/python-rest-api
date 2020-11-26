FROM python:3.9

ENV DATA_FOLDER=/data
ENV SRC_FOLDER=/src
ENV FILE=${DATA_FOLDER}/pokemon.csv
ENV PORT=8000

COPY ./data/pokemon.csv ${FILE}

WORKDIR ${SRC_FOLDER}

COPY ./src ${SRC_FOLDER}

RUN pip install -r ${SRC_FOLDER}/requirements.txt

EXPOSE ${PORT}

CMD python ${SRC_FOLDER}/main.py ${FILE} --port ${PORT}
