import React, { useEffect, useState } from "react";

function Feed( {users} ) {

    const [posts, setPosts] = useState([])
    const [comments, setComments] = useState([])
    const [groups, setGroups] = useState([])
    const [userGroups, setUserGroups] = useState([])

    return (
        <div className="main-feed">
            <h1>Main Feed Page</h1>
        </div>
    );
}

export default Feed;