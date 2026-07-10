# Frontend Reactive UI with React

What is React?

- it is a library that helps developers build reactive UIs as a tree of small reusables pieces called components.

- to build a React application we need the following stack:
    1. application code: React, Redux, ESLint, Prettier, and React Router.
    2. build tools: Webpack, Uglify, npn/yarn/pnpm/, and babel
    3. testing tools: Jest and Enzyme.

## Adding React Router

- routing in a frontend application represents everything that deals with moving from one view to another and loading the right page uisng the right URL.

- `React.StrictMode` component helps us receive warnings in the development mode/

## Adding React Bootstrap

- Bootsrap allows us to configure React with CSS frameworks.

## Creating the Home page

- creating a page in React Router follows this pattern most of the time:
    - first, create th component and the page
    - then, register the page in `BrowserRouter` with an URL.

- located inside the `src/pages` directory.

- to register a page with React Router, we use the `<Route />` component and pass two props:
    - the path
    - component element

## Configuring CORS

- **CORS** stands for **cross-origin resource sharing**.
- it is a browser mechanism that enables controlled access to resources located outside of a given domain.
    - helps prevent cross-domain attacks or unwanted requests.

## Useful ES6 and React features

- with React, instead of writing classes we write components using functions and React Hooks.

1. **const and let**

- `const` keyword makes any variables immutable when declared with the keyword. the varianles can't be redeclared nor reassigned. 
- `let` is used to declare a variable that can be reassigned to a new value.
    - useful when we want to create a variable that can change over time, such as a counter or an iterator.

    ```js
    let count = 0;
    // allowed because counter is not a constant
    counter++;
    ```

2. **Template literals**

