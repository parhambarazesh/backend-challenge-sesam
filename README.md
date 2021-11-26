# Sesam Backend Challenge

A small programming challenge for applicants for backend positions in Sesam.

# Overview

This task is designed to test some general skills that are important for a backend/fullstack developer without being too time-consuming. Some of the things you encounter while working on this task: Git, GitHub, a JSON REST API, Python, Flask, Docker.

This challenge involves building a small API server and corresponding command-line client, both in Python, that allow uploading and processing JSON files, such as those included in the repo.

# Setup

Fork this repository to your own GitHub account as a private repository (don't create pull requests to https://github.com/sesam-io/backend-challenge directly). Add `@branislavjenco`, `@BaardBouvet` and `@grove` as collaborators (you can do this when you are finished or right at the start).

# Task

For this task we'll be building a very simple Python 3-based REST API server and command-line client. 




## API Server

The API server should have a single root endpoint, `/datasets/`, that allows list and CRUD operations over a dataset object via the following API / HTTP verbs:

 - `GET /datasets/` - list the uploaded datasets
 - `POST /datasets/` - creates a dataset. This endpoint takes a JSON file as input, and stores it somewhere/how on the server. A reference to this created object is returned by the endpoint, for instance an `id` or `url`.
 - `GET /datasets/<id>/` - return the file name, and size of the dataset object
 - `DELETE /datasets/<id>/` - delete the dataset object
 - `GET /datasets/<id>/excel/` - export the dataset as an excel file

## Client Library

The client app should be a fully standalone command-line python application. The app should provide command-line arguments that correspond and support each of the API actions above - how you structure the command line arguments and what you call them is left up to you.

## Technologies

You may use any Python libraries and technologies of your choice, but we would like you to use [Flask](https://flask.palletsprojects.com/en/2.0.x/) for serving the requests. We would also like you to build a [Docker](https://www.docker.com/) image for the API server and run it as a Docker container. It's up to you to use other Python development and packaging tools, like `virtualenv` and `setuptools`.

# Notes

- do not hesitate to ask us any questions
- don't worry if you can't finish all aspects of the task - make notes on where you got stuck and why
- it's all about conveying to us what your process was when tackling the challenge
