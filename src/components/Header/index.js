import React, { Component } from "react";
import PropTypes from "prop-types";
import logo from "./assets/logo.png";
import "./style/index.scss";

class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="header__container">
        <img src={logo} alt="Logo" />
        <input type="text" name="search" placeholder="Use Key words..." />
        <button type="submit">Search</button>
      </div>
    );
  }
}

export default index;
