FROM python:3.12
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY templates ./templates
COPY main.py .

EXPOSE 8080

#RUN useradd app
#USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]