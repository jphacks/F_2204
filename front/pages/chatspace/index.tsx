import type { NextPage } from "next";
import BaseLayout from "../../components/templates/BaseLayout";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
    Avatar
} from "@chatscope/chat-ui-kit-react";


const ChatSpacePage: NextPage = () => {
  return <BaseLayout>
    ChatSpace
  </BaseLayout>;
};
<div style={{ position: "relative", height: "500px" }}>
<MainContainer>
  <ChatContainer>
    <MessageList>
      <Message
        model={{
          message: "Hello my friend",
          sentTime: "just now",
          sender: "Joe",
          position: "normal",
          direction: "incoming"
        }}
      />
    </MessageList>
    <MessageInput placeholder="Type message here" />
  </ChatContainer>
</MainContainer>
</div>


 

export default ChatSpacePage;
