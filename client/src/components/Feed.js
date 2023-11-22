import React, { useEffect, useState } from "react";
import NewPostForm from "./NewPostForm";

function Feed() {


    const [posts, setPosts] = useState([])

    useEffect(() => {
        fetch("/posts")
            .then((resp) => resp.json())
            .then((data) => setPosts(data))
    }, [])

    const handleNewPost = async (values, { resetForm }) => {

        try {

            // Send a POST request to add the new post
            const response = await fetch("/posts", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(values),
            });

            if (response.ok) {
                const createdPost = await response.json();

                // Update the posts state with the new post
                setPosts((prevPosts) => [createdPost, ...prevPosts]);

                // Reset the form after successful submission
                resetForm();

            } else {
                const error = await response.json();
                console.error("Failed to add post:", error);
            }
        } catch (error) {
          console.error("Error during post creation:", error);
        }
      };

    function viewPosts() {
        
        // Sort posts by the 'posted_at' timestamp in descending order
        const sortedPosts = posts.sort((a, b) => new Date(b.posted_at) - new Date(a.posted_at));
        
        const postCards = sortedPosts.map((post) => {
            // console.log(post.user.profile_image_url)

            // Sort comments by the 'commented_at' timestamp in ascending order
            const sortedComments = post.comments.sort((a, b) => new Date(a.commented_at) - new Date(b.commented_at));

            return (

                <div key={post.id} className="post-card">
                    <div className="postcontentbox">
                        <img src={post.user.profile_image_url} alt="User profile portrait" />
                        <h2>{post.user.name}</h2>
                        <h3><em>&lt;{post.user.username}&gt;</em></h3>
                        <p>{post.content}</p>
                        <p><em>Posted: {post.posted_at}</em></p>
                        <button className="postcardbuttons" onClick={() => addComment(post)}>Add comment</button>
                        <button className="postcardbuttons" onClick={() => editPost(post)}>Edit</button>
                        <button className="postcardbuttons" onClick={() => deletePost(post)}>Delete</button>
                        {post.comments.length > 0 ? 
                        <div className="commentcontentbox">
                            <h3>Comments:</h3>
                            {sortedComments.map((comment) => (
                                <div key={comment.id} className="comment">
                                    <h4>{comment.user.name}</h4>
                                    <h5>&lt;{comment.user.username}&gt;</h5>
                                    <p>{comment.content}</p>
                                    <p><em>{comment.commented_at}</em></p>
                                    <button className="commentcardbuttons" onClick={() => editComment(comment)}>Edit</button>
                                    <button className="commentcardbuttons" onClick={() => deleteComment(comment)}>Delete</button>
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

    function addComment(post) {
        console.log("add comment button selected")
        console.log(post)
    }

    function editPost(post) {
        console.log("edit button selected")
        console.log(post)
    }

    function deletePost(post) {
        console.log("delete button selected")
        console.log(post.id)
    }

    function editComment(comment) {
        console.log("edit button selected")
        console.log(comment)
    }

    function deleteComment(comment) {
        console.log("delete button selected")
        console.log(comment.id)
    }

    return (
        <div className="main-feed">
            <h1>Posts</h1>
            <NewPostForm onSubmit={handleNewPost} />
            <div className="card">
                {viewPosts()}
            </div>
        </div>
    );
}

export default Feed;