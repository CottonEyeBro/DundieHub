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

  useEffect(() => {
      fetch("/users")
          .then((resp) => resp.json())
          .then((data) => setUsers(data))
  }, [])

  useEffect(() => {
    // auto-login
    fetch("/check_user_session").then((r) => {
      if (r.ok) {
        r.json().then((data) => setUsers(data));
      }
    });
  }, []);

  if (!users) return <Login onLogin={setUsers} />;

  return (
    <>
      <div className="App">
        <NavBar user={users} setUser={setUsers} />
        <Switch>
          <Route exact path="/login">
            <Login />
          </Route>
          <Route exact path="/feed">
            <Feed users={users} />
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
