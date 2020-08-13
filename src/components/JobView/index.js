import React, { Component } from "react";
import PropTypes from "prop-types";
import Header from "../Header";
import JobDetails from "../Job_detail";

class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="App">
        <Header />
        <div className="body__cont">
          <JobDetails />
        </div>
      </div>
    );
  }
}

export default index;
