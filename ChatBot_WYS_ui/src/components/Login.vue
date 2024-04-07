<template>
  <div>
    <div class="backgroundbox">
      <img src="../img/bot.png" alt="bot" class="image">
      <h1 class="botname">ChatBot_WYS</h1>
      <div class="main-box">
        <div :class="['container', 'container-register', { 'is-txl': isLogin }]">
          <form>
            <h2 class="title">账号注册</h2>
            <div>
              <input class="form__input" id="email-input" type="text" placeholder="输入邮箱" v-model="registerForm.email"
                :class="{ 'error': isInvalidEmail }" />
              <el-button class="emailcode" size="mini" round="" type="primary" :disabled="countdown > 0"
                @click="validateEmail">
                {{ buttonText }}
              </el-button>
            </div>
            <input class="form__input" type="text" placeholder="输入6位验证码" v-model="registerForm.captcha" />
            <input class="form__input" type="name" placeholder="输入4-10位用户名" v-model="registerForm.name" />
            <div>
              <input class="form__input" :type="showPassword ? 'text' : 'password'" placeholder="输入8-16位密码"
                v-model="registerForm.password" />

            </div>
            <div class="gender">
              <el-radio v-model="radio" label="1">男性</el-radio>
              <el-radio v-model="radio" label="0">女性</el-radio>
              <p>{{ }}</p>
            </div>
            <div class="primary-btn" @click="register">立即注册</div>
          </form>
        </div>
        <div :class="['container', 'container-login', { 'is-txl is-z200': isLogin }]">
          <form>
            <h2 class="title">账号登录</h2>
            <input class="form__input" type="text" placeholder="用户名" v-model.lazy="loginForm.name" />
            <input class="form__input" type="password" placeholder="密码" v-model.lazy="loginForm.password" />
            <div class="primary-btn" @click="login">立即登录</div>
          </form>
        </div>
        <div :class="['switch', { login: isLogin }]">
          <div class="switch__circle"></div>
          <div class="switch__circle switch__circle_top"></div>
          <div class="switch__container">
            <h2>{{ isLogin ? '新朋友 !' : 'ChatBot 欢迎回来 !' }}</h2>
            <p>
              {{
                isLogin
                ? '注册新账号开启智能医疗问答'
                : '登录已有账号进行智能医疗问答'
              }}
            </p>
            <div class="primary-btn" @click="isLogin = !isLogin">
              {{ isLogin ? '立即注册' : '立即登录' }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

  name: 'LoginBox',
  data() {
    return {
      showPassword: false,
      isInvalidEmail: false,
      countdown: 0,
      buttonText: '获取验证码',
      radio: '1',
      isLogin: false,
      loginForm: {
        name: '',
        password: '',
      },
      registerForm: {
        name: '',
        captcha: '',
        email: '',
        password: '',
      },
    }
  },
  methods: {
    open2() {
      this.$message({
        showClose: true,
        message: '恭喜你，这是一条成功消息',
        type: 'success'
      });
    },
    open4(notice) {
      this.$message({
        showClose: true,
        message: notice,
        type: 'error'
      });
    },
    async validateEmail() {
      var url = "http://10.203.174.36:5002/user/captcha/email"
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // 简单的邮箱正则表达式

      if (emailRegex.test(this.registerForm.email)) {
        // 邮箱格式正确，发送验证码
        this.isInvalidEmail = false;
        this.startCountdown();
        var data = {
          u_email: this.registerForm.email,
        }
        console.log(data);
        // 发送请求
        await this.axios.post(url, data).then(function (response) {
          console.log(response.data)
        })
      } else {
        // 邮箱格式错误
        this.isInvalidEmail = true;
        this.shakeInput();
        this.open4("邮箱格式错误")
      }
    },
    shakeInput() {
      // 添加样式类名，用于触发振动效果
      this.$nextTick(() => {
        const inputElement = document.getElementById('email-input');
        inputElement.classList.add('shake');
      });
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    },
    async login() {
      var url = "http://10.203.174.36:5002/user/login"
      if (this.loginForm.name.length === 0 || this.loginForm.password.length === 0) {
        alert('请输入用户名和密码')
      }
      else {
        // 发送请求
        var data = {
          u_username: this.loginForm.name,
          u_password: this.loginForm.password // 需要加密传输 sha1/sha2/MD5
        }
        console.log(data);
        // 发送请求
        await this.axios.post(url, data).then(function (response) {
          console.log(response.data)
        })
        this.$router.push('/User')
      }
    },
    async register() {
      var url = "http://10.203.174.36:5002/user/register"
      if (this.registerForm.email.length === 0 ) {
        this.open4('请输入邮箱')
      }
      else if (this.registerForm.captcha.length === 0 ) {
        this.open4('请输入验证码')
      }
      else if (this.registerForm.name.length === 0 ) {
        this.open4('请输入用户名')
      }
      else if (this.registerForm.password.length === 0 ) {
        this.open4('请输入密码')
      }
      else {

        // 发送请求
        var data = {
          u_email: this.registerForm.email,
          u_captcha: this.registerForm.captcha,
          u_username: this.registerForm.name,
          u_password: this.registerForm.password, // 需要加密传输 sha1/sha2/MD5
          u_gender: this.radio
        }
        console.log(data);
        // 发送请求
        await this.axios.post(url, data).then(function (response) {
          console.log(response.data)
        })
      }
    },
    startCountdown() {
      if (this.countdown === 0) {
        this.countdown = 60;
        this.buttonText = `${this.countdown}秒后重新发送`;

        const countdownInterval = setInterval(() => {
          if (this.countdown > 0) {
            this.countdown--;
            this.buttonText = `${this.countdown}秒后重新发送`;
          } else {
            clearInterval(countdownInterval);
            this.countdown = 0;
            this.buttonText = '获取验证码';
          }
        }, 1000);
      }
    }

  },
}
</script>


