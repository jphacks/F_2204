import { Box } from "@chakra-ui/react";
import React, { FC } from "react";

type Props = {
  title: string;
  userName: string;
  communityName: string;
  date: string;
  onClick?: () => void;
};

const EventCard: FC<Props> = (props) => {
  return (
    <Box
      height={40}
      width="350px"
      borderWidth="1px"
      borderRadius="10px"
      overflow="hidden"
      paddingX="20px"
      paddingY="10px"
      display="flex"
      flexDirection="column"
      justifyContent="space-between"
      onClick={props.onClick}
    >
      <Box>
        <Box display="flex" justifyContent="space-between">
          <Box mt="1" as="h4" lineHeight="tight" noOfLines={2}>
            {props.title}
          </Box>
          <Box mt="1" as="h4" lineHeight="tight" noOfLines={1}>
            {props.userName}
          </Box>
        </Box>
        <Box display="flex" justifyContent="end">
          <Box mt="1" as="h4" lineHeight="tight" noOfLines={1}>
            {props.communityName}
          </Box>
        </Box>
      </Box>
      <Box>
        <Box display="flex" justifyContent="end">
          <Box>{props.date}</Box>
        </Box>
      </Box>
    </Box>
  );
};

export default EventCard;
