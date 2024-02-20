

FROM python:3.9
WORKDIR /code

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt


ENV H2O_WAVE_LISTEN=":7860"
ENV H2O_WAVE_ADDRESS='http://127.0.0.1:7860'

CMD ["wave", "run", "app", "--no-reload"]