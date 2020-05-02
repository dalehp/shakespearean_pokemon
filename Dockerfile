FROM python:3.7-slim
RUN pip install poetry
WORKDIR /tmp/myapp
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
ENV FLASK_APP shakespearean_pokemon
COPY . .
RUN poetry install
CMD poetry run flask run -h 0.0.0.0