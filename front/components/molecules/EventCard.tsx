import { Badge, Box, Image } from "@chakra-ui/react";
import React, { FC } from "react";

const EventCard: FC = () => {
  const property = {
    title: "料理名",
    userName: "ユーザー名",
    communityName: "コミュニティ名",
  };

  return (
    <Box
      height={40}
      maxW="sm"
      minW="xs"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
    >
      {/* <Image src={"/taco03_thumbnail_16×9.jpg"} alt={""} /> */}
      <Box paddingX="6" paddingY="3">
        <Box display="flex" justifyContent="space-between">
          <Box
            mt="1"
            fontWeight="semibold"
            as="h4"
            lineHeight="tight"
            noOfLines={1}
          >
            {property.title}
          </Box>
          <Box
            mt="1"
            fontWeight="semibold"
            as="h4"
            lineHeight="tight"
            noOfLines={1}
          >
            {property.userName}
          </Box>
        </Box>
        <Box display="flex" justifyContent="end">
          <Box
            mt="1"
            fontWeight="semibold"
            as="h4"
            lineHeight="tight"
            noOfLines={1}
          >
            {property.communityName}
          </Box>
        </Box>
      </Box>
    </Box>
  );
};

export default EventCard;
