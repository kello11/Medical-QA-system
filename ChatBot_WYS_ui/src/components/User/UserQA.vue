<template>
    <div class="qna-container">
      <div class="nav">
        <!-- 导航组件 -->
        <Navigation />
      </div>
      <div class="qna">
        <!-- 问答组件 -->
        <QnA />
      </div>
      <div class="chat-history">
        <!-- 聊天历史记录组件 -->
        <ChatHistory />
      </div>
    </div>
  </template>
  
  <script>
  import Navigation from './Navigation.vue';
  import QnA from './QnA.vue';
  import ChatHistory from './ChatHistory.vue';
  
  export default {
    name: 'QnAPage',
    components: {
      Navigation,
      QnA,
      ChatHistory,
    },
  };
  </script>
  
  <style>
  .qna-container {
    display: flex;
    height: 100%;
  }
  
  .nav {
    width: 20%;
    padding: 0px;
    background-color: #f5f5f5;
  }
  
  .qna {
    width:50%;
    flex: 1;
    padding: 0px;
  }
  
  .chat-history {
    width: 23.76%;
    padding: 0px;
  }
  </style>