import React, { Component } from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";
import "./style/index.scss";
import location from "./assets/location.svg";
import building from "./assets/building.svg";
import money from "./assets/money.svg";
import target from "./assets/target.svg";
import axios from 'axios';
import api from "../../ApiUrl";

class index extends Component {
  constructor(props) {
    super(props);
    this.state = {
      job : props.job,
      logo :'',
      error: null,
      isLoaded: false,
      data: [],
   }
  }
  static propTypes = {
    prop: PropTypes,
  };
  componentDidMount(){
    const children = this.props.children;
    fetch(api(children)).then(
      (result) => {
        console.log(result);
        this.setState({
          isLoaded: true,
          data: result,
        });
      },
      (error) => {
        this.setState({
          isLoaded: true,
          error,
        });
      }
    );
    
    }
  
  render() {
    const { job } = this.state
    const { logo } = this.state
    const { error, isLoaded } = this.state;
    const { url } = this.state.data;
    if (error) {
      console.log(error.message);
      return <h1>Oops, data no disponible</h1>;
    } else if (!isLoaded) {
      return <h1>Loading...</h1>;
    } else {
    return (
      <div className="card_container">
        <div>
        <article>
              <h2>{job[0]}</h2>
              <img src={url} alt="logo" />
        </article>
       
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
      </div>
    );
    }
  }
}

export default index;
