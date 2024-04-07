<template>
    <div class="about">
      <User></User>
    </div>
  </template>

<script>
// @ is an alias to /src
import User from '@/components/User/UserQA.vue'

export default {
  name: 'UserView',
  components: {
    User
  }
}
</script>
  