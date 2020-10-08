FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
COPY ./flask_demo  C:/2020Training/DataScientist1000/deploy_demo/
EXPOSE 5000
WORKDIR C:/2020Training/DataScientist1000/deploy_demo/
RUN pip install -r requirements.txt
CMD python flask_predict_file_api.py