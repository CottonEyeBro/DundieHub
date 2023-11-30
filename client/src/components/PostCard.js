import React, {useState, useEffect} from "react";

function PostCard() {

    const [checkUserSession, setCheckUserSession] = useState(null);

    useEffect(() => {
        fetch("/check_user_session").then((r) => {
          if (r.ok) {
            r.json().then((data) => setCheckUserSession(data));
          }
        });
    }, []);

    // console.log(checkUserSession)

    const sortedUserPosts = checkUserSession?.posts.sort((a, b) => new Date(b.posted_at) - new Date(a.posted_at));

    function viewUserPosts() {

        // console.log(checkUserSession?.posts)
        // console.log(sortedUserPosts)

        const userPostCards = checkUserSession?.posts.map((post) => {

            // console.log(post)

            return (
                <div key={post.id} className="user-post-card">
                    <h2>{checkUserSession?.name}</h2>
                    <h3>&lt;{checkUserSession?.username}&gt;</h3>
                    <p>{post.content}</p>
                    <p><em>Posted: {post.posted_at}</em></p>
                </div>
            );
        });
        return userPostCards
    }

    return (
        <>
            {viewUserPosts()}
        </>
    )
}

export default PostCard