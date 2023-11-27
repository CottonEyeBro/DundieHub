import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Footer from "./Footer";
import Login from "./Login";
import Feed from "./Feed";
import UserProfile from "./UserProfile";
import GroupProfile from "./GroupProfile";
import { Switch, Route } from "react-router-dom";

function App() {

  const [users, setUsers] = useState(null)
  const [checkUserSession, setCheckUserSession] = useState(null)

  useEffect(() => {
      fetch("/users")
          .then((resp) => resp.json())
          .then((data) => setUsers(data))
  }, [])

  useEffect(() => {
    // auto-login
    fetch("/check_user_session").then((r) => {
      if (r.ok) {
        r.json().then((data) => setCheckUserSession(data));
      }
    });
  }, []);

  const user_id = checkUserSession?.id

  // if (!users) console.log(setCheckUserSession)
  // if (!users) return <Login setUsers={setUsers} setCheckUserSession={setCheckUserSession} />;

  return (
    <>
      <div className="App">
        <NavBar users={users} setUsers={setUsers} />
        <Switch>
          <Route exact path="/login">
            <Login setUsers={setUsers} />
          </Route>
          <Route exact path="/feed">
            <Feed users={users} />
          </Route>
          <Route exact path={`/${user_id}`}>
            <UserProfile />
          </Route>
          <Route exact path="/group-profile">
            <GroupProfile />
          </Route>
        </Switch>
        <br></br>
        {/* <img src="./images/Office Logo.png" alt="The Office logo" /> */}
        <br></br>
        <Footer />
      </div>
    </>
  );
}

export default App;
