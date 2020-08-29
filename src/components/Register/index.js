import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
// import "../../../node_modules/bootstrap/dist/css/bootstrap.min.css";
// import "./style/index.scss";

export default class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <form>
        <h3>Sign Up</h3>

        <div className="form-group">
          <label>First name</label>
          <input
            type="text"
            className="form-control"
            placeholder="First name"
            id="reg-name"
          />
        </div>

        <div className="form-group">
          <label>Last name</label>
          <input
            type="text"
            className="form-control"
            placeholder="Last name"
            id="reg-lt-name"
          />
        </div>

        <div className="form-group">
          <label>Email address</label>
          <input
            type="email"
            className="form-control"
            placeholder="Enter email"
            id="reg-email"
          />
        </div>

        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            className="form-control"
            placeholder="Enter password"
            id="reg-password"
          />
        </div>

        <Link className="text-reset text-decoration-none" to={`/job/create`}>
          <button
            type="submit"
            className="btn btn-primary btn-block"
            id="register-btn"
          >
            Sign Up
          </button>
        </Link>
        <Link className="text-reset text-decoration-none" to={`/login`}>
          <p className="forgot-password text-right">
            Already registered <a href="#">sign in?</a>
          </p>
        </Link>
      </form>
    );
  }
}
