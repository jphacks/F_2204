import { Box } from "@chakra-ui/react";
import { css } from "@emotion/css";
import React, { FC, ReactNode } from "react";

type Props = {
  children: ReactNode;
};

const BaseLayout: FC<Props> = (props) => {
  return (
    <div
      className={css`
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow-x: hidden;
        padding-top: 30px;
      `}
    >
      <header></header>
      <main>{props.children}</main>
      <footer></footer>
    </div>
  );
};

export default BaseLayout;
