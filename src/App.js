import React from "react";
import "./App.css";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Home from "./components/Home";
import JobView from "./components/JobView";
import Login from "./components/Login";
import Register from "./components/Register";
import CreateJob from "./components/CreateJob";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/job/create" component={CreateJob} />
        <Route exact path="/job/:jobId" component={JobView} />
        
        {/* <Route component={NotFound} /> */}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
