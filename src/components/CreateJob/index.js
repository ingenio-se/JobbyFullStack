import React, { Component } from "react";
import { Link } from "react-router-dom";
import "./style/index.scss";
import axios from "axios";
import { Redirect } from "react-router-dom";

export default class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: "",
      location: "",
      company: "",
      salary: "",
      ratio: "",
      description: "",
      redirect: null,
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange({ target }) {
    this.setState({
      [target.id]: target.value,
    });
    //console.log(this.state)
  }
  handleSubmit(ev) {
    ev.preventDefault();
    console.log(this.state);
    const data = new FormData();
    data.append("title", this.state.title);
    data.append("location", this.state.location);
    data.append("company", this.state.company);
    data.append("salary", this.state.salary);
    data.append("ratio", this.state.ratio);
    data.append("description", this.state.description);

    fetch("/createJob", {
      method: "POST",
      body: data,
    })
      .then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);
        this.setState({ redirect: "/home" });
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
              <h2>Create Vacancy</h2>

              <div className="form-group">
                <label>Job Title</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="First name"
                  id="title"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Location</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="Location..."
                  id="location"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Company</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="Company Name..."
                  id="company"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Salary Rank</label>
                <input
                  type="text"
                  className="form-control"
                  placeholder="$37K-$66K (Glassdoor est.)"
                  id="salary"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Ratio (0-10)</label>
                <input
                  type="number"
                  className="form-control"
                  min="0"
                  max="10"
                  id="ratio"
                  onChange={this.handleChange}
                />
              </div>

              <div className="form-group">
                <label>Description</label>
                <textarea
                  type="text"
                  className="form-control"
                  placeholder="Job Description..."
                  id="description"
                  onChange={this.handleChange}
                />
              </div>
              <div className="buttons-container">
              <button
                type="submit"
                className="btn btn-primary btn-block"
                id="create-job-btn"
              >
                Create
              </button>
              <Link to="/home">
                  <button>{this.props.location.state.texto}</button>
                </Link>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}
