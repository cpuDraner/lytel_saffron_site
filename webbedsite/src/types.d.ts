// This project is in typescript, which is like javascript but less insane
// This file tells typescript how you want to import non typescript things

declare module "*.pdf" {
  const value: any; // Add better type definitions here if desired.
  export default value;
}
