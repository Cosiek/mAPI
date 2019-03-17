FROM python:3.7

# No buffering of messages
ENV PYTHONUNBUFFERED 1

# Open to outside world
EXPOSE 8000

# Copy app code into container
RUN mkdir /mAPI
WORKDIR /mAPI
ADD . /mAPI/

# Install requirements
RUN pip install -r requirements.txt

# Run this once the container is up
CMD ["sh", "on-container-start.sh"]
