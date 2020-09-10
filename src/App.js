import React from "react";
import "./App.css";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Home from "./components/Home";
import JobView from "./components/JobView";
import Login from "./components/Login";
import Register from "./components/Register";
import CreateJob from "./components/CreateJob";
import FirstPage from "./components/FirstPage";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={FirstPage} />
        <Route exact path="/home" component={Home} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/job/create" component={CreateJob} />
        <Route exact path="/job/:jobId" component={JobView} />
        
      </Switch>
    </BrowserRouter>
  );
}

export default App;
