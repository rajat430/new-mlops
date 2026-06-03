FROM python:3.13 as test

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/app

RUN pytest -v

FROM python:3.13

WORKDIR app/app
COPY --from=test /app/app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000