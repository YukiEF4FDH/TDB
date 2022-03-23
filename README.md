# TDB Report Demo

This is a demo version of our system, with classical server-client architecture.
To set up for each demo, both server-side and client-side need to be prepared.

Pipeline of this system (ver. 202112)
![](https://gyazo.com/bb95ea7d5eac8086ce9bcc0e9d4f2cfd.png)

## Server-side Setup

The server-side is developed with Flask.

Open the cmd window under the folder `server`, where to create and activate the virtual environment.

```
python -m venv env
env\Scripts\activate.bat
```

Install Flask and Flask-CORS extensions.

```
pip install Flask==1.1.2 Flask-Cors==3.0.10
```

Then, the preparation on the server-side is done.
Run the command to set up under the folder `server`.

```
python app.py
```

## Client-side Setup

The client-side is developed with Vue.js and managed with npm.

Open the cmd window under the folder `client`, and run the command to prepare the project.

```
npm install
```

You can fix the vulnerabilities according to the hints.

```
npm audit fix
```

Then, the preparation on the client-side is done. 
Run the command to set up under the folder `client`.

```
npm run serve
```

## Check the Demo

After the setup of both server and client, you can open http://localhost:8080/ in the browser to check the demo.

It would look like this.

<img src="C:\Users\Yuki_\AppData\Roaming\Typora\typora-user-images\image-20211230162149051.png" alt="image-20211230162149051" style="zoom:80%;" />
