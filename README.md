# This is a typescript/react website. It publishes via neocities


## FIRST TIME SETUP
1. Find out if you have node installed by opening a terminal and running `node -v`. If you don't follow this guide: https://nodejs.org/en/download/package-manager/
2. Install yarn. It's a tool that runs and installs stuff. To do so, run `npm install yarn -g`.
3. Install VS Code. It's a dev environment and it's just really so nice. https://code.visualstudio.com/download
4. Install the neocities command line tool. It will make it easy to release new versions of the site! https://neocities.org/cli
5. Take a look at (src/index.tsx)[./src/index.tsx], it's the base page of your application
6. Run `yarn` aka `yarn install`, this will look at the yarn.lock file and download all the libraries your code needs





## Developing
1. Run `yarn start`. This will host your page locally, and automatically reload it when files change!



## Deploying
1. Run `yarn build`. This compiles your project into the `/dist` folder.
1. Run `yarn deploy`. This will use the neocities tool to deploy your dist folder to your server account