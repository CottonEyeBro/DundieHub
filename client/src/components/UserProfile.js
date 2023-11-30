import React, { useState, useEffect } from "react";
import GroupCard from "./GroupCard";
import PostCard from "./PostCard";

function UserProfile() {

    const [checkUserSession, setCheckUserSession] = useState(null);

    useEffect(() => {
        fetch("/check_user_session").then((r) => {
          if (r.ok) {
            r.json().then((data) => setCheckUserSession(data));
          }
        });
    }, []);

    return (
        <div key={checkUserSession?.user_groups.id} className="userprofilepage">
            <div className="user-profile-div">
                <h1>User Profile: </h1>
                <img className="user-photo" src={checkUserSession?.profile_image_url} />
                <p>Welcome back, <strong>{checkUserSession?.name}</strong>!</p>
                <p>Username: <em>&lt;{checkUserSession?.username}&gt;</em></p>
            </div>
            <div className="user-posts">
                <h2>User Posts: </h2>
                <PostCard />
            </div>
            <div className="user-groups">
                <h2 className="group-title">User Affinity Groups: </h2>
                <GroupCard />
            </div>
        </div>
    );
}

export default UserProfile;