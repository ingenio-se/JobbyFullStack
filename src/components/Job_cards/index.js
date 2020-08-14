import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import "./style/index.scss";
import location from "./assets/location.svg";
import building from "./assets/building.svg";
import money from "./assets/money.svg";
import target from "./assets/target.svg";

class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      job : props.job
   }
  }
  static propTypes = {
    prop: PropTypes,
  };
  
  render() {
    const { job } = this.state
    return (
      <div className="card_container">
        <h2>{job[0]}</h2>
        <section className="card-aspects__container">
          <ul>
            <li>
              <span>
                <img src={location} alt="location" />{job[1]}
              </span>
            </li>
            <li>
              <span>
                <img src={building} alt="building" /> {job[2]}
              </span>
            </li>
            <li>
              <span>
                <img src={money} alt="money" />{job[3]}
              </span>
            </li>
            <li>
              <span>
                <img src={target} alt="target" />{job[4]}
              </span>
            </li>
          </ul>
        </section>
        <h5>{job[5].slice(0, 100) + "..."}
          
        </h5>
        <Link className="text-reset text-decoration-none" to={`/job/`+ job[6]}>
          <button>More...</button>
        </Link>
      </div>
    );
  }
}

export default index;
