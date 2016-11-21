import React, { PropTypes } from 'react';
import classNames from 'classnames';
import 'whatwg-fetch';


export default class VisualiseWeather extends React.Component {
  static propTypes = {
    'city_name': PropTypes.string,
    'city_id': PropTypes.number,
  }

  state = {
    forecast: null,
    status: 'empty',
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.city_id != this.props.city_id){
      this.fetchForecast(city_id);
    }
  }

  componentDidMount() {
    this.fetchForecast(this.props.city_id);
  }

  fetchForecast(city_id) {
    this.setState({
      forecast: null,
      status: 'loading'
    });

    fetch(`/api/v1.0/forecast/${city_id}/`, {
      method: 'get',
      credentials: 'same-origin',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    })
    .then(res => res.json())
    .then(res => {
      // Everything went to plan, so return the list
      // of companies.
      if (typeof res === 'undefined') {
        console.log('undefined');
      }
      this.setState({
        forecast: res,
        status: 'loaded'
      });
    })
  }

  render() {
    const {status, forecast} = this.state;
    const {city_name} = this.props;
    const min = forecast ? forecast.min : '';
    const average = forecast ? forecast.average.toFixed(2) : '';
    const max = forecast ? forecast.max : '';
    const humidity = forecast ? forecast.humidity : '';

    return (
      <div className="card card-block text-xs-center">
          <div className="row">
              <div className="col-xs-12">
                  <h2>{city_name}</h2>
              </div>
              <div className="col-xs-3">
                  <h2>{min}<small>°C</small></h2>
                  <span className="tag tag-info">minimum</span>
              </div>
              <div className="col-xs-3">
                  <h2>{average}<small>°C</small></h2>
                  <span className="tag tag-success">average</span>
              </div>
              <div className="col-xs-3">
                  <h2>{max}<small>°C</small></h2>
                  <span className="tag tag-danger">maximum</span>
              </div>
              <div className="col-xs-3">
                  <h2>{humidity}<small>%</small></h2>
                  <span className="tag tag-primary">humidity</span>
              </div>
          </div>
      </div>
    );
  }
}
