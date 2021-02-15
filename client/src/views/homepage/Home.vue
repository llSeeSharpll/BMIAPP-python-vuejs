<template>
  <div class="home">
    <Bmi/>
  </div>
</template>

<script>
// @ is an alias to /src
import Bmi from '@/components/Bmi.vue'

export default {
  name: 'Home',
  components: {
    Bmi
  }
}
</script>
