import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

const NOTE_URL = 'http://localhost:5000/note';

const fetchNextNote = () => 
  fetch(NOTE_URL).then(response => response.json());

const checkAnswer = (answer) => 
  fetch(NOTE_URL, {
    body: JSON.stringify(answer),
    cache: 'no-cache',
    headers: {
      'content-type': 'application/json'
    },
    method: 'POST'
  }).then(response => response.json());

ReactDOM.render(
  <App
    fetchNextNote={fetchNextNote}
    checkAnswer={checkAnswer}
  />,
  document.getElementById('root')
);
registerServiceWorker();
