import { Button } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {
  text: string;
  bottomPos: string;
  margin?: string;
  onClick: () => void;
};

const FloatingBottomButton: FC<Props> = (props) => {
  return (
    <Button
      position="fixed"
      bottom={props.bottomPos}
      left="calc(50% - 350px/2)"
      width="350px"
      height="60px"
      onClick={props.onClick}
    >
      {props.text}
    </Button>
  );
};

export default FloatingBottomButton;
