import { Box } from "@chakra-ui/react";
import { css } from "@emotion/css";
import React, { FC, ReactNode } from "react";
import Footer from "../molecules/Footer";
import Header from "../molecules/Header";

type Props = {
  children: ReactNode;
  hideSidebar?: boolean;
};

const BaseLayout: FC<Props> = (props) => {
  return (
    <>
      <Header />
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
        <main
          className={css`
            padding-top: 50px;
            padding-bottom: ${!props.hideSidebar ? "30px" : "0"};
          `}
        >
          {props.children}
        </main>

        {!props.hideSidebar && <Footer />}
      </div>
    </>
  );
};

export default BaseLayout;
