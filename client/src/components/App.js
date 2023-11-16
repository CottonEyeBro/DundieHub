import React, { useEffect, useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Feed from "./Feed";
import UserProfile from "./UserProfile";
import Login from "./Login";
import GroupProfile from "./GroupProfile";
import { Switch, Route } from "react-router-dom";

function App() {



  return (
    <>
      <h1>Project Client</h1>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/login">
            <Login />
          </Route>
        </Switch>
        <br></br>
        <br></br>
        <br></br>
        <Footer />
      </div>
    </>
  );
}

export default App;
