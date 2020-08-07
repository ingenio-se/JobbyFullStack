import React, { Component } from "react";
import PropTypes from "prop-types";
import "./style/index.scss";

class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="sidebar__container">
        <h3>Salary Rank</h3>
        <ul>
          <li>
            <input type="checkbox" name="" id="" /> 10k - 20k
          </li>
          <li>
            <input type="checkbox" name="" id="" /> 21k - 30k
          </li>
          <li>
            <input type="checkbox" name="" id="" /> 31k - 40k
          </li>
          <li>
            <input type="checkbox" name="" id="" /> 41k - 50k
          </li>
          <li>
            <input type="checkbox" name="" id="" /> 51k - 60k
          </li>
        </ul>
      </div>
    );
  }
}

export default index;
