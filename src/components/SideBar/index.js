import React, { Component } from "react";
import PropTypes from "prop-types";
import "./style/index.scss";
import axios from 'axios';

class index extends Component {
  constructor(props) {
    super(props);
   // console.log(props)
    this.state = {
       salary:'',
    }
    // bind
    
    this.handleChange = this.handleChange.bind(this);
    //this.search = this.search.bind(this);
    
  }

  static propTypes = {
    prop: PropTypes,
  };
  handleChange({ target }) {
    console.log(target.value)
    let url = '/salary/'+target.value
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
  
  }
  render() {
    return (
      <div className="sidebar__container">
        <h3>Salary Rank</h3>
        <ul>
         
          <li>
            <input type="checkbox" name="salary" id="" value="25-40" onClick={this.handleChange}/> 25k - 40k
          </li>
          <li>
            <input type="checkbox" name="salary" id="" value="40-60" onClick={this.handleChange} />40k - 60K
          </li>
          <li>
            <input type="checkbox" name="salary" id="" value="60-80" onClick={this.handleChange}/> 60k - 80k
          </li>
          <li>
            <input type="checkbox" name="salary" id="" value="80-100" onClick={this.handleChange}/>80k - 100k
          </li>
          <li>
            <input type="checkbox" name="salary" id="" value="100-180" onClick={this.handleChange}/>100k - 180k
          </li>
          <li>
            <input type="checkbox" name="salary" id="" value="120-180" onClick={this.handleChange}/>120k - 180k
          </li>
        </ul>
      </div>
    );
  }
}

export default index;
