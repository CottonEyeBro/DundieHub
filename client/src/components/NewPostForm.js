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
        <label htmlFor="content">Write a new post:</label>
        <Field as="textarea" id="content" name="content" placeholder="Type your post here..." />
        <ErrorMessage name="content" component="div" />
        <button type="submit">Post</button>
      </Form>
    </Formik>
  );
};

export default NewPostForm;