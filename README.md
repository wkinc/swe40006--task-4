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
| 4.4 | HD | `cli-app` | Command-line Multi-Tool App (non-web) |

## Public Links

| Item | Link |
|---|---|
| Python hello-world (port 80) | http://[VM-public-IP] |
| Notes web app (port 8080) | http://[VM-public-IP]:8080 |
| Docker Hub: Python hello-world | [link] |
| Docker Hub: Notes web app | [link] |
| Docker Hub: Multi-Tool App | [link] |

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
docker build -t [yourdockerid]/py-hello:1.0 .
docker run -d -p 5000:5000 --name py-hello [yourdockerid]/py-hello:1.0
```
Open `http://localhost:5000`.

**Pull and run on Device B (Azure VM):**
```bash
docker pull [yourdockerid]/py-hello:1.0
docker run -d --restart unless-stopped -p 80:5000 [yourdockerid]/py-hello:1.0
```
Open `http://[VM-public-IP]`.

## 4.3 – Notes Web App (`webapp`)
A Flask web app. The user can add and delete notes on a web page. Notes are kept in memory, so they are lost when the container restarts.

**Run on Device A:**
```bash
cd webapp
docker build -t [yourdockerid]/notes-app:1.0 .
docker run -d -p 5001:5001 --name notes-app [yourdockerid]/notes-app:1.0
```
Open `http://localhost:5001`.

**Pull and run on Device B (Azure VM):**
```bash
docker pull [yourdockerid]/notes-app:1.0
docker run -d --restart unless-stopped -p 8080:5001 --name notes-app [yourdockerid]/notes-app:1.0
```
Open `http://[VM-public-IP]:8080`.

## 4.4 – Multi-Tool App (`cli-app`)
A command-line app. It is **not** a web app and has no port. The user chooses a tool from a menu:
1. Temperature Converter (Celsius and Fahrenheit)
2. Number Guessing Game (number from 1 to 100)
3. Word Counter (words, characters, most common words)

If there is no keyboard input, the app runs in **demo mode** and prints to the logs.

**Run on Device A:**
```bash
cd cli-app
docker build -t [yourdockerid]/multi-tool:3.0 .
docker run -it --rm [yourdockerid]/multi-tool:3.0
```

**Demo mode and logs:**
```bash
docker run --name multi-demo [yourdockerid]/multi-tool:3.0
docker logs multi-demo
```

**Pull and run on Device B (Azure VM):**
```bash
docker pull [yourdockerid]/multi-tool:3.0
docker run -it --rm [yourdockerid]/multi-tool:3.0
```

## Technology Used
- Python 3.12 (slim Docker image)
- Flask (web apps)
- Docker [version]
- Docker Hub
- Azure Ubuntu Virtual Machine

## Notes
- The VM stays on during the marking period so the public links work.
- Source code is in this repository. It is not included in the report.
