import React, { useState, useEffect } from "react";

function UserProfile() {

    const [checkUserSession, setCheckUserSession] = useState(null);

    useEffect(() => {
        // auto-login
        fetch("/check_user_session").then((r) => {
          if (r.ok) {
            r.json().then((data) => setCheckUserSession(data));
          }
        });
    }, []);

    console.log(checkUserSession)

    return (
        <>
            <div className="user-profile">
                <h1>User Profile Page</h1>
                <img className="user-photo" src={checkUserSession?.profile_image_url} />
                <p>Welcome back, {checkUserSession?.name}!</p>
                <p>Username: &lt;{checkUserSession?.username}&gt;</p>
            </div>
            <div className="user-posts">

            </div>
            <div className="user-groups">

            </div>
        </>
    );
}

export default UserProfile;