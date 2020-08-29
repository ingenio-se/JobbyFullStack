import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class index extends Component {
  render() {
    return (
      <form>
        <h3>Create Vacancy</h3>

        <div className="form-group">
          <label>Job Title</label>
          <input
            type="text"
            className="form-control"
            placeholder="First name"
            id="job-title"
          />
        </div>

        <div className="form-group">
          <label>Location</label>
          <input
            type="text"
            className="form-control"
            placeholder="Location..."
            id="job-location"
          />
        </div>

        <div className="form-group">
          <label>Company</label>
          <input
            type="text"
            className="form-control"
            placeholder="Company Name..."
            id="job-company"
          />
        </div>

        <div className="form-group">
          <label>Salary Rank</label>
          <input
            type="text"
            className="form-control"
            placeholder="$37K-$66K (Glassdoor est.)"
            id="job-salary"
          />
        </div>

        <div className="form-group">
          <label>Ratio 0-10</label>
          <input
            type="number"
            className="form-control"
            min="0"
            max="10"
            id="ratio"
          />
        </div>

        <div className="form-group">
          <label>Description</label>
          <textarea
            type="text"
            className="form-control"
            placeholder="Job Description..."
            id="job-description"
          />
        </div>

        <Link className="text-reset text-decoration-none" to={`/job/:jobId`}>
          <button
            type="submit"
            className="btn btn-primary btn-block"
            id="create-job-btn"
          >
            Create
          </button>
        </Link>
      </form>
    );
  }
}
