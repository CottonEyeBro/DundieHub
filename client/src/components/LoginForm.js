import React from 'react';
import { useHistory } from "react-router-dom";
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const LoginForm = ({ users }) => {
  const initialValues = {
    username: '',
    password: '',
  };

  const validationSchema = Yup.object().shape({
    username: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid username').required('Required'),
    password: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid password').required('Required'),
  });

  const handleSubmit = async (values, { setSubmitting }) => {
    
    try {
      // Send login request to your backend
      const response = await fetch('/user_login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        const user = await response.json();
        users(user);
        
        // Redirect to "/feed" on successful login
        // history.push("/feed");

      } else {
        const error = await response.json();
        console.error('Login failed:', error);
      }
    } catch (error) {
      console.error('Error during login:', error);
    }

    setSubmitting(false);
  };

  let history = useHistory();

  function handleClick() {
    history.push("/feed");
  }

  return (

    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form>
      <br/>
        <div>
          <h2>Sign in:</h2>
          <label htmlFor="username">Username: </label>
          <Field type="username" id="username" name="username" placeholder="Enter username..." autoComplete="new-username" />
          <ErrorMessage name="username" component="div" />
        </div>
        <br/>
        <div>
          <label htmlFor="password">Password: </label>
          <Field type="password" id="password" name="password" placeholder="Enter password..." autoComplete="new-password" />
          <ErrorMessage name="password" component="div" />
        </div>
        <br/>
        <div>
          <button type="submit" onClick={handleClick}>Sign In</button>
        </div>
      </Form>
    </Formik>
  );
};

export default LoginForm;