import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import "./style/index.scss";
import location from "../Job_cards/assets/location.svg";
import building from "../Job_cards/assets/building.svg";
import money from "../Job_cards/assets/money.svg";
import target from "../Job_cards/assets/target.svg";

export default class index extends Component {
  static propTypes = {
    prop: PropTypes,
  };

  render() {
    return (
      <div className="job_container">
        <h2>Data Science</h2>
        <section className="card-aspects__container">
          <ul>
            <li>
              <span>
                <img src={location} alt="location" /> New York, NY
              </span>
            </li>
            <li>
              <span>
                <img src={building} alt="building" /> Vera Institute of justice
                3.2
              </span>
            </li>
            <li>
              <span>
                <img src={money} alt="money" /> $37K-$66K (Glassdoor est.)
              </span>
            </li>
            <li>
              <span>
                <img src={target} alt="target" /> 3.2
              </span>
            </li>
          </ul>
        </section>
        <h5>
          Are you eager to roll up your sleeves and harness data to drive policy
          change? Do you enjoy sifting ...
        </h5>
        <button className="apply">Apply</button>
        <Link className="text-reset text-decoration-none" to={`/`}>
          <button className="back">Back</button>
        </Link>
      </div>
    );
  }
}
