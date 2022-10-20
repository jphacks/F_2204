import { Button } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {
    text: string;
    margin?: string;
    onClick: () => void;
};

const LargeButton: FC<Props> = (props) => {
  return (
    <Button onClick={props.onClick} width="320px" height="60px" margin={props.margin}>{props.text}</Button>
  );
};

export default LargeButton;
