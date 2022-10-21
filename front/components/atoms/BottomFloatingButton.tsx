import { Button, ButtonProps } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {
  text: string;
  onClick: () => void;
} & ButtonProps;

const FloatingBottomButton: FC<Props> = (props) => {
  return (
    <Button
      {...props}
      position="fixed"
      left="calc(50% - 350px/2)"
      width="350px"
      onClick={props.onClick}
    >
      {props.text}
    </Button>
  );
};

export default FloatingBottomButton;
