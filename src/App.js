import React from "react";
import "./App.css";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Home from "./components/Home";
import JobView from "./components/JobView";

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={Home} />
        {/* <Route exact path="/" component={Badges} /> */}
        <Route exact path="/job/1" component={JobView} />
        {/* <Route exact path="/job/:jobId" component={BadgeDetails} /> */}
        {/* <Route component={NotFound} /> */}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
