import React, { Component } from "react";
import "./style/index.scss";
import logo from "../Header/assets/logo.png";
import { Link } from "react-router-dom";

export default class index extends Component {
  render() {
    return (
      <div className="page-container">
        <article>
          <img src={logo} alt="" />
          <h1>Welcome Employer!</h1>
          <div className="buttons-container">
            <Link to="/login">
              <button>Sign In</button>
            </Link>
            <Link to="/register">
              <button>Sign Up</button>
            </Link>
          </div>
        </article>
      </div>
    );
  }
}
