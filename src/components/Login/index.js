import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import "./style/index.scss";

export default class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="form-container">
        <div className="form-content">
          <form>
            <h2>Sign In</h2>

            <div className="form-group">
              <label>Email address</label>
              <input
                type="email"
                className="form-control"
                placeholder="Enter email"
                id="email"
              />
            </div>

            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                placeholder="Enter password"
                id="password"
              />
            </div>

            <div className="form-group">
              <div className="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  className="custom-control-input"
                  id="customCheck1"
                />
                <label className="custom-control-label" htmlFor="customCheck1">
                  Remember me
                </label>
              </div>
            </div>
            <Link to={`/`}>
              <button
                type="submit"
                className="btn btn-primary btn-block"
                id="submit-btn"
              >
                Sign In
              </button>
            </Link>
            <p className="forgot-password text-right" id="pwd-forgot">
              Forgot <a href="#">password?</a>
            </p>
          </form>
        </div>
      </div>
    );
  }
}