- in JS, template literals are a way to define string values that can contain placeholders for dynamic values. 
    - they are represented by the backtrick (`) character and use the dollar sign ($) and curly braces ({}) to insert expressions into the string.

    ```js
    const name = 'World';
    const message = `Hello, ${name}`;
    console.log(message); // "Hello, World!"
    ```
- template literals provide a more convenient and readable way to create strings with dynamic values compared to using the traditional string concatenation operator (+). 
- they also support **string interpolation** i.e., we can insert expressions into the string, as well as multiline strings.

```js
const a = 10;
const b = 20;
const message = `The sum of ${a} and ${b} is ${a + b}.`;
const.log(message); // "The sum of 10 and 20 is 30."
```

3. **JSX styling**

- JSX is a syntax extension to JavaScript that allows us to write JS code that looks like HTML. Example: JSX in a React component: 

```jsx
import React from 'react';
function Component() {
    return (
        <div>
          <h1>Hello, world!</h1>
          <p>This is some text.</p>
        </div>
    );
}
```

- when we write JSX, we can use JS expressions inside the curly braces ({}) to insert dynamic values into the JSX code. this allows us to easily create dynamic and interactive UIs using JSX:

```jsx
import Reacr from 'react';
function Component ({ name }) {
    return (
        <div>
          <h1>Hello, {name}!</h1>
          <p>This is some text.</p>
        </div>
    );
}
```

3. **Props versus states**

- in React, props and states are two different ways to manage data in a component.
- Props (properties) are used to pass data from a parent component to a child component.
    - props are read-only, which means that a child component cannot modify the props passed to it by the parent component.

    ```jsx
    import React from 'react'; {
        function ParentComponent() {
            return (
                <ChildComponent
                    name="John Doe"
                    age={25}
                />
            );
        }
        function ChildCompoent({ name, age }) {
            return (
                <p>
                 My name is {name} and I am {age} years old.
                </p>
            );
        }
    }
    ```

- a state is way to manage data in a component that can be modified by the component itself.
- the state is private to the component and can only be modified using special React methods, such as `useState`. e.g., how to modify a state in a React component:

```jsx
import React, { useState } from 'react';
function Counter() {
    // use useState to manage the state of the counter
    const [count, setCount] = useState(0);
    // function to increment the counter
    function handleIncrement() {
        setCount(count + 1);
    }
    return (
        <div>
          <p>The counter is at {count}.</p>
          <button onClick={handleIncrement}>Increment</button>
        </div>
    );
}
```

- here, we define a component called `Counter` that uses the `useState` Hook to manage the state of a counter. the Hook returns an array with two elements, the current value of the state (in this case, `count`) and a function to update the state (`setCount`). 

- in the render method of the component, we display the value of the count state and define a button that, when clicked, calls the `handleIncrement` function to update the count state. this causes the component to re-render and display the updated value of the count state.

> `useState` is a Hook in React that allows us to add a state to functional components i.e., it allows us to manage the state of the component, which is an object that holds information about the component and can be used re-render the component when this state changes.

4. **The Context API**

- the **Context API** is way to share data between different components in a React application. allows us to pass data through the component tree without having to pass props down manually at every level. Example:

```jsx
// create a context for sharing data
const Context = React.createContext();

function App() {
    // set some initial data in the context
    const data = {
        message: 'Hello, world!'
    };
    return (
        // provide the data to the components inside the provider
        <Context.Provider value={data}>
          <Component />
        </Context.Provider>
    );
}

function Component() {
    // use the useContext Hook to access the data in the context
    const context = React.useContext(Context);
    return (
        <p>{context.message}</p>
    );
}
```

- here, we use the `React.createContext` method to create a new context object, which we call `Context`. we then provide some initial data to the context by wrapping our top-level component in a `Context.Provider` component and passing the data as the value pop. finally, we use the `useContext` Hook in `Component` to access the data in the context and display it in the compent.

5. **useMemo**

- `useMemo` is a Hook in React that allows us to optimise the performance of the components by memoizing (caching) expensive calculations. it works by returning a memoized value that is only recalculated if one of the inputs to calculation changes.

> memoization is a technique used to speed up programs by storing the results of expensive function calls and returning the cached result when the same inputs are given again. this can be useful for optimizing programs that make repeated calculations with the same input.

Example:

```jsx
import React, { useMemo } from 'react';

function Component({ data }) {
    // use useMemo to memoize the expensive calculation
    const processData = useMemo(() => {
        // do some expensive calculation with the data
        return expensiveCalculation(data);
    }, [data]);
    return (
        <div>
          {/* Use the processed data in the component */}
          <p>{processedData.message}</p>
        </div>
    );
}
```

- in the code above, we use `useMemo` to memoize the result of an expensive calculation that we do with the data prop passed to the component. because `useMemo` only recalculates the value if the data prop changes, we can avoid making the expensive calculation every time the component is re-rendered, which can improve the performance of our application. 

6. **Handling forms - controlled components and uncontrolled components**

Controlled component is a component in React that is controlled by the state of the parent component i.e., the value of the input field is determined by the value prop passed to the component, and any changes to the input are handled by the parent compoent. 

Example: 

```jsx
import React, { useState } from 'react';

function Form() {
    // use useState to manage the state of the input field
    const [inputValue, setInputValue] = useState('');

    // function to handle changes to the input field
    function handleChange(event) {
        setInputValue(event.target.value);
    }
    return (
        <form>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={inputValue}
            onChange={handleChange}
          />
        </form>
    );
}
```

- in the above code snippet, we used `useState` to manage the state of the input field and the `handleChange` function to update the state when the input is changed. because the value of the input is determined by the `inputValue` state variable, the input is considered to be a controlled component. 

Uncontrolled component is a component in React that manages its own state internally i.e., the value of the input field is determined by the `defaultValue` prop passed to the component, and any changes to the input are handled by the component itself. 

Example:

```jsx
import React from 'react';

function Form() {
    // use a ref to manage the state of the input field
    const inputRef = React.useRef();

    //function to handle the form submission
    function handleSubmit(event) {
        event.preventDefault();
        // do something with the input value here
        // e.g., sending the input value to an API or saving it to the database.
        sendInputValue(inputRef.current.value);
        // clear the input after submitting
        inputRef.current.value = '';
    }
    return (
        <form onSubmit={handleSubmit}>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            defaultValue=""
            ref={inputRef}
          />
        </form>
    );
}
```

- here, we use `ref` to manage the state of the input field and the `handleSubmit` function to handle the form submission. because the value of the input is determined by the `defaultValue` prop and managed internally by the component, the input is considered to be an uncontrolled component.