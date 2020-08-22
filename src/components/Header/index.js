import React, { Component } from "react";
import PropTypes from "prop-types";
import logo from "./assets/logo.png";
import "./style/index.scss";
import axios from 'axios';

class index extends Component {
  constructor(props) {
    super(props);
   // console.log(props)
    this.state = {
       search : '',
       jobs:''
    }
    // bind
    
    this.handleChange = this.handleChange.bind(this);
    this.search = this.search.bind(this);
    
  }
  static propTypes = {
    prop: PropTypes,
  };
  handleChange({ target }) {
    this.setState({
        [target.name]: target.value
    });
 }
 search(){
  this.setState({
    jobs: '',
  }, () => {
    let url = '/search/'+this.state.search
    axios.get(url)
      .then(resp => {
          console.log(resp.data);
          this.setState({
              jobs: resp.data,
          });
          this.props.handleJobs(this.state.jobs);
      })
      .catch(err => {
          console.log(err)
      })
  
  });
  
 }
  render() {
    return (
      <div className="header__container">
        <img src={logo} alt="Logo" />
        <input type="text" name="search" placeholder="Use Key words..." value={this.state.search} onChange={this.handleChange} />
        <button type="submit" onClick={this.search}>Search</button>
      </div>
    );
  }
}

export default index;
