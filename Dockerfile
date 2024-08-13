FROM python:3.9-slim-buster


RUN mkdir /data /fastapi /model
# Set the working directory to /app
WORKDIR .

# Copy the current directory contents into the container at /app
COPY  /data/ /data
COPY /fastapi/ /fastapi
COPY /model/ /model
COPY phData.png .
COPY createModel.py .
COPY requirements.txt .
COPY conda_environment.yml .

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /fastapi

ENV POSTGRES_PASSWORD=AVNS_TkDOgQ4c89kBWqZOhls
ENV POSTGRES_USER=avnadmin
ENV POSTGRES_USER_DB=predictor


# Make port 80 available to the world outside this container
EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
