First of all you have to build project first and:

1. Create a Dockerfile:
First, we need to create a file called Dockerfile in our project folder. Inside this file, we write the following code:

![image](https://github.com/user-attachments/assets/0584207b-acc7-41d6-8493-211bbde37ea8)

Let me explain each line:

FROM python:3.10-alpine: 
This line tells Docker to use a version of Python 3.10 as the image.

WORKDIR /web: 
This sets the working directory inside the container to /web.

COPY finalweb/ .: 
This copies all files from the finalweb/ folder on my computer to the /web directory in the container.

COPY requirements.txt .: 
This copies the requirements.txt file to the container.

RUN pip install -r requirements.txt: 
This installs all the dependencies listed in requirements.txt.

EXPOSE 8000: 
This tells Docker that this app will use port 8000.

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]: 
This is the command that starts the Django web server and listens on port 8000.

2. Create a requirements.txt file:
Next, you need to create a file called requirements.txt in the project folder. This file lists all the dependencies my project needs. For example:

![image](https://github.com/user-attachments/assets/fd0511b1-9b0f-4eba-ba87-e0094c0f3582)

These are the packages my project needs to run properly.

3. Build the Docker image:
Once the Dockerfile and requirements.txt are ready, I need to build the Docker image using this command:

![image](https://github.com/user-attachments/assets/e3a6d1a1-4c21-4a2f-aeaa-b1dcdf672d35)

This command will build the image and tag it with the name demo-py-web.

4. Run the Docker container:
After the image is built, I can run the container with this command:

![image](https://github.com/user-attachments/assets/348e19b3-84ad-480f-ae86-d2def4dfd6a6)

Let me explain:

-d: This makes the container run in the background.
-p 8000:8000: This connects port 8000 on your machine to port 8000 in the container.
5. Access the web app:
Once the container is running, you can access the web app by going to http://localhost:8000 in your browser.