<style lang="scss" scoped>
.backgroundbox {
  width: 100%;
  height: 100%;
  // background-color: #181818;
  // background-color: #4b70e2;
  position: fixed;
  background-image: url(../img/Background.jpg);


  .backgroundbox::before,
  .backgroundbox::after {
    content: "";
    position: absolute;
    top: 0;
    height: 0;
    width: 100%;
    background-color: #fff;
  }

  .backgroundbox::after {
    bottom: 0;
    top: auto;
  }

  .botname {
    width: 150px;
    height: 100px;
    position: fixed;
    left: 170px;
    z-index: 9999;
    color: white
  }

  .image {
    width: 130px;
    height: 100px;
    position: fixed;
    left: 9px;
    z-index: 9999;
    /* 较大的z-index值 */
  }

  .main-box {
    margin-left: auto;
    margin-right: auto;
    margin-top: 120px;
    position: relative;
    width: 1000px;
    min-width: 1000px;
    min-height: 600px;
    height: 600px;
    padding: 25px;
    background-color: #ecf0f3;
    // box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
    border-radius: 12px;
    overflow: hidden;



    .container {
      display: flex;
      justify-content: center;
      align-items: center;
      position: absolute;
      top: 0;
      width: 450px;
      height: 100%;
      padding: 25px;
      background-color: #ecf0f3;
      transition: all 1.25s;

      form {
        display: flex;
        justify-content: center;
        align-items: left;
        text-align: left;
        flex-direction: column;
        width: 100%;
        height: 100%;
        color: #a0a5a8;

        .primary-btn {
          margin-left: 150px;
          align-items: center;
          text-align: center;
        }

        .title {
          font-size: 34px;
          text-align: center;
          font-weight: 700;
          line-height: 3;
          color: #181818;
        }

        .text {
          margin-top: 30px;
          margin-bottom: 12px;
        }

        .emailcode {
          right: 0;
        }

        .gender {
          text-align: center;
        }

        .form__input {
          width: 200px;
          height: 40px;
          text-align: left;
          margin: 4px 0;
          margin-left: 100px;
          padding-left: 25px;
          font-size: 13px;
          letter-spacing: 0.15px;
          border: none;
          outline: none;
          // font-family: 'Montserrat', sans-serif;
          background-color: #ecf0f3;
          transition: 0.25s ease;
          border-radius: 8px;
          box-shadow: inset 2px 2px 4px #d1d9e6, inset -2px -2px 4px #f9f9f9;

          &::placeholder {
            color: #a0a5a8;
          }
        }
      }
    }

    .container-register {
      z-index: 100;
      left: calc(100% - 600px);
    }

    .container-login {
      left: calc(100% - 600px);
      z-index: 0;
    }

    .is-txl {
      left: 0;
      transition: 1.25s;
      transform-origin: right;
    }

    .is-z200 {
      z-index: 200;
      transition: 1.25s;
    }

    .switch {
      display: flex;
      justify-content: center;
      align-items: center;
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      width: 350px;
      padding: 50px;
      z-index: 200;
      transition: 1.25s;
      background-color: #ecf0f3;
      overflow: hidden;
      box-shadow: 4px 4px 10px #d1d9e6, -4px -4px 10px #f9f9f9;
      color: #a0a5a8;

      .switch__circle {
        position: absolute;
        width: 500px;
        height: 500px;
        border-radius: 50%;
        background-color: #ecf0f3;
        box-shadow: inset 8px 8px 12px #d1d9e6, inset -8px -8px 12px #f9f9f9;
        bottom: -60%;
        left: -60%;
        transition: 1.25s;
      }

      .switch__circle_top {
        top: -30%;
        left: 60%;
        width: 300px;
        height: 300px;
      }

      .switch__container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        position: absolute;
        width: 400px;
        padding: 50px 55px;
        transition: 1.25s;

        h2 {
          font-size: 34px;
          font-weight: 700;
          line-height: 3;
          color: #181818;
        }

        p {
          font-size: 14px;
          letter-spacing: 0.25px;
          text-align: center;
          line-height: 1.6;
        }
      }
    }

    .login {
      left: calc(100% - 400px);

      .switch__circle {
        left: 0;
      }
    }

    .primary-btn {
      width: 180px;
      height: 50px;
      border-radius: 25px;
      margin-top: 50px;
      text-align: center;
      line-height: 50px;
      font-size: 14px;
      letter-spacing: 2px;
      background-color: red;
      color: #f9f9f9;
      cursor: pointer;
      box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #f9f9f9;

      &:hover {
        box-shadow: 4px 4px 6px 0 rgb(255 255 255 / 50%),
          -4px -4px 6px 0 rgb(116 125 136 / 50%),
          inset -4px -4px 6px 0 rgb(255 255 255 / 20%),
          inset 4px 4px 6px 0 rgb(0 0 0 / 40%);
      }
    }
  }
}

.form__input.error {
  border-color: red;
  animation: shake 0.3s ease-in;
}


@keyframes shake {
  0% {
    transform: translateX(0);
  }

  10% {
    transform: translateX(-5px);
  }

  20% {
    transform: translateX(5px);
  }

  30% {
    transform: translateX(-5px);
  }

  40% {
    transform: translateX(5px);
  }

  50% {
    transform: translateX(-5px);
  }

  60% {
    transform: translateX(5px);
  }

  70% {
    transform: translateX(-5px);
  }

  80% {
    transform: translateX(5px);
  }

  90% {
    transform: translateX(-5px);
  }

  100% {
    transform: translateX(0);
  }

}
</style>

