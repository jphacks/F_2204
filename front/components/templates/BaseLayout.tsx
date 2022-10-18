import { Box } from "@chakra-ui/react";
import { css } from "@emotion/css";
import React, { FC, ReactNode } from "react";
import Footer from "../molecules/Footer";
import Header from "../molecules/Header";

type Props = {
  children: ReactNode;
};

const BaseLayout: FC<Props> = (props) => {
  return (
    <div
      className={css`
        height: 100vh;
        width: 100%;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow-x: hidden;
        z-index: 1;
        position: relative;
      `}
    >
      <Header />
      <main
        className={css`
          padding-top: 70px;
          padding-bottom: 60px;
        `}
      >
        {props.children}
      </main>
      <footer>
        <Footer />
      </footer>
    </div>
  );
};

export default BaseLayout;
