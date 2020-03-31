# Sample Project: Activity to Practice Piano Notes

This project provides a work-in-progress codebase for a web-based activity that assists in learning the piano.

The project has two parts:

* A server (written in Python using Flask) which manages the data for the application
* A client (written in ES6 using React) which displays the activity to the user in a web browser

## Getting up and running

* Make sure python (version 3.5+) and node JS are installed on your system
* Install Flask into the python environment using `pip install flask`
* Navigate to the `client` folder and run `npm install`
* Once dependencies are installed, run `npm run build` to build the client project
* Navigate to the `server` folder, run `python run_server.py`
* Open http://localhost:5000/ to access the activity

## Task

This is a small starter project which we hope will become a fully-fledged activity. Your task is to add new functionality to this project to produce a working end product.

# New Functionality to Implement

The server and client need to be finished off such that:

## Server
* notes are served in a sequence (at the moment the same note is served over and over again - perhaps this could make a tune?)
* keys pressed by the user are checked on the server, against the current note in the sequence
* the sequence of notes progresses when the user provides the correct key (until the end of the sequence)
* a new method is added which provides the user with summary data of correct/incorrect attempts within the provided sequence

## Client
* when a key is pressed, it is checked with the server (using this.props.checkAnswer in App.js) to determine if this is the matching key, and feedback is given to the user (in a user-friendly manner of your design)
* the next note is then requested from the server, and displayed to the user
* a way for the activity to be completed, and a summary reported to the user's of their success (e.g. which keys were correct, and which they need to work on)

### Extension Ideas:

Demonstrate what you can do by adding your own functionality, e.g.
* storage of data in a data store (e.g. sqlite)
* support for multiple users: logging into a user session and storing where each user is up to in the activity
* improvement of look and feel, e.g. show off some CSS artisanry (or add other packages such as SCSS), or add audio when pressing the keys
* add unit tests that provide good testing coverage
* add a Redux store to the project such that state is no longer stored within App.js
* user results are reported on a separate page which can also be navigated to as a single page app (SPA)
* additional functionality of your choosing which adds educational value to the activity (be creative!)
* add a way for users to share their results, or upload their own sequences/tunes to teach each other

# Next Steps
Implement as much as you reasonably can, and document any ideas that you don't have the time to build - we may have the opportunity to try and implement some of them together.

