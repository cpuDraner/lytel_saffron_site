import * as React from "react";
import { createRoot } from "react-dom/client";

import { SiteRouter } from "./SiteRouter";
const root = createRoot(document.getElementById("root")!);

root.render(
  <React.StrictMode>
    <SiteRouter />
  </React.StrictMode>
);
