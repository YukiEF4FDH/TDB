# TDB Report Demo

This is a demo version of our system, with classical server-client architecture.
To set up for each demo, both server-side and client-side need to be prepared.

Pipeline of this system:
<img src="https://gyazo.com/32cddd1d70f0e3e3601b4b3a343604e9.png" style="zoom:67%;" />

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

Then, the preparation on the client-side is done. 
Run the command to set up under the folder `client`.

```
npm run serve
```

**If** there is any error looks like this:

```
error in ./node_modules/monaco-editor/esm/vs/basic-languages/_.contribution.js 
...
_languageId
...
```

, you should re-install the monaco-editor package and monaco-editor-webpack-plugin package with the `@` mark to assign the right versions, refer to [Version Matrix](https://www.npmjs.com/package/monaco-editor-webpack-plugin). For example,

```
npm install --save-dev monaco-editor@0.30.0
npm install --save-dev monaco-editor-webpack-plugin@6.0.0
```

(You don't need to do this if there's no error after running serve).

## Check the Demo

After the setup of both server and client, you can access http://localhost:8080/ in the browser to check the demo.

It would look like this.

<img src="https://gyazo.com/597133f2cc9a064266c97f4c216d8319.png" alt="image-20211230162149051" style="zoom:80%;" />

To check different demos, you can copy the content of different specification files in `/server` into `Specifications.json`.
