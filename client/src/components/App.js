import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Footer from "./Footer";
import Login from "./Login";
import Feed from "./Feed";
import UserProfile from "./UserProfile";
import GroupProfile from "./GroupProfile";
import { Switch, Route } from "react-router-dom";

function App() {

  const [loggedIn, setLoggedIn] = useState(false);
  const [loggedInID, setLoggedInID] = useState(1);



  return (
    <>
      <div className="App">
        <NavBar />
        <Switch>
          <Route exact path="/login">
            <Login />
          </Route>
          <Route exact path="/feed">
            <Feed />
          </Route>
          <Route exact path="/user-profile">
            <UserProfile />
          </Route>
          <Route exact path="/group-profile">
            <GroupProfile />
          </Route>
        </Switch>
        <br></br>
        <br></br>
        <br></br>
        <Footer className="footer" />
      </div>
    </>
  );
}

export default App;
