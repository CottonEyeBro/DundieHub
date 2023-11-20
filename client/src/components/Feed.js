import React, { useEffect, useState } from "react";

function Feed() {

    const [users, setUsers] = useState([])
    const [posts, setPosts] = useState([])
    const [comments, setComments] = useState([])
    const [groups, setGroups] = useState([])
    const [userGroups, setUserGroups] = useState([])

    useEffect(() => {
        fetch("/users")
            .then((resp) => resp.json())
            .then((data) => setUsers(data))
    }, [])

    useEffect(() => {
        fetch("/posts")
            .then((resp) => resp.json())
            .then((data) => setPosts(data))
    }, [])

    useEffect(() => {
        fetch("/comments")
            .then((resp) => resp.json())
            .then((data) => setComments(data))
    }, [])

    useEffect(() => {
        fetch("/groups")
            .then((resp) => resp.json())
            .then((data) => setGroups(data))
    }, [])

    useEffect(() => {
        fetch("/user_groups")
            .then((resp) => resp.json())
            .then((data) => setUserGroups(data))
    }, [])

    function viewPosts() {
        const postCards = posts.map((post) => {
            console.log(post)
            // Sort comments by the 'commented_at' timestamp in ascending order
            const sortedComments = post.comments.sort((a, b) => new Date(a.commented_at) - new Date(b.commented_at));
            return (
                <div key={post.id} className="post-card">
                    <div className="postcontentbox">
                        <h2>{post.user.name}</h2>
                        <h3><em>&lt;{post.user.username}&gt;</em></h3>
                        <p>{post.content}</p>
                        <p><em>Posted: {post.posted_at}</em></p>
                        {post.comments.length > 0 ? 
                        <div className="commentcontentbox">
                            <h3>Comments:</h3>
                            {sortedComments.map((comment) => (
                                <div key={comment.id} className="comment">
                                    <p>{comment.content}</p>
                                    <p><em>{comment.commented_at}</em></p>
                                </div>
                                
                            ))}
                        </div> : <></>
                        
                        }
                    </div>
                </div>
            )
        })
        return postCards
    }

    return (
        <div className="main-feed">
            <h1>Main Feed Page</h1>
            <div className="card">
                {viewPosts()}
            </div>
        </div>
    );
}

export default Feed;