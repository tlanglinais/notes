What is code splitting?

## Bundling

Most react apps have their filed bundled into chunks (Webpack does this in `create-react-app`). Bundling is the process of following imported files and merging them into a single file. This bundle can be included on a webpage to load the entire app at once.

The browser can also can also cache portions of the chunk to make repeat visits faster.

### Issues

The larger your app gets, the larger your bundle gets. To avoid having to deal up with a massive bundle, you can split up your code into smaller bundles.

Code splitting can help you 'lazy-load' just the things that are currently needed, improving performance.

## React Lazy

The React.lazy function lets you render a dynamic import as a regular component.

Before:

```
import OtherComponent from './OtherComponent';
```

After:

```
const OtherComponent = React.lazy(() => import('./OtherComponent'));
```

`React.lazy` is promised based so the component needs to be rendered inside a `Suspense` component. That way you can show a loading page while the lazy component loads.

> `Suspense` is a component that lets you 'wait' for some code to load and specify a fallback component to render while we're waiting:
