import React, { Component } from "react";
import PropTypes from "prop-types";
import Header from "../Header";
import Sidebar from "../SideBar";
import Cards from "../Job_cards";
import { Link } from "react-router-dom";
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
    
    this.handleJobs = this.handleJobs.bind(this);
    
  }
 
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
    
    this.setState({
      jobs: '',
    }, () => {
      let url = '/top/10'
      axios.get(url)
        .then(resp => {
            console.log(resp.data);
            this.handleJobs(resp.data)
        })
        .catch(err => {
            console.log(err)
        })
    
    });
    
  }
  render() {
    const { jobs } = this.state;
    console.log(jobs)
   
    if (jobs != '' ){
    return (
      <div className="App">
        <Header handleJobs ={this.handleJobs}/>
        <div className="body__container">
          <Sidebar handleJobs ={this.handleJobs}/>
          <section className="cards__cont">
            { 
            jobs.map((item) =>
                <Cards job={item} children={item[1]}/>
            )}
            
          </section>
        </div>
      </div>
    );
            }
            else{
              return (<div></div>);
            }
  }
}

export default index;
