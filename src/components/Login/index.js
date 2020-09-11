import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { Redirect } from "react-router-dom";
import "./style/index.scss";

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
      redirect: null,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  static propTypes = {
    prop: PropTypes,
  };
  handleChange({ target }) {
    this.setState({
      [target.id]: target.value,
    });
    //console.log(this.state)
  }
  handleSubmit(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append("email", this.state.email);
    data.append("password", this.state.password);

    fetch("loginUser", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);
        if (responseJson.includes("Bienvenido")) {
          this.setState({ redirect: "/home" });
        }
      });
  }
  render() {
    if (this.state.redirect) {
      return <Redirect to={this.state.redirect} />
    }
    return (
      <div className="view-container">
        <div className="form-container">
          <div className="form-content">
            <form onSubmit={this.handleSubmit}>
              <h3>Sign In</h3>

              <div className="form-group">
                <label>Email address</label>
                <input
                  type="email"
                  className="form-control"
                  placeholder="Enter email"
                  id="email"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Password</label>
                <input
                  type="password"
                  className="form-control"
                  placeholder="Enter password"
                  id="password"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <div className="custom-control custom-checkbox">
                  <input
                    type="checkbox"
                    className="custom-control-input"
                    id="customCheck1"
                  />
                  <label
                    className="custom-control-label"
                    htmlFor="customCheck1"
                  >
                    Remember me
                  </label>
                </div>
              </div>

              <button
                type="submit"
                className="btn btn-primary btn-block"
                id="submit-btn"
              >
                Sign In
              </button>

              <p className="forgot-password text-right" id="pwd-forgot">
                no <Link to={"/register"}>registered?</Link>
              </p>
              <p>
             
              </p>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
