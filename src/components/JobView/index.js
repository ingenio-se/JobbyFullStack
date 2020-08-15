import React, { Component } from "react";
import PropTypes from "prop-types";
import Header from "../Header";
import JobDetails from "../Job_detail";
import axios from 'axios';

class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
       job:'',
       jobId:0,
    }
    // bind
    
  }
  static propTypes = {
    prop: PropTypes,
  };
  componentDidUpdate(){
    //console.log(this.state.jobId)
  }
  componentDidMount () {
    const { jobId } = this.props.match.params
    //console.log(jobId)
    this.setState({
      jobId: jobId,
    }, () => {
    let url = '/get/'+this.state.jobId
    axios.get(url)
    .then(resp => {
        //console.log(resp.data);
        this.setState({
            job: resp.data,
        });
        
    })
    .catch(err => {
        console.log(err)
    })

  });
  }
  render() {
    if (this.state.job !==''){
    return (
      <div className="App">
        <Header />
        <div className="body__cont">
          <JobDetails job={this.state.job}/>
        </div>
      </div>
    );
    }
    else{
      return(
        <div></div>
      );
    }
  }
}

export default index;
