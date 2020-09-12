import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import "./style/index.scss";
import location from "../Job_cards/assets/location.svg";
import building from "../Job_cards/assets/building.svg";
import money from "../Job_cards/assets/money.svg";
import target from "../Job_cards/assets/target.svg";
import api from "../../ApiUrl";

class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      job: props.job,
      error: null,
      isLoaded: false,
      data: [],
    };
    console.log(props.job);
  }
  static propTypes = {
    prop: PropTypes,
  };
  // componentDidMount() {
  //   const children = this.props.children;
  //   fetch(api(children)).then(
  //     (result) => {
  //       console.log(result);
  //       this.setState({
  //         isLoaded: true,
  //         data: result,
  //       });
  //     },
  //     (error) => {
  //       this.setState({
  //         isLoaded: true,
  //         error,
  //       });
  //     }
  //   );
  // }
  render() {
    return (
      <div className="job_container">
        <div>
          <article>
            <h2>{this.state.job[0][0]}</h2>
            <img src={url} alt="logo" />
          </article>

          <section className="card-aspects__container">
            <ul>
              <li>
                <span>
                  <img src={location} alt="location" /> {this.state.job[0][1]}
                </span>
              </li>
              <li>
                <span>
                  <img src={building} alt="building" /> {this.state.job[0][2]}
                </span>
              </li>
              <li>
                <span>
                  <img src={money} alt="money" /> {this.state.job[0][3]}
                </span>
              </li>
              <li>
                <span>
                  <img src={target} alt="target" /> {this.state.job[0][4]}
                </span>
              </li>
            </ul>
          </section>
          <p>{this.state.job[0][5]}</p>
          <section className="tag-container">
            <span>1</span>
            <span>databases</span>
            <span>machine learning</span>
            <span>4</span>
            <span>5</span>
          </section>
          <section className="buttons">
            <button className="apply">Apply</button>
            <Link className="text-reset text-decoration-none" to={`/`}>
              <button className="back">Back</button>
            </Link>
          </section>
        </div>
      </div>
    );
  }
}
export default index;
