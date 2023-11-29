import React, { useEffect, useState } from "react";
import NewPostForm from "./NewPostForm";

function Feed() {


    const [posts, setPosts] = useState([])
    const [showForm, setShowForm] = useState(false)
    const [editPostContent, setEditPostContent] = useState([])
    const [editPostId, setEditPostId] = useState("")

    // console.log(showForm)
    // console.log(editPostContent)
    // console.log(editPostId)

    useEffect(() => {
        fetch("/posts")
            .then((resp) => resp.json())
            .then((data) =>{ 
                setPosts(data)
                setEditPostContent(data)
            })
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
                        <div className="user-info">
                            <img src={post.user.profile_image_url} alt="User profile portrait" />
                            <h2>{post.user.name}</h2>
                            <h3><em>&lt;{post.user.username}&gt;</em></h3>
                        </div>
                        <p>{post.content}</p>
                        <div className="edit-form-div">
                            {showForm === true ? displayForm() : <></>}
                        </div>
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

    function deletePost(post) {
        console.log("delete button selected")
        console.log(post.id)
        fetch(`/posts/${post.id}`, {
            method: "DELETE"
        })
        const updatedPosts = []
        posts.forEach(item => {
            if (item.id !== post.id) {
                updatedPosts.push(item)
            }
        })
        setPosts(updatedPosts)
    }

    function editComment(comment) {
        console.log("edit button selected")
        console.log(comment)
    }

    function deleteComment(comment) {
        console.log("delete button selected")
        console.log(comment.id)
    }

    function editPost(post) {
        console.log("edit button selected")
        // console.log(post.id)
        setEditPostId(post.id)
        setShowForm(true)
        setFormData({
            content: post.content
        })
    }

    // console.log(editPostId)

    const [formData, setFormData] = useState({ 
        content: editPostContent.content
        })
    
    function handleChange(e) { 
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
        }

    function handleEdit(e) {
        e.preventDefault()
        //console.log(editPostContent)
        fetch(`/posts/${editPostId}`, {
            method:"PATCH",
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(formData)
        })
        .then(resp => resp.json())
        .then(updatedPost => {
            // console.log(updatedPost)
            const updatedPosts = posts.map(originalPost => {
                if (originalPost.id === updatedPost.id) {
                    return updatedPost
                } else {
                    return originalPost
                }
            })
            setPosts(updatedPosts)
            setShowForm(false)
        })

    }

    function displayForm() {
        return (
            <div className="editcard">
                <h3> Edit Post: </h3>
                <form onSubmit={handleEdit} className="edit-form">
                    <label htmlFor="content"></label>
                    <input
                        type="text"
                        name="content"
                        value={formData.content}
                        defaultValue={editPostContent.content}
                        onChange={handleChange}
                        className="input-text"
                    />
                    <br/>
                    <br/>
                    <input className="buttons" type="submit" value="Save" />
                    <input className="buttons" type="button" value="Cancel" onClick={() => setShowForm(false)} />
                </form>
            </div>
        )
    }

    return (
        <div className="main-feed">
            <h1>Feed:</h1>
            <NewPostForm onSubmit={handleNewPost} />
            <div className="card">
                {viewPosts()}
            </div>
        </div>
    );
}

export default Feed;