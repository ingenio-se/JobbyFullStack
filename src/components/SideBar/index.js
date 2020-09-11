import React, { Component } from "react";
import PropTypes from "prop-types";
import "./style/index.scss";
import axios from "axios";

class index extends Component {
  constructor(props) {
    super(props);
    // console.log(props)
    this.state = {
      salary: "",
    };
    // bind

    this.handleChange = this.handleChange.bind(this);
    //this.search = this.search.bind(this);
  }

  static propTypes = {
    prop: PropTypes,
  };
  handleChange({ target }) {
    console.log(target.value);
    let url = "/salary/" + target.value;
    axios
      .get(url)
      .then((resp) => {
        console.log(resp.data);

        this.setState({
          jobs: resp.data,
        });

        this.props.handleJobs(this.state.jobs);
      })
      .catch((err) => {
        console.log(err);
      });
  }
  render() {
    return (
      <div className="sidebar__container">
        {/* <h3>Salary Rank</h3> */}
        <form>
          <div data-role="rangeslider">
            <label for="range-1a">Salary Rank</label>
            <input
              type="range"
              name="range-1a"
              id="range-1a"
              min="0"
              max="130"
              value="30"
              // data-popup-enabled="true"
              // data-show-value="true"
            ></input>
            <label for="range-1b">Salary Rank</label>
            <input
              type="range"
              name="range-1b"
              id="range-1b"
              min="0"
              max="130"
              value="90"
              // data-popup-enabled="true"
              // data-show-value="true"
            ></input>
          </div>
        </form>
      </div>
    );
  }
}

export default index;
