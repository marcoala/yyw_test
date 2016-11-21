require('babel-core/polyfill');
import React from 'react';
import ReactDOM from 'react-dom';

import Search from './components/search'
import VisualiseWeather from './components/visualise_weather'

var updateCity = function(city_id, city_name) {
  var element = document.getElementById('visualise-weather');
  ReactDOM.unmountComponentAtNode(element);
  ReactDOM.render(React.createElement(VisualiseWeather, {city_name: city_name, city_id: city_id}), element);
}

ReactDOM.render(React.createElement(Search, {onSelectCity: updateCity}), document.getElementById('search'));
ReactDOM.render(React.createElement(VisualiseWeather, {city_name: 'London', city_id: 18608}), document.getElementById('visualise-weather'));
