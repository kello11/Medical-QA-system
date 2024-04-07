<template>
    <div class="chat-container">
      <div class="chat-display">
        <div v-for="(message, index) in chatLogs" :key="index" class="message">
          <div v-if="message.type === 'user'" class="user-message">
            <div class="user-bubble chat-bubble">{{ message.content }}</div>
          </div>
          <div v-else class="assistant-message">
            <div class="assistant-bubble chat-bubble">{{ message.content }}</div>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input class="message" v-model="userInput" @keyup.enter="sendMessage" placeholder="Type your message...">
        <button class="send-bubble" @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        chatLogs: [],      // Array to store user and assistant messages
        userInput: ''      // Variable to hold user input
      }
    },
    methods: {
      sendMessage() {
        // Push user message to chatLogs array
        if (this.userInput.trim() !== '') {
          this.chatLogs.push({ type: 'user', content: this.userInput.trim() })
          this.userInput = ''
          this.scrollToBottom()
          this.getAssistantResponse()    // Call API to get assistant's response
        }
      },
      getAssistantResponse() {
        // Call your API or logic here to get the assistant's response
        // Assuming the response from the assistant is in variable `response`
        const response = "Sample response from the assistant"
  
        // Push assistant message to chatLogs array
        this.chatLogs.push({ type: 'assistant', content: response })
        this.scrollToBottom()
      },
      scrollToBottom() {
        // Scroll to the bottom of the chat display
        this.$nextTick(() => {
          const chatDisplay = document.querySelector('.chat-display')
          chatDisplay.scrollTop = chatDisplay.scrollHeight
        })
      }
    }
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 820px;
    width: 950px;
    border: 1px solid #ccc;
    background-color: #272b2c;
    border-radius: 4px;
    overflow: hidden;
  }
  
  .chat-display {
    flex: 1;
    overflow: auto;
    padding: 10px;
  }
  
  .chat-input {
    display: flex;
    align-items: center;
    padding: 10px;
    border-top: 1px solid #ccc;
  }
  
  .user-message {
    display: flex;
    flex-direction: row-reverse;
    margin-bottom: 10px;
    color:white
  }
  
  .assistant-message {
    display: flex;
    margin-bottom: 10px;
    color:white
  }
  
  .user-bubble{
    display: inline-block;
    padding: 8px;
    /* background-color: #eee; */
    background-color: #3f494c;
    border-radius: 8px;
    
  }
  .assistant-bubble {
    display: inline-block;
    padding: 8px;
    /* background-color: #eee; */
    background-color: #141718;
    border-radius: 8px;
  }
  
  .user-bubble {
    text-align: right;
  }
  
  .assistant-bubble {
    text-align: left;
  }
  .message{
    width:900px;
    height: 40px;
    border-radius:10px;
    font-size:20px;
  }
  .send-bubble{
    height:46px;
    border-radius:10px
  }
  </style>