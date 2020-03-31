import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render( <App
    fetchNextNote={() => Promise.resolve()}
    checkAnswer={() => Promise.resolve()}
  />, div);
  ReactDOM.unmountComponentAtNode(div);
});
