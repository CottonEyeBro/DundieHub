import React, {useState, useEffect} from 'react';
import { useHistory } from 'react-router-dom';
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';

const SignUpForm = ({ setUsers }) => {

  const [userSession, setUserSession] = useState(null)

  useEffect(() => {
    fetch("/check_user_session").then((r) => {
      if (r.ok) {
        r.json().then(setUserSession);
      }
    });
  }, []);

  const user_id = userSession?.id

  const history = useHistory()

  const initialValues = {
    name: '',
    username: '',
    password: '',
    confirmPassword: '',
  };

  const validationSchema = Yup.object().shape({
    name: Yup.string(),
    username: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid username'),
    password: Yup.string().matches(/^[a-zA-Z0-9]*$/, 'Invalid password'),
    confirmPassword: Yup.string()
      .oneOf([Yup.ref('password'), null], 'Passwords must match'),
  });

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
        setTimeout(() => {
          history.push(`/${user_id}`)
        }, 125)
        const user = await response.json();
        setUsers(user);

      } else {
        const error = await response.json();
        console.error('Signup failed:', error);
      }
    } catch (error) {
      console.error('Error during signup:', error);
    }

    setSubmitting(false);
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form>
        <br />
        <div className='signup'>
          <div>
            <h2>Sign up:</h2>
            <label htmlFor="name">Name: </label>
            <Field type="text" id="name" name="name" placeholder="Enter your name..." />
            <ErrorMessage name="name" component="div" />
          </div>
          <br />
          <div>
            <label htmlFor="username">Username: </label>
            <Field type="text" className="username" name="username" placeholder="Enter username..." autoComplete="new-username" />
            <ErrorMessage name="username" component="div" />
          </div>
          <br />
          <div>
            <label htmlFor="password">Password: </label>
            <Field type="password" className="password" name="password" placeholder="Enter password..." autoComplete="new-password" />
            <ErrorMessage name="password" component="div" />
          </div>
          <br />
          <div>
            <label htmlFor="confirmPassword">Confirm Password: </label>
            <Field type="password" id="confirmPassword" name="confirmPassword" placeholder="Confirm password..." autoComplete="new-password" />
            <ErrorMessage name="confirmPassword" component="div" />
          </div>
          <br />
          <div className='signup-button'>
            <button type="submit">Sign Up</button>
          </div>
        </div>
      </Form>
    </Formik>
  );
};

export default SignUpForm;