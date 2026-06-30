# Authentication and Authorization using JWTs


**Understanding JWTs**

- JWT stands for JSON Web Token.
- it's a JSON object defined as a safe way of transmitting information between two parties.
    - information transmitted by JWT is digitally signed so it can be verified and trusted.

- JWT contains three parts:
    1. header (x)
    2. payload (y)
    3. signature (z) all separated by a dot.

1. **Header**

- the header of the JWT consists of two parts:
    - type of token
    - signing algorithm being used [used to ensure that the message is authenticated and not altered] e.g.,

    ```text
    {
        "alg": "RSA",
        "typ": "JWT
    }
    ```

    - signing algorithms are used to sign tokens issued for the application or API.

2. **Payload**

- is the second part which contains the claims [which are statements about an entity typically the user & additional data].

    ```text
    {
        id": "d1397699-f37b-4de0-8e00-948fa8e9bf2c",
        "name": "John Doe",
        "admin": true 
    }
    ```

    - we have three claims here: user ID, name of user, and Boolean for the type of user.

3. **Signature**

- it is the encoded header, the encoded payload plus a secret, and an algorithm specified in the header e.g., using RSA algorithm:

```bash
RSA(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret)
```

- NB: the signature tracks whether the information has been changed.


**How JWTs are used in authentication??**

- every time a user successfully logs in, a JWT is created and returned. 
- the JWT is presented as credentials used to access protected resources. 
- NOTE: JWT expiration should be capped (should have short lifespan) to curb vulnerabilities.

Types of tokens:

1. access token - used to access resources and handle authorization.
2. refresh token - used to retrieve a new access token. 

    - NB: refresh token contains essential information needed to verify the user and generate a new access token. 

## Organising a project

- when working with Django, we have the ability to create many apps to handle different parts of the project.
- to create a Django application we run:

```bash
django-admin startapp core
```

## Creating a user model


**Django models**