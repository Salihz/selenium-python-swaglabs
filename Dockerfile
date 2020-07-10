FROM python:latest

RUN apt-get update && apt-get install jq -y && apt install dos2unix

RUN mkdir /home/selenium_python_swaglabs
WORKDIR /home/selenium_python_swaglabs
COPY . .

RUN chmod +x wait-for-grid.sh && dos2unix wait-for-grid.sh

RUN pip install -r requirements.txt
