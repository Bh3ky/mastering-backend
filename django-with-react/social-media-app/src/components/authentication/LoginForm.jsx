import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";

import { useUserActions } from "../../hooks/user.actions";

function LoginForm() {
  const [validated, setValidated] = useState(false);

  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState(null);
  const userActions = useUserActions();

  const handleSubmit = async (event) => {
    event.preventDefault();

    const loginForm = event.currentTarget;

    if (loginForm.checkValidity() === false) {
      event.stopPropagation();
      setValidated(true);
      return;
    }

    setValidated(true);
    setError(null);

    const data = {
      email: form.email,
      password: form.password,
    };

    try {
      await userActions.login(data);
    } catch (err) {
      const responseText = err?.request?.response;

      if (responseText) {
        setError(responseText);
      } else {
        setError(err?.message ?? "Login failed.");
      }
    }
  };

  return (
    <Form
      id="login-form"
      className="border p-4 rounded"
      noValidate
      validated={validated}
      onSubmit={handleSubmit}
      data-testid="login-form"
    >
      <Form.Group className="mb-3">
        <Form.Label>Email</Form.Label>

        <Form.Control
          value={form.email}
          data-testid="email-field"
          onChange={(event) =>
            setForm({
              ...form,
              email: event.target.value,
            })
          }
          required
          type="email"
          placeholder="Enter email"
        />

        <Form.Control.Feedback type="invalid">
          Please provide a valid email address.
        </Form.Control.Feedback>
      </Form.Group>

      <Form.Group className="mb-3">
        <Form.Label>Password</Form.Label>

        <Form.Control
          value={form.password}
          data-testid="password-field"
          minLength={8}
          onChange={(event) =>
            setForm({
              ...form,
              password: event.target.value,
            })
          }
          required
          type="password"
          placeholder="Password"
        />

        <Form.Control.Feedback type="invalid">
          Please provide a valid password.
        </Form.Control.Feedback>
      </Form.Group>

      <div className="text-danger">
        {error && <p>{error}</p>}
      </div>

      <Button
        disabled={!form.password || !form.email}
        variant="primary"
        type="submit"
      >
        Submit
      </Button>
    </Form>
  );
}

export default LoginForm;