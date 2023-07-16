FROM python
LABEL maintainer "Pulugia <pulugia57@gmail.com>"

ENV DATAPATH='/data/'
RUN pip3 install flask numpy pandas

COPY data/ /data
WORKDIR /app
COPY attack/pokemon_att.py .

ENTRYPOINT [ "python" ]
CMD ["pokemon_att.py"]
