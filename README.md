# SWE40006 – Task 4: Deploy Containers Using Docker

> For assignment submission and lecturer only.

## Student Details
- **Name:** Chua Weng Kin
- **Student ID:** 106214072
- **Unit:** SWE40006 Software Deployment and Evolution
- **Level attempted:** 4.4 (High Distinction)

## Tasks Attempted

| Task | Level | Folder | What it is |
|---|---|---|---|
| 4.1 | Pass | – | Docker account, Docker install, hello-world |
| 4.2 | Credit | `dockertaskCredit` | Python hello-world web server, pulled to another Docker device |
| 4.3 | Distinction | `webapp` | Notes web app (Flask) |
| 4.4 | HD | `cli-app` | Command-line App (non-web) |

# Note
**Everything is documented in my Submission assignment**, all the instructions below are for those who want to test it out.
i.e [VM-public-ip] = Your ip when testing

# Docker Pulling
My docker images for these task is Public, so you can pull it if you want to and not download the the files here. (unless pulling not working)

Task 4.2
```
docker pull wkin/dockertask:1.0
```

Task 4.3
```
docker pull wkin/webapp:1.0
```

Task 4.4
```
docker pull wkin/cli-app:1.0
```
## Folder Structure

```
swe40006--task-4
├── cli-app
│   ├── dockerfile
│   └── main.py
├── dockertaskCredit
│   ├── app.py
│   ├── dockerfile
│   └── requirements.txt
└── webapp
    ├── dockerfile
    ├── requirements.txt
    └── webapp.py
```

## 4.2 – Python Hello-World Web Server (`dockertaskCredit`)
A small Flask server that shows a "Hello World" message. The Dockerfile uses a Python image, so it adds the Python run-time.

**Run on Device A (laptop):**
```bash
cd dockertaskCredit
docker build -t wkin/dockertask:1.0 .
docker run -d -p 5000:5000 --name dockertask wkin/dockertask:1.0
```
Open `http://localhost:5000`.

**Pull and run on Device B (Ubuntu VM):**
```bash
docker pull wkin/dockertask:1.0
docker run -d --restart unless-stopped -p 80:5000 wkin/dockertask:1.0
```
Open `http://[VM-public-IP]`.

## 4.3 – Notes Web App (`webapp`)
A Flask web app. The user can add and delete notes on a web page. Notes are kept in memory, so they are lost when the container restarts.

**Run on Device A:**
```bash
cd webapp
docker build -t wkin/webapp:1.0 .
docker run -d -p 5001:5001 --name webapp wkin/webapp:1.0
```
Open `http://localhost:5001`.

**Pull and run on Device B (Ubuntu VM):**
```bash
docker pull wkin/webapp:1.0
docker run -d --restart unless-stopped -p 8080:5001 --name webapp wkin/webapp:1.0
```
Open `http://[VM-public-IP]:8080`.

## 4.4 – cli-app App (`cli-app`)
A command-line app. It is **not** a web app and has no port. The user chooses a tool from a menu:
1. Temperature Converter (Celsius and Fahrenheit)
2. Number Guessing Game (number from 1 to 100)
3. Word Counter (words, characters, most common words)

If there is no keyboard input, the app runs in **demo mode** and prints to the logs.

**Run on Device A:**
```bash
cd cli-app
docker build -t wkin/cli-app:1.0 .
docker run -it --rm wkin/cli-app:1.0
```

**Demo mode and logs:**
```bash
docker run --name cli-demo wkin/cli-app:1.0
docker logs cli-demo
```

**Pull and run on Device B (Ubuntu VM):**
```bash
docker pull wkin/cli-app:1.0
docker run -it --rm wkin/cli-app:1.0
```

## Technology Used
- Python 3.12 (slim Docker image)
- Flask (web apps)
- Docker
- Docker Hub
- Ubuntu Virtual Machine


