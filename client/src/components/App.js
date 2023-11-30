import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Footer from "./Footer";
import Login from "./Login";
import Feed from "./Feed";
import UserProfile from "./UserProfile";
import GroupProfile from "./GroupProfile";
import officeLogo from "/home/clindsley/Development/Code/phase-5/DundieHub-project/client/src/images/Officelogo.jpg";
import { Switch, Route } from "react-router-dom";

function App() {

  const [checkUserSession, setCheckUserSession] = useState(null);

  useEffect(() => {
    // auto-login
    fetch("/check_user_session").then((r) => {
      if (r.ok) {
        r.json().then((data) => setCheckUserSession(data));
      }
    });
  }, []);

  const user_id = checkUserSession?.id

  // console.log(user_id)

  return (
    <>
      <div className="App">
        <NavBar />
        <Switch>
          <Route exact path = "/">
            <div className="hero-image">
            <img src={officeLogo} alt="The Office logo" />
            </div>
          </Route>
          <Route exact path="/login">
            <Login />
          </Route>
          <Route exact path="/feed">
            <Feed />
          </Route>
          <Route exact path={`/${user_id}`}>
            <UserProfile />
          </Route>
          <Route exact path="/group-profile">
            <GroupProfile />
          </Route>
        </Switch>
        <Footer />
      </div>
    </>
  );
}

export default App;
