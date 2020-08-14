import React, { Component } from "react";
import PropTypes from "prop-types";
import Header from "../Header";
import Sidebar from "../SideBar";
import Cards from "../Job_cards";
import axios from 'axios';

class index extends Component {
  constructor(props) {
    super(props);
   // console.log(props)
    this.state = {
       search : '',
       jobs:[]
    }
    // bind
    
    this.handleJobs = this.handleJobs.bind(this);
    
  }
  static propTypes = {
    prop: PropTypes,
  };
  handleJobs(jobs){
    this.setState({
      jobs: [],
    }, () => {
    this.setState({
      jobs: jobs
    })
  });
  }
  componentDidMount(){
    /*
    let url = '/search/python'
    axios.get(url)
      .then(resp => {
          console.log(resp.data);
          this.setState({
              jobs: resp.data,
          });
          
      })
      .catch(err => {
          console.log(err)
      })
    */
  }
  render() {
    const { jobs } = this.state;
    console.log(jobs)
   
    
    return (
      <div className="App">
        <Header handleJobs ={this.handleJobs}/>
        <div className="body__container">
          <Sidebar />
          <section className="cards__cont">
            { 
            jobs.map((item) =>
                <Cards job={item}/>
            )}
            
          </section>
        </div>
      </div>
    );
  }
}

export default index;
