import {
  createBrowserRouter,
  RouterProvider,
  Route,
  Link,
} from "react-router-dom";
import { App } from "./App";
import { SecretElement } from "./secret-element";

const router = createBrowserRouter([
  {
    path: "/secret",
    element: <SecretElement />,
  },
  {
    path: "/",
    element: <App />,
  },
]);

export const SiteRouter = () => {
  return <RouterProvider router={router} />;
};
