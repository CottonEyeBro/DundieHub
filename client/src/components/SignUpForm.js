import React from 'react';
import { useHistory } from 'react-router-dom';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const SignUpForm = ({ users }) => {
  const initialValues = {
    name: '',
    username: '',
    password: '',
    confirmPassword: '',
  };

  const validationSchema = Yup.object().shape({
    name: Yup.string().required('Required'),
    username: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid username').required('Required'),
    password: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid password').required('Required'),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref('password'), null], 'Passwords must match')
      .required('Required'),
  });

  // let history = useHistory();

  const handleSubmit = async (values, { setSubmitting }) => {
    try {
      // Send signup request to your backend
      const response = await fetch('/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      });

      if (response.ok) {
        const user = await response.json();
        users(user);

        // Redirect to "/feed" on successful signup
        // history.push('/feed');

      } else {
        const error = await response.json();
        console.error('Signup failed:', error);
      }
    } catch (error) {
      console.error('Error during signup:', error);
    }

    setSubmitting(false);
  };

  // function handleClick() {
  //   history.push("/user-profile");
  // }

  // onClick={handleClick}

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form>
        <br />
        <div>
          <h2>Sign up:</h2>
          <label htmlFor="name">Name: </label>
          <Field type="text" id="name" name="name" placeholder="Enter your name..." />
          <ErrorMessage name="name" component="div" />
        </div>
        <br />
        <div>
          <label htmlFor="username">Username: </label>
          <Field type="text" id="username" name="username" placeholder="Enter username..." autoComplete="new-username" />
          <ErrorMessage name="username" component="div" />
        </div>
        <br />
        <div>
          <label htmlFor="password">Password: </label>
          <Field type="password" id="password" name="password" placeholder="Enter password..." autoComplete="new-password" />
          <ErrorMessage name="password" component="div" />
        </div>
        <br />
        <div>
          <label htmlFor="confirmPassword">Confirm Password: </label>
          <Field type="password" id="confirmPassword" name="confirmPassword" placeholder="Confirm password..." autoComplete="new-password" />
          <ErrorMessage name="confirmPassword" component="div" />
        </div>
        <br />
        <div>
          <button type="submit">Sign Up</button>
        </div>
      </Form>
    </Formik>
  );
};

export default SignUpForm;