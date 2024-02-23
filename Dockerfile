# The Base image to be used
FROM python:3.8-slim-buster 

# Updating the essential packages
RUN apt update 


# Setting the working directory for application
WORKDIR /app 


COPY requirements.txt /app/requirements.txt 
RUN python -m pip --no-cache-dir install -r requirements.txt


COPY . /app/ 


EXPOSE 8082


CMD ["streamlit", "run", "interface.py", "--server.port", "8082"]