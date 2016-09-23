FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY helloworld.py /src/helloworld.py

COPY templates /src/templates

EXPOSE  8000
CMD ["python", "/src/helloworld.py", "-p 8000"]