import React, { Component } from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { Redirect } from "react-router-dom";
// import "../../../node_modules/bootstrap/dist/css/bootstrap.min.css";
//
import axios from "axios";

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      redirect: null,
    };
    this.registerUser = this.registerUser.bind(this);
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
    data.append("first_name", this.state.first_name);
    data.append("last_name", this.state.last_name);
    data.append("email", this.state.email);
    data.append("password", this.state.password);

    fetch("registerUser", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);
        if (responseJson.includes("User")) {
          this.setState({ redirect: { pathname: "/job/create", state: { texto: "Skip" } } });
        }
      });
  }
  registerUser() {
    let url = "registerUser";
    console.log(this.state);
    axios
      .post(url, { datos: this.state })
      .then((resp) => {
        console.log(resp.data);
        alert(resp.data);
      
      })
      .catch((err) => {
        console.log(err);
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
              <h3>Sign Up</h3>

              <div className="form-group">
                <label>First name</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="First name"
                  id="first_name"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Last name</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="Last name"
                  id="last_name"
                  onChange={this.handleChange}
                />
              </div>

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

             
                <button
                  type="submit"
                  className="btn btn-primary btn-block"
                  id="register-btn"
                >
                  Sign Up
                </button>
           

              <p className="forgot-password text-right">
                Already registered? <Link to={`/login`}>sign in</Link>
              </p>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
