import React, { PropTypes } from 'react';
import classNames from 'classnames';
import 'whatwg-fetch';


export default class Search extends React.Component {
  static propTypes = {
    onSelectCity: PropTypes.func
  }

  static defaultProps = {
    onSelectCity: function(city_id, city_name) {}
  };

  state = {
    status: 'empty',
    lookup_string: '',
    search_results: []
  }

  handleChange(evt) {
    const lookupString = evt.target.value;

    this.setState({
      lookup_string: lookupString
    });

    this.fetchCities(lookupString);
  }

  fetchCities(query) {
    const encodedQuery = encodeURIComponent(query);
    this.setState({
      search_results: [],
      status: 'loading'
    });

    fetch(`/api/v1.0/city/?q=${encodedQuery}`, {
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
        search_results: res,
        status: 'loaded'
      });
    })
  }

  handleSelectCity(search_result) {
    this.props.onSelectCity(search_result.id, search_result.name);
    this.setState({
      search_results: []
    });
  }

  render() {
    const {status, search_results, lookupString} = this.state;
    const hasResults = (search_results.length) ? true : false
    return (
      <div>
        <div className="form-group">
          <label htmlFor="seach_input">Search a city name</label>
          <input
            type="text"
            className="form-control"
            id="seach_input"
            placeholder="London..."
            onChange={::this.handleChange}
            ></input>
          <small className="form-text text-muted">Type something and we'll search the city in our database</small>
          { hasResults &&
            <div className="dropdown">
              <div className="dropdown-menu">
              { search_results.map((search_result, i) => {
                return(<a
                  className="dropdown-item"
                  key={i}
                  onClick={this.handleSelectCity.bind(this, search_result)}
                >{search_result.name}
              </a>);
              })}
            </div>
          </div>}
        </div>
      </div>
    );
  }
}
