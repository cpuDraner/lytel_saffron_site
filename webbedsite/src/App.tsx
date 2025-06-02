import styled from "@emotion/styled";
import PGB from "../public/PGBb.pdf";

export const App = () => {
  return (
    <StyleContainer>
      <h1>Welcome to my Website!</h1>
      I'm still learning how to properly make the website, so for now have a
      link to my <a href="https://discord.gg/r85TNPRfNw">project discord</a>. If
      your looking for the current beta of Punch Game BLITZ!,{" "}
      <a href={PGB} target="_blank">
        click here
      </a>
      .
    </StyleContainer>
  );
};

// styled is super cool! you pass it the type of HTML element you want to render, then an object containing the CSS styles you want to render it in!
const StyleContainer = styled("div")({
  fontFamily: "helvetica",
  fontSize: "25px",
});
