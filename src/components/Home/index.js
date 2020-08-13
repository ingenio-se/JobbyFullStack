import React, { Component } from "react";
import PropTypes from "prop-types";
import Header from "../Header";
import Sidebar from "../SideBar";
import Cards from "../Job_cards";

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
      jobs: jobs
    })
  }
  render() {
    const { jobs } = this.state;
    jobs.map((item) =>
        console.log(item)
    );
   
    
    return (
      <div className="App">
        <Header handleJobs ={this.handleJobs}/>
        <div className="body__container">
          <Sidebar />
          <section className="cards__cont">
            {jobs.map((item) =>
                <Cards job={item}/>
            )}
            
          </section>
        </div>
      </div>
    );
  }
}

export default index;
