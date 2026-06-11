FROM python:3.13 AS build

WORKDIR /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pytest -v

FROM python:3.13
COPY --from=build /venv /venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /app
COPY --from=build /app/app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000