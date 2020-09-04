import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

export default class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="form-container">
        <div className="form-content">
          <form>
            <h2>Sign Up</h2>

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

            <Link to={`/job/create`}>
              <button
                type="submit"
                className="btn btn-primary btn-block"
                id="register-btn"
              >
                Sign Up
              </button>
            </Link>
            <p className="forgot-password text-right">
              Already registered? <Link to={`/login`}>sign in</Link>
            </p>
          </form>
        </div>
      </div>
    );
  }
}
