<template>
  <div class="home">
     <p>{{ message }} </p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Main',
    data() {
        return {
            message: "New Message from VueJs"
        }
    },
    methods: {
      getMessages() {
        const path = 'http://localhost:5000/api/v1/message'
        axios.get(path).then((resp) =>  {
          this.message = resp.data
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    created() {
      this.getMessages()
    }
}
</script>
