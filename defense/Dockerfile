FROM python
LABEL maintainer "Pulugia <pulugia57@gmail.com>"

ENV DATAPATH='/data'
RUN pip3 install flask numpy pandas

COPY data/ /data
WORKDIR /app
COPY defense/pokemon_def.py .

ENTRYPOINT [ "python" ]
CMD ["pokemon_def.py"]
