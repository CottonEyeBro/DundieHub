import React from "react";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";

const NewPostForm = ({ onSubmit }) => {
  const initialValues = {
    user_id: "",
    content: "",
    posted_at: ""
  };

  const validationSchema = Yup.object().shape({
    content: Yup.string().required("Content is required"),
  });

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={onSubmit}
    >
      <Form>
        <div className="new-post-form">
          <label htmlFor="content"></label>
          <Field as="textarea" id="content" name="content" placeholder="Type your post here..." />
          <ErrorMessage name="content" component="div" />
          <button className="post-button" type="submit">Post</button>
        </div>
      </Form>
    </Formik>
  );
};

export default NewPostForm;