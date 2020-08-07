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
        <p>hola</p>
      </div>
    );
  }
}

export default index;
